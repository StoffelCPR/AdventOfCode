import string

with open('./resources/2.txt') as f:
    content = f.readlines()

content = [x.strip('\n') for x in content]


def part_one():
    twos = 0
    threes = 0

    for box_id in content:
        alphabet = [0]*26
        for letter in box_id:
            alphabet[string.ascii_lowercase.index(letter)] += 1
        if 2 in alphabet:
            twos += 1
        if 3 in alphabet:
            threes += 1

    checksum = twos*threes
    print(checksum)


def part_two():
    # PART TWO
    index = -1
    common_letters = ''
    for box_id in content:
        for b_id in content:
            checksum = [None]*len(box_id)
            for x in range(0, len(box_id)):
                checksum[x] = string.ascii_lowercase.index(box_id[x])-string.ascii_lowercase.index(b_id[x])
                if checksum[x] != 0:
                    index = checksum[x]
            differences = sum(1 for i in checksum if i != 0)
            if differences == 1:
                common_letters = box_id[0:index+1] + box_id[index+2:len(box_id)]
    print(common_letters)


part_one()
part_two()
