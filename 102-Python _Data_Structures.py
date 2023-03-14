fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index , letter, end = ' , ')
    index = index + 1
print()

print('------------------------------------------------------------')

fruit = 'banana'
for letter in fruit:
    print(letter)

print('--------------------------------------------------------')

word = 'banana'
count = 0       #shomarande
for letter in word:
    if letter == 'a' :
        count = count + 1
    print(count)

print(dir(word))     # dir : be ma neshon mide ke che method haye mitonim ro in moteghyer ke az jens str ast(dar inja yani word) bzanim

print('--------------------------------------------------------------')

word2 = '            pedram           '
x = word2.strip()                           # space ro az left va right hazf kard.
y = word2.rstrip()                          # space ro az right(e) string hazf kard.
z = word2.lstrip()                          # space ro az left(e) string hazf kard.
print(x)
print(y)
print(z)

print('-----------------------------------------------------------')

line = 'pedi pedi pedram'
xx = line.startswith('pedi')
print(xx)
yy = line.startswith('p')
print(yy)

print('------------------------------------------------------------')

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])

print('---------------------------------------------------')

text = "X-DSPAM-Confidence:    0.8475"
x = text.find("0")
y = text[23:]
z = float(y)
print(z)

text = "X-DSPAM-Confidence:    0.8475"
x = text.find(':')
y = text[x+1:]
z = float(y)
print(z)

print('-------------------------------------------------------------')

xfile = open('Coursera2.txt', 'r')
count = 0
for line in xfile:
    count = count + 1
print('line count:', count)


xfile = open('Coursera2.txt')
for line in xfile:
    line = line.rstrip()
    if line.startswith('from:') :
        print(line)

#OR

xfile = open('Coursera2.txt')
for line in xfile:
    line = line.rstrip()
    if not line.startswith('from:'):
        continue
    print(line)


fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('subject: '):
        count = count + 1

    print('There were', count, 'subject lines in', fname)


fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    quit()
    
count = 0
for line in fhand:
    if line.startswith('subject: '):
        count = count + 1

    print('There were', count, 'subject lines in', fname)


# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fhand = open(fname, 'r')
except:
    print('File cannot be opened')
    quit()

for line in fhand:
    fhand = line.upper()
    print(fhand.rstrip())

#OR

fname = input("Enter file name: ")                            #hamon balayee vali super easy tar.
fhand = open(fname, 'r')
for line in fhand:
    line = line.rstrip()
    print(line.upper())


# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
average = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    average += float(line[20:-1].strip())
    count = count + 1
    print(line)
    
print("Average spam confidence:", (average/count))


friends = ['pedram', 'pedram', 'pedram']

for friend in friends :
    print('Hi my buddy', friend, end=' , ')
print()

for i in range(len(friends)):
    friend = friends[i]
    print('Hi buddy', friend)

print('-------------------------------------------------------')

count = 0
total = 0
while True :
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    count = count + 1
    total = value + total

average = total / count
print('Average: ', average)

#OR

numlist = list()
while True :
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average: ', average)


line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
word = line.split()
print(word)

print('---------------------------------------------------------------------')

fhand = open('filename.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('from: ') : continue
    word = line.split()
    print(word[2])

#alan dar code bala masalan roz hay hafte be namayesh gozashte mishavad.


line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
word = line.split()
email = word[1]
print(email)
pieces = email.split('@')           #adsain ro hazf kardim va khod jaygah 1 ra do ozv az list kardim.
print(pieces)
print(pieces[1])

print('-------------------------------------------')

fname = "romeo.txt"     # OR    fname = input("Enter file name: ")
fhand = open(fname)
lst = list()
for line in fhand:
    words = line.rstrip().split()
    for word in words:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)



#Open the file mbox-short.txt and read it line by line. When you find a line
#that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the
#line (i.e. the entire address of the person who sent the message). Then print
#out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'.
#Also look at the last line of the sample output to see how to print the count.


fname = input("Enter file name: ")
fhand = open(fname)
count = 0
for line in fhand:
    if not line.startswith('From'):     #from ro shamel beshe
        continue
    if line.startswith('From:'):        #from: ro shamel nashe
        continue
    else:
        line = line.split()
        line = line[1]
        print(line)
    count += 1              #count = count + 1
print("There were",count,"lines in the file with From as the first word")


handel = open('mbox-short.txt')

for line in handel:
    line = line.rstrip().split()
    guardian
    if len(line) < 1 or line[0] != 'From' :                # tartib in do amal mohem ast va agar baraks benevisim erorr mide behemon
        continue
    print(line[2])


counts = dict()
names = {'pedram' , 'ali' , 'mamad' , 'ali' , 'pedram' , 'ali' , 'ali'}
for name in names :
    counts[name] = counts.get(name, 0) + 1
print(counts)

print('-----------------------------------------------------')

count = dict()
names = {'pedram', 'ali', 'mamad', 'ali', 'pedram'}
for name in names :
    if name not in count:
        count[name] = 1
    else:
        count[name] = count[name] + 1
print(count)

print('----------------------------------------------------')

counts = dict()
print('Please enter a line of text')
line = input('')

words = line.split()
print('Words:', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts: ', counts)



counts = {'pedram' : 100 , 'maman' : 200 , 'baba' : 300}
for key in counts:
    print(key, counts[key])


x = {'pedram' : 100 , 'maman' : 200 , 'baba' : 300}
print(list(x))
print(x.keys())
print(x.values())
print(x.items())

x = {'pedram' : 100 , 'maman' : 200 , 'baba' : 300}
for k,v in x.items() :
    print(k,v)

print('------------------------------------------------------')

name = input('Enter name file: ')
name = 'coursera1.txt'
handel = open(name)

counts = dict()
for line in handel:
    words = line.rstrip().split()                       # rstrip() mitonim nazarim chon niazi nist behesh
    for word in words:
        counts[word] = counts.get(word, 0) + 1          # 0 : To provide a default value if the key is not found

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)                        # print bishtarin tekrar kalame.

print('--------------------------------------------------------------')


# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

fname = input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"        # in khat yani hata age jay vared kardan wsm file enter bezanim ham file ejra shavad.
hand = open(fname)

lst = list()

for line in hand:
    if not line.startswith("From:"): continue
    line = line.split()
    lst.append(line[1])

counts = dict()
for word in lst:
    counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print (bigword,bigcount)



# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
d=dict()
for line in handle:
    if not line.startswith("From "):
        #continue
    else:
        line=line.split()
        line=line[5]
        line=line[0:2]
        d[line]=d.get(line,0)+1

lst=list()
for value,count in d.items():
    lst.append((value,count))

lst.sort()
for value,count in lst:
    print(value,count)



a = list()
print(dir(a))           # be ma neshon mide ke che harkat haye mishe roye listmon bezanim

print()

a = tuple()             # be ma neshon mide ke che harkat haye mishe roye tuplemon bezanim
print(dir(a))

print()

(a, b) = ('pedram', 2)
print(a)
print(b)

print('--------------------------------------------------------------------------')

d = {'b' : 10, 'a' : 20, 'c' : 5}

f = sorted(d.items())
print(f)
for k,v in f:
    print(k , v)

print('--------------------------------------------------------')

x = {'b' : 10, 'a' : 20, 'c' : 5}
tmp = list()
for k,v in x.items() :
    tmp.append( (v, k) )

print(tmp)
tmp = sorted(tmp, reverse=True)             # baraks va be tartib mikonim
print(tmp)

print('--------------------------------------------------------')

fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    #print(counts)
lst = list()
for key, val in counts.items() :
    newtub = (val, key)
    lst.append(newtub)

lst = sorted(lst, reverse=True)
#print(lst)
for val, key in lst[:10] :          #[:10] : yani ma 10 tay bartar ro mikhaym yani 10 tay por tekrar.
    print(key, val)

print('-----------------------------------------------')

c = {'a' : 10, 'b' : 1, 'c' : 22}
print(sorted( [ (v,k) for k,v in c.items()] ))     # mitonim in khat az code ro bejay 437 ta 440 code bala estefade konim. 

print('---------------------------------------------------------------------')

fname = input('Enter file: ')
if len(fname) < 1 : fname = 'Coursera1.txt'
hand = open(fname)

di = dict()
for line in hand :
    line = line.rstrip().split()
    for word in line :
        if word in di :
            di[word] = di[word] + 1
            print('**Existing**')
        else :
            di[word] = 1
            print('**New**')
        print(word,di[word])
print(di)


#OR BETTER WAY


fname = input('Enter file: ')
if len(fname) < 1 : fname = 'Coursera1.txt'
hand = open(fname)

di = dict()
for line in hand :
    line = line.rstrip().split()
    for word in line :
        oldcount = di.get(w,0)                 #if the key not there the count is zero
        print(word,'old',oldcount)
        newcount = oldcount + 1
        di[word] = newcount
        print(word,'new',newcount)

print(di)
        
######## jay 4 khat kode 483 ta 487 menvesim : di[word] = di.get(word,0) + 1
######## dar khat code bala : idiom : retrieve/create/update counter

print('--------------------------------------------------------------------------------')

## MOST COMMON WORD

fname = input('Enter file: ')
if len(fname) < 1 : fname = 'Coursera1.txt'
hand = open(fname)

di = dict()
for line in hand :
    line = line.rstrip().split()
    for word in line :
        di[word] = di.get(word,0) + 1

print(di)

tmp = list()
for k,v in di.items() :
    newt = (v,k)
    tmp.append(newt)

print('Flipped', tmp)

tmp = sorted(tmp, reverse=True)
print('Sorted', tmp[:5])

for v,k in tmp[:5] :
    print(k,v)
