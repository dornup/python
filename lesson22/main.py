import json

# write_f = open("file.json", "w", encoding="utf-8")
# #write_f.write("True")
# content = [None, True, (1,2,3), [1,2,3], "Куку"]
# json.dump(content, write_f, ensure_ascii=False)
# print(json.dumps(content))
# write_f.close()

# read_f = open("file.json", "r", encoding="utf-8")
# # print(read_f.read())
# # print(type(read_f.read()))
# print(json.load(read_f))
# read_f.close()


#задача уан:

# read_f = open("file.txt", "r", encoding="utf-8")
# content = read_f.readlines()
# read_f.close()
#
# print(content)
#
# d = {}
# for record in content:
#     splited = record.split(": ")
#     d[splited[0]] = splited[1].rstrip()
# print(d)
#
# f = open("file.json", "w", encoding="utf-8")
# json.dump(d, f, ensure_ascii=False)
# f.close()

import  requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
data = response.json()["iss_position"]
print(f"Широта: {data['latitude']}\n"
      f"Долгота: {data['longitude']}")

