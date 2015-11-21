"""
Implement a simple morse code decoder
"""

MORSE_CODE = {
    '....':'H',
    '.':'E' ,
    '-.--':'Y',
    '.---':'J',
    '..-':'U',
    '-..':'D',
    '':' '
}

def decodeMorse(morseCode):
    r = ''
    for word in morseCode.split('   '):
        for c in word.split(' '):
            try:
                r += MORSE_CODE[c]
            except KeyError:
                pass
        r += ' '
    return r[:-1]

import unittest
class TestFirst(unittest.TestCase):
    def test_first(self):
        self.assertEqual(decodeMorse('.... . -.--   .--- ..- -.. .'),'HEY JUDE')