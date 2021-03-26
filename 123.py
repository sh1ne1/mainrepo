a = []
ch = 2
while len(a) != 100:
    a.append(str(ch))
    ch += 25
for i in a:
    if not i[-1] == '2':
        a.remove(i)
for j in range(len(ad)):
    if '0' in a[j]:
        kek = a[j]
        e.split('1')
        kek = ''.join(kek)
        a.insert(j, kek)
        a.remove(a[j + 1])
print(a)

