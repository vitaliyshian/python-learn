import pprint
import datetime

'''
def my_function(x): # Обьявление функции
    print("Hello My Function: %s" % x) # Тело функции

def sum(a, b):
    x = a + b
    return x

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def subtract(a, b):
    return a - b

def is_even(a):
    if a % 2 == 0:
        return True
    else:
        return False
'''

'''
a = [2, 44, 444, 4, 4, 4, 2]

def unique(raw, sort = False):
    un = []
    for val in raw:
        if val not in un:
            un.append(val)
    un.sort(reverse=sort)
    return un


print(unique(a))


'''

'''
111
# Функция сортировки и уникальных значений
def unique(raw, sort = False):
    has_letter = False
    has_numeral = False

    for val in raw:
        if isinstance(val, str):
            has_letter = True
        if isinstance(val, int):
            has_numeral = True

    if has_letter and has_numeral:
        print("Пожалуйста передайте массив с однородными данными")
        return []

    un = []
    for val in raw:
        if val not in un:
            un.append(val)
    un.sort(reverse=sort)
    return un

a = [2, 44, 444, 4, 4, 4, 2]
b = [7, 7, 7, 7, 7, 6]
c = [1, 2, 3, 4, 4, 5, 5, 6, 7, 0]
d = [8, 8, 9, 0, 0, 5, 5, 8, 8, 0]
e = [3, 3, 3, 3, 3]
f = [0]
g = [1, 1, 0, 0]
q = []

print(unique(a))
111
'''

'''
111
# Функция которая проверяет является ли слово полиндромом
def is_poly(word = ''):
    if not isinstance(word, str):
        print("Не правильный формат данных!")
        return False

    lower_word = word.lower()
    if lower_word == lower_word[::-1]:
        return True
    else:
        return False
'''

'''
111
poly = ["Aра", "Дом", "Доход", "Дример", "Трико", "Весело", "Шалаш", "Казак", "Атака", 2, 3]

for val in poly:
    if is_poly(val) == True:
        print("Cлово является полиндромом! %s" % val)
    else:
        print("Cлово Не является полиндром %s" % val)

'''

'''
# Функция проверки на типы данных
xxx = [1, 3, "f"]

def print_type(val):
    if isinstance(val, str):
        print("Тип данных Строка %s" % val)
    elif isinstance(val, int):
        print("Тип данных числовой %s" % val)
    elif isinstance(val, float):
        print("Тип данных вещественый %s" % val)
    elif isinstance(val, list):
        print("Тип данных массив %s" % val)
    else:
        print("Неизвестный тип Данных!!!")

print_type(xxx)
'''

'''
aList = [4, 6, 8, 24, 12, 2]
bList = []

def min(arr):
    if not isinstance(arr, list):
        print("Не массив!!!")
        return None
    if len(arr) == 0:
        print("Массив не имеет елементов!!!")
        return None
    m = arr[0]
    for val in arr:
        if val < m:
            m = val
    return m

print(min(aList))
'''

'''
def max(arr):
    if not isinstance(arr, list):
        print("Не массив")
        return None
    if len(arr) == 0:
        print("Массив не имеет елементов!!!")
        return None
    b = 0
    for val in arr:
        if val > b:
            b = val
    return b

print(max(aList))
'''

'''
def unique(raw, sort = False):
    has_letter = False
    has_numeral = False

    for val in raw:
        if isinstance(val, str):
            has_letter = True
        if isinstance(val, int):
            has_numeral = True

    if has_letter and has_numeral:
        print("Пожалуйста передайте массив с однородными данными")
        return []

    un = []
    for val in raw:
        if val not in un:
            un.append(val)
    un.sort(reverse=sort)
    return un

def median(arr):
    sorted_arr = unique(arr)
    index = int(len(sorted_arr) / 2)
    return sorted_arr[index]


aList = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]
bList = [1, 2, 3, 4, 5, 6]

import statistics
res = median(aList)
res2 = statistics.median(aList)
print(res, res2)
'''

'''
emails = ["fringilla@nonummyacfeugiat.com", "posuere.cubilia.curae@eleifend.com", "dictum.phasellus@nasceturridiculusmus.edu", "pellentesque@nascetur.org", "neque@euismodenim.edu", "donec@blandit.org", "metus.in.nec@disparturient.co.uk", "magna.lorem@pedeetrisus.com", "volutpat.ornare.facilisis@sed.com", "ullamcorper@cubiliacurae.ca", "in@etiamimperdietdictum.ca", "donec@ullamcorpernislarcu.net", "at.pede.cras@ipsumportaelit.net", "vulputate@etpedenunc.com", "enim@vestibulumneque.ca", "fermentum@lacus.net", "praesent@vitaevelit.com", "sagittis@sagittis.co.uk", "dapibus.ligula.aliquam@loremsemper.co.uk", "lobortis.nisi.nibh@praesent.net", "ut.pellentesque@fusce.edu", "nulla.donec.non@hendreritnequein.co.uk", "ante.blandit.viverra@lorem.net", "velit@elitsed.net", "velit.dui.semper@pharetra.edu", "nunc@quisquelibero.edu", "dolor.quam@nullaat.net", "etiam.laoreet.libero@malesuadavel.edu", "nunc.est.mollis@velitpellentesque.net", "purus@amet.org", "varius.orci@nequenullamnisl.net", "proin.velit@porttitor.com", "ac.mattis.velit@ut.edu", "sed.nec.metus@idmollis.org", "natoque@nullacraseu.com", "fermentum@enim.net", "bibendum.fermentum.metus@imperdiet.org", "purus.nullam.scelerisque@utipsumac.co.uk", "laoreet.libero@ametconsectetuer.ca", "congue.a.aliquet@justonec.co.uk", "enim.mauris.quis@nullaat.com", "dolor@enimcommodohendrerit.com", "vel.est@nunc.co.uk", "id@tempus.ca", "sem.magna.nec@euaugue.ca", "iaculis.quis@eulacus.net", "mauris.a@inornare.co.uk", "quis.lectus.nullam@pellentesque.edu", "quam@classaptenttaciti.net", "tellus.imperdiet@ullamcorperduis.edu", "eget.metus.in@sem.org", "magna.lorem@egestas.ca", "ipsum.phasellus.vitae@tellusphaselluselit.net", "scelerisque.lorem.ipsum@liberolacus.com", "arcu.sed.et@aliquetvelvulputate.org", "non@congueturpis.com", "justo.sit.amet@euodiotristique.org", "adipiscing.non@montesnascetur.ca", "sem@vel.net", "condimentum.eget@morbi.ca", "nonummy.ipsum@magnaloremipsum.net", "suspendisse@vel.net", "phasellus.libero@non.ca", "in@afeugiattellus.co.uk", "maecenas@volutpatornare.co.uk", "ante.lectus@vestibulum.ca", "malesuada.malesuada.integer@aeneansed.org", "aliquam@semut.org", "est.nunc@sodalesmaurisblandit.edu", "donec.fringilla@arcu.ca", "aliquet.diam@duis.co.uk", "tincidunt.nunc@euenimetiam.com", "consequat.auctor@volutpatnulla.edu", "non@quamvelsapien.org", "est.ac.mattis@duis.ca", "feugiat.lorem.ipsum@mattisornarelectus.co.uk", "dapibus.ligula@sitametconsectetuer.ca", "pellentesque.tincidunt@magna.net", "pede.cras@eu.com", "non.bibendum.sed@ametfaucibusut.ca", "maecenas@maurissapiencursus.net", "mollis.duis.sit@felisorciadipiscing.ca", "lobortis@velesttempor.com", "vestibulum@sit.co.uk", "dapibus.quam@eleifendvitaeerat.net", "massa.integer@inaliquet.com", "eget.venenatis.a@loremauctor.edu", "lectus@blandit.edu", "cursus@loremipsum.org", "eleifend.vitae.erat@aliquetvel.ca", "egestas.lacinia@etiam.co.uk", "donec.est.mauris@ametrisus.ca", "nascetur@tincidunt.com", "lorem.ipsum.dolor@erosnon.com", "tincidunt.tempus@donecvitaeerat.net", "quis.tristique.ac@enimcondimentumeget.co.uk", "risus@dapibusrutrum.org", "semper@famesac.edu", "ac.eleifend.vitae@atpretiumaliquet.com", "integer.eu.lacus@inmolestie.co.uk"]
# функция сортировки по окончанию строки на .com

def email_com_search(arr):
    res = []
    for val in arr:
        if str('.com') in val:
            res.append(val)
    return res

result = email_com_search(emails)
count = len(result)
pprint.pprint(result)
print("Количество email заканчивающихся на .com: %d" % count)
'''
'''
def sum(a, b):
    try:
        s = int(a) + int(b)
        return s
    except:
        print("Пожалуйста Введите цифры")
        return None


print("Калькулятор")
while True:
    x = input("Введите первое число:")
    y = input("Введите второе число:")
    print("Результат a + b = %s" % sum(x, y))
'''
'''
def search(arr, user_input):
    for val in arr:
        if user_input.lower() == val.lower():
            return val
    return None

countries = ["Malta", "Burkina Faso", "French Polynesia", "Laos", "Yemen", "Guatemala", "Norfolk Island", "Jamaica",
             "Saint Kitts and Nevis", "Malaysia", "Malaysia", "Panama", "Mauritania", "Guam", "Seychelles",
             "Uzbekistan", "Anguilla", "Hungary", "Montenegro", "French Polynesia", "Benin", "Viet Nam", "Afghanistan",
             "Grenada", "Belize", "Pakistan", "Venezuela", "Reunion", "Ireland", "Bonaire, Sint Eustatius and Saba",
             "Northern Mariana Islands", "Uzbekistan", "Austria", "Uruguay", "Christmas Island", "Gabon", "Sweden",
             "Malaysia", "Czech Republic", "Sierra Leone", "Guinea", "Macao", "Uganda", "Australia",
             "Equatorial Guinea", "Saudi Arabia", "Luxembourg", "China", "Oman", "Angola", "Latvia", "Montenegro",
             "Germany", "Sweden", "Kiribati", "British Indian Ocean Territory", "Estonia", "Cambodia", "Egypt", "Palau",
             "Taiwan", "Guatemala", "Palestine, State of", "Lebanon", "Moldova", "Guyana", "Burkina Faso", "Belarus",
             "Cameroon", "American Samoa", "Portugal", "Ethiopia", "Nigeria", "Mauritania", "Slovakia",
             "Virgin Islands, United States", "Côte D'Ivoire (Ivory Coast)", "Viet Nam", "Nicaragua", "Cook Islands",
             "Guatemala", "Bhutan", "Malta", "United States", "Kiribati", "Italy", "Cape Verde", "Micronesia",
             "French Southern Territories", "Swaziland", "Azerbaijan", "Suriname", "Côte D'Ivoire (Ivory Coast)",
             "Congo, the Democratic Republic of the", "Brunei", "Israel", "Samoa", "Serbia",
             "United Kingdom (Great Britain)", "Senegal"]
while True:
    c_name = input("Введите название страны: ")
    res = search(countries, c_name)
    if isinstance(res, str):
        print("Страна найдена: %s" % res)
    else:
        print("Ничего не найденно повторите попытку")

'''
'''
def log(history, str):
    history.append(str)
    return history
history = []

while True:
    data = input("Введите данные")
    print(log(history, data))
'''
'''

def sum(a1, a2):
    res = []
    min_len = 0
    a1_len = len(a1)
    a2_len = len(a2)
    if a1_len == a2_len:
        min_len = a1_len
    elif a1_len > a2_len:
        min_len = a2_len
    elif a2_len > a1_len:
        min_len = a1_len
    for idx in range(min_len):
      sum = a1[idx] + a2[idx]
      res.append(sum)
    return res

arr = [1, 2, 3, 4, 5]
arr2 = [6, 7, 8, 9, 9, 7]

res = sum(arr, arr2)
print(res)
'''
'''
dates = ["1595162840", "1605656145", "1599266087", "1612476653", "1609316939", "1591684701", "1611950688", "1603160871",
         "1601976516", "1609346365", "1598976511", "1598301926", "1587390919", "1590390641", "1604813142", "1587025642",
         "1586309759", "1615274266", "1612285733", "1589292794", "1616573090", "1594912220", "1593072934", "1586430763",
         "1586682706", "1597045130", "1614566077", "1586948529", "1597071518", "1595104052", "1586389274", "1594955986",
         "1608537173", "1614772923", "1615261527", "1593587962", "1597589874", "1609584509", "1602034314", "1599919830",
         "1598550696", "1615756387", "1608403156", "1586900042", "1613527808", "1614021509", "1593002457", "1610503035",
         "1606623537", "1588560036", "1594544042", "1591054404", "1589592980", "1590149883", "1589945599", "1608627553",
         "1593155142", "1592829880", "1606391371", "1592626326", "1609829152", "1591392548", "1613077498", "1592378109",
         "1596279629", "1586275232", "1615957993", "1607317175", "1607266672", "1602761600", "1596316469", "1616731040",
         "1611339554", "1600692892", "1590120256", "1614457682", "1608594257", "1592054537", "1598035692", "1612566083",
         "1587557011", "1603889709", "1597190793", "1586388480", "1601186715", "1593207946", "1610564204", "1593341108",
         "1607463867", "1599119399", "1588648205", "1608259822", "1588605909", "1609559837", "1602298678", "1590328695",
         "1595932422", "1596187678", "1606273886", "1595066024"]

'''
'''
def get_date(arr):
    tmp = []
    for val in arr:
        date = datetime.datetime.fromtimestamp(int(val))
        tmp.append(date)
    return tmp

converted_dates = get_date(dates)
for val in converted_dates:
    print(f"{val:%Y-%m-%d %H:%M:%S}")
'''
'''
def get_years(arr):
    tmp = []
    for val in arr:
        year_seconds = 365 * 24 * 60 * 60
        res = int(val) / year_seconds
        tmp.append(int(res))

    return tmp

years = get_years(dates)
print(years)
'''

# взять массив dates - и посчитать сколько дней пользователь не был на сайте начиная с 2020 года
'''
def get_years(arr):
    tmp = []
    for val in arr:
        years_seconds_50 = 50 * 365 * 24 * 60 * 60  # количество секунд в 50 годах
        res = int(val) - years_seconds_50  # оставшиеся количество секунд от 2020 по 2021год
        day_seconds = 24 * 60 * 60  # количество секунд в дне
        inactive_days = res / day_seconds  # Количество дне с 1 января 2020 года
        tmp.append(inactive_days)
    return tmp


result_day = get_years(dates)
for val in result_day:
    if val > 365:
        print("Воу вы вернулись! мы вас ждали! вас не было %d дн" % val)
    else:
        print("Вас не было на сайте %d" % val)
'''
'''
arr_3d = [
    [1, 3, 5, [1, 2, 3]],
    [8, 5, 6, [1, 2, 3]],
    [7, 1, 6, [2, 4, 7]]
]

for val in arr_3d:
    for i in val:
        if isinstance(i, list):
            for x in i:
                print(x)
        else:
            print(i)
'''
'''
sirets = ["059015941-00004", "347543761-00006", "397739681-00005", "940956329-00004", "670795830-00009",
          "271385841-00009", "038185252-00004", "102497831-00002", "740228515-00004", "487403255-00002",
          "947684387-00006", "858986219-00005", "733334858-00004", "806564357-00002", "846834653-00004",
          "407322437-00002", "195232376-00002", "625498639-00008", "271353914-00002", "994213718-00004",
          "342874732-00007", "764879425-00008", "631741154-00001", "964635981-00001", "360438352-00005",
          "902517952-00005", "509198586-00000", "934646035-00006", "171612765-00007", "440783470-00006",
          "164415853-00005", "154916316-00008", "749166013-00005", "708264981-00000", "667509343-00006",
          "496831033-00006", "107811929-00002", "832468060-00005", "726885460-00006", "185546678-00003",
          "552843641-00002", "766264006-00004", "054286661-00001", "323377283-00003", "972049035-00009",
          "244634739-00001", "021243498-00009", "640938643-00007", "854550860-01111", "854544319-00007",
          "408689396-00005", "892146499-00009", "723252730-00004", "605467182-00008", "859391385-00001",
          "578000697-00008", "102544053-00006", "604545020-00009", "757226006-00000", "446432924-00004",
          "800210817-00006", "083912386-00006", "224509588-00006", "192124386-00009", "027654094-00005",
          "967005927-00009", "088386545-00003", "838412708-00003", "858787112-00003", "095846515-00005",
          "832759112-00002", "737157479-00004", "447190794-00001", "653660779-00006", "829777903-00008",
          "726570823-00005", "613426287-00009", "294843818-00005", "406872010-00003", "783644164-00007",
          "399748599-00004", "057425951-00111", "930348743-00004", "062112149-00000", "680726130-00007",
          "881051189-00002", "727014615-00007", "610912107-00006", "493248934-00009", "690676853-00003",
          "298376427-00001", "075128421-00007", "144700077-00007", "745978320-00000", "752261214-00007",
          "443640198-00000", "478835952-00001", "659631170-00001", "187635305-00001", "021206206-00001"]

'''
'''
def grup_siret(arr):
    tmp = []
    for val in arr:
        res = val.split("-")
        glue = res[1] + "-" + res[0]
        tmp.append(glue)
    tmp.sort()

    multi = []
    current_group = None
    for val in tmp:
        res = val.split("-")
        normal = res[1] + "-" + res[0]
        res = int(res[0])
        if res == current_group:
            multi[current_group].append(normal)
        else:
           multi.append([normal])
           current_group = res

    return multi


res = grup_siret(sirets)
pprint.pprint(res)
'''
'''
sirets = ["059015941-00004", "347543761-00006", "397739681-00005", "940956329-00004", "670795830-00009",
          "271385841-00009", "038185252-00004", "102497831-00002", "740228515-00004", "487403255-00002",
          "947684387-00006", "858986219-00005", "733334858-00004", "806564357-00002", "846834653-00004",
          "407322437-00002", "195232376-00002", "625498639-00008", "271353914-00002", "994213718-00004",
          "342874732-00007", "764879425-00008", "631741154-00001", "964635981-00001", "360438352-00005",
          "902517952-00005", "509198586-00000", "934646035-00006", "171612765-00007", "440783470-00006",
          "164415853-00005", "154916316-00008", "749166013-00005", "708264981-00000", "667509343-00006",
          "496831033-00006", "107811929-00002", "832468060-00005", "726885460-00006", "185546678-00003",
          "552843641-00002", "766264006-00004", "054286661-00001", "323377283-00003", "972049035-00009",
          "244634739-00001", "021243498-00009", "640938643-00007", "854550860-01111", "854544319-00007",
          "408689396-00005", "892146499-00009", "723252730-00004", "605467182-00008", "859391385-00001",
          "578000697-00008", "102544053-00006", "604545020-00009", "757226006-00000", "446432924-00004",
          "800210817-00006", "083912386-00006", "224509588-00006", "192124386-00009", "027654094-00005",
          "967005927-00009", "088386545-00003", "838412708-00003", "858787112-00003", "095846515-00005",
          "832759112-00002", "737157479-00004", "447190794-00001", "653660779-00006", "829777903-00008",
          "726570823-00005", "613426287-00009", "294843818-00005", "406872010-00003", "783644164-00007",
          "399748599-00004", "057425951-00111", "930348743-00004", "062112149-00000", "680726130-00007",
          "881051189-00002", "727014615-00007", "610912107-00006", "493248934-00009", "690676853-00003",
          "298376427-00001", "075128421-00007", "144700077-00007", "745978320-00000", "752261214-00007",
          "443640198-00000", "478835952-00001", "659631170-00001", "187635305-00001", "021206206-00001"]

def search_sirets(serial):
    for val in sirets:
        if serial == val:
            return val
        else:
            None
    print("Нет совпадений")


res = search_sirets("478835952-00001")
print(res)
'''
