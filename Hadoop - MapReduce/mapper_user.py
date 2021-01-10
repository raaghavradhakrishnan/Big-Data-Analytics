import sys

# input comes from STDIN (standard input)

for line in sys.stdin:
    line = line.strip()
    line = line.split("::")

    if len(line) >=2:
        movieID = line[0]
        rating = line[2]

        print ('%s\t%s' % (movieID,float(rating)))

