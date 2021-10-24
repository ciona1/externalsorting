import random

afile = open("largefile.txt", "w" )

for i in range(int(input('How many random numbers?: '))):
    line = str(random.randint(1, 100))
    afile.write(line+"\n")
    print(line)

afile.close()