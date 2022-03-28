import json

def load_can(path):
    with open(path, 'r', encoding = 'utf-8') as file:
        data = json.load(file)
    return data

def get_candidate(id,data):
    pass

def get_can_name(name,data):
    pass

def get_can_skill(skill,data):
    pass