import pandas as pd

# Loading data
with open('./resources/3.txt') as f:
    content = f.readlines()

content = [x.strip('\n') for x in content]

# Setting up a dataframe
a = ['.']*1000  # 1000 '.'
y = [a]*1000    # 1000x1000 '.'
c = []  # colums of the DataFrame
for x in range(0, 1000):
    c.append(x)
df = pd.DataFrame(y, columns=c)

# Analyzing claims
perfect_claimer = []
for claim in content:
    # All informations inside one line
    informations = claim.split(' ', 5)
    # Where to start the claim
    column_start = int(informations[2].split(',', 1)[0])
    row_start = int(informations[2].split(',', 1)[1].split(':', 1)[0])
    # Where to end the claim
    column_end = int(column_start) + int(informations[3].split('x', 1)[0])
    row_end = int(row_start) + int(informations[3].split('x', 1)[1])
    # The id of the claimer
    claimer_id = informations[0].split('#', 1)[1]
    # Does the claim overlap ?
    claim_overlap = False
    # Iterate through our rectangle
    for i in range(column_start, column_end):
        for j in range(row_start, row_end):
            # If there is already a claim
            if df[i][j] != '.':
                # If the cell variable is listed as perfect claim
                if df[i][j] in perfect_claimer:
                    # Deny the perfect claim
                    perfect_claimer[perfect_claimer.index(df[i][j])] = None
                # Mark this cell as double claim (or more)
                df[i][j] = 'X'
                # Mark that this claim had an overlap
                claim_overlap = True
            # If there is no claim in that cell
            else:
                # Write the claimer id into the cell
                df[i][j] = claimer_id
    # if there wasn't an overlap
    if not claim_overlap:
        # write the elves id onto the perfect claimer list
        perfect_claimer.append(claimer_id)

# counting overlaps
count = 0

# iterating over DataFrame
for i in range(0, 1000):
    for j in range(0, 1000):
        # If there is more than one claim in a cell (marked by the X)
        if df[i][j] == 'X':
            # increment by 1
            count += 1

# Output
print(count)
print(next((item for item in perfect_claimer if item is not None), 'All are Nones'))  # Get the first cell with id

