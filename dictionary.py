# dictionary Словарь
import pprint

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

parcels = [{"city": "Venezia", "company": "Pede Nec Foundation", "siret": "315695304-00008", "country": "Nepal"},
           {"city": "Tauranga", "company": "Diam Ltd", "siret": "858465677-00004", "country": "Venezuela"},
           {"city": "Blagoveshchensk", "company": "Blandit Congue In Consulting", "siret": "552681876-00009",
            "country": "Chad"}, {"city": "Saltillo", "company": "Quisque Limited", "siret": "373959469-00009",
                                 "country": "Pitcairn Islands"},
           {"city": "Perth", "company": "Nibh Quisque Nonummy Ltd", "siret": "526917463-00006", "country": "Cyprus"},
           {"city": "Peine", "company": "Magna Malesuada Vel Industries", "siret": "558528956-00003",
            "country": "Botswana"},
           {"city": "Patos", "company": "Sem Corp.", "siret": "322068065-00000", "country": "Palestine, State of"},
           {"city": "Moio Alcantara", "company": "Ipsum Institute", "siret": "695288795-00005", "country": "Palau"},
           {"city": "Ciudad Madero", "company": "Lectus Cum LLC", "siret": "547399808-00005",
            "country": "Saint Helena, Ascension and Tristan da Cunha"},
           {"city": "Sacramento", "company": "Augue Company", "siret": "740365895-00003", "country": "Faroe Islands"},
           {"city": "New Bombay", "company": "Orci Luctus PC", "siret": "613761238-00005", "country": "Japan"},
           {"city": "Wekweti", "company": "Amet Ornare Ltd", "siret": "799809694-00000", "country": "El Salvador"},
           {"city": "Penrith", "company": "Odio Sagittis Incorporated", "siret": "118503770-00000", "country": "Gabon"},
           {"city": "Köthen", "company": "Dolor Limited", "siret": "105229439-00002", "country": "Hong Kong"},
           {"city": "Moignelee", "company": "Ornare Lectus Corp.", "siret": "668465891-00004",
            "country": "Cook Islands"},
           {"city": "Tramutola", "company": "Et LLC", "siret": "066460676-00001", "country": "Czech Republic"},
           {"city": "Merdorp", "company": "Odio A Limited", "siret": "732498845-00005",
            "country": "Russian Federation"},
           {"city": "Latinne", "company": "Urna Incorporated", "siret": "297140006-00000", "country": "Isle of Man"},
           {"city": "Saint Paul", "company": "Purus Sapien Consulting", "siret": "151220514-00005",
            "country": "French Guiana"},
           {"city": "Märsta", "company": "Pharetra Corp.", "siret": "526549506-00008", "country": "Jordan"},
           {"city": "Ledbury", "company": "Diam Pellentesque Limited", "siret": "829945575-00001",
            "country": "Bosnia and Herzegovina"},
           {"city": "Bikaner", "company": "Mauris Magna Consulting", "siret": "215974627-00006",
            "country": "Dominican Republic"},
           {"city": "Roosendaal", "company": "Tempor Foundation", "siret": "620933192-00002",
            "country": "French Southern Territories"},
           {"city": "Portobuffolè", "company": "Dictum Institute", "siret": "509693529-00000", "country": "Vanuatu"},
           {"city": "Rochester", "company": "Leo Cras Vehicula Industries", "siret": "321588246-00009",
            "country": "Sudan"},
           {"city": "Lampernisse", "company": "Eget Institute", "siret": "498673466-00005", "country": "China"},
           {"city": "La Unión", "company": "Ultricies Adipiscing Corp.", "siret": "564409985-00004",
            "country": "Saint Vincent and The Grenadines"},
           {"city": "Paranaguá", "company": "Ipsum Dolor Sit Consulting", "siret": "571863562-00005",
            "country": "Sint Maarten"},
           {"city": "Rixensart", "company": "Non Arcu Company", "siret": "455032284-00008", "country": "Algeria"},
           {"city": "Heppenheim", "company": "Praesent Eu Nulla Foundation", "siret": "284882438-00005",
            "country": "Åland Islands"},
           {"city": "Hoorn", "company": "Adipiscing Industries", "siret": "635076862-00005", "country": "Colombia"},
           {"city": "Auvelais", "company": "Amet Risus Corporation", "siret": "743581514-00002",
            "country": "Montenegro"}, {"city": "Chekhov", "company": "Pellentesque LLP", "siret": "322624974-00000",
                                       "country": "United States Minor Outlying Islands"},
           {"city": "Probolinggo", "company": "Interdum Feugiat Sed Industries", "siret": "169447091-00003",
            "country": "Israel"},
           {"city": "Bad Nauheim", "company": "Vestibulum Accumsan Neque PC", "siret": "019138924-00006",
            "country": "Anguilla"},
           {"city": "Wenduine", "company": "Orci Ltd", "siret": "527818850-00002", "country": "Kazakhstan"},
           {"city": "Donstiennes", "company": "Cum LLP", "siret": "119460202-00003", "country": "Cook Islands"},
           {"city": "Torgny", "company": "Odio Inc.", "siret": "299070896-00004", "country": "Greece"},
           {"city": "Victor Harbor", "company": "A Magna Lorem LLC", "siret": "545731093-00005",
            "country": "Bonaire, Sint Eustatius and Saba"},
           {"city": "Louisville", "company": "Ante Lectus Convallis Limited", "siret": "549743672-00004",
            "country": "Sierra Leone"},
           {"city": "Lolol", "company": "Malesuada Fringilla Est Corporation", "siret": "900840109-00004",
            "country": "Saint Martin"},
           {"city": "Kitchener", "company": "Aliquet Limited", "siret": "170139489-00000", "country": "Portugal"},
           {"city": "Overland Park", "company": "At Corp.", "siret": "363220112-00009", "country": "Luxembourg"},
           {"city": "Concón", "company": "Luctus Sit Associates", "siret": "089342356-00006",
            "country": "Dominican Republic"},
           {"city": "Daska", "company": "Dictum Cursus Nunc Industries", "siret": "674498845-00009", "country": "Togo"},
           {"city": "Cabras", "company": "Purus Maecenas Libero Industries", "siret": "200414365-00003",
            "country": "Micronesia"}, {"city": "Castanhal", "company": "Turpis Non Ltd", "siret": "499083798-00003",
                                       "country": "Falkland Islands"},
           {"city": "Santander de Quilichao", "company": "Metus LLP", "siret": "315487140-00008", "country": "Ireland"},
           {"city": "Pazarcık", "company": "Nulla Donec LLC", "siret": "180080947-00005",
            "country": "Equatorial Guinea"},
           {"city": "Turgutlu", "company": "Viverra Incorporated", "siret": "122232457-00004", "country": "Moldova"},
           {"city": "Thanjavur", "company": "Nunc Ac Mattis LLC", "siret": "526034111-00009", "country": "Syria"},
           {"city": "Renfrew", "company": "At Risus Nunc Ltd", "siret": "161824057-00004", "country": "Mozambique"},
           {"city": "Siculiana", "company": "Cras Ltd", "siret": "811288505-00001", "country": "Puerto Rico"},
           {"city": "Perpignan", "company": "Neque Tellus Company", "siret": "485901888-00001", "country": "Benin"},
           {"city": "Sheffield", "company": "Nec Tellus Limited", "siret": "392701256-00001", "country": "Italy"},
           {"city": "Blenheim", "company": "Nisi Corporation", "siret": "614419984-00008", "country": "Hungary"},
           {"city": "Detroit", "company": "Ut Institute", "siret": "346092950-00002", "country": "Czech Republic"},
           {"city": "Poza Rica", "company": "Aliquam Nisl Nulla Foundation", "siret": "040516197-00007",
            "country": "South Georgia and The South Sandwich Islands"},
           {"city": "Dumai", "company": "Eget Laoreet Posuere Corporation", "siret": "793097163-00000",
            "country": "Japan"},
           {"city": "San Giovanni Suergiu", "company": "Non Lorem Incorporated", "siret": "607876851-00009",
            "country": "Guernsey"},
           {"city": "Raigarh", "company": "Urna Corporation", "siret": "148351927-00006", "country": "Benin"},
           {"city": "A Coruña", "company": "Vitae Aliquet Nec LLP", "siret": "682669452-00000",
            "country": "Falkland Islands"},
           {"city": "Hasselt", "company": "Aliquam Corporation", "siret": "491891487-00002",
            "country": "Holy See (Vatican City State)"},
           {"city": "Geel", "company": "At Augue Industries", "siret": "327467734-00007", "country": "Poland"},
           {"city": "Altmünster", "company": "Lobortis Nisi Ltd", "siret": "844334359-00008", "country": "Costa Rica"},
           {"city": "Comblain-Fairon", "company": "Mauris Blandit Inc.", "siret": "101217990-00007",
            "country": "Cambodia"},
           {"city": "Kohistan", "company": "Posuere Cubilia Consulting", "siret": "061977997-00008",
            "country": "Senegal"},
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
           {"city": "Fort William", "company": "Varius Nam Porttitor PC", "siret": "411277551-00007",
            "country": "South Georgia and The South Sandwich Islands"},
           {"city": "Bokaro Steel City", "company": "Tempor Lorem Incorporated", "siret": "645424680-00009",
            "country": "Jersey"},
           {"city": "Barrie", "company": "Aliquam Foundation", "siret": "878097450-00000", "country": "Hungary"},
           {"city": "Dégelis", "company": "Dolor Vitae Company", "siret": "286642814-00003", "country": "Iceland"},
           {"city": "Osogbo", "company": "Non Consulting", "siret": "297237232-00006", "country": "Tuvalu"},
           {"city": "San Gregorio nelle Alpi", "company": "Non Nisi LLP", "siret": "505371369-00008",
            "country": "Guadeloupe"},
           {"city": "Quinta de Tilcoco", "company": "Curabitur Massa PC", "siret": "385205612-00000",
            "country": "Bouvet Island"},
           {"city": "Loppem", "company": "Arcu Eu Odio LLC", "siret": "243702552-00007", "country": "Faroe Islands"},
           {"city": "Newton Stewart", "company": "Enim Etiam Gravida LLC", "siret": "431713585-00005",
            "country": "Taiwan"},
           {"city": "Rocourt", "company": "Libero Institute", "siret": "681248407-00006", "country": "Singapore"},
           {"city": "Gagliano del Capo", "company": "Hendrerit Neque Limited", "siret": "400520490-00006",
            "country": "Indonesia"},
           {"city": "Florianópolis", "company": "Mattis Integer Foundation", "siret": "954778247-00005",
            "country": "Grenada"},
           {"city": "Sant'Angelo Limosano", "company": "Lorem Associates", "siret": "334033826-00002",
            "country": "Malaysia"},
           {"city": "Coalhurst", "company": "Dis Parturient Montes Foundation", "siret": "103883344-00006",
            "country": "Kuwait"},
           {"city": "Thon", "company": "Proin Velit Sed Corp.", "siret": "076470988-00007", "country": "Guam"},
           {"city": "Petorca", "company": "Velit In Aliquet Company", "siret": "165313685-00001",
            "country": "Bonaire, Sint Eustatius and Saba"},
           {"city": "Suxy", "company": "Dictum Incorporated", "siret": "632741658-00009", "country": "Burundi"},
           {"city": "Paço do Lumiar", "company": "Lectus Pede Incorporated", "siret": "088189196-00004",
            "country": "Faroe Islands"},
           {"city": "Hildesheim", "company": "Eu Erat Semper Limited", "siret": "826212938-00003", "country": "Guyana"},
           {"city": "Niel-bij-As", "company": "Mauris Elit Dictum PC", "siret": "916344237-00000",
            "country": "Turkmenistan"},
           {"city": "Piotrków Trybunalski", "company": "Neque In Ornare Corporation", "siret": "871909727-00004",
            "country": "Qatar"},
           {"city": "Harrisburg", "company": "Vitae Company", "siret": "409595485-00007", "country": "Egypt"},
           {"city": "Mumbai", "company": "Lacus Incorporated", "siret": "665106001-00001", "country": "Burkina Faso"},
           {"city": "Tranent", "company": "At Limited", "siret": "828668988-00003", "country": "Korea, South"},
           {"city": "Parndorf", "company": "Ultrices LLP", "siret": "662907617-00002", "country": "Indonesia"},
           {"city": "Rimbey", "company": "Pellentesque Industries", "siret": "136125614-00000", "country": "Slovakia"}]

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

import json
import pprint
import datetime


with open('sample/data.json', 'r') as f:
    upwork_data = json.load(f)

jobs = upwork_data["searchResults"]["jobs"]
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