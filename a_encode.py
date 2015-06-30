#!/usr/bin/env python
import sys

def start(arg, val):
	if arg == '-e':
		try:
			binary = bin(int(val) + 8192)[2:].zfill(8)
			divisor = len(binary) / 2
			hex = "{0:#0x}".format(int("1"+binary[:divisor], 2))[3:] + "{0:#0x}".format(int("1"+binary[divisor:], 2))[3:]
			print hex.zfill(4)
		except ValueError:
			print 'You should enter an Integer'
	elif arg == '-d':
		if len(val) > 4 or len(val) < 4:
			print 'Invalid a_encode encoding'
		else:
			decimal = str(int(val, 16))
			print int(bin(int(decimal[:2]))[2:] + bin(int(decimal[2:]))[2:].zfill(8), 2)
	else:
	  __help()

def __help():
  print """
/--------------------------------------\ \n
ART & LOGIC custom encoding c (2015)   / \n
--------------------------------------|

Encoding:
./a_encode.py  -e YOUR_INTEGER

Decoding:
./a_encoder.py -d DECODED_VALUE
"""

if __name__ == '__main__':
  if len(sys.argv) < 3:
    __help();
  else:
    start(sys.argv[1], sys.argv[2])