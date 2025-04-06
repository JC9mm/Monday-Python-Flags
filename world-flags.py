import requests

# API for country data
URL = "https://restcountries.com/v3.1/all"

# Get country data
response = requests.get(URL)
countries = response.json()

# Generate Markdown
markdown_lines = []

for country in sorted(countries, key=lambda x: x["name"]["common"]):
    name = country["name"]["common"]
    code = country.get("cca2", "").lower()
    if not code:
        continue
    flag_url = f"https://flagcdn.com/w320/{code}.png"
    line = f"### {name}\n![{name}]({flag_url})\n"
    markdown_lines.append(line)

# Save to file
with open("world_flags.md", "w", encoding="utf-8") as f:
    f.writelines(markdown_lines)

print("Markdown file with world flags generated: world_flags.md")
