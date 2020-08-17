fname = input("Enter file:")
if len(fname) < 1 : name = "mbox-short.txt"
handle = open(fname)
counts = dict()

for line in handle:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    words = line.split()
#    print(words)
    time = words[5]
#    print(time)
    hours = time.split(':')
#    print(hours[0])

    counts[hours[0]] = counts.get(hours[0], 0) + 1

for k,v in sorted(counts.items()):
    print(k,v)
