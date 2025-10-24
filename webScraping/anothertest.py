import requests
import json
url = "https://obs.itu.edu.tr/public/DersPlan/GetAkademikProgramByBirimIdAndPlanTipi"

with open("faculties.json",mode="r") as f:
    faculties = json.load(f)




for key,data in faculties.items():
    faculties[key]["courses"] = json.loads(faculties[key]["courses"])
    # data = {"birimId": key, "planTipiKodu": "lisans"}
    # r = requests.post(url, data=data)
    # faculties[key] = {
    #     name:name,
    #     "courses":r.text,
    # }
    # print(key,data)  # or r.json() if JSON


with open("faculties.json",mode="w") as f:
    json.dump(faculties,f)