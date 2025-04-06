import requests

# API for country data
URL = f"https://restcountries.com/v3.1/all"

# Fetch data from the API
try:
    response = requests.get(URL)
    response.raise_for_status()  # Raise an error for bad responses
except requests.RequestException as e:
    print(f"Error fetching data from API: {e}")
    response = None
# Check if the response is valid
if response is None:
    print("No response from the API.")
    countries = []
else:
    # Debug: Print response status code
    print(f"Response status code: {response.status_code}")
    print("Response headers:", response.headers)
# Check if the request was successful

# Generate Markdown
markdown_lines = []

# Ensure countries is a list
if isinstance(countries, list):
    for country in sorted(countries, key=lambda x: x.get("name", {}).get("common", "")):
        name = country.get("name", {}).get("common", "Unknown")
        code = country.get("cca2", "").lower()
        if not code:
            continue
        flag_url = f"https://flagcdn.com/w320/{code}.png"
        line = f"### {name}\n![{name}]({flag_url})\n"
        markdown_lines.append(line)
else:
    print("Error: Unexpected data format. 'countries' is not a list.")

# Save to file
if markdown_lines:
    with open("world_flags.md", "w", encoding="utf-8") as f:
        f.writelines(markdown_lines)
    print("Markdown file with world flags generated: world_flags.md")
else:
    print("No data available to generate the Markdown file.")
