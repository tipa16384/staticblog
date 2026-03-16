import xml.etree.ElementTree as ET
import os
from datetime import datetime
from pathlib import Path
import re
from urllib.parse import urlparse

wp_xml = 'chasingdings.WordPress.2026-01-26.xml'

def extract_slug_from_url(url):
    """Extract the title-slug from a WordPress URL like https://chasingdings.com/YYYY/MM/DD/title-slug/"""
    # Parse the URL and get the path
    parsed = urlparse(url)
    path = parsed.path.strip('/')
    
    # Split by '/' and get the last part (the slug)
    parts = path.split('/')
    if len(parts) >= 4:  # Expected: YYYY/MM/DD/title-slug
        return parts[-1]  # Return the slug
    return None

def parse_wordpress_date(wp_date_str):
    """Parse WordPress date string and convert to ISO format with timezone"""
    # WordPress format: YYYY-MM-DD HH:MM:SS
    try:
        dt = datetime.strptime(wp_date_str, '%Y-%m-%d %H:%M:%S')
        # Convert to ISO format with timezone (assuming EST for now)
        # You might want to adjust the timezone based on your blog's timezone
        iso_date = dt.strftime('%Y-%m-%dT%H:%M:%S-05:00')
        return iso_date
    except ValueError:
        print(f"Error parsing date: {wp_date_str}")
        return None

def create_hugo_post(post_date, title, slug):
    """Create a Hugo markdown file with frontmatter"""
    # Extract year, month, day from the URL slug path or date
    try:
        dt = datetime.strptime(post_date, '%Y-%m-%d %H:%M:%S')
        year = dt.strftime('%Y')
        month = dt.strftime('%m')
        day = dt.strftime('%d')
    except ValueError:
        print(f"Error parsing date for directory structure: {post_date}")
        return
    
    # Create directory structure
    post_dir = Path(f'content/posts/{year}/{month}/{day}')
    post_dir.mkdir(parents=True, exist_ok=True)
    
    # Create the markdown file
    file_path = post_dir / f'{slug}.md'
    
    # Convert date to ISO format
    iso_date = parse_wordpress_date(post_date)
    if not iso_date:
        return
    
    # Debug output
    print(f"DEBUG: Raw title: '{repr(title)}'")
    print(f"DEBUG: Date: '{post_date}' -> ISO: '{iso_date}'")
    print(f"DEBUG: Slug: '{slug}'")
    print(f"DEBUG: File path: '{file_path}'")
    
    # Escape quotes and other problematic characters in title
    if title:
        escaped_title = title.replace('"', '\\"').replace('\n', ' ').replace('\r', ' ')
    else:
        escaped_title = "Untitled"
    
    print(f"DEBUG: Escaped title: '{escaped_title}'")
    
        # Create Hugo frontmatter in YAML format
    frontmatter = f"""---
date: '{iso_date}'
draft: false
title: "{escaped_title}"
canonicalURL: "https://example.com/"
editPost:
    URL: "https://github.com/tipa16384/staticblog/tree/main/content"
---

This post intentionally left blank.
"""
    
    print(f"DEBUG: Frontmatter length: {len(frontmatter)}")
    
    # Write the file
    try:
        print(f"DEBUG: About to write file...")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(frontmatter)
        print(f"Created: {file_path}")
        
        # Verify file was written correctly
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            print(f"DEBUG: File size after writing: {len(content)} chars")
            if len(content) < 20:
                print(f"DEBUG: File content: '{content}'")
                
    except Exception as e:
        print(f"Error creating file {file_path}: {e}")
        import traceback
        traceback.print_exc()

# Test with just one post
try:
    tree = ET.parse(wp_xml)
    root = tree.getroot()
    
    # Find all items (posts)
    items = root.findall('.//item')
    
    count = 0
    for item in items:
        # Check if this is a post (not page, attachment, etc.)
        post_type = item.find('.//{http://wordpress.org/export/1.2/}post_type')
        if post_type is None or post_type.text != 'post':
            continue
            
        # Check if post is published
        status = item.find('.//{http://wordpress.org/export/1.2/}status')
        if status is None or status.text != 'publish':
            continue
        
        # Extract post data
        title = item.find('title')
        link = item.find('link')
        post_date = item.find('.//{http://wordpress.org/export/1.2/}post_date')
        
        if title is None or link is None or post_date is None:
            print("Missing required fields for post, skipping...")
            continue
        
        title_text = title.text if title.text else "Untitled"
        link_url = link.text if link.text else ""
        date_text = post_date.text if post_date.text else ""
        
        # Extract slug from URL
        slug = extract_slug_from_url(link_url)
        if not slug:
            print(f"Could not extract slug from URL: {link_url}")
            continue
        
        # Create the Hugo post
        print(f"Processing post: {title_text}")
        create_hugo_post(date_text, title_text, slug)
        count += 1
        
        # Only do first post for debugging
        if count >= 1:
            break
    
    print(f"Processed {count} test posts.")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()