import re
from alive_progress import alive_bar
from datetime import datetime
import io

name = 'fellowship.txt' #File where you want to find invalid or unknown words
relative= 'detectNotValidWords/' #path to where the files are
validFile = relative+'english'  #dictionary with valid words

print('Starting process at ',datetime.now())
verifyFile = relative+name
notValidFile = relative+'invalids/notValid'+name

pattern = r'[^A-Za-zÀ-ÿÀ-ÖØ-öø-ÿ0-9 -]+' #Pattern of accepted characters


file = io.open(verifyFile, mode='r',encoding='utf-8') #File where you want to find invalid words
text = file.readlines()

invalid = []
splitted=[]
for line in text: #Reads every line of the text file to check
    for sline in line.split():
        splitted.append(re.sub(pattern,'',sline)) #Removes any special characters
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
with alive_bar(len(splitted)) as bar:
    for line in splitted:
        found = False
        bar()
        if line.lower().startswith('a'):
            file = open(relative+'catalogs/'+'a'+'catalog', 'r') #File where you want to find invalid words
            text = file.readlines()
            for validWord in text:
                if re.sub('\n','',validWord) == line.lower():
                    found = True
                    break
            if found == False:
                invalid.append(line)
        elif  line.lower().startswith('b'):
            file = open(relative+'catalogs/'+'b'+'catalog', 'r') #File where you want to find invalid words
            text = file.readlines()
            for validWord in text:
                if re.sub('\n','',validWord) == line.lower():
                    found = True
                    break
            if found == False:
                invalid.append(line)
        elif line.lower().startswith('c'):
            file = open(relative+'catalogs/'+'c'+'catalog', 'r') #File where you want to find invalid words
            text = file.readlines()
            for validWord in text:
                if re.sub('\n','',validWord) == line.lower():
                    found = True
                    break
            if found == False:
                invalid.append(line)
        elif line.lower().startswith('d'):
            file = open(relative+'catalogs/'+'d'+'catalog', 'r') #File where you want to find invalid words
            text = file.readlines()
            for validWord in text:
                if re.sub('\n','',validWord) == line.lower():
                    found = True
                    break
            if found == False:
                invalid.append(line)
        elif line.lower().startswith('e'):
            file = open(relative+'catalogs/'+'e'+'catalog', 'r') #File where you want to find invalid words
            text = file.readlines()
            for validWord in text:
                if re.sub('\n','',validWord) == line.lower():
                    found = True
                    break
            if found == False:
                invalid.append(line)
        elif line.lower().startswith('f'):
            file = open(relative+'catalogs/'+'f'+'catalog', 'r') #File where you want to find invalid words
            text = file.readlines()
            for validWord in text:
                if re.sub('\n','',validWord) == line.lower():
                    found = True
                    break
            if found == False:
                invalid.append(line)
        elif line.lower().startswith('g'):
            file = open(relative+'catalogs/'+'g'+'catalog', 'r') #File where you want to find invalid words
            text = file.readlines()
            for validWord in text:
                if re.sub('\n','',validWord) == line.lower():
                    found = True
                    break
            if found == False:
                invalid.append(line)
        elif line.lower().startswith('h'):
            file = open(relative+'catalogs/'+'h'+'catalog', 'r') #File where you want to find invalid words
            text = file.readlines()
            for validWord in text:
                if re.sub('\n','',validWord) == line.lower():
                    found = True
                    break
            if found == False:
                invalid.append(line)
        elif line.lower().startswith('i'):
            file = open(relative+'catalogs/'+'i'+'catalog', 'r') #File where you want to find invalid words
            text = file.readlines()
            for validWord in text:
                if re.sub('\n','',validWord) == line.lower():
                    found = True
                    break
            if found == False:
                invalid.append(line)
        elif line.lower().startswith('j'):
            file = open(relative+'catalogs/'+'j'+'catalog', 'r') #File where you want to find invalid words
            text = file.readlines()
            for validWord in text:
                if re.sub('\n','',validWord) == line.lower():
                    found = True
                    break
            if found == False:
                invalid.append(line)
        elif line.lower().startswith('k'):
            file = open(relative+'catalogs/'+'k'+'catalog', 'r') #File where you want to find invalid words
            text = file.readlines()
            for validWord in text:
                if re.sub('\n','',validWord) == line.lower():
                    found = True
                    break
            if found == False:
                invalid.append(line)
        elif line.lower().startswith('l'):
            file = open(relative+'catalogs/'+'l'+'catalog', 'r') #File where you want to find invalid words
            text = file.readlines()
            for validWord in text:
                if re.sub('\n','',validWord) == line.lower():
                    found = True
                    break
            if found == False:
                invalid.append(line)
        elif line.lower().startswith('m'):
            file = open(relative+'catalogs/'+'m'+'catalog', 'r') #File where you want to find invalid words
            text = file.readlines()
            for validWord in text:
                if re.sub('\n','',validWord) == line.lower():
                    found = True
                    break
            if found == False:
                invalid.append(line)
        elif line.lower().startswith('n'):
            file = open(relative+'catalogs/'+'n'+'catalog', 'r') #File where you want to find invalid words
            text = file.readlines()
            for validWord in text:
                if re.sub('\n','',validWord) == line.lower():
                    found = True
                    break
            if found == False:
                invalid.append(line)
        elif line.lower().startswith('o'):
            file = open(relative+'catalogs/'+'o'+'catalog', 'r') #File where you want to find invalid words
            text = file.readlines()
            for validWord in text:
                if re.sub('\n','',validWord) == line.lower():
                    found = True
                    break
            if found == False:
                invalid.append(line)
        elif line.lower().startswith('p'):
            file = open(relative+'catalogs/'+'p'+'catalog', 'r') #File where you want to find invalid words
            text = file.readlines()
            for validWord in text:
                if re.sub('\n','',validWord) == line.lower():
                    found = True
                    break
            if found == False:
                invalid.append(line)
        elif line.lower().startswith('q'):
            file = open(relative+'catalogs/'+'q'+'catalog', 'r') #File where you want to find invalid words
            text = file.readlines()
            for validWord in text:
                if re.sub('\n','',validWord) == line.lower():
                    found = True
                    break
            if found == False:
                invalid.append(line)
        elif line.lower().startswith('r'):
            file = open(relative+'catalogs/'+'r'+'catalog', 'r') #File where you want to find invalid words
            text = file.readlines()
            for validWord in text:
                if re.sub('\n','',validWord) == line.lower():
                    found = True
                    break
            if found == False:
                invalid.append(line)
        elif line.lower().startswith('s'):
            file = open(relative+'catalogs/'+'s'+'catalog', 'r') #File where you want to find invalid words
            text = file.readlines()
            for validWord in text:
                if re.sub('\n','',validWord) == line.lower():
                    found = True
                    break
            if found == False:
                invalid.append(line)
        elif line.lower().startswith('t'):
            file = open(relative+'catalogs/'+'t'+'catalog', 'r') #File where you want to find invalid words
            text = file.readlines()
            for validWord in text:
                if re.sub('\n','',validWord) == line.lower():
                    found = True
                    break
            if found == False:
                invalid.append(line)
        elif line.lower().startswith('u'):
            file = open(relative+'catalogs/'+'u'+'catalog', 'r') #File where you want to find invalid words
            text = file.readlines()
            for validWord in text:
                if re.sub('\n','',validWord) == line.lower():
                    found = True
                    break
            if found == False:
                invalid.append(line)
        elif line.lower().startswith('v'):
            file = open(relative+'catalogs/'+'v'+'catalog', 'r') #File where you want to find invalid words
            text = file.readlines()
            for validWord in text:
                if re.sub('\n','',validWord) == line.lower():
                    found = True
                    break
            if found == False:
                invalid.append(line)
        elif line.lower().startswith('w'):
            file = open(relative+'catalogs/'+'w'+'catalog', 'r') #File where you want to find invalid words
            text = file.readlines()
            for validWord in text:
                if re.sub('\n','',validWord) == line.lower():
                    found = True
                    break
            if found == False:
                invalid.append(line)
        elif line.lower().startswith('x'):
            file = open(relative+'catalogs/'+'x'+'catalog', 'r') #File where you want to find invalid words
            text = file.readlines()
            for validWord in text:
                if re.sub('\n','',validWord) == line.lower():
                    found = True
                    break
            if found == False:
                invalid.append(line)
        elif line.lower().startswith('y'):
            file = open(relative+'catalogs/'+'y'+'catalog', 'r') #File where you want to find invalid words
            text = file.readlines()
            for validWord in text:
                if re.sub('\n','',validWord) == line.lower():
                    found = True
                    break
            if found == False:
                invalid.append(line)
        elif line.lower().startswith('z'):
            file = open(relative+'catalogs/'+'z'+'catalog', 'r') #File where you want to find invalid words
            text = file.readlines()
            for validWord in text:
                if re.sub('\n','',validWord) == line.lower():
                    found = True
                    break
            if found == False:
                invalid.append(line)
        else:
            file = open(relative+'catalogs/'+'other'+'catalog', 'r') #File where you want to find invalid words
            text = file.readlines()
            for validWord in text:
                if re.sub('\n','',validWord) == line.lower():
                    found = True
                    break
            if found == False:
                invalid.append(line)

#eliminate duplicates
invalid = list(dict.fromkeys(invalid))
#write the invalid words into a file
tempFile=notValidFile
io.open(tempFile, 'w',encoding='utf-8').close()
for word in invalid:
    print(word)
    temp = io.open(tempFile, mode='a',encoding='utf-8')
    temp.write(word+'\n')
    temp.close()


print('Finished process at ',datetime.now())