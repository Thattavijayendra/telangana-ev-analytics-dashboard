import requests
from pathlib import Path
from urllib.parse import urlparse
import re

# 1. API URL
# https://data.telangana.gov.in/api/1/metastore/schemas/dataset/items/d50f805e-e5ac-48ff-9b7a-40402c8b6e64?show-reference-ids   -- south data
# https://data.telangana.gov.in/api/1/metastore/schemas/dataset/items/6c3628e1-89b3-4d53-9087-10e32dc4be22?show-reference-ids   -- north data

API_URL = (
    "https://data.telangana.gov.in/api/1/metastore/"
    "schemas/dataset/items/"
    "d50f805e-e5ac-48ff-9b7a-40402c8b6e64"
    "?show-reference-ids"
)


# 2. Main data folder


BASE_DIR = Path("TGSPDCL/raw")



# 3. Get dataset metadata


print("Connecting to Telangana Open Data API...")

response = requests.get(API_URL, timeout=30)
response.raise_for_status()

data = response.json()

print("API connection successful!")



# 4. Get all CSV files


files = []

for item in data.get("distribution", []):

    info = item.get("data", {})

    title = info.get("title")
    file_format = info.get("format")
    download_url = info.get("downloadURL")

    if file_format == "csv" and download_url:
        files.append({
            "title": title,
            "url": download_url
        })


print(f"\nTotal CSV files found: {len(files)}")



# 5. Download each file


successful = []
failed = []

for number, file in enumerate(files, start=1):

    title = file["title"]
    url = file["url"]

    print("\n" + "=" * 60)
    print(f"[{number}/{len(files)}] {title}")
    print("=" * 60)

    
    # Extract year from title
    

    year_match = re.search(r"(20\d{2})", title)

    if not year_match:
        print("Could not identify year.")
        failed.append(title)
        continue

    year = year_match.group(1)

    
    # Extract month
    

    months = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]

    month = None

    for m in months:
        if m.lower() in title.lower():
            month = m
            break

    if month is None:
        print("Could not identify month.")
        failed.append(title)
        continue

    
    # Create year folder
    

    year_folder = BASE_DIR / year
    year_folder.mkdir(parents=True, exist_ok=True)

    
    # File path
    

    output_file = year_folder / f"{month}.csv"

    
    # Download
    

    try:

        print(f"Downloading: {url}")

        file_response = requests.get(
            url,
            timeout=60
        )

        file_response.raise_for_status()

        with open(output_file, "wb") as f:
            f.write(file_response.content)

        print(f"Saved → {output_file}")

        successful.append(title)

    except Exception as e:

        print(f"ERROR: {e}")

        failed.append(title)



# 6. Final summary


print("\n")
print("=" * 60)
print("DOWNLOAD SUMMARY")
print("=" * 60)

print(f"Total files found : {len(files)}")
print(f"Downloaded        : {len(successful)}")
print(f"Failed            : {len(failed)}")

if failed:

    print("\nFailed files:")

    for file in failed:
        print(f"  - {file}")

else:

    print("\n🎉 All files downloaded successfully!")

print("\nData location:")
print(BASE_DIR.resolve())