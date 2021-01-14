with open('input.txt', 'r') as f:
    rec=f.readline()
w=0
x=0
y=0
z=0
for i in rec:
    if ord(i) in range (65,91):
        w+=1
for i in rec:
    if ord (i) in range (97,123):
        x+=1
for i in rec:
    if ord(i) in range (49,58):
        y+=1
for i in rec:
    if ord(i) in rage (33,42):
        z+=1
with open('Litmajuscule.txt', 'w') as f:
    f.write(str(w))
with open('Litminuscule.txt', 'w') as f:
    f.write(str(x))
with open('Cifre.txt', 'w') as f:
    f.write(str(y))
with open('operatori.txt', 'w') as f:
    f.write(str(z))