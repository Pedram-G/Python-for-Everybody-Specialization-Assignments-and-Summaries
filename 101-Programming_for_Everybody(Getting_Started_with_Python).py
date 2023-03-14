# convert elevator floor

inp = input('europe floor ?')
usf = int(inp) + 1
print('us floor' , usf)

print('-----------------------------------------')

x = 10
if x < 15:
    print('samaller')
if x > 20:
    print('bigeer')

print('finish')

print('-----------------------------------------')

x = 5
if x == 5 :
    print('Equals 5')
if x > 4 :
    print('Greater than 4')
if x >= 5 :
    print('Greater or Equals 5')
if x < 6 :
    print('Less than 5')
if x <= 5 :
    print('Less than or Equals 5')
if x != 6 :
    print('Not equals 6')

print('--------------------------------')

x = 4
if x < 2 :
    print('Bigeer')
elif x > 3 :
    print('Medium')
else :
    print('Smaller')

print('All done')

# Az in 3 faghat yeki anjam beshe.

print('--------------------------------------------------')

astr = 'pedram'
try:
    istr = int(astr)            #inja be moshkel mekhorim
except:
    istr = -1

print('first' , istr)
print()

astr = '525'
try:
    istr = int(astr)
except:
    istr = -1

print('second' , istr)

print('---------------------------------------------------')

vorod = input('enter a number :')
try:
    khoroj = int(vorod)
except:
    khoroj = -1

if khoroj > 0 :
    print('eyval baba')
else :
    print('please select a number')


x = 0
if x < 2 :
    print('Small')
elif x < 10 :
    print('Medium')
else :
    print('LARGE')
print('All done')

print('-------------------------------------')

astr = 'Hello Bob'
istr = 0
try:
    istr = int(astr)
except:
    istr = -1
print(istr)

print('---------------------------------------------------------------')


#Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
#Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
#Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
#You should use input to read a string and float() to convert the string to a number.
#Do not worry about error checking the user input - assume the user types numbers properly. ?????????????????????????????


hr = input("Enter Hours:")
rt = input("Enter rate:")
fh = float(hr)
ft = float(rt)

if fh > 40 :
    x = fh * ft
    y = (fh - 40.0) * (ft * 0.5)
    xy = x + y

else :
    xy = fh * ft
print('Pay:',xy)

# OR ANOTHER WAY FOR THIS QUESTION

hr = float(input("Enter Hours:"))
rt = float(input("Enter rate:"))

if hr > 40 :
    x = hr * rt
    y = (hr - 40.0) * (rt * 0.5)
    xy = x + y

else :
    xy = hr * rt
print('Pay:',xy)


print('------------------------------------------------')

score = input("Enter Score: ")
try :
    nomre = float(score)
    if nomre >= 0.9 and nomre <= 1.0 :
        print('A')
    elif nomre == 0.8 :
        print('B')
    elif nomre == 0.7 :
        print('C')
    elif nomre == 0.6 :
        print('D')
    elif nomre < 0.6 and nomre > 0.0 :
        print('F')
    else :
        print('Erorr 1, please enter number between 0.0 to 1.0')
 
except :
    print('Erorr 2, please enter number between 0.0 to 1.0')

print('------------------------------------------------------')

def thing(damn):
    if damn == 'pp' :
        print('hi')
    elif damn == 'nn' :
        print('hello')
    else :
        print('oh nooo')

thing('pedi')

print('----------------------------------------')

def thing(damn):
    if damn == 'pp' :
        return 'hi'
    elif damn == 'nn' :
        return 'hello'
    else :
        return 'oh nooo'

print(thing('pp') , 'pedrammm')
print(thing('nn') , 'pariiiiiii')
print(thing('pspspspsp') , 'what the fuck')

print('---------------------------------------------------')

def addtwo(a, b):
    added = a + b
    return added

p = addtwo(5, 6)
print(p)
#OR
print(addtwo(5, 6))             # in behtare

print('-------------------------------------')

def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('fr'),'Michael')

print('------------------------------')

def addtwo(a, b):
    added = a + b
    return a

x = addtwo(2, 7)
print(x)
#OR
print(addtwo(2, 7))

print('----------------------------------------------------------')

friend = ['pedram' , 'ahmad' , 'parham' , 'mamad']
for friend in friend :
    print('hi and how are you', friend, end=' , ')

print('Done')

print('-------------------------------------------')

largest_so_far = -1
print('before', largest_so_far)
for the_num in [9 , 41 , 12 , 3 , 74 , 15] :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print(largest_so_far, the_num)

print('after', largest_so_far)

print('--------------------------------------------------')

zork = 0
print('Before', zork)
for love in [5 , 4 , 8 , 9 , 1 , 2 , 3 , 77 , 88 , 95]:
    zork = love + zork
    print(zork, love, end=' , ')

print('After', zork)

print('-------------------------------------------')


count = 0           #shomarande
sum = 0             #jaam
print('Before', count, sum)
for value in [9 , 41 , 12 , 3, 74 , 15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, int(sum / count))

print('----------------------------------------------')

print('before')
for value in [10, 20 , 30 , 40 , 50 , 60, 5, 7]:
    if value > 40 :
        print('yohaha', value)
    else :
        print('hahahaha', value)
print('no touch')    

print('-----------------------------------------------------------')

found = False
print(type(found))
print('Before', found)
for value in [9 , 41 , 12 , 33 , 3 , 74 , 15 ]:
    if value == 3 :
        found = True
    print(found, value)
print('After', found)

print('--------------------------------------')

samllest_so_far = None
#print(type(None))
print('before')
for the_num in [9 , 41 , 12 , 3 , 74 , 15] :
    if samllest_so_far is None:
        samllest_so_far = the_num
    elif the_num < samllest_so_far :
        samllest_so_far = the_num
    print(samllest_so_far, the_num)

print('after', samllest_so_far)

print('----------------------------------------------')


while True:
    line = input('> ')
    if line[0] == '#' :
        continue
        break
    print(line)
print('done')

print('---------------------------------------------------')

xh = input('enter hours:')
xb = input('enter rate:')
xp = float(xh) * float(xb)
print('pay:',xp)

print('---------------------------------------------------')

hr = input("Enter Hours:")
rt = input("Enter rate:")

try :
    fh = float(hr)
    ft = float(rt)
except :
    print('ERORR, Please enter numeric input')
    quit()

if fh > 40 :
    x = fh * ft
    y = (fh - 40.0) * (ft * 0.5)
    xy = x + y

else :
    xy = fh * ft
print('Pay:',xy)

print('---------------------------------------------------')

inp=input('Enter score:')
try:
    score = float(inp)
    if score<=1.0 and score>=0.9:
        print('A')
    elif score>=0.8 and score<0.9:
        print('B')
    elif score>=0.7 and score<0.8:
        print('C')
    elif score>=0.6 and score<0.7:
        print('D')
    elif score<0.6:
        print('F')
    else:
        print('Bad Score.')
except:
    print('Bad Score.')

print('---------------------------------------------------')

#4.6 Write a program to prompt the user for hours and rate per hour using input
#to compute gross pay. Pay should be the normal rate for hours up to 40 and
#time-and-a-half for the hourly rate for all hours worked above 40 hours.
#Put the logic to do the computation of pay in a function called computepay()
#and use the function to do the computation. The function should return a value.
#Use 45 hours and a rate of 10.50 per hour to test the program
#(the pay should be 498.75). You should use input to read a string and float()
#to convert the string to a number. Do not worry about error checking the user
#input unless you want to - you can assume the user types numbers properly.
#Do not name your variable sum or use the sum() function


def computepay(h,r):
    if h > 40:
        p = 1.5 * r * (h - 40) + (40 *r)
    else:
        p = h * r
    return p

hrs = input("Enter Hours:")
hr = float(hrs)
rphrs = input("Enter rate per hour:")
rphr = float(rphrs)

p = computepay(hr,rphr)
print('Pay',p)

print('---------------------------------------------------')

#5.2 Write a program that repeatedly prompts a user for integer numbers until the
#user enters 'done'. Once 'done' is entered, print out the largest and smallest
#of the numbers. If the user enters anything other than a valid number catch it
#with a try/except and put out an appropriate message and ignore the number.
#Enter 7, 2, bob, 10, and 4 and match the output below.


largest = None
smallest = None
num = 0
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        numb = int(num)
    except:
        print ("Invalid input")
        continue
    if smallest is None:
        smallest = numb
    elif numb < smallest :
        smallest = numb
    if largest is None:
        largest = numb
    elif numb > largest:
        largest = numb
print ("Maximum is", largest)
print ("Minimum is", smallest)

print('---------------------------------------------------')

num = 0
tot = 0.0
while True :
    aval = input('Enter a number: ')
    if aval == 'Done' :
        break
    try:
        dovom = float(aval)
    except:
        print('Invaild input')
        continue
        print(dovom)
    num = num + 1
    tot = tot + dovom

print('All Done')
print(tot,num,tot/num)
