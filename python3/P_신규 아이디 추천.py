import re


def solution(new_id):
    new_id = new_id.lower()

    new_id = re.sub('[^a-z0-9\-_.]', '', new_id)
    new_id = re.sub('\.+', '.', new_id)
    new_id = re.sub('^[.]|[.]$', '', new_id)
    new_id = 'a' if new_id == '' else new_id if len(new_id) <= 15 else new_id[:15]
    new_id = re.sub('^[.]|[.]$', '', new_id)
    for _ in range(3 - len(new_id)):
        new_id += new_id[-1]

    return new_id


print(solution("...!@BaT#*..y.abcdefghijklm"))
