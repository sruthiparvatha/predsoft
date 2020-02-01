import random, json

d={}
random.seed(3)
for id in range(100):
    d[id]={
        'MId': id,
        'Temperature': random.uniform(20, 75),
        'Speed': random.randint(1000, 3000),
        'Current': random.uniform(10, 50),
        'Voltage': random.uniform(150, 300),
    }

data = json.dumps(d)
print(d)

with open("preddata.json", "w") as f:
    f.write(data)

