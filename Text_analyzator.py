udaje = {'bob' : '123', 'ann' : 'pass123', 'mike' : 'password123', 'liz' : 'pass123'}
texts_zoznam = ['''Enzým je biokatalyzátor – niečo, čo pomáha niečomu inému k tomu, 
aby to malo lepši a rýchlejší výkon. Chemické reakcie sú vo všeobecnosti pomalé, 
avšak enzýmy tieto reakcie urýchľujú.''',
'''Bez enzýmov by chemické reakcie, vďaka ktorým žijeme, boli príliš pomalé na to, aby sme prežili. 
V ľudskom tele sa nachádza asi 3000 enzýmov, ktoré sa podieľajú na viac ako 7000 
chemických reakciách.''',
'''Aj keď jednou z dôležitých úloh enzýmov je trávenie, je to ich celkom posledná funkcia. 
Dôležitejšie úlohy proteolitických (bielkovinu tráviacich) enzýmov sú napríklad protizápalové, 
antifibrózne, čistiace, imunitné, antivirálne či protirakovinové účinky. V nasledujúcich 
riadkoch si ich podrobnejšie rozoberieme.''']

meno = None
heslo = None
pomocka_na_whileloop = True
uvitanie = 'Vitajte v programe "Text Analyzátor". Pre prihlásenie si vyberte jednu z možností:'
oddelovac = '~' * len(uvitanie)

print(oddelovac)
print(uvitanie)
print(oddelovac)

ucet = 1
reg_loop = True
registracia = False #pomocná premenná na registráciu

while ucet: #testujeme číslo, ktoré zadal používateľ
    ucet = input('Ak si prajete prihlásiť sa, zadajte 1. Ak si chcete vytvoriť účet, zadajte 2: ')
    if ucet == '1' or ucet == '2':
        break
    else:
        print('Nesprávne číslo.')
        continue

while reg_loop: #loop na buď vytvorenie účtu a následné prihlásenie, alebo iba na samotné prihlásenie
    if ucet == '2' and registracia == False: #ak si užívateľ vybral registráciu
        reg_while = True
        while reg_while:
            print(oddelovac)
            meno = input('Zadajte nové meno: ')
            heslo = input('Zadajte nové heslo: ')
            if meno not in udaje.keys():
                udaje[meno] = heslo
                registracia = True
                reg_while = False #escaping loop aby sme sa mohli prihlásiť
                print(oddelovac)
                print('Prosím, prihláste sa.')
            elif meno in udaje.keys():
                print('Meno sa už používa. Zadajte, prosím, iné. ')


    elif ucet == '1' or registracia == True: #ak je užívateľ zaregistrovaný, alebo sa práve zaregistroval
        while pomocka_na_whileloop: #while loop na vloženie a test prihlasovacích údajov a ich opätovné vloženie pri zlých údajoch
            print(oddelovac)
            meno = input('Prihlasovacie meno: ')
            heslo = input('Prihlasovacie heslo: ')
            print(oddelovac)
            reg_loop = False

            if meno not in udaje.keys() and heslo != udaje.get(meno):
                print('Nesprávne údaje!')
                continue
            elif meno in udaje.keys() and heslo != udaje.get(meno):
                print('Nesprávne heslo!')
                continue
            elif meno in udaje.keys() and heslo == udaje.get(meno):
                print('Pokračujem...')
                print(oddelovac)
                pomocka_na_whileloop = False





text = ''
pomocka = True
while pomocka:
    volba = input('''Ak si prajete zadať vlastný text, zadajte 1, 
ak si prajete načítať text z našej databázy,
zadajte 2: ''')
    if volba == '1':
        print(oddelovac)
        text = input('Vložte text: ')
        text = text.split()
        pomocka = False
    elif volba == '2':
        pomocka_na_whileloop2 = True
        while pomocka_na_whileloop2: #while loop na kontrolu toho, či je zvolené číslo textu v zozname
            text = int(input('Zadajte číslo textu: '))
            print(oddelovac)
            if text > len(texts_zoznam) or text <= 0:
                print(f'Máme iba {len(texts_zoznam)} texty!')
                continue
            elif text <= len(texts_zoznam):
                text = texts_zoznam[text - 1].split() # číslo textu sa stane daným textom a rozdelí ho
                pomocka_na_whileloop2 = False
        pomocka = False
    else:
        print(oddelovac)
        print('Nesprávne číslo.')
        print(oddelovac)
        continue

for i in text:
    text[text.index(i)] = i.strip(",().:'/-") #z textu berieme string a ukladáme ho upravený nas5

for i in text:
    if i in ",().:'/-":
        text.remove(i)

pocet = len(text) #1. počet slov v texte

pocet_title = 0 #2. počet slov s veľkým písmenom
for i in text:
    if i.istitle():
        pocet_title += 1

pocet_upper = 0 #3. počet slov veľkými písmenami
for i in text:
    if i.isupper():
        pocet_upper += 1

pocet_lower = 0 #4. počet slov malými písmenami
for i in text:
    if i.islower():
        pocet_lower += 1

pocet_cisel = 0 #5. počet čísel
for i in text:
    if i.isdigit():
        pocet_cisel += 1

print(f'Počet slov v texte: {pocet}')
print(f'Počet slov začínajúcich veľkým písmenom: {pocet_title}')
print(f'Počet slov napísaných iba veľkými písmenami: {pocet_upper}')
print(f'Počet slov napísaných iba malými písmenami: {pocet_lower}')
print(f'Počet čísel v texte: {pocet_cisel}')
print(oddelovac)

dlzky = {} #slovník s dĺžkou slov a ich počtom
for slovo in text:
    dlzky[len(slovo)] = dlzky.setdefault(len(slovo), 0) + 1 #dĺžka slova ako kľúč, hodnota buď rovnaká, alebo +1

pomocka_na_whileloop3 = True
print(f'Zobrazené dĺžky slov (1-{max(dlzky.keys())}).')
while pomocka_na_whileloop3:
    statistika_pocet = int(input('Vyberte počet: '))
    if statistika_pocet <= max(dlzky.keys()) and statistika_pocet > 0:
        pomocka_na_whileloop3 = False
    else:
        print('Číslo mimo rozpätia!')
print(oddelovac)

zoradene_udaje = sorted(dlzky.keys()) #zoraďujem kľúče zo slovniku (dĺžky slov)

if statistika_pocet <= max(dlzky.keys()) and statistika_pocet > 0:
    print('Počet slov s danou dĺžkou:')
    for i in range(1, statistika_pocet + 1):
        if dlzky.get(i) == None:
            continue
        print(f'Dĺžka slova {i}: {dlzky.get(i) * "*"} ({dlzky.get(i)})')

hodnota_cisel = 0
print(oddelovac)
for i in text:
    if i.isdigit():
        hodnota_cisel += int(i)
print(f'Ak by sme zrátali hodnotu všetkých čísel v tomto texte, dostali by sme hodnotu {hodnota_cisel}.')
print(oddelovac)

#vkladanie vlastného textu mi relatívne často hádže argument error v ďalšej časti programu pokiaľ text vkladám ctrl+v
#a tak má len veľmi obmedzené možnosti, ale mal by byť dostatočne funkčný