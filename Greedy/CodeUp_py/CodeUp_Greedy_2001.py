p = []
j = []
for i in range(0,3):
    p.append(float(input()))
    
for k in range(0,2):
    j.append(float(input()))

p.sort(reverse=False)
a = p[0]*(10/100)

j.sort(reverse=False)
b = j[0]*(10/100)

print(p[0]+j[0]+a+b)