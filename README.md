# Monday Python Flags

This project fetches country data from an API, generates a Markdown file with country flags, and provides a script to download the flag images.

## Features

1. **Fetch Country Data**:
   - Retrieves country information, including names and flag URLs, from the [REST Countries API](https://restcountries.com/).

2. **Generate Markdown**:
   - Creates a `world_flags.md` file containing country names and their corresponding flag images.

3. **Download Flag Images**:
   - Downloads flag images from the URLs in the Markdown file and saves them to a local directory.

## Requirements

- Python 3.7 or higher
- `requests` library

Install the required library using:
```bash
pip install requests
```

## Usage

### 1. Fetch Country Data and Generate Markdown
Run the `world-flags.py` script to fetch country data and generate the `world_flags.md` file:
```bash
python world-flags.py
```

### 2. Download Flag Images
Run the `download_flags.py` script to download flag images from the `world_flags.md` file:
```bash
python download_flags.py
```

The images will be saved in the `flags-png` directory.
