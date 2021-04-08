# dictionary Словарь
#import pprint
#import json
#import pprint
#import datetime

'''
phonebook = {}
phonebook["Jack"] = 30977647635 # Добавление елементов в dictionary
phonebook["Jill"] = 30984233149 # Добавление елементов в dictionary
phonebook["John"] = 38093896970 # Добавление елементов в dictionary

print(phonebook["Jill"]) # Добавление елементов в dictionary
print(phonebook["Jack"]) # Добавление елементов в dictionary
'''
'''
phonebook = {"Jack" : 380976758493, "Jill" : 389574823759, "John" : 398574666555}

del phonebook["Jack"]# Удаление елементов по ключу
del phonebook["Jill"]# Удаление елементов по ключу

for key, val in phonebook.items():
  print("Телефонный номер %s является %d" % (key, val))
'''
'''
phonebook = {"Jack" : 380976758493, "Jill" : 389574823759, "John" : 398574666555}
rez = phonebook.pop("Jack")# функция pop удаляет и возращает ключ

print(rez, phonebook)
'''

'''
#Добавить "Jake" в список контактов phonebook с телефонным номером 938273443, и удалить Jill из телефонной книги.
phonebook = {
    "John": 938477566,
    "Jack": 938377264,
    "Jill": 947662781
}
# кодить здесь
phonebook["Jake"] = 938273443 # Добавление елементов в dictionary
del phonebook["Jill"]

# код для тестов
if "Jake" in phonebook:
    print("Джейк представлен в контактах")

if "Jill" not in phonebook:
    print("Джил НЕ представлена в контактах")
'''
'''
# выводим пользоватилей по имене email и телефон:
users = [{"email": "a@libero.org", "name": "Linus Weeks", "phone": "07711 543497"},
         {"email": "amet.dapibus@pretium.edu", "name": "Caesar Lawrence", "phone": "(0121) 798 6942"},
         {"email": "odio@facilisis.co.uk", "name": "Tyler Odom", "phone": "055 4207 8497"},
         {"email": "vitae.semper@montesnascetur.net", "name": "Jeremy Mccarty", "phone": "070 9557 9742"},
         {"email": "eget.odio@diamvelarcu.com", "name": "Jameson Hoffman", "phone": "07624 826968"},
         {"email": "dolor@sedcongueelit.com", "name": "August Howe", "phone": "(0161) 236 9529"},
         {"email": "vel.convallis.in@facilisis.org", "name": "Hu Cantrell", "phone": "0800 306 0878"},
         {"email": "justo@utcursus.co.uk", "name": "Cameron Velazquez", "phone": "0937 736 1318"},
         {"email": "vulputate.velit.eu@dolorfusce.co.uk", "name": "Dennis Martin", "phone": "070 8802 5517"},
         {"email": "at@eu.ca", "name": "Elliott Spears", "phone": "0314 053 6906"},
         {"email": "sed.malesuada@dictum.edu", "name": "Gil Dean", "phone": "0992 658 0483"},
         {"email": "ullamcorper.nisl@volutpat.ca", "name": "Beck Parsons", "phone": "0345 745 8358"},
         {"email": "in.lorem.donec@eratvivamus.com", "name": "Luke Maddox", "phone": "07575 486355"},
         {"email": "id@eget.edu", "name": "Holmes Forbes", "phone": "(01584) 146838"},
         {"email": "ac@justofaucibus.co.uk", "name": "Kuame Gray", "phone": "07624 819344"},
         {"email": "consectetuer.mauris@etnetuset.org", "name": "Zephania Davis", "phone": "0845 46 40"},
         {"email": "enim.consequat@cum.co.uk", "name": "Ahmed Cantu", "phone": "07946 755678"},
         {"email": "aliquam@loremipsum.com", "name": "Camden Morrison", "phone": "0800 1111"},
         {"email": "gravida@sedmolestiesed.com", "name": "Adam Conley", "phone": "(01394) 604886"},
         {"email": "eget@semper.org", "name": "Allen Kelly", "phone": "(0171) 911 2559"},
         {"email": "sociis.natoque.penatibus@magna.ca", "name": "Bradley Jenkins", "phone": "(0141) 730 2571"},
         {"email": "mi.lacinia@maecenas.org", "name": "Finn Mitchell", "phone": "(0161) 104 4626"},
         {"email": "odio.a.purus@utodiovel.co.uk", "name": "Carlos Andrews", "phone": "0918 850 4281"},
         {"email": "ac.turpis.egestas@liberonecligula.org", "name": "Christian Holder", "phone": "(0181) 656 6641"},
         {"email": "magna@nonlaciniaat.net", "name": "Mannix Lindsey", "phone": "0845 46 40"},
         {"email": "faucibus.id@proin.edu", "name": "Leonard Hill", "phone": "07161 675597"},
         {"email": "consequat.enim.diam@cras.org", "name": "Rogan Acevedo", "phone": "070 5090 7752"},
         {"email": "neque.nullam.nisl@maecenasiaculis.com", "name": "Geoffrey Dorsey", "phone": "(0151) 536 7454"},
         {"email": "odio@euismodurna.ca", "name": "Randall White", "phone": "0800 1111"},
         {"email": "sapien.gravida@quis.net", "name": "Lucian Matthews", "phone": "0500 337116"},
         {"email": "est@vitae.com", "name": "Wylie Chandler", "phone": "0800 120 8427"},
         {"email": "aliquam.enim@condimentumegetvolutpat.net", "name": "Raja Walter", "phone": "0500 255556"},
         {"email": "laoreet@velitegestas.org", "name": "Brody Mcleod", "phone": "0800 785 9633"},
         {"email": "amet.ante@cubiliacurae.edu", "name": "Vance Talley", "phone": "(016432) 72617"},
         {"email": "dapibus@sagittisplacerat.org", "name": "Coby Norman", "phone": "056 8021 8671"},
         {"email": "sed.auctor@vehicularisusnulla.org", "name": "Jamal Snider", "phone": "0933 688 1305"},
         {"email": "est.arcu.ac@magnaphasellusdolor.net", "name": "Cameron Hobbs", "phone": "070 9828 2258"},
         {"email": "ipsum@atiaculis.org", "name": "Ali Ray", "phone": "(0113) 856 9687"},
         {"email": "erat.eget@convallisliguladonec.org", "name": "Felix Lott", "phone": "(01778) 691806"},
         {"email": "auctor.velit.aliquam@nunc.co.uk", "name": "Knox Vincent", "phone": "(0114) 360 2425"},
         {"email": "ac@sapienimperdiet.com", "name": "Aristotle Gill", "phone": "(0181) 315 2657"},
         {"email": "eleifend.vitae@dictumeu.com", "name": "Samson Haney", "phone": "0315 196 0215"},
         {"email": "rutrum@sed.com", "name": "Nathan Larsen", "phone": "(016977) 0216"},
         {"email": "adipiscing.elit.etiam@utsemnulla.org", "name": "Lucas Kirby", "phone": "(016977) 0448"},
         {"email": "morbi.quis.urna@maurisvestibulumneque.com", "name": "Richard Larsen", "phone": "0500 679329"},
         {"email": "morbi.quis@erat.ca", "name": "Mason Valenzuela", "phone": "0800 281 9787"},
         {"email": "ut.eros@donecfelis.edu", "name": "Lars Owen", "phone": "0500 588204"},
         {"email": "vel.est@morbineque.ca", "name": "Colby Stewart", "phone": "0500 226677"},
         {"email": "vel.faucibus.id@loremloremluctus.net", "name": "William Hoffman", "phone": "(011913) 24876"},
         {"email": "libero@erat.net", "name": "Christopher Ayala", "phone": "0800 1111"},
         {"email": "dapibus.id.blandit@auctormauris.net", "name": "Kelly Bowen", "phone": "(01938) 95725"},
         {"email": "ut.nulla.cras@et.co.uk", "name": "Brennan Gamble", "phone": "070 5102 4938"},
         {"email": "donec@acfeugiat.org", "name": "Cain Wilson", "phone": "07596 884970"},
         {"email": "facilisis.non.bibendum@aeneaneuismodmauris.org", "name": "Ishmael Beard", "phone": "0800 1111"},
         {"email": "non.luctus@ornarefusce.com", "name": "Vernon Pena", "phone": "0845 46 43"},
         {"email": "at@ipsum.ca", "name": "Odysseus Le", "phone": "0800 1111"},
         {"email": "adipiscing.elit@congueturpisin.com", "name": "Garrison Rosales", "phone": "07624 080738"},
         {"email": "sagittis@auguescelerisquemollis.co.uk", "name": "Acton Rodgers", "phone": "(016977) 3458"},
         {"email": "dictum.mi.ac@egetmagnasuspendisse.edu", "name": "Forrest Booth", "phone": "0800 768 1523"},
         {"email": "quis.pede@consequat.co.uk", "name": "Zane Short", "phone": "07667 306355"},
         {"email": "lorem.luctus@semperetlacinia.edu", "name": "Charles Serrano", "phone": "0800 397 4498"},
         {"email": "in@donec.edu", "name": "Rogan Vaughan", "phone": "0500 230949"},
         {"email": "in.consequat@vitaeerat.co.uk", "name": "Jakeem Cervantes", "phone": "(010809) 28258"},
         {"email": "semper.rutrum.fusce@felisullamcorperviverra.net", "name": "Emmanuel Lewis",
          "phone": "(016977) 7219"},
         {"email": "ut.sem@ligulaconsectetuerrhoncus.edu", "name": "Donovan Torres", "phone": "(010181) 72843"},
         {"email": "ultricies.ligula.nullam@pellentesque.org", "name": "August Hull", "phone": "0930 898 3249"},
         {"email": "libero@ipsumdolorsit.org", "name": "Lucian Garza", "phone": "0813 073 1364"},
         {"email": "enim.sit@idmollis.co.uk", "name": "Dale Andrews", "phone": "(0118) 288 8000"},
         {"email": "nec.urna.et@nibh.org", "name": "Jason Booker", "phone": "(01726) 94049"},
         {"email": "vel.lectus@sedeu.co.uk", "name": "Ulric Pitts", "phone": "(0110) 637 9699"},
         {"email": "enim.nunc.ut@accumsan.co.uk", "name": "Neville Page", "phone": "0800 235 6392"},
         {"email": "id.ante@nec.org", "name": "Grady Lancaster", "phone": "0845 46 49"},
         {"email": "pellentesque.a.facilisis@praesenteudui.edu", "name": "Jesse Henry", "phone": "(016977) 4368"},
         {"email": "sit.amet@cumsociis.edu", "name": "Louis Dalton", "phone": "055 7148 4287"},
         {"email": "lorem.semper.auctor@imperdietnec.co.uk", "name": "Kato Hoffman", "phone": "0800 823215"},
         {"email": "libero.morbi@ullamcorpereu.org", "name": "Orlando Larsen", "phone": "(016977) 6345"},
         {"email": "nisi.mauris.nulla@vulputate.net", "name": "Mason Bentley", "phone": "0319 077 4232"},
         {"email": "non@magnisdis.com", "name": "Chandler Booth", "phone": "0800 004 5663"},
         {"email": "dignissim.magna.a@donectempus.edu", "name": "Aquila Riley", "phone": "(01929) 51736"},
         {"email": "id.risus.quis@scelerisquescelerisque.org", "name": "Malcolm Wynn", "phone": "0906 624 8471"},
         {"email": "sapien@aliquet.org", "name": "Jerry Benson", "phone": "0902 003 7224"},
         {"email": "augue.porttitor@nullatempor.ca", "name": "Ira Knowles", "phone": "07624 649008"},
         {"email": "egestas@aliquamornare.co.uk", "name": "Tucker Williamson", "phone": "07624 954945"},
         {"email": "vestibulum.ante@lacus.ca", "name": "Cairo Holder", "phone": "070 2896 8403"},
         {"email": "consectetuer.rhoncus@amalesuadaid.net", "name": "Channing Burch", "phone": "(0113) 445 3332"},
         {"email": "sapien.cras@blanditenimconsequat.co.uk", "name": "Colton Valenzuela", "phone": "0800 1111"},
         {"email": "sed@ametmassaquisque.org", "name": "Cooper Holland", "phone": "0888 877 7541"},
         {"email": "amet.nulla.donec@ligulaaliquamerat.co.uk", "name": "Quentin Ayers", "phone": "0800 1111"},
         {"email": "phasellus.at.augue@eusempellentesque.com", "name": "Tobias Henry", "phone": "0890 068 0367"},
         {"email": "phasellus.nulla.integer@elitaliquamauctor.net", "name": "Nissim Mcguire", "phone": "(01927) 71134"},
         {"email": "mollis.nec.cursus@suspendisse.com", "name": "Jonas Williamson", "phone": "07956 221872"},
         {"email": "tempor.erat.neque@semper.ca", "name": "Ferris Garza", "phone": "0800 1111"},
         {"email": "parturient.montes@mattisornare.edu", "name": "Hammett Bell", "phone": "(0119) 818 1259"},
         {"email": "odio.vel.est@dolortempus.co.uk", "name": "Ulysses Perry", "phone": "(01138) 94540"},
         {"email": "phasellus@malesuada.org", "name": "Griffith Sexton", "phone": "055 0440 6744"},
         {"email": "velit.dui@ornaresagittisfelis.co.uk", "name": "Joel Osborne", "phone": "07636 586531"},
         {"email": "interdum@vivamusnisi.edu", "name": "Derek Robertson", "phone": "0500 661089"},
         {"email": "pede@tinciduntorciquis.com", "name": "Zachary Forbes", "phone": "(0161) 044 7936"},
         {"email": "molestie@dolorsitamet.edu", "name": "Bert Pope", "phone": "055 4971 4314"},
         {"email": "auctor.vitae.aliquet@montes.ca", "name": "Clark Walter", "phone": "055 6940 8751"}]

for val in users:
    print("пользователь с именем: %s имеет email: %s и телефон: %s" % (val["name"], val["email"], val["phone"]))
'''
'''
           {"city": "Bhimavaram", "company": "Tincidunt Adipiscing Mauris LLC", "siret": "020600490-00005",
            "country": "Korea, North"},
           {"city": "Guri", "company": "Ornare Elit PC", "siret": "989772074-00005", "country": "Sint Maarten"},
           {"city": "Serampore", "company": "Enim Corp.", "siret": "117453001-00002", "country": "Montenegro"},
           {"city": "Cairns", "company": "Nec Mauris Blandit LLP", "siret": "569755788-00001", "country": "Mongolia"},
           {"city": "Arequipa", "company": "Augue Malesuada Malesuada LLC", "siret": "492501812-00001",
            "country": "United Kingdom (Great Britain)"},
           {"city": "Bolano", "company": "Odio PC", "siret": "766317697-00007", "country": "Saint Kitts and Nevis"},
           {"city": "Pickering", "company": "Tellus Suspendisse Sed Inc.", "siret": "610832248-00005",
            "country": "Madagascar"}, 
       ]
'''
# Полиморфная функция поиска Посилок по ключу значению
'''
def search_country(arr, key, value):
    rez = []
    for val in arr:
        if val[key] == value:
            rez.append(val)
    return rez


key = input("Введите ключ")
value = input("Введите значение")
found_parcels = search_country(parcels, key, value)

pprint.pprint(found_parcels)
'''

'''
def rect(y, x):
    for val in range(y):
        for i in range(x):
            print("*", end="    ")# end="    " Будет выводить * через пробелы
        print("\n")

while True:

    h = input("Введите высоту: \n")# Переход строки
    w = input("Введите ширину: \n")
    h = int(h)
    w = int(w)

    rect(h, w)
'''

'''
# Выводим триугольник из * чек !!!!!!!!!!!!!!!!!!!!!!!
def triangle(y):
    for val in range(y):# ! 1 for Ресует по вертикили!!!!!!!!
        rez = val + 1
        for i in range(rez):# ! 2 for Ресует по ГОРИЗОНТАЛИ!!!!!!!!!!!
            print("*", end="   ")# end="    " Будет выводить * через пробелы
        print("\n")# Переход строки

h = input("Введите высоту: \n")
h = int(h)

triangle(h)
'''

'''
# Выводим числа из масива в виде *
printer = [1, 2, 3, 5, 8, 13, 21]

for val in printer:
    for i in range(val):
        print("*", end=" ")
    print("\n")
'''
'''
# Получить history из Словаря!!!!!!
sampleDict = {
   "class":{
      "student":{
         "name":"Mike",
         "marks":{
            "physics":70,
            "history":80
         }
      }
   }
}

print(sampleDict["class"]["student"]["marks"]["history"]) # Получить history из Словаря !!!!!!
print(sampleDict["class"]["student"]["name"])# Получить "name":"Mike", из Словаря !!!!!!
'''


'''
with open('sample/data.json', 'r') as f:
    upwork_data = json.load(f)

jobs = upwork_data["searchResults"]["jobs"]
'''

'''
for job in jobs:
    print(job["title"])
    print(job["hourlyBudgetText"])
    print("https://www.upwork.com/jobs/%s" % job["ciphertext"])
    print(job["publishedOn"])
    print(job["proposalsTier"])
    print(job["tierLabel"])
    print(job["description"])
    print(job["durationLabel"])
    print(job["tierLabel"])
    print(job["durationLabel"])
    print(job["engagement"])
    print(job["occupations"]["category"])
    print(job["client"]["location"]["country"])
    print(job["client"]["totalSpent"])
    print(job["client"]["totalReviews"])
    print(job["client"]["totalFeedback"])
    print("\n")

'''
'''
# Выводим именеа из словаря
ar_dicshen = [{"name": "Madden, Dai X."}, {"name": "Franco, Ariana N."}, {"name": "Colon, Uma W."}, {"name": "Hampton, Hedda R."},
 {"name": "Noel, Brittany Y."}, {"name": "Patterson, Yuri L."}, {"name": "Vincent, Meghan W."},
 {"name": "Christian, Shad E."}, {"name": "Norman, Rogan Q."}, {"name": "Hawkins, Perry S."},
 {"name": "Joyce, Eagan W."}, {"name": "Dawson, Shoshana F."}, {"name": "Strickland, Peter F."},
 {"name": "Deleon, Kirsten D."}, {"name": "Barton, Barry D."}, {"name": "Meyer, Gregory O."},
 {"name": "Shannon, Judith F."}, {"name": "Sanchez, Nehru U."}, {"name": "Avila, Gemma H."},
 {"name": "Macias, Bradley T."}, {"name": "Cole, Charlotte K."}, {"name": "Cunningham, Rashad X."},
 {"name": "Carver, Reese E."}, {"name": "Hamilton, Yuli F."}, {"name": "Ayala, Jasmine J."},
 {"name": "Kim, Zephania R."}, {"name": "Guthrie, TaShya R."}, {"name": "Hoover, Callum I."},
 {"name": "Shepherd, Aidan R."}, {"name": "Cain, Linus E."}, {"name": "Wall, Alana I."}, {"name": "Mcdaniel, Colin Y."},
 {"name": "Herring, Nichole F."}, {"name": "Jenkins, Aspen P."}, {"name": "Lambert, Deanna F."},
 {"name": "Keller, Scott K."}, {"name": "Mueller, Keaton S."}, {"name": "Valenzuela, Addison K."},
 {"name": "Harrison, Murphy L."}, {"name": "Massey, Guy H."}, {"name": "Cotton, Amal S."}, {"name": "Miles, Shad V."},
 {"name": "May, Herrod O."}, {"name": "Burgess, Britanney V."}, {"name": "Koch, Chase D."},
 {"name": "Fleming, Hope R."}, {"name": "Bradshaw, Hilary T."}, {"name": "Ryan, Lila F."},
 {"name": "Allison, Meghan Q."}, {"name": "Hardin, Ursula A."}, {"name": "Logan, Joel E."}, {"name": "Oneill, Axel T."},
 {"name": "Mcgee, Matthew R."}, {"name": "English, Zenaida Z."}, {"name": "Kirk, Nina X."},
 {"name": "Compton, Rooney E."}, {"name": "Peck, Garrett Q."}, {"name": "Ratliff, Price N."},
 {"name": "Gonzalez, Oprah E."}, {"name": "Mcdaniel, Price H."}, {"name": "William, Rigel Z."},
 {"name": "Berg, Amery W."}, {"name": "Cardenas, McKenzie T."}, {"name": "York, Ferris M."},
 {"name": "Harper, Camilla A."}, {"name": "Callahan, Carolyn W."}, {"name": "Lynn, Helen E."},
 {"name": "Hampton, Gary C."}, {"name": "Gillespie, Virginia N."}, {"name": "Witt, Ira Y."},
 {"name": "Vasquez, Dillon Y."}, {"name": "Casey, Paula K."}, {"name": "Conley, Kim V."}, {"name": "Hobbs, Grace P."},
 {"name": "Russell, Aretha V."}, {"name": "Alston, McKenzie I."}, {"name": "Sullivan, Fritz R."},
 {"name": "Garza, Olga H."}, {"name": "Mathews, Clinton P."}, {"name": "Stephenson, Vivian W."},
 {"name": "Mullen, Giselle Q."}, {"name": "Griffin, Ina L."}, {"name": "Forbes, Jena T."},
 {"name": "Collins, Illiana Z."}, {"name": "Lawson, Samson A."}, {"name": "Monroe, Tana V."},
 {"name": "Newman, Murphy M."}, {"name": "Ortiz, Joshua F."}, {"name": "Arnold, Mona P."},
 {"name": "Campbell, Kitra R."}, {"name": "Mccarty, Eliana M."}, {"name": "Dillon, Driscoll U."},
 {"name": "Odonnell, Carla K."}, {"name": "Powers, Marsden I."}, {"name": "Cummings, Norman Y."},
 {"name": "Lowe, Illiana X."}, {"name": "Leblanc, Alan U."}, {"name": "Turner, Alice G."},
 {"name": "Hendricks, Scarlett D."}, {"name": "Medina, Vivien N."}]

for val in ar_dicshen:
    under_the_line = val["name"].split(",")
    print("\x1b[36m %s" % under_the_line[1][:-2])
'''