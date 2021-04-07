#ayhaga
f = open('ReadPairsInput.txt', 'r')
#t = open('ReadPairsOutput.txt', 'r')
#output = t.read()
lines = f.read()
lines = lines.split('\n')
pair = lines[0].split()
size = int(pair[0])
gap = int(pair[1])
lines.pop(0)

prefix = []
suffix = []
for line in lines:
    p = line.split('|')
    # print(p)
    prefix.append(p[0])
    suffix.append(p[1])


firstsPrefix = []
secondsPrefix = []
for read in prefix:
    firstsPrefix.append(read[:size-1])
    secondsPrefix.append(read[1:size])

firstsSuffix = []
secondsSuffix = []
for read in suffix:
    firstsSuffix.append(read[:size-1])
    secondsSuffix.append(read[1:size])

start=0
end = 0

for i in range(len(firstsPrefix)):
    flag = 0
    for j in range(len(firstsPrefix)):
        if firstsPrefix[i] == secondsPrefix[j] and firstsSuffix[i] == secondsSuffix[j]:
            flag = 1
            break
    if flag == 0:
        start=i
        break


for i in range(len(prefix)):
    if secondsPrefix[i] in firstsPrefix and secondsSuffix[i] in firstsSuffix:
        continue
    end = i
    break

index = start
preRes = firstsPrefix[index][0]
sufRes = ''
while True:
    valPre = secondsPrefix[index]
    valSuf = secondsSuffix[index]

    if index == end:
        preRes = preRes + valPre
        sufRes = sufRes + valSuf
        break

    preRes = preRes + valPre[0]
    sufRes = sufRes + valSuf[0]

    for i in range(len(firstsSuffix)):
        if firstsPrefix[i] == valPre and firstsSuffix[i] == valSuf:
            index = i
            break

res = preRes + sufRes[-(size+gap):]
print(res)
if(res == output):
    print("Dr Esraa Ahsan TA Felkoleya")
else:
    print("7asal kheer")
