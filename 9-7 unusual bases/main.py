# define an input file
fs = "input.txt"
file = open(fs, 'r')


# parse all the lines for the first and second numbers
def parse(line):
    arr = line.strip().split(" ")
    first = arr[0]
    second = arr[1]
    return first, second


""" generate fib sequence"""


def fib(limit):
    a, b = 1, 1

    while a <= int(limit):
        yield a
        a, b = b, a + b


"""input a fib number and output a decimal number"""


def dec_to_fib(num):
    fib_seq = list(fib(int(num)))
    tmp = int(num)
    output = []

    # reverse the generator
    fib_rev = fib_seq[::-1]

    for i in fib_rev:
        val = int(i)

        # if the current total (tmp) - the current value from the sequence (val) < 0 reject from sequence
        if tmp - val < 0:
            output.append(0)
        else:
            # fib sequence val (val) is subtracted from total and tracked
            tmp -= val
            output.append(1)

    return output


"""convert fib number sequence to base 10 number """


def fib_to_dec(num):
    fib_seq = list(fib(int(num)))
    output = 0

    for i, j in zip(reversed(num), fib_seq):
        if i == '1':
            output += j

    return output


# output file
out = open("output.txt", 'w')

for line in file:
    f, s = parse(line)
    if f == "10":
        output = dec_to_fib(s)
        out.write(f + " " + s + " " + "\t" + str(output) + "\n")
    elif f == "F":
        output = fib_to_dec(s)
        out.write(f + " " + s + " " + "\t" + str(output) + "\n")

# close output file
out.close()
