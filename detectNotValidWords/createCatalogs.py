validFile ='detectNotValidWords/english'            

file = open(validFile, 'r') #File with valid words
validLines = file.readlines()

a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []
i = []
j = []
k = []
l = []
m = []
n = []
o = []
p = []
q = []
r = []
s = []
t = []
u = []
v = []
w = []
x = []
y = []
z = []
other = []
#separates the word in the corresponding list
for line in validLines:
    if line.lower().startswith('a'):
        a.append(line.lower())
    elif  line.lower().startswith('b'):
        b.append(line.lower())
    elif line.lower().startswith('c'):
        c.append(line.lower())
    elif line.lower().startswith('d'):
        d.append(line.lower())
    elif line.lower().startswith('e'):
        e.append(line.lower())
    elif line.lower().startswith('f'):
        f.append(line.lower())
    elif line.lower().startswith('g'):
        g.append(line.lower())
    elif line.lower().startswith('h'):
        h.append(line.lower())
    elif line.lower().startswith('i'):
        i.append(line.lower())
    elif line.lower().startswith('j'):
        j.append(line.lower())
    elif line.lower().startswith('k'):
        k.append(line.lower())
    elif line.lower().startswith('l'):
        l.append(line.lower())
    elif line.lower().startswith('m'):
        m.append(line.lower())
    elif line.lower().startswith('n'):
        n.append(line.lower())
    elif line.lower().startswith('o'):
        o.append(line.lower())
    elif line.lower().startswith('p'):
        p.append(line.lower())
    elif line.lower().startswith('q'):
        q.append(line.lower())
    elif line.lower().startswith('r'):
        r.append(line.lower())
    elif line.lower().startswith('s'):
        s.append(line.lower())
    elif line.lower().startswith('t'):
        t.append(line.lower())
    elif line.lower().startswith('u'):
        u.append(line.lower())
    elif line.lower().startswith('v'):
        v.append(line.lower())
    elif line.lower().startswith('w'):
        w.append(line.lower())
    elif line.lower().startswith('x'):
        x.append(line.lower())
    elif line.lower().startswith('y'):
        y.append(line.lower())
    elif line.lower().startswith('z'):
        z.append(line.lower())
    else:
        other.append(line.lower())

catalogs=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','other']

for letter in catalogs:
    tempFile='detectNotValidWords/catalogs/'+letter+'catalog'
    open(tempFile, 'w').close()
    temp = open(tempFile, 'a')
    for word in globals()['%s' % letter]:
        temp.write(word)
    temp.close()

print('Catalogs were created succesfully')