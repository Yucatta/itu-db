import requests
from bs4 import BeautifulSoup
import json

headers_get = {
    "Accept": "*/*",
    "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0"
}

data = {}

def scrape_test(id):
    url = f"https://obs.itu.edu.tr/public/DersProgram/DersProgramSearch?programSeviyeTipiAnahtari=LS&dersBransKoduId={id}"
    response = requests.get(url, headers=headers_get)
    soup = BeautifulSoup(response.text, 'html.parser')
    rows = soup.select("#dersProgramContainer tbody tr")


    for row in rows:
        columns = row.find_all("td")
        if not columns or len(columns) < 11:
            continue


        crn = columns[0].get_text(strip=True)
        derslik = columns[8]
        saat = columns[7]
        gun = columns[6]
        bina = columns[5]

        

        derslik_parts = derslik.get_text(separator="|", strip=True).split("|")
        derslik_parts = [p.strip() for p in derslik_parts if p.strip()]
        if derslik_parts[0] == "-" or derslik_parts[0] == "--":
            continue

        saat_parts = saat.get_text(separator="|", strip=True).split("|")
        saat_parts = [p.strip() for p in saat_parts if p.strip()]

        gun_parts = gun.get_text(separator="|", strip=True).split("|")
        gun_parts = [p.strip() for p in gun_parts if p.strip()]

        bina_parts = bina.get_text(separator="|", strip=True).split("|")
        bina_parts = [p.strip() for p in bina_parts if p.strip()]
        for b in bina_parts:
            if not b in data:
                data[b] = {}

        if derslik_parts[0] in data[bina_parts[0]] and gun_parts[0] in data[bina_parts[0]][derslik_parts[0]]:
            data[bina_parts[0]][derslik_parts[0]][gun_parts[0]].append(saat_parts[0])
        elif derslik_parts[0] in data[bina_parts[0]]:
            data[bina_parts[0]][derslik_parts[0]][gun_parts[0]] = [saat_parts[0]]
        else:
            _object = {gun_parts[0]: [saat_parts[0]]}
            data[bina_parts[0]][derslik_parts[0]] = _object

        if len(gun_parts) > 1:
            if derslik_parts[1] in data[bina_parts[1]] and gun_parts[1] in data[bina_parts[1]][derslik_parts[1]]:
                data[bina_parts[1]][derslik_parts[1]][gun_parts[1]].append(saat_parts[1])
            elif derslik_parts[1] in data[bina_parts[1]]:
                data[bina_parts[1]][derslik_parts[1]][gun_parts[1]] = [saat_parts[1]]
            else:
                _object = {gun_parts[1]: [saat_parts[1]]}
                data[bina_parts[1]][derslik_parts[1]] = _object 

with open("derskodlari.json", "r") as file:
    derskodlari = json.load(file)

for ders in derskodlari:
    scrape_test(ders["bransKoduId"])
    print(f"{ders["bransKoduId"]} {ders["dersBransKodu"]} bitti")

    with open("output.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)  # indent=4 makes it pretty-printed


# data = BBF:{
#         "Z-17": {
#             "Pazartesi": ["8.30/11.30", "14.30/17.30"]
#         }
#     }

# gun= {
#     "dersin gunu": "asdasdasd"
# }

# data["a"] = gun
# data["a"]["dersin gun"] = "sdasd" 
# print(data)