word = str(input("enter a word/sentence:"))
new_word = ""
for i in word:
    new_word = i + new_word

print("result:", new_word)