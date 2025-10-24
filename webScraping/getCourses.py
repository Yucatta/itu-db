import requests
from bs4 import BeautifulSoup
import re,json,time

with open("faculties.json",mode="r") as f:
    faculties = json.load(f)

# 1. Get the page HTML (same as curl)
BASE_URL = "https://obs.itu.edu.tr"
# url = "https://obs.itu.edu.tr/public/DersPlan/DersPlanDetay/2340"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

for faculty_name,faculty_courses in faculties.items():
	faculty_course_times = {}
	for course in faculty_courses:
		url = f"https://obs.itu.edu.tr/public/DersPlan/DersPlanlariList?PlanTipiKodu=lisans&programKodu={course["programKodu"]}"
		response = requests.get(url, headers=headers, timeout=10)
		html = response.text
		soup = BeautifulSoup(html, "html.parser")

		target_class = "datalist table table-striped table-bordered compact small" 
		table = soup.find("table", class_=target_class)

		donemler = [c.get_text(strip=True) for c in table.find_all("a")]
		rows = table.find_all("tr")
		rows = rows[1:]
		time_codes = []
		for row in rows:
			cells = [c for c in row.find_all(["td", "th"])]
			link_tag = cells[0].find("a", class_="btn btn-default btn-xs btn-info")
			if link_tag:
				href = link_tag["href"]
				text = link_tag.get_text(strip=True)
				time_codes.append([href.split("/")[-1] ,cells[1].get_text(strip=True)])
				print(href.split("/")[-1] ,cells[1].get_text(strip=True))
		faculty_course_times[course["programKodu"]] = time_codes
	
	with open(f"Faculties/{faculty_name.replace(" ","_")}.json",mode="w") as f:
		json.dump(faculty_course_times,f)
	time.sleep(1)
	print("hello world")
	

	





