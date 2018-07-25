import random

def Rand(start, end, num):
    res = []
 
    for j in range(num):
        res.append(random.randint(start, end))
 
    return res
 
num = 53
start = 10
end = 53
print(Rand(start, end, num))
