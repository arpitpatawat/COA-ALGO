def decimalToBinary(n):
    return bin(n).replace("0b", "")

def binaryToDecimal(n):
    return int(n,2)

def to_twoscomplement(bits, value):
    if value < 0:
        value = ( 1<<bits ) + value
    formatstring = '{:0%ib}' % bits
    return formatstring.format(value)

def rotateList(arr,d,n):
  arr[:]=arr[d:n]+arr[0:d]
  return arr

def convert(list):
      
    s = [str(i) for i in list]
    res = ("".join(s))
    return(res)
    
###############################
print("Non Restoring Division")
print("please enter value as Q / M :")
q = int(input("Enter value of Q :"))
m = int(input("Enter value of M :"))

Q = decimalToBinary(q)
M = decimalToBinary(m)
print("the binary value of q is: ",Q,"and M is : ",M)
count = len(Q)
zeta= count
k = [int(d) for d in str(Q)]
l = [int(d) for d in str(M)]
#adding 0's in list
temp = len(Q)-len(M)
while temp >= 0 :
    l.insert(0,0)
    temp = temp -1
p = to_twoscomplement(count+1,-m)
P = [int(d) for d in p]  
AC = []
for i in range(0,count+1):
    AC.insert(0,0)
X = AC + k

print("C \t AC \t Q \t Operation")
print(X)
for i in range(1,zeta+1):
    print("####",i,"cycle #####")
    X = rotateList(X,1,len(X)) 
    X[-1] = "X"
    print(X[0],"\t",X[1:count+1],"\t",X[count+1:],"left shift")
    AC = X[:count+1]
    if X[0] == 0:
        sum = bin(int(convert(AC), 2) + int(convert(P), 2))
        AC = sum[-(count+1):]
        AC = [int(d) for d in str(AC)]
        X[:count+1] = AC
        Operation = "AC = AC - M"
    elif X[0] ==1:
        sum = bin(int(convert(AC), 2) + int(convert(l), 2))
        AC = sum[-(count+1):]
        AC = [int(d) for d in str(AC)]
        X[:count+1] = AC
        Operation = "AC = AC + M"
    print(X[0],"\t",X[1:count+1],"\t",X[count+1:],"\t",Operation)
    if X[0] == 0:
        X[-1] =1
        Operation = "Q0 -> 1"
    elif X[0] == 1:
        X[-1] =0
        Operation = "Q0 -> 0"
    print(X[0],"\t",X[1:count+1],"\t",X[count+1:],"\t",Operation,"\n")

if X[0] == 0:
    print("Correct output\n")
elif X[0] == 1:
    print("-ve value of AC, doing AC = AC +M")
    sum = bin(int(convert(AC), 2) + int(convert(l), 2))
    AC = sum[-(count+1):]
    AC = [int(d) for d in str(AC)]
    X[:count+1] = AC

print(X[0],"\t",X[1:count+1],"\t",X[count+1:],"\t",Operation,"\n")

print("quotient is :",convert(X[count+1:]),"or in decimal :",binaryToDecimal(convert(X[count+1:])))
print("Remainder is :",convert(X[1:count+1]),"or in decimal :",binaryToDecimal(convert(X[1:count+1])))
