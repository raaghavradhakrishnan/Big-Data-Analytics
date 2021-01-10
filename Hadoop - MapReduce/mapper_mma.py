

import sys

# input comes from STDIN (standard input)

for line in sys.stdin:
    line = line.strip()
    line = line.split(",")

    if len(line) >=2:
        sex = line[3]
        age = line[6]

        print ('%s\t%s' % (sex, age))




