import sys

def look_up(lookup):
    result = 0
    with open("verben.csv", "r") as f:
        searchlines = f.readlines()
    for line in searchlines:
        verben = line.strip('\n').split(',')
        if lookup == verben[0]:
            return verben
    for line in searchlines:
        verben = line.strip('\n').split(',')
        if lookup in verben[0]:
            return verben

    return ['0','0','0','0','0','0','0','0','0','0']

result = open('verben_query_result.csv', 'w')
with open(sys.argv[1], 'r') as f:
    searchlines = f.readlines()
for verb in searchlines:
    query = look_up(verb.strip('\n'))
    result.write('{},{} {},{}\n'.format(query[0],query[-1].strip('\n'),query[5],query[-3]))
