import os
import ast
from datetime import datetime

MyClippingPath = ''
DestinationPath = ''
toIgnore=[]

def getDate(intestazione):
    dizMonths= {
        'gennaio': '01',
        'febbraio': '02',
        'marzo': '03',
        'aprile': '04',
        'maggio': '05',
        'giugno': '06',
        'luglio': '07',
        'agosto': '08',
        'settembre': '09',
        'ottobre': '10',
        'novembre': '11',
        'dicembre': '12'}
    dati = intestazione.split(' ')
    dati[-3] = dizMonths[dati[-3]]
    dati[-1] = dati[-1].replace(':','')
    date = ''.join(dati[-4:])
    if len(date) == 13:
        date = '0'+date
    return  date


def recente(data1, data2):
    formato_data = "%d%m%Y%H%M%S"
    data1_dt = datetime.strptime(data1, formato_data)
    data2_dt = datetime.strptime(data2, formato_data)
    return data1_dt > data2_dt



supportFilePath=DestinationPath+"/.supportFile.txt"

file0=open(MyClippingPath,'r').read()
v=chr(65279)
file=''.join(filter(lambda x: x!=v , file0))
del file0

appunti = file.split('==========\n')
INIZIALIZZA = False
lastNote = {}
try:
    supporto = open(supportFilePath,'r').read()
    for r in supporto.split('\n'):
        if ':' in r:
            titolo,data = r.rsplit(':',1)
            lastNote[titolo]=data
except FileNotFoundError:
    INIZIALIZZA = True

countDuplicate=0
updateNotes=[]
numeroAppunti = len(appunti) - 1 

for i,f  in enumerate(appunti[:-1]):
    intestazione,dati,ignore,contenuto=f.split('\n',3)
    if i+1!=numeroAppunti:
        t_,d_,i_,contenutoNext = appunti[i+1].split('\n',3)
        if contenuto[:-1] in appunti[i+1] or contenutoNext[:-1] in f:
            countDuplicate+=1
            continue
    try:
        title,autore=intestazione.rsplit('(', 1)
    except:
        errorText=f'''Error:
        heading doesn't match  _Title (Authors)_:
        {intestazione}'''
        print(errorText)
        continue

    autore=autore[:-1].strip()
    title=title.split('(',1)[0].strip()



    fileName=f'{title}_kindle.md'
    dateNote = getDate(dati.split(' | ')[-1])

    if title in toIgnore:
        continue

    elif os.path.exists(DestinationPath+'/'+fileName):

        if INIZIALIZZA or recente(dateNote,lastNote[title]):
            if title not in updateNotes:
                updateNotes.append(title)
            lastNote[title]=dateNote
            file = open(DestinationPath+'/'+fileName,'a')
            file.write(f'{dati}\n\n{contenuto}***\n')
            file.close()
    else:
        lastNote[title] = dateNote
        print('new: '+str(title))
        file=open(DestinationPath+'/'+fileName,'w')
        file.write(f'Libro: {title}  \nAutore: {autore}\n\n\n')
        file.close()

print()
print(f'{updateNotes} notes update')
for a in updateNotes:
    print('    '+str(a))
    
print()
print(f'{countDuplicate} notes skipped because classified as duplicates')  

filelastNote = open(supportFilePath,'w')
for t in lastNote:
  filelastNote.write(f'{t}:{lastNote[t]}\n')
filelastNote.close()


