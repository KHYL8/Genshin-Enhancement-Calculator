from datetime import date

characterList = {}

tBooks = {
    'Mondstadt: Freedom' : 1,
    'Mondstadt: Resistance' : 2,
    'Mondstadt: Ballad' : 3,
    'Liyue:     Prosperity - ' : 1,
    'Liyue:     Diligence' : 2,
    'Liyue:     Gold' : 3,
    'Inazuma:   Transience' : 1,
    'Inazuma:   Elegance' : 2,
    'Inazuma:   Light' : 3,
    'Sumeru:    Admonition' : 1,
    'Sumeru:    Ingenuity' : 2,
    'Sumeru:    Praxis' : 3
    }

class Character:

    def __init__(self, name, star, nmat, mmat, bmat, book, dmat):
        self.name = name
        self.stars = star
        self.nmat = nmat
        self.mmat = mmat
        self.bmat = bmat
        self.book = book
        self.dmat = dmat

with open('Characters.txt') as characterfile:
    for lineCounter, line in enumerate(characterfile):
        chara = line.split(" - ")
        if chara[0] not in characterList:
            characterList[chara[0]] = {
                'Stars' : chara[1],
                'Nature Material' : chara[2],
                'Mob Material' : chara[3],
                'Boss Material' : chara[4],
                'Talent Book' : chara[5],
                'Domain Material' : chara[6]
                }


#print(date.today().isoweekday())

curDate = date.today().isoweekday()

for available in tBooks:
    if curDate > 3:
        curDate -= 3
    if curDate == 0:
        print(available)
    if curDate == tBooks[available]:
        print(available)

#while True:
#    c_name = input("Character Name: ")
#    print(characterList[c_name]['Stars'])
#    print(characterList[c_name]['Nature Material'])
#    print(characterList[c_name]['Mob Material'])
#    print(characterList[c_name]['Boss Material'])
#    print(characterList[c_name]['Talent Book'])
#     print(characterList[c_name]['Domain Material'])

