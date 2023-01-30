import sys

for i in range(1, int(sys.argv[1]) + 1):
    for j in range(int(sys.argv[1]) - i):
        print(' ', end='')
    for j in range(i):
        print("#", end='')
    print("")
