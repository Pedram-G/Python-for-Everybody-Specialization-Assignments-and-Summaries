import re
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)


import re
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+?@\S+' , x)
print(y)

print('--------------------------------------------------------')

import re

file = open('regex_sum_1330132.txt', 'r')

sum = 0

for line in file:
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        sum = sum + int(number)

print(sum)

# print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )

print('------------------------------------------------------')

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()

print('-----------------------------------------------------')

print(ord('H'))

print('---------------------------------------------------------')

#Actual data: http://py4e-data.dr-chuck.net/comments_1330134.html (Sum ends with 2670)

from urllib import request
from bs4 import BeautifulSoup
html=request.urlopen('http://py4e-data.dr-chuck.net/comments_1330134.html').read()
soup = BeautifulSoup(html)
tags=soup('span')
sum=0
for tag in tags:
    sum=sum+int(tag.contents[0])
print(sum)

print('--------------------------------------------------------------------')

