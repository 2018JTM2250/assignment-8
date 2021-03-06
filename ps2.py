#
#  @file ps2.py
#
#  @author Kartik Gupta
#  @date 27 September 2018
#

# Creating groups for different characters
group1 = list("abcdefghi")
group2 = list("jklmnopqr")
group3 = list("stuvwxyz_")

# initializing list for groups
gr1=[]
gr2=[]
gr3=[]
gr1new=[]
gr2new=[]
gr3new=[]

# initializing list for index
index1=[]
index2=[]
index3=[]

#Getting k1,k2 and k3 values
k1,k2,k3 = [int(i) for i in input().split()]

# getting input string
msgword=list(input())

# Dividing the characters into different groups
for i in range(len(msgword)):
    if msgword[i] in group1:
        gr1.append(msgword[i])
        index1.append(i)
    elif msgword[i] in group2:
        gr2.append(msgword[i])
        index2.append(i)
    elif msgword[i] in group3:
        gr3.append(msgword[i])
        index3.append(i)

# Rotating the groups
gr1new = (gr1[-k1:] + gr1[:-k1])
gr2new = (gr2[-k2:] + gr2[:-k2])
gr3new = (gr3[-k3:] + gr3[:-k3])

#Getting decrypted msg
x=y=z=0
for i in range(len(msgword)):
    if i in index1:
        msgword[i]=gr1new[x]
        x+=1
    elif i in index2:
        msgword[i]=gr2new[y]
        y+=1
    elif i in index3:
        msgword[i]=gr3new[z]
        z+=1

#displaying the decrypted msg
for i in msgword[:]:
    print (i, end ='')

print("\n")


