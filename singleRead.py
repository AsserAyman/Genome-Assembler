#ayhaga
def readFastq(filename):
    sequences = []
    fh=open(filename)
    seqlen = int(fh.readline().rstrip())
    while True:
        fh.readline()
        seq = fh.readline().rstrip()
        fh.readline()
        qual = fh.readline().rstrip()
        if len(seq) == 0:
            break
        sequences.append(seq)
    return sequences, seqlen


sequences, size = readFastq('SingleReads.fastq')
print(sequences)
print(size)
#f = open('SingleReadsInput.txt', 'r')
#t = open('SingleReadOutput.txt', 'r')
#output = t.read()
#lines = f.read()
lines = sequences
#print(lines)
#lines = lines.split('\n')
#size = int(lines[0])
#lines.pop(0)

firsts = []
seconds = []
for read in lines:
    firsts.append(read[:size-1])
    seconds.append(read[1:size])

start=0
end=0
for i in range(len(firsts)):
    if firsts[i] in seconds:
        continue
    start = i
    break

for i in range(len(seconds)):
    if seconds[i] in firsts:
        continue
    end = i
print(start)
res = firsts[start]
index = start
while True:
    val = seconds[index]
    res = res + val[-1]
    if val == seconds[end]:
        break
    for i in range(len(firsts)):
        if firsts[i] == val:
            index = i
            break
print(res)
print(len(res))
