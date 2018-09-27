

group1 = list("abcdefghi")
group2 = list("jklmnopqr")
group3 = list("stuvwxyz_")

gr1=[]
gr2=[]
gr3=[]
gr1new=[]
gr2new=[]
gr3new=[]
k1,k2,k3 = [int(i) for i in input().split()]

word=input()
list(word)

for i in word[:]:
    if i in group1:
        gr1.append(i)
    elif i in group2:
        gr2.append(i)
    elif i in group3:
        gr3.append(i)

gr1new = (gr1[-k1:] + gr1[:-k1])
gr2new = (gr2[-k2:] + gr2[:-k2])
gr3new = (gr3[-k3:] + gr3[:-k3])

print(gr1)
print(gr2)
print(gr3)

