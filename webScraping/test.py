import requests
from bs4 import BeautifulSoup

# 1. Get the page HTML (same as curl)
BASE_URL = "https://obs.itu.edu.tr"
url = "https://obs.itu.edu.tr/public/DersPlan/DersPlanDetay/2340"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers, timeout=10)
html = response.text

# 2. Parse HTML
soup = BeautifulSoup(html, "html.parser")

# 3. Find all tables with a specific class
target_class = "datalist table table-striped table-bordered compact small"  # change to match your actual table class
tables = soup.find_all("table", class_=target_class)

# 4. Handle each table separately

dersler = []

for i, table in enumerate(tables, start=0):
    donemler = [c.get_text(strip=True) for c in table.find_all("a")]
    # print(donemler)
    dersler.append(donemler)
    # dersler.append(donemler)
    
    # print(f"\n--- Table {i} ---")
    # # Extract rows
    # rows = table.find_all("tr")
    # for row in rows:
    #     cells = [c.get_text(strip=True) for c in row.find_all(["td", "th"])]
    #     print(cells)

print(dersler)