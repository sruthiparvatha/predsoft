# import json
# # d ={}
# # d['reshma']={
# #     'first_name':'reshma',
# #     'last_name':'kumar',
# #     'age': 20
# #     }
# #
# # d['anusha']={
# #     'first_name':'anusha',
# #     'last_name':'suresh',
# #     'age': 21
# #
# # }
# # print(d)
# # print(type(d))
# # s = json.dumps(d)
# # print(s)
# # print(type(s))
# #
# # with open("test1.json",'w') as f:
# #     f.write(s)

import random, json
d={}
data={}
random.seed(3)
for id in range(100):
    d[id+1]=({'Mid': '0',
        'Temperature': round(random.uniform(20, 75), 2),
        'Speed': random.randint(1000, 3000),
        'Current': round(random.uniform(10, 50), 2),
        'Voltage': round(random.uniform(150, 300), 2),
    })

data = json.dumps(d)
print(d)

with open("pred1.json", "w") as f:
    f.write(data)
with open("preddata.json") as f:
    data=json.load(f)

print(d)
