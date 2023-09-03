''' 
Let us define a string, comprising English alphabets, as NICE
if each vowel within it is equidistant from its successor and
predecessor vowel, if applicable. E.g., “rhythm”, “cool”,
“malayalam” are NICE strings. Write a program to verify
whether a given string is NICE or not. You are required to
take the string as a direct input without asking for its length.
'''
import re

str=input("Please input the string \n")
index = [m.start() for m in re.compile(r'[aeiouAEIOU]').finditer(str)]

mybool = False
if len(index)>2:
	for i in range(1,len(index)-1):
		if index[i-1]-index[i]!= index[i]-index[i+1]:
			mybool = True
			break
if mybool==False:
	print(str, " is NICE")
else:
	print(str, "is not NICE")