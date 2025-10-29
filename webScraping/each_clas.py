import re, json, time, os 
from pathlib import Path

folder = Path("Courses")

all_classes = []

count_of_class = 0
count_of_unique_class = 0
for faculty_folder in folder.glob("*"):
    faculty_folder_path = Path(f"Courses/{faculty_folder.stem}")
    for course_folder in faculty_folder_path.glob("*"):
        course_folder_path = Path(f"Courses/{faculty_folder.stem}/{course_folder.stem}")
        for plan_file in course_folder_path.glob("*"):
            with open(plan_file, "r", encoding="utf-8") as f:
                course_plan = json.load(f)
            for semester in course_plan:
                for semester_class in semester: 
                    if not semester_class in all_classes:
                        all_classes.append(semester_class)
                        count_of_unique_class+=1
                    count_of_class+=1

print(count_of_unique_class,count_of_class)

with open("all_classes.json","w", encoding="utf-8") as f:
    json.dump(all_classes, f,ensure_ascii=False)