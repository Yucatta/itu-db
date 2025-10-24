import requests
from bs4 import BeautifulSoup
import re, json, time, os 
from pathlib import Path

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
course_object_keys = ["Ders Kodu","Ders Adı","Ders Dili","Z/S","Kredi","AKTS","Teo.","Uyg.","Lab.","Türü"]

folder = Path("Faculties")

for file in folder.glob("*.json"):
    with open(file, "r", encoding="utf-8") as f:
        faculty_courses = json.load(f)

    os.mkdir(f"Courses/{file.stem}")
    for course, Plans in faculty_courses.items():
        os.mkdir(f"Courses/{file.stem}/{course}")

        for plan in Plans:
            url = f"https://obs.itu.edu.tr/public/DersPlan/DersPlanDetay/{plan[0]}"
            response = requests.get(url, headers=headers, timeout=10)
            html = response.text
            soup = BeautifulSoup(html, "html.parser")

            target_class = "datalist table table-striped table-bordered compact small" 
            tables = soup.find_all("table", class_=target_class)

            # 4. Handle each table separately

            current_course = []


            for i, table in enumerate(tables, start=1):
                current_semester = []
                rows = table.find_all("tr")
                rows = rows[2:]
                for row in rows:
                    cells = [c.get_text(strip=True) for c in row.find_all(["td", "th"])]
                    cell_details = {}
                    for i,cell in enumerate(cells):
                        cell_details[course_object_keys[i]] = cell
                    current_semester.append(cell_details)
                current_course.append(current_semester)

            with open(f"Courses/{file.stem}/{course}/{plan[0]}.json",mode="w") as f:
                json.dump(current_course,f)
            print(f"completed Courses/{file.stem}/{course}/{plan[0]}.json")
        print(f"Completed {course} ---------------------")
    print(f"Completed {file.stem} ---------------------")
    