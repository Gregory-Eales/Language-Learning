Alice = open("alice_words.txt", "w")
Alice.write("Word          Count\n")
Alice.write("===================\n")
Alice_in_Wonderland = open("Alice in Wonderland.txt", "r")
text = Alice_in_Wonderland.readlines()
word_count = {}
for (i, v) in enumerate(text):
    words = text[i].split()
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
for key in word_count.keys():
    Alice.write(str(key) + (" "*(19-len(str(key))-len(str(word_count[key])))) + str(word_count[key]) + "\n")
Alice.close()
