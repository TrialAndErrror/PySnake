KEY_CODES = {
    'w': 87,
    'a': 65,
    's': 83,
    'd': 68,
    'Left Arrow': 37,
    'Right Arrow': 39,
    'Up Arrow': 38,
    'Down Arrow': 40,
    '8': 56,
    '4': 52,
    '5': 53,
    '6': 54
}

PIXEL_SIZE = 50

LEFT_KEYS = (KEY_CODES['a'], KEY_CODES['Left Arrow'], KEY_CODES['4'])
RIGHT_KEYS = (KEY_CODES['d'], KEY_CODES['Right Arrow'], KEY_CODES['6'])
UP_KEYS = (KEY_CODES['w'], KEY_CODES['Up Arrow'], KEY_CODES['8'])
DOWN_KEYS = (KEY_CODES['s'], KEY_CODES['Down Arrow'], KEY_CODES['5'])

DIRECTIONS = {
    'right': {'x': 1, 'y': 0},
    'left': {'x': -1, 'y': 0},
    'up': {'x': 0, 'y': -1},
    'down': {'x': 0, 'y': 1},
}
