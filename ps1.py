#
#  @file ps1.py
#
#  @author Kartik Gupta
#  @date 27 September 2018
#

# Getting number of rows and columns
r,c = list([int(i) for i in input().split()])

# Initializing lists for the pattern 
listarr=[]
listnew=[]
x=0

# Getting characters for pattern
for i in range(r):
    si=input()
    l=list(si[:c])
    listarr.append(l)

print(listarr)


# Pattern Matching
for i in range(r):
    for j in range(c):
        if listarr[i][j]=="S":
            for k in range(2):
                if j+k <0 or j+k >2:
                    print("Single Element")
                else:
                    if (listarr[i][j+k]=="S") and (listarr[i][j-k]=="S"):
                        x+=1
                        listnew.append(x)
                        x=0

print(listnew)

