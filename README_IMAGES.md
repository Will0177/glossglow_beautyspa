# Image Download Script

This script downloads beauty/spa images featuring Black people and updates the HTML to use local images.

## Setup

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Optional: Get Unsplash API Key (for better results)**
   - Go to https://unsplash.com/developers
   - Create a new application
   - Copy your Access Key
   - Update `UNSPLASH_ACCESS_KEY` in `download_images.py`

## Usage

Run the script:
```bash
python download_images.py
```

The script will:
1. Download images to `assets/images/` folder
2. Update `index.html` to use local image paths instead of Unsplash URLs

## Images Downloaded

- 4 hero slider images
- 3 service detail images
- 8 gallery preview images
- 3 team member photos

All images feature Black people in beauty/spa contexts.

## Notes

- Without an API key, the script uses Unsplash Source which is less reliable
- With an API key, you get better search results and more specific images
- Images are saved as JPG files in the `assets/images/` directory

