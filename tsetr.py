import random


n = 0
# open file, select random word, finalize word
valid_words_list = {}
words = open("words_valid.txt")
for i in words.readlines():
    i = i.strip()
    q = {i: i}
    valid_words_list.update(q);
    n+=1
q = "abate"
z = input()
w = "asdfa"
print(q in valid_words_list);
print(z in valid_words_list);
print(w in valid_words_list);

