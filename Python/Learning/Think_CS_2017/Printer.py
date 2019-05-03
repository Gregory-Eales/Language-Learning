size = int(input("What size would you like to print? (0-26)\n\n"))

for x in range(1, size + 1):

    print("-" * 2 * (size - x), end="")

    for n in range(1, x):
        print(chr(97 + size - n) + "-", end="")

    print(chr(97 + size - x), end="")

    for n in range(1, x):
        print("-" + chr(97 + size - x + n), end="")

    print("-" * 2 * (size - x))

for x in range(1, size):

    print("-" * 2 * (x), end="")

    for n in range(1, size - x):
        print(chr(97 + size - n) + "-", end="")

    print(chr(97 + x), end="")

    for n in range(1, size - x):
        print("-" + chr(97 + x + n), end="")

    print("-" * 2 * (x))