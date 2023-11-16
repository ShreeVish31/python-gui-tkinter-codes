import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
sys = "[]{}()*;/,._-@#!$&"

all = lower+upper+num+sys
length = 16
password = "".join(random.sample(all,length))

print(password)