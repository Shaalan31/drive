#! /usr/bin/python2
# -*- coding: UTF-8 -*-

conversion = {'a':' أي ',
              'A':'',
              'b': ' بي ',
              'B': '',
              'c': ' سي ',
              'C': '',
              'd': ' دي ',
              'D': '',
              'e': ' إي ',
              'E': '',
              'f': ' اف ',
              'F': '',
              'g': ' جي ',
              'G': '',
              'h': ' هيتش ',
              'H': '',
              'i': ' ايي ',
              'I': '',
              'j': ' جَي ',
              'J': '',
              'k': ' كَي ',
              'K': '',
              'l': ' إل ',
              'L': '',
              'm': ' إم ',
              'M': '',
              'n': ' إن ',
              'N': '',
              'o': ' آو ',
              'O': '',
              'p': ' بِيِي ',
              'P': '',
              'q': ' كِو ',
              'Q': '',
              'r': ' أر ',
              'R': '',
              's': ' إس ',
              'S': '',
              't': ' تي ',
              'T': '',
              'u': ' يو ',
              'U': '',
              'v': ' في ',
              'V': '',
              'w': ' دبليو ',
              'W': '',
              'x': ' إكس ',
              'X': '',
              'y': ' وَاي ',
              'Y': '',
              'z': ' زي ',
              'Z': '',
              }

def post_processing(text):
    for key,value in conversion:
        text = text.replace(key,value)
    return text