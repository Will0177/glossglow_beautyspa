# Setting Up Your Unsplash API Key Securely

## Option 1: Using .env File (Recommended)

1. **Install python-dotenv** (if not already installed):
   ```bash
   pip install -r requirements.txt
   ```

2. **Create a `.env` file** in the project root:
   ```bash
   cp .env.example .env
   ```

3. **Edit `.env`** and add your Unsplash API key:
   ```
   UNSPLASH_ACCESS_KEY=your_actual_api_key_here
   ```

4. **The `.env` file is already in `.gitignore`** so it won't be committed to git.

## Option 2: Using Environment Variable (macOS/Linux)

Add to your shell profile (`~/.zshrc` or `~/.bash_profile`):

```bash
export UNSPLASH_ACCESS_KEY="your_actual_api_key_here"
```

Then reload your shell:
```bash
source ~/.zshrc  # or source ~/.bash_profile
```

## Option 3: Set for Current Session Only

```bash
export UNSPLASH_ACCESS_KEY="your_actual_api_key_here"
python download_images.py
```

## Getting Your Unsplash API Key

1. Go to https://unsplash.com/developers
2. Click "Your apps" or "Register as a developer"
3. Create a new application
4. Copy your "Access Key"
5. Use it in one of the methods above

## Verify It's Working

Run the script and you should see it using the API (no warning message):
```bash
python download_images.py
```

If you see the warning about Unsplash Source, the key isn't being loaded correctly.

