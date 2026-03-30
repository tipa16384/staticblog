import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse
import re
from html import unescape

WP_UPLOADS_OLD = 'https://chasingdings.com/wp-content/uploads/'
WP_UPLOADS_NEW = 'https://tipa16384.github.io/wkblog/uploads/'
WP_BASE_OLD = 'https://chasingdings.com/'
WP_BASE_NEW = 'https://tipa16384.github.io/wkblog/'

def rewrite_upload_url(text):
    """Replace all chasingdings.com URLs with GitHub Pages equivalents.
    Uploads (/wp-content/uploads/) get the 'uploads/' path; all other URLs
    are rewritten to the new blog base.
    """
    if not text:
        return text
    # Rewrite uploads first (more specific), then the base domain.
    text = text.replace(WP_UPLOADS_OLD, WP_UPLOADS_NEW)
    text = text.replace(WP_BASE_OLD, WP_BASE_NEW)
    return text

def process_wordpress_content(content_encoded):
    """Convert WordPress HTML content to Markdown"""
    if not content_encoded:
        return "This post intentionally left blank."
    
    # Unescape HTML entities
    content = unescape(content_encoded)
    
    # Check if this is a block editor post (has wp: comments)
    is_block_editor = '<!-- wp:' in content
    
    if is_block_editor:
        return process_block_editor_content(content)
    else:
        return process_legacy_content(content)

def process_block_editor_content(content):
    """Process WordPress block editor content"""
    # Remove WordPress block comments
    content = re.sub(r'<!-- wp:[^>]*? -->', '', content)
    content = re.sub(r'<!-- /wp:[^>]*? -->', '', content)
    
    # Convert WordPress caption shortcodes to Hugo figure shortcodes
    content = convert_wordpress_captions(content)
    
    # Convert WordPress block editor figures to Hugo figure shortcodes
    content = convert_block_editor_figures(content)
    
    # Convert HTML to Markdown
    content = convert_html_to_markdown(content)
    
    # Convert YouTube links to Hugo shortcodes
    content = convert_youtube_links(content)
    
    return content.strip()

def process_legacy_content(content):
    """Process pre-block editor WordPress content"""
    # Convert legacy WordPress caption shortcodes to Hugo figure shortcodes FIRST
    content = convert_legasy_wp_captions(content)
    
    # Then convert HTML to Markdown
    content = convert_html_to_markdown(content)
    
    # Convert YouTube links to Hugo shortcodes
    content = convert_youtube_links(content)
    
    # Split by line breaks and make each non-empty line a paragraph
    lines = content.split('\n')
    paragraphs = []
    
    for line in lines:
        line = line.strip()
        if line:
            paragraphs.append(line)
    
    return '\n\n'.join(paragraphs)

def get_image_class(align):
    """Determine image class based on alignment.
    Returns 'fig-20' for left/right aligned images, 'center' otherwise."""
    if not align:
        return 'center'
    # Check if alignment is left or right (various formats)
    align_lower = align.lower()
    if 'left' in align_lower or 'right' in align_lower:
        return 'fig-20'
    return 'center'

def convert_wordpress_captions(content):
    """Convert WordPress caption shortcodes to Hugo figure shortcodes"""
    # Pattern to match [caption ...]content[/caption]
    caption_pattern = r'\[caption([^\]]*)\](.*?)\[/caption\]'
    
    def replace_caption(match):
        attributes = match.group(1)
        caption_content = match.group(2).strip()
        
        # Extract align attribute
        align_match = re.search(r'align=["\']?([^"\'\\s]+)["\']?', attributes)
        align = align_match.group(1) if align_match else ''
        
        # Clean align value - WordPress uses 'aligncenter', we want 'align-center'
        if align.startswith('align'):
            align = align.replace('align', 'align-')
        elif align and not align.startswith('align-'):
            align = f'align-{align}'
        
        # Extract image URL from the content
        img_url = ""
        
        # Look for HTML img tag (most common in WordPress)
        img_match = re.search(r'<img[^>]*src=["\']([^"\']+)["\'][^>]*>', caption_content)
        if img_match:
            img_url = img_match.group(1)
        
        # Extract caption text - check both caption attribute and text content
        caption_text = ""
        
        # Enhanced regex to handle quoted caption attributes with internal escaped quotes
        # This regex properly handles: caption="text with \"quotes\" inside" and caption="text with \'apostrophe\' inside"
        caption_attr_match = re.search(r'caption=(["\'])((?:[^"\'\\]|\\.)*)\1', attributes)
        if caption_attr_match:
            caption_text = caption_attr_match.group(2)
        else:
            # Fallback: replace <br/> tags with spaces, then remove all HTML tags from content
            caption_content_clean = re.sub(r'<br\s*/?>', ' ', caption_content, flags=re.IGNORECASE)
            caption_text = re.sub(r'<[^>]*>', '', caption_content_clean).strip()
        # Normalize all whitespace to a single space for all captions
        caption_text = re.sub(r'\s+', ' ', caption_text).strip()
        
        # Clean up WordPress escape sequences
        caption_text = caption_text.replace('\"', '"').replace("\'", "'").replace('\\&', '&')

        # Force normalization of newlines and tabs to spaces right before shortcode generation
        caption_text = re.sub(r'[\n\r\t]+', ' ', caption_text)
        caption_text = re.sub(r' +', ' ', caption_text).strip()
        
        if img_url:
            image_class = get_image_class(align)
            if caption_text:
                # Escape quotes for Hugo shortcode
                escaped_caption = caption_text.replace('"', '\\"')
                result = f'{{{{< image src="{img_url}" title="{escaped_caption}" classes="{image_class}" >}}}}'
            else:
                result = f'{{{{< image src="{img_url}" classes="{image_class}" >}}}}'
            return result
        else:
            # Fallback if we can't extract image URL
            return caption_content
    
    return re.sub(caption_pattern, replace_caption, content, flags=re.DOTALL)

def convert_legasy_wp_captions(content):
    """Convert legacy WordPress caption shortcodes to Hugo figure shortcodes."""
    caption_pattern = r'\[caption([^\]]*)\](.*?)\[/caption\]'

    def replace_caption(match):
        attributes = match.group(1)
        caption_content = match.group(2)

        # Replace legacy line breaks before any other processing.
        attributes = re.sub(r'<br\s*/?>', ' ', attributes, flags=re.IGNORECASE)
        caption_content = re.sub(r'<br\s*/?>', ' ', caption_content, flags=re.IGNORECASE)

        # Extract align attribute.
        align_match = re.search(r'align=["\']?([^"\'\\s]+)["\']?', attributes)
        align = align_match.group(1) if align_match else ''
        if align.startswith('align'):
            align = align.replace('align', 'align-')
        elif align and not align.startswith('align-'):
            align = f'align-{align}'

        # Extract image URL.
        img_url = ''
        img_match = re.search(r'<img[^>]*src=["\']([^"\']+)["\'][^>]*>', caption_content)
        if img_match:
            img_url = img_match.group(1)

        # Legacy caption extraction pattern requested by user.
        caption_text = ''
        caption_attr_match = re.search(r'caption="((?:\\.|[^"\\])*)"', attributes)
        if caption_attr_match:
            caption_text = caption_attr_match.group(1)
        else:
            caption_text = re.sub(r'<[^>]*>', '', caption_content).strip()

        # Normalize escaped chars and whitespace.
        caption_text = caption_text.replace('\\"', '"').replace("\\'", "'").replace('\\&', '&')
        caption_text = re.sub(r'\s+', ' ', caption_text).strip()

        if not img_url:
            return caption_content

        image_class = get_image_class(align)
        if caption_text:
            escaped_caption = caption_text.replace('"', '\\"')
            return f'{{{{< image src="{img_url}" title="{escaped_caption}" classes="{image_class}" >}}}}'

        return f'{{{{< image src="{img_url}" classes="{image_class}" >}}}}'

    return re.sub(caption_pattern, replace_caption, content, flags=re.DOTALL)

def convert_block_editor_figures(content):
    """Convert WordPress block editor figure elements to Hugo figure shortcodes"""
    # Pattern to match <figure class="wp-block-image ...">...</figure>
    figure_pattern = r'<figure\s+class="wp-block-image[^"]*"[^>]*>(.*?)</figure>'
    
    def replace_figure(match):
        figure_content = match.group(1)
        
        # Extract alignment from the figure class
        figure_tag = match.group(0)
        align = ""
        if 'aligncenter' in figure_tag:
            align = 'align-center'
        elif 'alignleft' in figure_tag:
            align = 'align-left'  
        elif 'alignright' in figure_tag:
            align = 'align-right'
        
        # Extract image URL from img tag
        img_match = re.search(r'<img[^>]*src=["\']([^"\']+)["\'][^>]*>', figure_content)
        if not img_match:
            return match.group(0)  # Return original if no image found
        
        img_url = img_match.group(1)
        
        # Extract caption text from figcaption
        caption_match = re.search(r'<figcaption[^>]*>(.*?)</figcaption>', figure_content, flags=re.DOTALL)
        caption_text = ""
        if caption_match:
            # Remove any HTML tags from caption and clean up
            caption_text = re.sub(r'<[^>]*>', '', caption_match.group(1)).strip()
            # Clean up WordPress escape sequences
            caption_text = caption_text.replace("\\'", "'").replace('\\"', '"').replace('\\&', '&')
        
        if caption_text:
            # Escape quotes in caption text for Hugo shortcode
            escaped_caption = caption_text.replace('"', '\\"')
            image_class = get_image_class(align)
            result = f'{{{{< image src="{img_url}" title="{escaped_caption}" classes="{image_class}" >}}}}'
        else:
            image_class = get_image_class(align)
            result = f'{{{{< image src="{img_url}" classes="{image_class}" >}}}}'
        return result
    
    return re.sub(figure_pattern, replace_figure, content, flags=re.DOTALL)

def convert_html_to_markdown(html_content):
    """Convert HTML elements to Markdown"""
    content = html_content
    
    # Convert images - handle both self-closing and regular img tags
    # Look for caption in various places
    def convert_image(match):
        img_tag = match.group(0)
        
        # Extract src
        src_match = re.search(r'src=["\']([^"\']*)["\']', img_tag)
        src = src_match.group(1) if src_match else ""
        
        # Extract alignment info (could be in align attribute, class, or style)
        align = ""
        # Check for align attribute
        align_match = re.search(r'align=["\']?([^"\'\\s]+)["\']?', img_tag)
        if align_match:
            align = align_match.group(1)
        # Check for alignment classes (alignLeft, alignRight, align-left, align-right)
        elif re.search(r'(?:align-?(?:left|right)|alignLeft|alignRight)', img_tag, re.IGNORECASE):
            align = 'aligned'
        # Check for style attribute with text-align
        style_match = re.search(r'style=["\']([^"\']*)["\']', img_tag)
        if style_match and not align:
            style = style_match.group(1)
            if 'left' in style.lower():
                align = 'left'
            elif 'right' in style.lower():
                align = 'right'
        
        # Look for title or caption - could be in title attribute or nearby
        title_match = re.search(r'title=["\']([^"\']*)["\']', img_tag)
        title = title_match.group(1) if title_match else ""

        image_class = get_image_class(align)
        if title:
            escaped_title = title.replace('"', '\\"')
            return f'{{{{< image src="{src}" title="{escaped_title}" classes="{image_class}" >}}}}'

        return f'{{{{< image src="{src}" classes="{image_class}" >}}}}'
    
    # Convert images
    content = re.sub(r'<img[^>]*/?>', convert_image, content)
    
    # Convert links
    def convert_link(match):
        href = match.group(1)
        link_text = match.group(2)
        return f'[{link_text}]({href})'
    
    content = re.sub(r'<a[^>]*href=["\']([^"\']*)["\'][^>]*>(.*?)</a>', convert_link, content, flags=re.DOTALL)
    
    # Convert formatting
    content = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', content, flags=re.DOTALL)
    content = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', content, flags=re.DOTALL)
    content = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', content, flags=re.DOTALL)
    content = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', content, flags=re.DOTALL)
    content = re.sub(r'<s[^>]*>(.*?)</s>', r'~~\1~~', content, flags=re.DOTALL)
    content = re.sub(r'<strike[^>]*>(.*?)</strike>', r'~~\1~~', content, flags=re.DOTALL)
    content = re.sub(r'<del[^>]*>(.*?)</del>', r'~~\1~~', content, flags=re.DOTALL)
    
    # Convert headers
    content = re.sub(r'<h1[^>]*>(.*?)</h1>', r'# \1', content, flags=re.DOTALL)
    content = re.sub(r'<h2[^>]*>(.*?)</h2>', r'## \1', content, flags=re.DOTALL)
    content = re.sub(r'<h3[^>]*>(.*?)</h3>', r'### \1', content, flags=re.DOTALL)
    content = re.sub(r'<h4[^>]*>(.*?)</h4>', r'#### \1', content, flags=re.DOTALL)
    content = re.sub(r'<h5[^>]*>(.*?)</h5>', r'##### \1', content, flags=re.DOTALL)
    content = re.sub(r'<h6[^>]*>(.*?)</h6>', r'###### \1', content, flags=re.DOTALL)
    
    # Convert paragraphs - replace with double newlines
    content = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', content, flags=re.DOTALL)
    
    # Convert line breaks
    content = re.sub(r'<br\s*/?>', '\n', content)
    
    # Convert blockquotes
    def convert_blockquote(match):
        quote_body = match.group(1).strip()
        quote_lines = [line.strip() for line in quote_body.split('\n') if line.strip()]
        if not quote_lines:
            return ''
        return '\n'.join(f'> {line}' for line in quote_lines) + '\n'

    content = re.sub(r'<blockquote[^>]*>(.*?)</blockquote>', convert_blockquote, content, flags=re.DOTALL)
    
    # Convert code blocks and inline code
    content = re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', r'```\n\1\n```', content, flags=re.DOTALL)
    content = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', content, flags=re.DOTALL)
    
    # Convert lists
    content = re.sub(r'<ul[^>]*>', '', content)
    content = re.sub(r'</ul>', '\n', content)
    content = re.sub(r'<ol[^>]*>', '', content)
    content = re.sub(r'</ol>', '\n', content)
    content = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1', content, flags=re.DOTALL)
    
    # Remove remaining HTML tags (but protect Hugo shortcodes)
    # First protect Hugo shortcodes by temporarily replacing them
    shortcodes = []
    def protect_shortcode(match):
        shortcodes.append(match.group(0))
        return f"HUGO_SHORTCODE_{len(shortcodes)-1}"
    
    content = re.sub(r'{{<[^>]+>}}', protect_shortcode, content)
    
    # Now remove HTML tags
    content = re.sub(r'<[^>]+>', '', content)
    
    # Restore Hugo shortcodes in reverse index order to avoid prefix collisions
    # (e.g. HUGO_SHORTCODE_1 appearing inside HUGO_SHORTCODE_10).
    for i in range(len(shortcodes) - 1, -1, -1):
        content = content.replace(f"HUGO_SHORTCODE_{i}", shortcodes[i])
    
    # Clean up extra whitespace
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)  # Multiple newlines to double
    content = content.strip()
    
    return content

def extract_youtube_id(url):
    """Extract YouTube video ID from various YouTube URL formats"""
    import re
    
    # Common YouTube URL patterns
    patterns = [
        r'(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/)([a-zA-Z0-9_-]{11})',
        r'youtube\.com/watch\?.*?v=([a-zA-Z0-9_-]{11})',
        r'youtube\.com/v/([a-zA-Z0-9_-]{11})',  # for iframe src format
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    
    return None

def convert_youtube_links(content):
    """Convert YouTube links and embeds to Hugo shortcodes"""
    import re
    
    # First, convert YouTube iframes to shortcodes
    def replace_youtube_iframe(match):
        src = match.group(1)
        video_id = extract_youtube_id(src)
        if video_id:
            return f'{{{{< youtube {video_id} >}}}}'
        else:
            return match.group(0)  # Return original if can't extract
    
    # Replace YouTube iframes
    content = re.sub(r'<iframe[^>]*src=["\']([^"\']*youtube[^"\']*)["\'][^>]*></iframe>', replace_youtube_iframe, content, flags=re.IGNORECASE)
    
    # Find YouTube links in markdown format
    def replace_youtube_link(match):
        link_text = match.group(1)
        url = match.group(2)
        
        video_id = extract_youtube_id(url)
        if video_id:
            return f'{{{{< youtube {video_id} >}}}}'
        else:
            # Return original link if we can't extract video ID
            return f'[{link_text}]({url})'
    
    # Replace markdown YouTube links
    content = re.sub(r'\[([^\]]*)\]\((https?://(?:www\.)?(?:youtube\.com|youtu\.be)[^\)]+)\)', replace_youtube_link, content)
    
    # Also handle bare YouTube URLs (not in link format)
    def replace_bare_youtube_url(match):
        url = match.group(0)
        video_id = extract_youtube_id(url)
        if video_id:
            return f'{{{{< youtube {video_id} >}}}}'
        else:
            return url
    
    # Replace bare YouTube URLs
    content = re.sub(r'https?://(?:www\.)?(?:youtube\.com/watch\?[^\s]+|youtu\.be/[^\s]+|youtube\.com/v/[^\s&]+)', replace_bare_youtube_url, content)
    
    return content

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

def find_featured_image(item, child_items):
    """Find featured image URL and whether it came from content fallback.

    Returns:
        tuple[str | None, bool]: (image_url, used_content_fallback)
    """
    # First check for _thumbnail_id in postmeta
    thumbnail_id = None
    postmeta_elements = item.findall('.//{http://wordpress.org/export/1.2/}postmeta')
    
    for postmeta in postmeta_elements:
        meta_key = postmeta.find('.//{http://wordpress.org/export/1.2/}meta_key')
        meta_value = postmeta.find('.//{http://wordpress.org/export/1.2/}meta_value')
        
        if meta_key is not None and meta_key.text == '_thumbnail_id':
            if meta_value is not None and meta_value.text:
                thumbnail_id = meta_value.text
                break
    
    # If we found a thumbnail ID, look for the corresponding attachment
    if thumbnail_id and child_items:
        for child_item in child_items:
            post_id_elem = child_item.find('.//{http://wordpress.org/export/1.2/}post_id')
            if post_id_elem is not None and post_id_elem.text == thumbnail_id:
                # Found the attachment, get the URL
                attachment_url_elem = child_item.find('.//{http://wordpress.org/export/1.2/}attachment_url')
                if attachment_url_elem is not None and attachment_url_elem.text:
                    return attachment_url_elem.text, False
    
    # No featured image found via postmeta, check content for first image
    content_elem = item.find('.//{http://purl.org/rss/1.0/modules/content/}encoded')
    if content_elem is not None and content_elem.text:
        import re
        content = content_elem.text
        
        # Look for img tags in the content
        img_pattern = r'<img[^>]*src=["\']([^"\']*)["\'][^>]*/?>'
        img_matches = re.findall(img_pattern, content, re.IGNORECASE)
        
        if img_matches:
            # Return the first image URL found
            return img_matches[0], True
    
    return None, False

def remove_promoted_featured_image(post_content, featured_image_url):
    """Remove the first in-body image when it has been promoted to featured image."""
    def normalize_after_removal(content):
        # Keep intentional leading spacing (e.g., when first body image is removed)
        # while preventing runaway blank-line expansion.
        content = re.sub(r'\n{3,}', '\n\n', content)
        return content.rstrip()

    if not post_content:
        return post_content

    # Try the most precise removals first: match image blocks that reference the promoted URL.
    if featured_image_url:
        escaped_url = re.escape(featured_image_url)

        # Hugo figure shortcode generated from captions/block figures.
        content, count = re.subn(
            rf'\n?[ \t]*\{{\{{<\s*image\s+[^>]*src="{escaped_url}"[^>]*>\}}\}}[ \t]*\n?',
            '\n\n',
            post_content,
            count=1,
            flags=re.IGNORECASE,
        )
        if count:
            return normalize_after_removal(content)

        # Markdown image with optional title.
        content, count = re.subn(
            rf'\n?[ \t]*!\[[^\]]*\]\({escaped_url}(?:\s+"[^"]*")?\)[ \t]*\n?',
            '\n\n',
            post_content,
            count=1,
        )
        if count:
            return normalize_after_removal(content)

    # Fallback: remove the first image-like element if URL-specific matching failed.
    content, count = re.subn(
        r'\n?[ \t]*\{{\{{<\s*image\s+[^>]*>\}}\}}[ \t]*\n?',
        '\n\n',
        post_content,
        count=1,
        flags=re.IGNORECASE,
    )
    if count:
        return normalize_after_removal(content)

    content, count = re.subn(
        r'\n?[ \t]*!\[[^\]]*\]\([^\)]*\)[ \t]*\n?',
        '\n\n',
        post_content,
        count=1,
    )
    if count:
        return normalize_after_removal(content)

    return post_content

def markdown_to_plain_text(text):
    """Convert markdown-ish text to plain text for metadata fields."""
    if not text:
        return ""

    plain = unescape(text)

    # Remove Hugo shortcodes from metadata text.
    plain = re.sub(r'\{\{<[^>]+>\}\}', ' ', plain)

    # Keep visible text, drop markdown URL wrappers.
    plain = re.sub(r'!\[([^\]]*)\]\([^\)]*\)', r'\1', plain)
    plain = re.sub(r'\[([^\]]+)\]\([^\)]*\)', r'\1', plain)

    # Remove common markdown decorations.
    plain = re.sub(r'`([^`]*)`', r'\1', plain)
    plain = re.sub(r'\*\*([^*]+)\*\*', r'\1', plain)
    plain = re.sub(r'__([^_]+)__', r'\1', plain)
    plain = re.sub(r'\*([^*]+)\*', r'\1', plain)
    plain = re.sub(r'_([^_]+)_', r'\1', plain)
    plain = re.sub(r'~~([^~]+)~~', r'\1', plain)

    # Remove HTML tags and line-level markdown tokens.
    plain = re.sub(r'<[^>]+>', ' ', plain)
    plain = re.sub(r'(?m)^\s{0,3}(?:[-*+]\s+|\d+\.\s+|>\s*)', '', plain)
    plain = re.sub(r'(?m)^\s{0,3}#{1,6}\s*', '', plain)

    plain = re.sub(r'\s+', ' ', plain).strip()
    return plain

def extract_first_25_words(post_content):
    """Extract the first 25 words from the first non-image content block."""
    if not post_content:
        return ""

    blocks = re.split(r'\n\s*\n', post_content)
    for block in blocks:
        text = block.strip()
        if not text:
            continue

        # Skip image-only blocks and image shortcodes.
        if re.fullmatch(r'\{\{<\s*image\s+[^>]*>\}\}', text, flags=re.IGNORECASE):
            continue

        # Keep paragraph text compact for YAML front matter.
        text = markdown_to_plain_text(text)
        if text:
            words = text.split()
            if not words:
                return ""
            return " ".join(words[:25]) + "..."

    return ""

def extract_and_normalize_taxonomies(item, tag_normalization_dict):
    """Extract categories and tags from WordPress item and normalize them"""
    # Find all category elements in the item
    categories = item.findall('.//category')
    
    # Get the text content and domain of each category/tag
    raw_terms = []
    for category in categories:
        if category.text:
            domain = category.get('domain', '')
            # Map WordPress domains to our CSV types
            if domain == 'category':
                term_type = 'category'
            elif domain == 'post_tag':
                term_type = 'tag'
            else:
                term_type = domain  # fallback to original domain
            
            raw_terms.append((category.text, term_type))
    
    # Group by type (left part of tuple) with normalized values (right part of tuple) as lists
    taxonomy_dict = {}
    for term_text, term_type in raw_terms:
        if term_text in tag_normalization_dict:
            # Get the normalized tuple (type, normalized_name)
            normalized_type, normalized_name = tag_normalization_dict[term_text]
        else:
            # Pass through unchanged under its original type
            normalized_type, normalized_name = term_type, term_text

        if normalized_type not in taxonomy_dict:
            taxonomy_dict[normalized_type] = []
        if normalized_name not in taxonomy_dict[normalized_type]:
            taxonomy_dict[normalized_type].append(normalized_name)
    
    return taxonomy_dict

def create_hugo_post(item, child_items=None, tag_normalization_dict=None, tags_only=True):
    """Create a Hugo markdown file with frontmatter from WordPress XML item"""
    
    if child_items is None:
        child_items = []
    
    if tag_normalization_dict is None:
        tag_normalization_dict = {}
    
    # Extract required fields from the item
    title_elem = item.find('title')
    link_elem = item.find('link')
    post_date_elem = item.find('.//{http://wordpress.org/export/1.2/}post_date')
    content_elem = item.find('.//{http://purl.org/rss/1.0/modules/content/}encoded')
    excerpt_elem = item.find('.//{http://wordpress.org/export/1.2/excerpt/}encoded')
    if excerpt_elem is None:
        excerpt_elem = item.find('.//{http://wordpress.org/export/1.2/excerpt}encoded')
    
    if title_elem is None or link_elem is None or post_date_elem is None:
        print("Missing required fields for post, skipping...")
        return False
    
    title = title_elem.text if title_elem.text else "Untitled"
    link_url = link_elem.text if link_elem.text else ""
    post_date = post_date_elem.text if post_date_elem.text else ""
    content_encoded = content_elem.text if content_elem is not None and content_elem.text else ""
    excerpt_encoded = excerpt_elem.text if excerpt_elem is not None and excerpt_elem.text else ""
    
    # Extract slug from URL
    slug = extract_slug_from_url(link_url)
    if not slug:
        print(f"Could not extract slug from URL: {link_url}")
        return False
    
    # Extract year, month, day from the date
    try:
        dt = datetime.strptime(post_date, '%Y-%m-%d %H:%M:%S')
        year = dt.strftime('%Y')
        month = dt.strftime('%m')
        day = dt.strftime('%d')
    except ValueError:
        print(f"Error parsing date for directory structure: {post_date}")
        return False
    
    # Create directory structure
    post_dir = Path(f'content/posts/{year}/{month}/{day}')
    post_dir.mkdir(parents=True, exist_ok=True)
    
    # Create the markdown file
    file_path = post_dir / f'{slug}.md'
    
    # Convert date to ISO format
    iso_date = parse_wordpress_date(post_date)
    if not iso_date:
        return False
    
    # Normalize title text for front matter serialization
    if title:
        normalized_title = title.replace('\n', ' ').replace('\r', ' ')
    else:
        normalized_title = "Untitled"

    # Rewrite chasingdings.com URLs to new host
    link_url = rewrite_upload_url(link_url)

    # Process the WordPress content to Markdown
    post_content = rewrite_upload_url(process_wordpress_content(content_encoded))
    
    # Find featured image from postmeta and child items
    featured_image_url, used_content_fallback = find_featured_image(item, child_items)
    featured_image_url = rewrite_upload_url(featured_image_url)

    # If the featured image is promoted from the first in-body image, remove it from content.
    if used_content_fallback and featured_image_url:
        post_content = remove_promoted_featured_image(post_content, featured_image_url)

    # Use explicit excerpt when available; otherwise use the first 25 words.
    if excerpt_encoded.strip():
        summary_text = re.sub(r'[\r\n]+', ' ', excerpt_encoded)
        summary_text = re.sub(r'\s+', ' ', summary_text).strip()
        summary_text = markdown_to_plain_text(summary_text)
    else:
        summary_text = extract_first_25_words(post_content)
    
    # Extract and normalize categories and tags
    taxonomies = extract_and_normalize_taxonomies(item, tag_normalization_dict)
    
    def escape_yaml_string(value):
        """Escape text for YAML double-quoted strings."""
        return value.replace('\\', '\\\\').replace('"', '\\"')

    def yaml_list_block(key, values):
        """Build a YAML list block with proper escaping."""
        lines = [f"{key}:"]
        for value in values:
            lines.append(f"  - \"{escape_yaml_string(value)}\"")
        return "\n".join(lines)

    def dedupe_preserve_order(values):
        """Deduplicate a sequence while preserving input order."""
        seen = set()
        result = []
        for value in values:
            if value not in seen:
                seen.add(value)
                result.append(value)
        return result

    # Create Hugo frontmatter in YAML format
    frontmatter_lines = [
        "---",
        f"date: '{iso_date}'",
        "draft: false",
        f"title: \"{escape_yaml_string(normalized_title)}\"",
        "author: \"Tipa\"",
    ]

    frontmatter_lines.append(f"summary: \"{escape_yaml_string(summary_text)}\"")

    categories = dedupe_preserve_order(taxonomies.get('category', []))
    tags = dedupe_preserve_order(taxonomies.get('tag', []))

    if categories:
        frontmatter_lines.append(yaml_list_block("categories", categories))

    if tags:
        frontmatter_lines.append(yaml_list_block("tags", tags))

    escaped_featured = escape_yaml_string(featured_image_url) if featured_image_url else ""
    if escaped_featured:
        frontmatter_lines.append(f"coverImage: \"{escaped_featured}\"")
        frontmatter_lines.append(f"thumbnailImage: \"{escaped_featured}\"")

    body_prefix = f"{summary_text}\n<!--more-->\n\n" if summary_text else "<!--more-->\n\n"
    frontmatter = "\n".join(frontmatter_lines) + f"\n---\n{body_prefix}{post_content}\n"
    
    # Write the file
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(frontmatter)
        print(f"Created: {file_path}")
        return True
    except Exception as e:
        print(f"Error creating file {file_path}: {e}")
        return False