import re
validFile ='english'
verifyFile = 'LOTR'
notValidFile = 'notValid'
pattern = r'[^A-Za-z0-9 -]+' #Pattern to look for special characters

file1 = open(verifyFile, 'r') #File where you want to find invalid words
text = file1.readlines()

file2 = open(validFile, 'r') #File with valid words
validLines = file2.readlines()

splitted = []
valid = []
notValid = []
count = 0



open(notValidFile, 'w').close()
for line in validLines:
    valid.append(line.replace('\n','').replace(' ',''))
for line in text: #Reads every line of the text file to check
    for sline in line.split():
        splitted.append(re.sub(pattern,'',sline)) #Removes any special characters


for line in splitted:
    found = False
    for vword in valid: #checks in the valid word list
        if vword.lower() == line.lower() or vword.lower()+'s' == line.lower() or vword.lower()+'-' == line.lower() or '-'+vword.lower() == line.lower():
            found = True
            break #stops looking when the word i s found
    if found == False:
        if line not in notValid and line != '-':
            count+=1 #Count when an invalid word is found
            print(line)
            notValid.append(line)
            f = open(notValidFile, "a")
            f.write(line+'\n')
            f.close()

print('Not valid count: ',count)