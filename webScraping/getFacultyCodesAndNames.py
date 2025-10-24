import re
import json
string = """
                                <option value="1">Faculty of Science and Letters</option>
                                <option value="2">Faculty of Architecture</option>
                                <option value="3">Faculty of Electrical and Electronics Engineering</option>
                                <option value="4">Faculty of Civil Engineering</option>
                                <option value="5">Faculty of Mechanical Engineering</option>
                                <option value="6">Faculty of Mines</option>
                                <option value="7">Faculty of Chemical and Metallurgical Engineering</option>
                                <option value="8">Faculty of Naval Architecture and Ocean Engineering</option>
                                <option value="10">Faculty of Management</option>
                                <option value="13">Faculty of Aeronautics and Astronautics</option>
                                <option value="19">Faculty of Maritime</option>
                                <option value="20">Turkish Classical Music Conservatoire</option>
                                <option value="23">Faculty of Textile Technologies and Design</option>
                                <option value="28">Faculty of Computer and Informatics Engineering</option>
                                <option value="30">ITU-TRNC Education-Research Campuses</option>
                                <option value="33">Graduate School</option>
                                <option value="47">Cyber Security Vocational School</option>
"""

pattern = r'<option\s+value="([^"]*)">([^<]*)<\/option>'

matches = re.findall(pattern, string)

faculties = {} 

for value, name in matches:
    faculties[value] = name

with open("faculties.json",mode="w") as f:
    json.dump(faculties,f)