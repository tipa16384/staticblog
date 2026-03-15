import xml.etree.ElementTree as ET
import csv
from collections import Counter

def parse_categories_csv(csv_file):
    """Parse categories CSV file and create a mapping from slug to normalized_name"""
    slug_to_normalized = {}
    
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['type'] == 'category':  # Only process category types
                slug = row['slug']
                normalized_name = row['normalized_name']
                slug_to_normalized[slug] = normalized_name
    
    return slug_to_normalized

def parse_wordpress_xml(xml_file):
    """Parse WordPress XML file and extract category nice names from posts"""
    category_nicenames = []
    
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # WordPress XML uses a namespace, we need to handle this
    namespaces = {
        'wp': 'http://wordpress.org/export/1.2/',
        'content': 'http://purl.org/rss/1.0/modules/content/',
        'excerpt': 'http://wordpress.org/export/1.2/excerpt/'
    }
    
    # Find all items (posts)
    for item in root.findall('.//item'):
        # Check if this is a post (not attachment, page, etc.)
        post_type = item.find('./wp:post_type', namespaces)
        if post_type is not None and post_type.text == 'post':
            # Check post status - only count published posts
            status = item.find('./wp:status', namespaces)
            if status is not None and status.text == 'publish':
                # Find all categories for this post
                for category in item.findall('./category'):
                    # Only process categories (not tags or nav menus)
                    domain = category.get('domain')
                    if domain == 'category':
                        nicename = category.get('nicename')
                        if nicename:
                            category_nicenames.append(nicename)
    
    return category_nicenames

def count_normalized_category_usage(xml_file, csv_file, output_file):
    """Main function to count normalized category usage"""
    print(f"Parsing categories from {csv_file}...")
    slug_to_normalized = parse_categories_csv(csv_file)
    
    print(f"Parsing WordPress XML file {xml_file}...")
    category_nicenames = parse_wordpress_xml(xml_file)
    
    print(f"Found {len(category_nicenames)} category references in posts")
    
    # Map nicenames to normalized names and count
    normalized_counts = Counter()
    unmapped_categories = set()
    
    for nicename in category_nicenames:
        if nicename in slug_to_normalized:
            normalized_name = slug_to_normalized[nicename]
            normalized_counts[normalized_name] += 1
        else:
            unmapped_categories.add(nicename)
    
    if unmapped_categories:
        print(f"\nWarning: Found {len(unmapped_categories)} categories that couldn't be mapped:")
        for cat in sorted(unmapped_categories):
            print(f"  - {cat}")
    
    # Write results to CSV
    print(f"\nWriting results to {output_file}...")
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['normalized_category_name', 'usage_count'])
        
        # Sort by count descending
        for normalized_name, count in normalized_counts.most_common():
            writer.writerow([normalized_name, count])
    
    print(f"\nResults written! Found {len(normalized_counts)} unique normalized categories.")
    
    # Print top 10
    print("\nTop 10 most used categories:")
    for normalized_name, count in normalized_counts.most_common(10):
        print(f"  {count:3d}: {normalized_name}")


if __name__ == '__main__':
    wp_xml = 'chasingdings.WordPress.2026-01-26.xml'
    category_csv = 'categories_simple_normalized.csv'
    output_csv = 'category_count.csv'
    
    count_normalized_category_usage(wp_xml, category_csv, output_csv)

