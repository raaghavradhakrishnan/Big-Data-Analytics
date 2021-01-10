import sys

# input comes from STDIN (standard input)

for line in sys.stdin:
    line = line.strip()
    line = line.split(",")

    if len(line) >=2:
        arr = line[4]
        delay = line[8]

        print ('%s\t%s' % (arr,delay))

