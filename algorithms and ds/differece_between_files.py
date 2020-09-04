
filename1 = "namespaces.txt"
filename2 = filename1[:-4] + "created.txt"

namespaceslist = list()
namespacescreatedlist = list()

with open(filename1, 'r') as f:
    for line in f.readlines():
        namespaceslist.append(line[:-1])
namespaceslist[-1] += 'h'

with open(filename2, 'r') as f:
    for line in f.readlines():
        namespacescreatedlist.append(line[:-1])

tobedeleted = list()
for i in namespacescreatedlist:
    if i not in namespaceslist:
        tobedeleted.append(i)

tobecreated = list()
for i in namespaceslist:
    if i not in namespacescreatedlist:
        tobecreated.append(i)

print(tobecreated, len(tobecreated))
print(tobedeleted)



