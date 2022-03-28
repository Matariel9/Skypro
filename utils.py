import json

def load_can(path):
    with open(path, 'r', encoding = 'utf-8') as file:
        data = json.load(file)
    return data

def get_candidate(id,data):
    for candidate in data:
        if candidate['id'] == id:
            return {
                'name': candidate['name'],
                'position': candidate['position'],
                'picture': candidate['picture'],
                'skills':candidate['skills']
            }

def get_can_name(name,data):
    can = []
    for i in data:
        if name.lower() in i['name'].lower():
            can.append(i)
    return can

def get_can_skill(skill,data):
    can = []
    for i in data:
        if skill.lower() in [a.lower() for a in i['skills'].split(', ')]:
            can.append(i)
            print(len(data))
    return can
