#!/usr/bin/env python3
"""
Script to download beauty/spa images featuring Black people from Unsplash
and update the HTML file to use local images.
"""

import os
import requests
import re
from pathlib import Path
from urllib.parse import urlparse

# Try to load from .env file if python-dotenv is available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv not installed, will use environment variables directly

# Configuration
# Get API key from environment variable or .env file
# Priority: environment variable > .env file > default
UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY", "YOUR_UNSPLASH_ACCESS_KEY")
IMAGES_DIR = Path("assets/images")
HTML_FILE = Path("index.html")

# Image mappings: (search_query, filename, description, html_selector)
# html_selector helps identify which image to replace in the HTML
IMAGE_MAPPINGS = [
    # Hero slider images (in order of appearance)
    ("african american woman spa facial luxury", "hero-slide-1.jpg", "Luxury spa interior", "data-slide=\"0\""),
    ("black woman spa relaxation treatment", "hero-slide-2.jpg", "Spa treatment room", "data-slide=\"1\""),
    ("african american woman facial skincare", "hero-slide-3.jpg", "Facial treatment", "data-slide=\"2\""),
    ("black woman massage therapy spa", "hero-slide-4.jpg", "Massage therapy", "data-slide=\"3\""),
    
    # Detailed services section
    ("black woman luxury facial treatment gold", "service-facial-1.jpg", "Luxury facial treatment", "Hydrating Gold Facial"),
    ("african american woman threading eyebrow", "service-threading-1.jpg", "Threading service", "Precision Threading"),
    ("black woman massage therapy deep tissue", "service-massage-1.jpg", "Massage therapy", "Therapeutic Deep Tissue"),
    
    # Gallery preview (8 images) - Updated with more aesthetic searches
    ("african american woman luxury facial spa aesthetic", "gallery-facial-aesthetic.jpg", "Luxury facial treatment", "Luxury facial treatment"),
    ("african american woman hair styling salon", "gallery-2.jpg", "Hair styling", "gallery-2"),
    ("black woman spa treatment relaxation", "gallery-3.jpg", "Spa treatment", "gallery-3"),
    ("black woman beautiful nail art manicure aesthetic", "gallery-nails-aesthetic.jpg", "Beautiful nail art", "Beautiful nail art"),
    ("black woman facial mask skincare", "gallery-5.jpg", "Facial mask", "gallery-5"),
    ("african american woman hair color salon", "gallery-6.jpg", "Hair color", "gallery-6"),
    ("black woman spa room luxury", "gallery-7.jpg", "Spa room", "gallery-7"),
    ("african american woman beauty products", "gallery-8.jpg", "Beauty products", "gallery-8"),
    
    # Team section
    ("professional black woman esthetician", "team-1.jpg", "Lead Esthetician", "Sarah Johnson"),
    ("african american woman threading specialist", "team-2.jpg", "Threading Specialist", "Priya Patel"),
    ("black woman massage therapist professional", "team-3.jpg", "Massage Therapist", "Maria Rodriguez"),
]


def download_image_from_unsplash(query, filename, width=1920, height=1080):
    """
    Download an image from Unsplash based on search query.
    Note: This uses Unsplash Source API which doesn't require authentication for basic usage.
    """
    # Unsplash Source API format
    # For more specific results, we'll use a direct URL with search terms
    # Note: Unsplash Source doesn't support search directly, so we'll use placeholder images
    # For production, you'd need Unsplash API with search functionality
    
    # Alternative: Use Unsplash Source with curated images
    # Format: https://source.unsplash.com/{width}x{height}/?{keywords}
    
    url = f"https://source.unsplash.com/{width}x{height}/?{query.replace(' ', ',')}"
    
    try:
        print(f"Downloading: {filename} (query: {query})...")
        response = requests.get(url, timeout=30, allow_redirects=True)
        response.raise_for_status()
        
        # Save the image
        filepath = IMAGES_DIR / filename
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        print(f"✓ Saved: {filepath}")
        return filepath
        
    except Exception as e:
        print(f"✗ Error downloading {filename}: {e}")
        return None


def download_with_unsplash_api(query, filename, width=1920, height=1080):
    """
    Download image using Unsplash API (requires access key).
    This is more reliable and allows specific searches.
    """
    if UNSPLASH_ACCESS_KEY == "YOUR_UNSPLASH_ACCESS_KEY" or not UNSPLASH_ACCESS_KEY:
        print("⚠ Warning: Using Unsplash Source (less reliable).")
        print("   For better results, get an API key from https://unsplash.com/developers")
        print("   and set it in your .env file or environment variable:")
        print("   export UNSPLASH_ACCESS_KEY='your_key_here'")
        print("   Or create a .env file with: UNSPLASH_ACCESS_KEY=your_key_here")
        return download_image_from_unsplash(query, filename, width, height)
    
    # Search for photos
    search_url = "https://api.unsplash.com/search/photos"
    headers = {"Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"}
    params = {
        "query": query,
        "per_page": 1,
        "orientation": "landscape"
    }
    
    try:
        print(f"Searching Unsplash for: {query}...")
        response = requests.get(search_url, headers=headers, params=params, timeout=30)
        response.raise_for_status()
        
        data = response.json()
        if data['results']:
            image_url = data['results'][0]['urls']['regular']
            
            # Download the image
            print(f"Downloading: {filename}...")
            img_response = requests.get(image_url, timeout=30)
            img_response.raise_for_status()
            
            filepath = IMAGES_DIR / filename
            with open(filepath, 'wb') as f:
                f.write(img_response.content)
            
            print(f"✓ Saved: {filepath}")
            return filepath
        else:
            print(f"✗ No results found for: {query}")
            return None
            
    except Exception as e:
        print(f"✗ Error with API: {e}")
        # Fallback to source API
        return download_image_from_unsplash(query, filename, width, height)


def update_html_file(downloaded_files):
    """Update HTML file to use local images instead of Unsplash URLs."""
    
    if not HTML_FILE.exists():
        print(f"✗ HTML file not found: {HTML_FILE}")
        return
    
    print("\nUpdating HTML file with local image paths...")
    
    # Read the HTML file
    with open(HTML_FILE, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Create mapping from filename to local path
    file_mapping = {Path(f).name: f for f in downloaded_files}
    
    # Replace images based on context in HTML
    updated_count = 0
    
    # Replace hero slider images (by data-slide attribute)
    for i, (query, filename, desc, selector) in enumerate(IMAGE_MAPPINGS[:4], 1):
        if filename in file_mapping:
            # Find img tags within slide divs with matching data-slide
            pattern = rf'(<div class="slide"[^>]*{re.escape(selector)}[^>]*>.*?<img[^>]*src=")[^"]*(")'
            replacement = rf'\1{file_mapping[filename]}\2'
            if re.search(pattern, html_content, re.DOTALL):
                html_content = re.sub(pattern, replacement, html_content, flags=re.DOTALL)
                updated_count += 1
                print(f"  ✓ Updated hero slide {i}: {filename}")
    
    # Replace service images (by alt text or nearby text)
    service_mappings = [
        ("service-facial-1.jpg", "Hydrating Gold Facial"),
        ("service-threading-1.jpg", "Precision Threading"),
        ("service-massage-1.jpg", "Therapeutic Deep Tissue"),
    ]
    
    for filename, search_text in service_mappings:
        if filename in file_mapping:
            # Find img tags near the service title
            pattern = rf'({re.escape(search_text)}.*?<img[^>]*src=")[^"]*(")'
            replacement = rf'\1{file_mapping[filename]}\2'
            if re.search(pattern, html_content, re.DOTALL):
                html_content = re.sub(pattern, replacement, html_content, flags=re.DOTALL)
                updated_count += 1
                print(f"  ✓ Updated service image: {filename}")
    
    # Replace gallery images (by alt text or filename)
    gallery_mappings = [
        ("gallery-facial-aesthetic.jpg", "Luxury facial treatment"),
        ("gallery-2.jpg", "Hair styling"),
        ("gallery-3.jpg", "Spa treatment"),
        ("gallery-nails-aesthetic.jpg", "Beautiful nail art"),
        ("gallery-5.jpg", "Facial mask"),
        ("gallery-6.jpg", "Hair color"),
        ("gallery-7.jpg", "Spa room"),
        ("gallery-8.jpg", "Beauty products"),
    ]
    
    for filename, alt_text in gallery_mappings:
        if filename in file_mapping:
            # Try to find by alt text first
            pattern = rf'(<img[^>]*alt="[^"]*{re.escape(alt_text)}[^"]*"[^>]*src=")[^"]*(")'
            replacement = rf'\1{file_mapping[filename]}\2'
            if re.search(pattern, html_content):
                html_content = re.sub(pattern, replacement, html_content)
                updated_count += 1
                print(f"  ✓ Updated gallery image: {filename} (by alt text)")
            # Also try direct filename replacement in src
            elif filename in str(file_mapping[filename]):
                pattern2 = rf'(src=")[^"]*{re.escape(filename)}(")'
                if re.search(pattern2, html_content):
                    html_content = re.sub(pattern2, rf'\1{file_mapping[filename]}\2', html_content)
                    updated_count += 1
                    print(f"  ✓ Updated gallery image: {filename} (by filename)")
    
    # Replace team images (by name in nearby text)
    team_mappings = [
        ("team-1.jpg", "Sarah Johnson"),
        ("team-2.jpg", "Priya Patel"),
        ("team-3.jpg", "Maria Rodriguez"),
    ]
    
    for filename, name in team_mappings:
        if filename in file_mapping:
            # Find img tags near the team member name
            pattern = rf'({re.escape(name)}.*?<img[^>]*src=")[^"]*(")'
            replacement = rf'\1{file_mapping[filename]}\2'
            if re.search(pattern, html_content, re.DOTALL):
                html_content = re.sub(pattern, replacement, html_content, flags=re.DOTALL)
                updated_count += 1
                print(f"  ✓ Updated team image: {filename}")
    
    # Replace any remaining Unsplash URLs with a fallback
    unsplash_pattern = r'https://images\.unsplash\.com/photo-[^"\']+'
    remaining = len(re.findall(unsplash_pattern, html_content))
    if remaining > 0:
        # Use first gallery image as fallback
        fallback = 'assets/images/gallery-1.jpg' if 'gallery-1.jpg' in file_mapping else None
        if fallback:
            html_content = re.sub(unsplash_pattern, fallback, html_content)
            updated_count += remaining
            print(f"  ✓ Replaced {remaining} remaining Unsplash URLs with fallback")
    
    # Write updated HTML
    with open(HTML_FILE, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"\n✓ Updated {updated_count} image references in HTML file")


def main():
    """Main function to download images and update HTML."""
    
    # Create images directory if it doesn't exist
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Images will be saved to: {IMAGES_DIR.absolute()}\n")
    
    # Download all images
    downloaded = []
    for query, filename, description, html_selector in IMAGE_MAPPINGS:
        filepath = download_with_unsplash_api(query, filename)
        if filepath:
            downloaded.append(filepath)
        print()  # Empty line for readability
    
    print(f"\n{'='*60}")
    print(f"Downloaded {len(downloaded)}/{len(IMAGE_MAPPINGS)} images")
    print(f"{'='*60}\n")
    
    # Update HTML file
    if downloaded:
        update_html_file(downloaded)
        print("\n✓ All done! Images downloaded and HTML updated.")
    else:
        print("\n⚠ No images were downloaded. HTML was not updated.")


if __name__ == "__main__":
    main()

