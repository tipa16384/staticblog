import xml.etree.ElementTree as ET
import csv
from hugo_post_creator import create_hugo_post

wp_xml = 'chasingdings.WordPress.2026-01-26.xml'
tag_normalization_file = 'categories_simple_normalized.csv'

def load_tag_normalization_dict():
    """Load tag normalization data from CSV file into a dictionary"""
    tag_dict = {}
    
    try:
        with open(tag_normalization_file, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header row
            
            for row in reader:
                if len(row) >= 6:  # Ensure we have all required columns
                    name = row[2]  # name column
                    tag_type = row[0]  # type column  
                    normalized_name = row[5]  # normalized_name column
                    
                    # Only add if key doesn't already exist
                    if name not in tag_dict:
                        tag_dict[name] = (tag_type, normalized_name)
                        
    except FileNotFoundError:
        print(f"Warning: Tag normalization file {tag_normalization_file} not found")
    except Exception as e:
        print(f"Error reading tag normalization file: {e}")
    
    return tag_dict

def migrate_wordpress_to_hugo():
    """Main function to migrate WordPress posts to Hugo format"""
    try:
        # Load tag normalization dictionary
        tag_normalization_dict = load_tag_normalization_dict()
        print(f"Loaded {len(tag_normalization_dict)} tag normalizations")
        
        # Parse the WordPress XML
        tree = ET.parse(wp_xml)
        root = tree.getroot()
        
        # Find all items (posts)
        items = root.findall('.//item')
        
        # Build parent-child relationship dictionary
        parent_children_map = {}
        all_items_by_id = {}
        
        # First pass: collect all items by post_id
        for item in items:
            post_id_elem = item.find('.//{http://wordpress.org/export/1.2/}post_id')
            if post_id_elem is None or not post_id_elem.text:
                continue
            all_items_by_id[post_id_elem.text] = item
        
        # Second pass: build parent_children_map via post_parent AND _thumbnail_id postmeta
        for item in items:
            post_id_elem = item.find('.//{http://wordpress.org/export/1.2/}post_id')
            if post_id_elem is None or not post_id_elem.text:
                continue
            post_id = post_id_elem.text
            
            # Add this item to its parent's list if it has a non-zero post_parent
            post_parent_elem = item.find('.//{http://wordpress.org/export/1.2/}post_parent')
            parent_id = post_parent_elem.text if post_parent_elem is not None and post_parent_elem.text else "0"
            if parent_id != "0" and parent_id != "":
                parent_children_map.setdefault(parent_id, []).append(item)
            
            # Add thumbnail attachment to this post's list via _thumbnail_id postmeta
            for postmeta in item.findall('.//{http://wordpress.org/export/1.2/}postmeta'):
                meta_key = postmeta.find('.//{http://wordpress.org/export/1.2/}meta_key')
                meta_value = postmeta.find('.//{http://wordpress.org/export/1.2/}meta_value')
                if (meta_key is not None and meta_key.text == '_thumbnail_id'
                        and meta_value is not None and meta_value.text):
                    thumbnail_item = all_items_by_id.get(meta_value.text)
                    if thumbnail_item is not None:
                        children = parent_children_map.setdefault(post_id, [])
                        if thumbnail_item not in children:
                            children.append(thumbnail_item)
                    break
        
        post_count = 0
        
        # Second pass: process only parent posts
        for item in items:
            # Check if this is a post (not page, attachment, etc.)
            post_type = item.find('.//{http://wordpress.org/export/1.2/}post_type')
            if post_type is None or post_type.text != 'post':
                continue
                
            # Check if post is published
            status = item.find('.//{http://wordpress.org/export/1.2/}status')
            if status is None or status.text != 'publish':
                continue
            
            # Check if this is a parent post (not a child)
            post_parent_elem = item.find('.//{http://wordpress.org/export/1.2/}post_parent')
            parent_id = post_parent_elem.text if post_parent_elem is not None and post_parent_elem.text else "0"
            
            if parent_id != "0" and parent_id != "":
                continue  # Skip child posts
            
            # Get this post's ID to find its children
            post_id_elem = item.find('.//{http://wordpress.org/export/1.2/}post_id')
            if post_id_elem is None or not post_id_elem.text:
                continue
            
            post_id = post_id_elem.text
            child_items = parent_children_map.get(post_id, [])
            
            # Create the Hugo post using the entire item and its children
            if create_hugo_post(item, child_items, tag_normalization_dict, tags_only=True):
                post_count += 1
        
        print(f"\nMigration complete! Processed {post_count} posts.")
        
    except FileNotFoundError:
        print(f"Error: Could not find WordPress XML file: {wp_xml}")
    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    migrate_wordpress_to_hugo()

