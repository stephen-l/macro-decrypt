__author__ = "stephen-l"
__date__ = "27/9/16 09:56"
__version__ = "0.2"


def a(crypt, x, y):
    return decrypt(crypt, x, y, 1).replace('\n', '\n')[:-7].lower()

def b(x, y, crypt):
    return decrypt(crypt, x, y , 2)

def d(x, y, crypt):
    return decrypt(crypt, x, y, 1).replace('\n', '\n')[:-7].lower()

def decrypt(inStr, x, y, div):
    intMod = y % len(inStr)
    strStore = ""
    while len(strStore) < (len(inStr) / div):
        strStore += right(left(inStr, intMod + 1), 1)
        intMod = (intMod + x) % len(inStr)
    return strStore

def left(s, amount):
    return s[:amount]

def right(s, amount):
    return s[-amount:]
