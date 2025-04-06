import os
import re
import requests

# Path to the Markdown file
markdown_file = "/workspaces/Monday-Python-Flags/world_flags.md"

# Directory to save the downloaded PNG files
output_dir = "/workspaces/Monday-Python-Flags/flags-png"
os.makedirs(output_dir, exist_ok=True)

# Regular expression to extract country names and image URLs from Markdown
pattern = r"### (.*?)\n!\[.*?\]\((https://flagcdn\.com/w320/.*?\.png)\)"

# Read the Markdown file
with open(markdown_file, "r", encoding="utf-8") as file:
    content = file.read()

# Find all matches for country names and image URLs
matches = re.findall(pattern, content)

# Download each image
for country_name, url in matches:
    try:
        # Create a valid filename from the country name
        filename = f"{country_name.replace(' ', '_').replace(',', '').replace('&', 'and')}.png"
        output_path = os.path.join(output_dir, filename)

        # Download the image
        print(f"Downloading {url} for {country_name}...")
        response = requests.get(url)
        response.raise_for_status()

        # Save the image to the output directory
        with open(output_path, "wb") as img_file:
            img_file.write(response.content)
        print(f"Saved: {output_path}")
    except requests.RequestException as e:
        print(f"Failed to download {url} for {country_name}: {e}")

print("Download complete.")