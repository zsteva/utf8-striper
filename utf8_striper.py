#!/usr/bin/env python3

# MIT License
# 
# Copyright (c) 2021 Zeljko Stevanovic
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys

cyr2lat = {
	b'\xd0\xb0': b'a',
	b'\xd0\xb1': b'b',
	b'\xd1\x86': b'c',
	b'\xd0\xb4': b'd',
	b'\xd0\xb5': b'e',
	b'\xd1\x84': b'f',
	b'\xd0\xb3': b'g',
	b'\xd1\x85': b'h',
	b'\xd0\xb8': b'i',
	b'\xd1\x98': b'j',
	b'\xd0\xba': b'k',
	b'\xd0\xbb': b'l',
	b'\xd0\xbc': b'm',
	b'\xd0\xbd': b'n',
	b'\xd0\xbe': b'o',
	b'\xd0\xbf': b'p',
	b'\xd1\x99': b'lj',
	b'\xd1\x80': b'r',
	b'\xd1\x81': b's',
	b'\xd1\x82': b't',
	b'\xd1\x83': b'u',
	b'\xd0\xb2': b'v',
	b'\xd1\x9a': b'nj',
	b'\xd1\x9f': b'd\xc5\xbe',
	b'\xd0\xb6': b'\xc5\xbe',
	b'\xd0\xb7': b'z',
	b'\xd1\x88': b'\xc5\xa1',
	b'\xd1\x92': b'\xc4\x91',
	b'\xd1\x87': b'\xc4\x8d',
	b'\xd1\x9b': b'\xc4\x87',
	b'\xd0\x90': b'A',
	b'\xd0\x91': b'B',
	b'\xd0\xa6': b'C',
	b'\xd0\x94': b'D',
	b'\xd0\x95': b'E',
	b'\xd0\xa4': b'F',
	b'\xd0\x93': b'G',
	b'\xd0\xa5': b'H',
	b'\xd0\x98': b'I',
	b'\xd0\x88': b'J',
	b'\xd0\x9a': b'K',
	b'\xd0\x9b': b'L',
	b'\xd0\x9c': b'M',
	b'\xd0\x9d': b'N',
	b'\xd0\x9e': b'O',
	b'\xd0\x9f': b'P',
	b'\xd0\x89': b'LJ',
	b'\xd0\xa0': b'R',
	b'\xd0\xa1': b'S',
	b'\xd0\xa2': b'T',
	b'\xd0\xa3': b'U',
	b'\xd0\x92': b'V',
	b'\xd0\x8a': b'NJ',
	b'\xd0\x8f': b'D\xc5\xbd',
	b'\xd0\x96': b'\xc5\xbd',
	b'\xd0\x97': b'Z',
	b'\xd0\xa8': b'\xc5\xa0',
	b'\xd0\x82': b'\xc4\x90',
	b'\xd0\xa7': b'\xc4\x8c',
	b'\xd0\x8b': b'\xc4\x86',
}

cyr2cp1250 = {
	b'\xd0\xb0': b'a',
	b'\xd0\xb1': b'b',
	b'\xd1\x86': b'c',
	b'\xd0\xb4': b'd',
	b'\xd0\xb5': b'e',
	b'\xd1\x84': b'f',
	b'\xd0\xb3': b'g',
	b'\xd1\x85': b'h',
	b'\xd0\xb8': b'i',
	b'\xd1\x98': b'j',
	b'\xd0\xba': b'k',
	b'\xd0\xbb': b'l',
	b'\xd0\xbc': b'm',
	b'\xd0\xbd': b'n',
	b'\xd0\xbe': b'o',
	b'\xd0\xbf': b'p',
	b'\xd1\x99': b'lj',
	b'\xd1\x80': b'r',
	b'\xd1\x81': b's',
	b'\xd1\x82': b't',
	b'\xd1\x83': b'u',
	b'\xd0\xb2': b'v',
	b'\xd1\x9a': b'nj',
	b'\xd1\x9f': b'd\x9e',
	b'\xd0\xb6': b'\x9e',
	b'\xd0\xb7': b'z',
	b'\xd1\x88': b'\x9a',
	b'\xd1\x92': b'\xf0',
	b'\xd1\x87': b'\xe8',
	b'\xd1\x9b': b'\xe6',
	b'\xd0\x90': b'A',
	b'\xd0\x91': b'B',
	b'\xd0\xa6': b'C',
	b'\xd0\x94': b'D',
	b'\xd0\x95': b'E',
	b'\xd0\xa4': b'F',
	b'\xd0\x93': b'G',
	b'\xd0\xa5': b'H',
	b'\xd0\x98': b'I',
	b'\xd0\x88': b'J',
	b'\xd0\x9a': b'K',
	b'\xd0\x9b': b'L',
	b'\xd0\x9c': b'M',
	b'\xd0\x9d': b'N',
	b'\xd0\x9e': b'O',
	b'\xd0\x9f': b'P',
	b'\xd0\x89': b'LJ',
	b'\xd0\xa0': b'R',
	b'\xd0\xa1': b'S',
	b'\xd0\xa2': b'T',
	b'\xd0\xa3': b'U',
	b'\xd0\x92': b'V',
	b'\xd0\x8a': b'NJ',
	b'\xd0\x8f': b'D\x8e',
	b'\xd0\x96': b'\x8e',
	b'\xd0\x97': b'Z',
	b'\xd0\xa8': b'\x8a',
	b'\xd0\x82': b'\xd0',
	b'\xd0\xa7': b'\xc8',
	b'\xd0\x8b': b'\xc6',
}

def striper():
	while True:
		byte = sys.stdin.buffer.read(1)
		if byte == b'':
			break
		utf8 = b''
		if byte[0] & 0xe0 == 0xc0: # utf 2 byte char
			remaind = sys.stdin.buffer.read(1)
			if remaind[0] & 0xc0 == 0x80:
				utf8 = byte + remaind
				byte = b'.'
			else:
				byte += remaind
		elif byte[0] & 0xf0 == 0xe0: # utf 3 byte char
			remaind = sys.stdin.buffer.read(2)
			if remaind[0] & 0xc0 == 0x80 and remaind[1] & 0xc0 == 0x80:
				utf8 = byte + remaind
				byte = b'.'
			else:
				byte += remaind
		elif byte[0] & 0xf8 == 0xf0: # utf 4 byte char
			remaind = sys.stdin.buffer.read(3)
			if remaind[0] & 0xc0 == 0x80 and remaind[1] & 0xc0 == 0x80 and remaind[2] & 0xc0 == 0x80:
				utf8 = byte + remaind
				byte = b'.'
			else:
				byte += remaind
		if utf8 in cyr2cp1250:
			sys.stdout.buffer.write(cyr2cp1250[utf8])
		else:
			sys.stdout.buffer.write(byte)

def usage():
	print("usage:")
	print("\t" + sys.argv[0] + " < file_with_mixed_encding.srt > clean.srt")
	print()

def main():
	if sys.stdin.isatty():
		usage()
		sys.exit(-1)
	else:
		striper()

if __name__ == "__main__":
	main()
