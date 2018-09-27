#
#  @file ps1.py
#
#  @author Kartik Gupta
#  @date 27 September 2018
#

# Getting number of rows and columns
r,c = list([int(i) for i in input().split()])
listarr=[]
listnew=[]
x=1

# Initializing lists for the pattern
for i in range(106):
     listarr.append('')

listnew=[]

# Getting characters for pattern
for i in range(r):
    si=input()
    l=list(si[:c])+['','','','','','','']
    listarr.insert(i,l)


for i in range(r):
    for j in range(c):
        if listarr[i][j]=="S":
            for k in range(1,c):
                if (listarr[i][j+k]=="S") and (listarr[i][j-k]=="S") :
                    x+=2

            listnew.append(x)
            x=1

maxvalue=max(listnew)
minvalue=min(listnew)
print("Maximum matching pattern in horizontal direction" +  " " + str(maxvalue))
print("Minimum matching pattern in horizontal direction" +  " " + str(minvalue))
