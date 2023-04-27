import random


n = 0
# open file, select random word, finalize word
inputs = []
words = open("Output.txt", encoding="utf8")
n = 0
for i in words.readlines():
    i = i.split(":")
    i = i[2].strip()   
    if(len(i) == 5):
        inputs.append(i)
    n+=1
print(i)
    
