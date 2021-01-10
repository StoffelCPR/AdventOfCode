import string
import datetime

with open('./resources/5.txt') as f:
    content = f.readlines()

content = [x.strip('\n') for x in content]
content = content[0]


def full_reaction(content_string):
    has_reacted = True
    while has_reacted:
        content_length = len(content_string)
        reaction = []
        for x in range(0, content_length):
            if x != content_length-1 and content_string[x].lower() == content_string[x+1].lower():
                if content_string[x].isupper() and content_string[x+1].islower() or content_string[x].islower() \
                        and content_string[x+1].isupper():
                    content_string = content_string[:x] + content_string[(x + 2):]
                    reaction.append(True)
                    break
                else:
                    reaction.append(False)
        if True not in reaction:
            break
    return len(content_string)


def shortest_reaction(content_string):
    alphabet = string.ascii_lowercase
    lengths = []
    for letter in alphabet:
        temp_string = content_string
        lowercase = letter
        uppercase = letter.upper()
        while True:
            deletion = False
            for x in range(0, len(temp_string)):
                if temp_string[x] == lowercase or temp_string[x] == uppercase:
                    temp_string = temp_string[:x] + temp_string[(x + 1):]
                    deletion = True
                    break
            if not deletion:
                break
        lengths.append(full_reaction(temp_string))
    return min(lengths)


start = datetime.datetime.now()

full_reaction(content)
print(str(shortest_reaction(content)))

end = datetime.datetime.now()
elapsed_time = int((end - start).total_seconds())
print('Duration: {:.0f}min {:.0f}s'.format(elapsed_time // 60, elapsed_time % 60))
