a = []
ch = 2
while len(a) != 1100:
    a.append(str(ch))
    ch += 24
for i in a:
    if i[-1] == '2':
        a.remove(i)
for j in range(len(a)):
    if '024' in a[j]:
        kek = a[j]we.split('0')
        kek = ''.join(kek)
        a.insert(j, kek)
        a.remove(a[j+1])
print(a)'fe'