import re

def remove_endline(data):
    return data.replace('\n', '')

def remove_tags(data):
    return re.sub(r'<[^>]+>', '', data)
