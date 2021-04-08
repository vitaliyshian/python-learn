import pprint
import lib.functions as utils
import lib.game as black_jack


#black_jack.play()
'''
test1 = black_jack.eval_aces([{"name": "ace", "color": "clubs", "view": "A", "colorView": "C", "value": 11},
    {"name": "ace", "color": "spades", "view": "A", "colorView": "S", "value": 11}])
print(test1)
assert test1 == 12


test2 = black_jack.eval_aces([{"name": "ace", "color": "diamonds", "view": "A", "colorView": "D", "value": 11},
    {"name": "ace", "color": "clubs", "view": "A", "colorView": "C", "value": 11},
    {"name": "ace", "color": "spades", "view": "A", "colorView": "S", "value": 11}])
print(test2)
assert test2 == 13


test3 = black_jack.eval_aces([{"name": "king", "color": "hearts", "view": "K", "colorView": "H", "value": 10},
                              {"name": "ace", "color": "hearts", "view": "A", "colorView": "H", "value": 11}])
print(test3)
assert test3 == 21


test4 = black_jack.eval_aces([{"name": "eight", "color": "hearts", "view": "8", "colorView": "H", "value": 8},
                              {"name": "eight", "color": "diamonds", "view": "8", "colorView": "D", "value": 8},
                              {"name": "ace", "color": "spades", "view": "A", "colorView": "S", "value": 11},
                              {"name": "two", "color": "spades", "view": "2", "colorView": "S", "value": 2}])
print(test4)
assert test4 == 19


test5 = black_jack.eval_aces([{"name": "ace", "color": "hearts", "view": "A", "colorView": "H", "value": 11},
    {"name": "ace", "color": "diamonds", "view": "A", "colorView": "D", "value": 11},
    {"name": "ace", "color": "clubs", "view": "A", "colorView": "C", "value": 11},
    {"name": "ace", "color": "spades", "view": "A", "colorView": "S", "value": 11}])
print(test5)
assert test5 == 14


test6 = black_jack.eval_aces([{"name": "jack", "color": "hearts", "view": "J", "colorView": "H", "value": 10},
                              {"name": "jack", "color": "diamonds", "view": "J", "colorView": "D", "value": 10},
                              {"name": "ace", "color": "spades", "view": "A", "colorView": "S", "value": 11},
                              {"name": "two", "color": "spades", "view": "2", "colorView": "S", "value": 2}])
print(test6)
assert test6 > 21
'''


