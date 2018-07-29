import os,sys
from os import path
import random


fp = open("digits_train.txt", "r")
f = open('digits_train2.txt','w')
sys.stdout = f
for line in fp.readlines():
	my_list = line.split(",")
	index = random.randint(1,64)
	my_list[index] = "0"
	str1 = ','.join(my_list)
	print str1
fp.close()
f.close()