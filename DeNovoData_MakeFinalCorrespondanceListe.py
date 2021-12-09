import cv2
import os
os.chdir("Folder")
import random

def openFile(NameFile):
    F=open(NameFile, "r")
    L=F.readlines()
    return L  


def NameListe(File):
	Liste = []
	for i in File:
		if i[0] == ">":
			name = i[1:len(i)-1]
			Liste.append(name)
	return Liste



def CompareTwoFiles(Genes, F):
	Liste = []
	for i in Genes:
		for j in F:
			lala = j.split(",")
			Name = lala[0][1:len(lala[0])-1]
			if Name == i:
				Liste.append(lala)
				break
	return Liste


def PrintFinalFile(File):
	F = open("CorrectCorrespondance", "w")
	for i in File:
		F.write(i[0][1:len(i[0])-1])
		lolo = i[1:4]
		for j in lolo:
			F.write(","+j)
		F.write("\n")


FSequences = openFile("hsapiens.orfs.dna.fa")
ListeDeNovoSeqs = NameListe(FSequences)
print len(ListeDeNovoSeqs)
Fdata = openFile("orfs_coords_filtered.csv")
Lfinale = CompareTwoFiles(ListeDeNovoSeqs, Fdata)
print len(Lfinale)
#PrintFinalFile(Lfinale)


def MixWithThirdFile(Begin, Third):
	Liste = []
	for i in Begin:
		lala = i.split(",")
		Name = lala[0]
		for j in Third:
			lili = j.split(",")
			Name2 = lili[0][1:len(lili[0])-1]
			if Name2 == Name:
				lolo = i.split("\n")
				Deb = lolo[0]
				New = Deb+","+j
				Liste.append(New)
				break
	return Liste


def PrintLast(Liste):
	F=open("CorrespondanceFinal1", "w")
	for i in Liste:
		F.write(i)
	F.close()

Begin = openFile("CorrectCorrespondance")
Third = openFile("orf_age_annotation.csv")
LastListe = MixWithThirdFile(Begin, Third)
PrintLast(LastListe)
