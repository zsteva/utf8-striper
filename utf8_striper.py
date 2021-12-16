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

# šđčćžŠĐČĆŽ
cp1250chars = [ 0x9a, 0xf0, 0xe8, 0xe6, 0x9e, 0x8a, 0xd0, 0xc8, 0xc6, 0x8e ]

def striper():
	while True:
		byte = sys.stdin.buffer.read(1)
		if byte == b'':
			break
		if byte[0] & 0xe0 == 0xc0: # utf 2 byte char
			remaind = sys.stdin.buffer.read(1)
			if remaind[0] & 0xc0 == 0x80:
				byte = b'.'
			else:
				byte += remaind
		elif byte[0] & 0xf0 == 0xe0: # utf 3 byte char
			remaind = sys.stdin.buffer.read(2)
			if remaind[0] & 0xc0 == 0x80 and remaind[1] & 0xc0 == 0x80:
				byte = b'.'
			else:
				byte += remaind
		elif byte[0] & 0xf8 == 0xf0: # utf 4 byte char
			xxx = sys.stdin.buffer.read(3)
			if remaind[0] & 0xc0 == 0x80 and remaind[1] & 0xc0 == 0x80 and remaind[2] & 0xc0 == 0x80:
				byte = b'.'
			else:
				byte += remaind
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
