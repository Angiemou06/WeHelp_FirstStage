import urllib.request as request
import json
import csv

src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data = json.load(response)

clist = data["result"]["results"]

with open("data.csv", "w", newline="", encoding="UTF-8-Sig") as csvfile:
    for attractions in clist:
        data_list=[]
        data_list.append(attractions["stitle"])
        data_list.append(attractions["address"][5:8])
        data_list.append(attractions["longitude"])
        data_list.append(attractions["latitude"])
        text = attractions["file"].lower()
        index = text.find(".jpg")
        data_list.append(attractions["file"][:index+4])
        writer = csv.writer(csvfile)
        writer.writerow(data_list)

def find_keys_with_same_value(input_dict):
    result_dict = {}
    for key, value in input_dict.items():
        if value not in result_dict:
            result_dict[value] = [key]
        else:
            result_dict[value].append(key)
    return result_dict

data={}
for attractions in clist:
    data.update({attractions["stitle"]:attractions["MRT"]})
data=find_keys_with_same_value(data)
with open("mrt.csv", "w", newline="", encoding="UTF-8-Sig") as csvfile:
    for key, value in data.items():
        if key == None:
            continue
        else:
            writer = csv.writer(csvfile)
            data_list = value
            data_list.insert(0, key)
            writer.writerow(data_list)
