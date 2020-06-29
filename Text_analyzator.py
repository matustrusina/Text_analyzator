data = {'bob' : '123', 'ann' : 'pass123', 'mike' : 'password123', 'liz' : 'pass123'}
texts_database = ['''Enzymes also have valuable industrial and medical applications. 
The fermenting of wine, leavening of bread, curdling of cheese, and brewing of beer have been 
practiced from earliest times, but not until the 19th century were these reactions 
understood to be the result of the catalytic activity of enzymes. Since then, enzymes 
have assumed an increasing importance in industrial processes that involve organic chemical 
reactions. The uses of enzymes in medicine include killing disease-causing microorganisms, 
promoting wound healing, and diagnosing certain diseases.''',
'''When you have this breathing pattern down, record your pulse. You will need to have a pulse of 80 
beats per minute or less while you are deep breathing in order to be ready to start freediving. 
If you keep at it, you will find that your pulse starts to slow down with your deep breathing 
exercises over time. You will gradually be able to descend further as your pulse adapts. You 
may not be able to hold your breath for longer than 11 minutes and descend to more than 200 meters 
below the surface like veteran freedivers, but you can certainly attain and best your own 
goals as you progress in the sport.''',
                  '''Sport climbers tend to use single ropes. They are easy to handle and can be clipped in quickly. 
This type of rope is usually the best choice for relatively straight routes and secure 
climbing on the climbing walls. Caution: Before setting of on a tour you must make sure your 
rope is long enough (check the climbing topo or ask the locals). Too many serious accidents 
have occurred as a result of ropes that were too short. At the end of the day, the best climbing 
equipment is only as good as the climber using it! A conscientious climber gets acquainted with 
each and every piece of their equipment. Experienced climbing partners and trained climbing 
instructors can provide you with information about the limits and uses of climbing equipment 
which you won't find in the instructions.''']

name = None
passw = None
pomocka_na_whileloop = True
greet = 'Welcome to Text analyzer. A program that gives you some basic statistics about your text:'
separator = '~' * len(greet)

print(separator)
print(greet)
print(separator)

reg_loop = True
registration = False #auxiliary var for registration

while reg_loop: #testing number user has added
    account = input('For sign up, type "1" and press enter. For registration, type "2" and press enter: ')
    if account == '1' or account == '2':
        break
    print(separator)
    print('Wrong number.')
    print(separator)

while reg_loop: #loop for either creating an account and sign up, or only sign up
    if account == '2' and registration == False: #if the user chose to registrate
        reg_while = True
        while reg_while:
            print(separator)
            name = input('Add a new username: ')
            passw = input('Add a new password: ')
            if name not in data.keys():
                data[name] = passw
                registration = True
                reg_while = False #escaping loop in order to sign up
                print(separator)
                print('Now, please, sign up.')
            elif name in data.keys():
                print('Username is already being used. Please, choose something else. ')


    elif account == '1' or registration == True: #if the user is already registered or he has just registered
        while pomocka_na_whileloop: #while loop for insertion and test of user-added data and repeated insertion if the data was wrong
            print(separator)
            name = input('Username: ')
            passw = input('Password: ')
            print(separator)
            reg_loop = False

            if name not in data.keys() and passw != data.get(name):
                print('Wrong username or password!')
                continue
            elif name in data.keys() and passw != data.get(name):
                print('Wrong password!')
                continue
            elif name in data.keys() and passw == data.get(name):
                print('In progress...')
                print(separator)
                pomocka_na_whileloop = False

print('Now, choose one of the following for statistics... ')
print(separator)

text = ''
pomocka = True
while pomocka:
    volba = input('''If you wish to use your own text, type "1" and press enter, if you
wish to choose a text from our database, type "2" and press enter: ''')
    print(separator)

    if volba == '1':
        text = input('Insert text: ')
        text = text.split()
        pomocka = False
    elif volba == '2':
        pomocka_na_whileloop2 = True
        while pomocka_na_whileloop2: #while loop to check, if the number is valid (in the database)
            text = int(input(f'Add a text number (we currently have {len(texts_database)} texts): '))
            print(separator)
            if text > len(texts_database) or text <= 0:
                print(f'We have only {len(texts_database)} texts!')
                print(separator)
            elif text <= len(texts_database):
                text = texts_database[text - 1].split() #text number becomes the text itself and splits it
                pomocka_na_whileloop2 = False
        pomocka = False
    else:
        print('Wrong number.')
        print(separator)

for i in text:
    text[text.index(i)] = i.strip(",().:'/-*") #we take a string from text, strip it and insert it back

for i in text:
    if i in ",().:'/-":
        text.remove(i)

count_title = 0 #2. number of titled words
count_upper = 0 #3. number of capital words
count_lower = 0 #4. number of small words
number_of_nums = 0 #5. number of numbers
for i in text:
    if i.istitle():
        count_title += 1

    if i.isupper():
        count_upper += 1

    if i.islower():
        count_lower += 1

    if i.isdigit():
        number_of_nums += 1

count = len(text) - number_of_nums #1. number of words in text


print(f'Words in text: {count}')
print(f'Numbers in text: {number_of_nums}')
print(f'Number of words beginning with a capital letter: {count_title}')
print(f'Number of words written by capital letters: {count_upper}')
print(f'Number of words written by lowercase letters: {count_lower}')

lengths = {} #dict {len(word) : sum(words with that lenght),...,...,...}
for slovo in text:
    lengths[len(slovo)] = lengths.setdefault(len(slovo), 0) + 1 #lenght of word as key, value either 0 (if key is new) or 1 (if the key is already present)

pomocka_na_whileloop3 = True
print(separator)
print(f'Number of different lenghts: {max(lengths.keys())}')
while pomocka_na_whileloop3:
    figureof_lengths = int(input('Add number of lenghts you would like to display in a graph: '))
    if figureof_lengths <= max(lengths.keys()) and figureof_lengths > 0:
        pomocka_na_whileloop3 = False
    else:
        print(separator)
        print(f'Number out of range! (range: 1-{max(lengths.keys())})')
        print(separator)
print(separator)

sorted_data = sorted(lengths.keys()) #sorting keys from the dict

if figureof_lengths <= max(lengths.keys()) and figureof_lengths > 0:
    for i in range(1, figureof_lengths + 1):
        if lengths.get(i) == None:
            print(f'Length: {i: >2}: (0)')
            continue
        print(f'Length: {i: >2}: {lengths.get(i) * "*"} ({lengths.get(i)})')

summed_numbers = 0
print(separator)
for i in text:
    if i.isdigit():
        summed_numbers += int(i)
print(f'If we summed all the numbers in this text, we would get number {summed_numbers}.')
print(separator)