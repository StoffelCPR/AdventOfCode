import datetime
start = datetime.datetime.now()
with open('./resources/1.txt') as f:
    content = f.readlines()

content = [x.strip('\n') for x in content]

# Supposed to contain the sum for each iteration (summed of course)
answers_for_one = [0]
# Supposed to hol the answer to Part 1
answer_one = 0
# This list has all sums for every time something is added or removed (Part 2)
answers = [0]
# Contains the sum of an iteration
sum_calc = 0
# Contains the answer for Part 2
answer = 0
# Flag for the While loop
done = False
while not done:
    # checks for every frequency given
    for x in content:
        # adds it up
        sum_calc += int(x)
        # checks if it is already the second answer
        if sum_calc in answers:
            # stores answer for Part 2
            answer = sum_calc
            # sets flag so the while loop ends
            done = True
            break
        # adds to the answers
        answers.append(sum_calc)
    # Adds all iteration end results
    answers_for_one.append(sum_calc)
# Stores for Part 1
answer_one = answers_for_one[0]

print('Answer One: ' + str(answer_one))
print('Answer Two: ' + str(answer))

end = datetime.datetime.now()
elapsed_time = int((end - start).total_seconds())
print('Duration: {:.0f}min {:.0f}s'.format(elapsed_time // 60, elapsed_time % 60))
