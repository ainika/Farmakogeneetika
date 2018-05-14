import csv

## Siin teeme sõnastiku, kus igale rskoodile vastab list, mille esimene element on normaalne alleel ja teine mutatsioon

mutat_ref = {}
with open('C:/Kasutaja/Bakatöö/CYP2C19/rs_norm_mut.csv') as csvfile:
    reader = csv.reader(csvfile)
    for r in reader:
        mutat_ref.setdefault(r[0].strip('\t'), []).append(r[1].strip('\t'))
        mutat_ref.setdefault(r[0].strip('\t'), []).append(r[2].strip('\t'))



## Võtame kõik Euroopas esinevad haplotüübid ja märgime nad vastava PharmGKB tähistusega.
# (Tärnalleelid,  töös tabelites 2 ja 3)

haplotüüp = {}
haplotüüp['rs4244285'] = '2'
haplotüüp['rs4986893'] = '3'
haplotüüp['rs12248560'] = '4'
haplotüüp['rs56337013'] = '5'
haplotüüp['rs72552267'] = '6'
haplotüüp['rs72558186'] = '7'
haplotüüp['rs41291556'] = '8'
haplotüüp['rs17884712'] = '9'
haplotüüp['rs6413438'] = '10'
haplotüüp['rs17879685'] = '13'
haplotüüp['rs55752064'] = '14'
haplotüüp['rs17882687'] = '15'
haplotüüp['rs12248560'] = '17'


##Nüüd loeme sisse GSA NÄITEandmed ja fitreerime välja meie jaoks olulised rskoodid

mutatsiooni_esinemine = {}
olemasolevad_rs = set()
kounter = 0
inimeste_mut = {}


with open('C:/Kasutaja/Bakatöö/Andmed/GSA_naidis.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        kounter += 1
        listike = str(row[0]).split(',')

        if listike[0] in mutat_ref.keys():
            ##hoiame järge, mis rskoodid meil andmetes olemas on
            olemasolevad_rs.add(listike[0])
            ##teeme sõnastiku, kus rskoodile vastavad konkreetse inimese tuvastatud alleelid
            mutatsiooni_esinemine.setdefault(listike[0], []).append(listike[4])
            mutatsiooni_esinemine.setdefault(listike[0], []).append(listike[5])
            ## sõnastik sõnastikus, kus peavõti on inimese kood, millele vastab eelnevalt tehtud rskoodi-alleeli sõnastik
            if listike[0] in mutatsiooni_esinemine.keys():
                inimeste_mut.setdefault(listike[3], {})[listike[0]] = [listike[4], listike[5]]
#print(inimeste_mut)


## Loeme kokku, missusgused kombiantsioonid üldse esindatud on, ehk millised diplotüübid ja haplotüübid üldse eksisteerivad
arvukus  = {}
suurlist = []
for i in inimeste_mut.keys():
    for j in inimeste_mut[i].keys():
        if inimeste_mut[i][j][0] == mutat_ref[j][1]:
            arvukus.setdefault(i,[]).append(j)
        if inimeste_mut[i][j][1] == mutat_ref[j][1]:
            arvukus.setdefault(i, []).append(j)

for i in arvukus.keys():
    listike2 = []
    for a in arvukus[i]:
        listike2.append(haplotüüp[a])
    suurlist.append(listike2)

print("----------- ")
print("Siin prinditakse esinevad diplotüübid ja haplotüübid:")
print(suurlist)
print("----------- ")


### Nüüd leiame igale diplotüübile või haplotüübile esinemisarvukuse (absoluutarvudes)

erinevus  = {}
l = 0
for s in suurlist:
    erinevus.setdefault(str(s), []).append(1)
    if len(s) == 2:
        l += 1

vastusega = {}
for e in erinevus.keys():
    vastusega[e] = len(erinevus[e])

print("Siin prinditakse esinevate diplotüüpide või haplotüüpide esinemisarvud:")
print(vastusega)
print("-------------")

loendur_mutatsioonita = 0
loendur_ühene = 0
for v in vastusega:
    loendur_mutatsioonita +=  int(vastusega[v])
    if len(v) > 6:
        loendur_ühene += 1


print("Inimeste arv kokku on " + str(len(inimeste_mut.keys())))
mutatsioonita_arv = len(inimeste_mut.keys()) - int(loendur_mutatsioonita)
print("Mutatsioonita oli neist " + str(mutatsioonita_arv))
print("Üheselt määrati diplotüüp " + str(loendur_ühene) + " inimesel")


