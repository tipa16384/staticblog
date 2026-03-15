import xml.etree.ElementTree as ET
import csv

wp_xml = 'chasingdings.WordPress.2026-01-26.xml'

def extract_categories_and_tags(xml_filename, csv_filename='categories.csv'):
    """
    Extract categories and tags from a WordPress XML export file and save to CSV.
    
    Args:
        xml_filename (str): Path to the WordPress XML file
        csv_filename (str): Output CSV filename (default: 'categories.csv')
    """
    
    # Parse the XML file
    tree = ET.parse(xml_filename)
    root = tree.getroot()
    
    # Define WordPress namespace
    wp_ns = {'wp': 'http://wordpress.org/export/1.2/'}
    
    # List to store all categories and tags
    items = []
    
    # Extract categories
    categories = root.findall('.//wp:category', wp_ns)
    for cat in categories:
        term_id = cat.find('wp:term_id', wp_ns)
        nicename = cat.find('wp:category_nicename', wp_ns)
        parent = cat.find('wp:category_parent', wp_ns)
        cat_name = cat.find('wp:cat_name', wp_ns)
        
        items.append({
            'type': 'category',
            'term_id': term_id.text if term_id is not None else '',
            'name': cat_name.text if cat_name is not None else '',
            'slug': nicename.text if nicename is not None else '',
            'parent': parent.text if parent is not None and parent.text else ''
        })
    
    # Extract tags
    tags = root.findall('.//wp:tag', wp_ns)
    for tag in tags:
        term_id = tag.find('wp:term_id', wp_ns)
        tag_slug = tag.find('wp:tag_slug', wp_ns)
        tag_name = tag.find('wp:tag_name', wp_ns)
        
        items.append({
            'type': 'tag',
            'term_id': term_id.text if term_id is not None else '',
            'name': tag_name.text if tag_name is not None else '',
            'slug': tag_slug.text if tag_slug is not None else '',
            'parent': ''  # Tags don't have parents in WordPress
        })
    
    # Write to CSV
    if items:
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['type', 'term_id', 'name', 'slug', 'parent']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write header
            writer.writeheader()
            
            # Write data
            for item in items:
                writer.writerow(item)
        
        print(f"Successfully extracted {len([i for i in items if i['type'] == 'category'])} categories and {len([i for i in items if i['type'] == 'tag'])} tags to {csv_filename}")
    else:
        print("No categories or tags found in the XML file.")

# Run the extraction
if __name__ == "__main__":
    extract_categories_and_tags(wp_xml)

