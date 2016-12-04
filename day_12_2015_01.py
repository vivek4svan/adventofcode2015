import json
import collections
sum_data = 0


def chk_json(data):
    global sum_data
    if isinstance(data,collections.Iterable) and not isinstance(data,str):
        if isinstance(data,list):
            [chk_json(i) for i in data]
        elif isinstance(data,dict):
            [chk_json(data[i]) for i in data]
    else:
        sum_data += data

with open("day_12_2015_01.txt") as f:
    for line in f:
        json_data = json.loads(line)
        print json_data
        chk_json(json_data)

print sum_data #111,754