"""file=open("new.txt", 'r')
data=file.read()
print('data in file', data)
list=data.split(',')
file.close()
print('list of data', list)




with open('color.txt', 'r') as f:
    line=f.read().split(',')

for i in line:
    print(i)


file=open('dati.txt', 'r')
list=file.readlines()
print(list) """

from numpy import loadtxt
line=loadtxt('dati.txt', delimiter=',')
for i in line:
    print(i)