import re

logic = """	( ( BLG 221 MIN. DD Or BLG 221E MIN. DD )
Or ( BLG 223 MIN. DD Or BLG 223E MIN. DD )
Or ( YZV 201 MIN. DD Or YZV 201E MIN. DD )
Or ( BLG 233 MIN. DD Or BLG 233E MIN. DD ) )
And( ( BLG 252 MIN. DD Or BLG 252E MIN. DD )
Or ( YZV 201 MIN. DD Or YZV 201E MIN. DD ) )"""


logic = logic.strip()
and_parts = logic.split("And")

requisetes = []

class_regex = r"\b[A-Z]{3}\s\d{3}E?\b"

for part in and_parts:
    or_classes = re.findall(class_regex,part)
    requisetes.append(or_classes)

print(requisetes)
    


