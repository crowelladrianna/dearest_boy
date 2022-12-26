import random
import re

# splits a text file by punctuation and returns list of parts
def break_letter(file_name):
    broken_parts = []
    with open(file_name) as f:
        for line in f:
            broken_parts = broken_parts + re.split(r"\s*[\!\.\"\?,\–\(\)\-\:;\n]\s*",line)
    broken_parts_2 = []
    for part in broken_parts:
        if part:
            broken_parts_2.append(part)
    return broken_parts_2

# parts: list of phrases, length: integer number of lines desired in poem, shuffle: boolean representing
# whether to shuffle order of lines in final poem
# inspired by Lillian-Yvonne Bertram's Travesty Generator 
# and Nick Montfort's Through the Park at https://nickm.com/poems/through_the_park.py
def make_poem(parts, length, shuffle):
    poem = parts[:len(parts)]
    while len(poem) > length:
        poem.remove(random.choice(poem))
    if shuffle:
        random.shuffle(poem)
    return "\n".join(poem)

# 40 lines
ow1 = break_letter("letters/oscar_wilde/oscar_wilde_1.txt")

# 18 lines
ow2 = break_letter("letters/oscar_wilde/oscar_wilde_2.txt")

# 31 lines
ow3 = break_letter("letters/oscar_wilde/oscar_wilde_3.txt")

# 18 lines
ow4 = break_letter("letters/oscar_wilde/oscar_wilde_4.txt")

# 245 lines
ow5 = break_letter("letters/oscar_wilde/oscar_wilde_5.txt")
print(len(ow5))


while(True):
    if(input("Continue? y/n ") == "n"):
        break
    length = int(input("Length: "))
    shuffle_s = input("Shuffle? y/n ")
    shuffle = True if shuffle_s == "y" else False
    print()
    print(make_poem(ow5, length, shuffle))
    print()

    
