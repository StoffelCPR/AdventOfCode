import pandas as pd

with open('./resources/4.txt') as f:
    content = f.readlines()

content = [x.strip('\n') for x in content]
content.sort()
print(content)
c = []
for x in range(0, 61):
    c.append(x)


guards_sleep_df = pd.DataFrame(None, columns=c)

print(guards_sleep_df)

guard_id = None
fell_asleep = None
woke_up = None
for event in content:
    informations = event.split(' ')
    print()
    event_type = informations[2]
    if fell_asleep is not None and woke_up is not None:
        for x in range(0, 60):
            if fell_asleep <= x < woke_up:
                guards_sleep_df.loc[guard_id][x] += 1
                guards_sleep_df.loc[guard_id][60] += 1
    if event_type == 'Guard':
        guard_id = informations[3][1:len(informations[3])]
        fell_asleep = None
        woke_up = None
        if guard_id not in guards_sleep_df.index:
            guards_sleep_df.loc[guard_id] = 0
    if event_type == 'falls':
        fell_asleep = int(informations[1][3:len(informations[1])-1])
    if event_type == 'wakes':
        woke_up = int(informations[1][3:len(informations[1])-1])

guards_sleep_df.to_csv('gg.csv', sep=',')
print((guards_sleep_df.max()))

