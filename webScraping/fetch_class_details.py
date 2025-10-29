import requests
from bs4 import BeautifulSoup
import re, json, time, os 
from pathlib import Path

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
course_object_keys = ["Ders Kodu","Ders Adı","Ders Dili","Z/S","Kredi","AKTS","Teo.","Uyg.","Lab.","Türü"]

class_regex = r"\b[A-Z]{3}\s\d{3}E?\b"

with open("all_classes.json",mode="r", encoding="utf-8") as f:
    all_classes = json.load(f)


for class_info in all_classes:
    url = f"https://obs.itu.edu.tr/public/DersBilgi/DersBilgiSearch?bransKodu={"BLG"}&dersNo={"335"}"
    response = requests.get(url, headers=headers, timeout=10)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    target_class = "table table-bordered" 
    tables = soup.find_all("table", class_=target_class)
    print("----------------------------------")
    tables = tables[0].find_all("table", class_=target_class)


    prerequisete_row = tables[2].find_all("tr")[1]
    Equivalence_row = tables[3].find_all("tr")[1]

    prerequisete_cell = [c.get_text(strip=True) for c in prerequisete_row.find_all(["td", "th"])][1]
    Equivalence_cell = [c.get_text(separator="|", strip=True) for c in Equivalence_row.find_all(["td", "th"])][0]


    requisetes = []

    requisete_and_parts = prerequisete_cell.split("Ve(")

    for part in requisete_and_parts:
        part = part.replace("MIN"," ")
        or_classes = re.findall(class_regex,part)
        requisetes.append(or_classes)

    Equivalences = re.findall(class_regex,Equivalence_cell)


print(Equivalences,requisetes)





