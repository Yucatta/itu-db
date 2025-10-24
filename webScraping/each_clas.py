import re, json, time, os 
from pathlib import Path

folder = Path("Courses")

for faculty_folder in folder.glob("*"):
    faculty_folder_path = Path(f"Courses/{faculty_folder.stem}")
    for course_folder in faculty_folder_path.glob("*"):
        course_folder_path = Path(f"Courses/{faculty_folder.stem}/{course_folder.stem}")
        for plan_file in course_folder_path.glob("*"):
            with open(plan_file, "r", encoding="utf-8") as f:
                course_plan = json.load(f)