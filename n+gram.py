import fileinput

def hamming_distance(a, b):
    hd = 0
    if len(a) > 2 and len(b) > 2:
        for i in range(3):
            if a[i] != b[i]:
                hd += 1
    return hd

last_line = "   "

for line in fileinput.input():
    print(line, hamming_distance(last_line, line))
    last_line = line
