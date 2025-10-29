import requests
from bs4 import BeautifulSoup
import re, json, time, os, pprint
from pathlib import Path

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
course_object_keys = ["Ders Kodu","Ders Adı","Ders Dili","Z/S","Kredi","AKTS","Teo.","Uyg.","Lab.","Türü"]

BASE_URL = "https://obs.itu.edu.tr"

folder = Path("Faculties")

os.mkdir("Courses")

for file in folder.glob("*.json"):
    with open(file, "r", encoding="utf-8") as f:
        faculty_courses = json.load(f)

    os.mkdir(f"Courses/{file.stem}")
    for course, Plans in faculty_courses.items():
        os.mkdir(f"Courses/{file.stem}/{course}")

        for plan in Plans:
            url = f"https://obs.itu.edu.tr/public/DersPlan/DersPlanDetay/{plan[0]}"
            response = requests.get(url, headers=headers, timeout=30)
            html = response.text
            soup = BeautifulSoup(html, "html.parser")

            target_class = "datalist table table-striped table-bordered compact small" 
            tables = soup.find_all("table", class_=target_class)


            current_course = []

            for i, table in enumerate(tables, start=1):
                current_semester = []
                rows = table.find_all("tr")
                rows = rows[2:]
                for row in rows:
                    cells = row.find_all(["td", "th"])
                    cell_details = {}
                    selective_classes = 0
                    if cells[0].get_text(strip=True) == "Dersler":
                        link_tag = cells[0].find("a")

                        href = link_tag["href"]
                        cell_details["href"] = href
                        # response = requests.get(BASE_URL + href, headers=headers, timeout=10)
                        # html = response.text
                        # soup = BeautifulSoup(html, "html.parser")
                        # selective_table = soup.find("table", class_=target_class)

                        # selective_classes = []
                        # rows = selective_table.find_all("tr")
                        # rows = rows[1:]
                        # for row in rows:
                        #     selective_cells = row.find_all(["td", "th"])
                        #     selective_cell_details = {}

                        #     selective_class_code_name = selective_cells[0].get_text(separator="|", strip=True).split("|")

                        #     selective_cells = [*selective_class_code_name ,*[c.get_text(strip=True) for c in selective_cells[1:]]]

                        #     if len(selective_cells[0]) > 8: 
                        #         selective_cells[0] = selective_cells[0][0:7]

                        #     for i,cell in enumerate(selective_cells):
                        #         selective_cell_details[course_object_keys[i]] = cell
                        #     selective_classes.append(selective_cell_details)
                        # cell_details["selective_classes"] = selective_classes


                    for i,cell in enumerate(cells):
                        if i == 0 and len(cell.get_text(strip=True)) > 8:
                            cell_details[course_object_keys[i]] = cell.get_text(strip=True)[0:7]

                        else:
                            cell_details[course_object_keys[i]] = cell.get_text(strip=True)                   
                    current_semester.append(cell_details)

                current_course.append(current_semester)

            with open(f"Courses/{file.stem}/{course}/{plan[0]}.json",mode="w", encoding="utf-8") as f:
                json.dump(current_course,f,ensure_ascii=False)
            
            print(f"completed Courses/{file.stem}/{course}/{plan[0]}.json")
            # time.sleep(10)
        print(f"Completed {course} ---------------------")

    print(f"Completed {file.stem} ---------------------")


    