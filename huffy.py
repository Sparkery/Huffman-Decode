#Sparkery
#September 28, 2013
#Huffman Decode with Shannon Entropy

from math import log

array = []
for X in range(10000):
	array.append(None)

key = open("decodeFIXED.txt", "r").read().split()

code = key.pop()

for X in key:
	char = X[0]
	position = 1
	for Y in range(1, len(X)):
		position *= 2
		if X[Y] == '1':
			position += 1
	array[position] = char

for X in range(len(array)):
	if array[X] is not None:
		print(str(X) + " " + array[X])


#
#

chars = []
message = []
new = False
pos = 1
for X in code:
	if new is True:
		new = False
		pos = 1
	pos *= 2
	if X == '1':
		pos += 1
	if array[pos] is not None:
		message.append(array[pos])
		if array[pos] not in chars:
			chars.append(array[pos])
		new = True

print("".join(message))
print("ASCII: " + str(len(message)*8))
print("CUSTOM: " + str(len(code)))

prob = []
for X in chars:
	num = 0
	for Y in message:
		if X == Y:
			num += 1
	prob.append(num / float(len(message)))

check = 0
minimum = 0
for X in prob:
	minimum += ( X * log(X)/log(2.0) )
	check += X

print("MINIMUM: " + str(int(-1 * minimum * float(len(message)))))
