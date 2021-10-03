import re

input_text = open("stripvocab.txt", "r").read()
input_text = re.sub(r'[^a-zA-Z\n\s\']', '', input_text)
input_text = re.sub(r'\'s', "", input_text)
input_text = list(dict.fromkeys(input_text.split()))

words_to_remove = open("wordstoremove.txt", "r").read().splitlines()
words_to_remove_capitalized = []
for item in words_to_remove:
    item = item.capitalize()
    words_to_remove_capitalized.append(item)

for word in words_to_remove:
    try:
        input_text.remove(word)
    except ValueError:
        print("Key %s not found" %word)

for word in words_to_remove_capitalized:
    try:
        input_text.remove(word)
    except ValueError:
        print("Key %s not found" %word)

print('\n'.join(map(str, input_text)))
