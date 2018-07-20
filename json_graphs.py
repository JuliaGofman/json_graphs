# входные данные в формате json. Вывести для каждого предка количество потомков
# import json
# data = json.loads(input())
# data = [{"name": "G", "parents": ["F"]}, {"name": "A", "parents": []},
#         {"name": "B", "parents": ["A"]}, {"name": "C", "parents": ["A"]},
#         {"name": "D", "parents": ["B", "C"]}, {"name": "E", "parents": ["D"]},
#         {"name": "F", "parents": ["D"]}, {"name": "X", "parents": []},
#         {"name": "Y", "parents": ["X", "A"]}, {"name": "Z", "parents": ["X"]},
#         {"name": "V", "parents": ["Z", "Y"]}, {"name": "W", "parents": ["V"]}]
# создаем словарь потомок: [предки]
# dict1 = {}
# for el in data:
#     if el["name"] not in dict1:
#         dict1[el["name"]] = el['parents']
# print(dict1)
# рекурсией находим всех предков для каждого потомка
# def find_path(start, path):
#     path.add(start)
#     for node in dict1[start]:
#         if node not in path:
#             find_path(node, path)
# выводим для каждого потомка количество предков
# for i in dict1:
#     path = set()
#     find_path(i, path)
#     print(i, ':', len(path), path)

# data = [
#   {"name": "kvrwxkmqfy", "parents": ["zemrehxvuo", "qzntzflodp", "pjvisgmdrw"]},
#   {"name": "ogqoyccgkn", "parents": ["ppcmlxqgmn", "titthqeskb"]},
#   {"name": "uhfdrfrhzx", "parents": ["ogqoyccgkn", "ppcmlxqgmn", "wubwjzolrx", "pjvisgmdrw", "titthqeskb"]},
#   {"name": "zemrehxvuo", "parents": ["uhfdrfrhzx", "wubwjzolrx", "pjvisgmdrw", "titthqeskb"]},
#   {"name": "ppcmlxqgmn", "parents": ["pjvisgmdrw", "thceozowkb"]},
#   {"name": "qzntzflodp", "parents": ["wubwjzolrx", "titthqeskb", "thceozowkb"]},
#   {"name": "wubwjzolrx", "parents": []},
#   {"name": "pjvisgmdrw", "parents": []},
#   {"name": "titthqeskb", "parents": ["wubwjzolrx", "pjvisgmdrw"]},
#   {"name": "thceozowkb", "parents": ["pjvisgmdrw", "titthqeskb"]}
# ]
data = [{"name": "B", "parents": ["A", "C"]},
        {"name": "C", "parents": ["A"]},
        {"name": "A", "parents": []},
        {"name": "D", "parents":["C", "F"]},
        {"name": "E", "parents":["D"]},
        {"name": "F", "parents":[]}]

# создаем словарь для ответов и словарь предок: [потомки]
dict_answer, dict2 = {}, {}
for el in data:
    if el['parents'] == [] and el['name'] not in dict2:
        dict2[el['name']] = [el['name']]
    else:
        for i in el['parents']:
            if i not in dict2:
                dict2[i] = [el['name']]
            else:
                dict2[i] += [el['name']]

for elem in data:
    if elem['name'] not in dict2:
        dict2[elem['name']] = [elem['name']]

# находим всех потомков для каждого предка рекурсией
def find_path(start, path):
    path.add(start)
    for node in dict2[start]:
        if node not in path and node in dict2:
            find_path(node, path)
        else:
            path.add(node)
#  и добавляем их в словарь ответов
for i in dict2:
    way = set()
    find_path(i, way)
    dict_answer[i] = len(way)

#  выводим ответы в лексикографическом порядке
for key, value in sorted(dict_answer.items()):
    print(key, ':', value)
