import cv2
import os
os.chdir("Folder")
import random

def openFile(NameFile):
    F=open(NameFile, "r")
    L=F.readlines()
    return L  


DicoHumanChromSize = {"chr1" : 248956422, "chr2":242193529, "chr3":198295559, "chr4":190214555, "chr5":181538259, "chr6":170805979, "chr7": 159345973, "chr8":145138636, "chr9": 138394717, "chr10": 133797422, "chr11": 135086622, "chr12": 133275309, "chr13": 114364328, "chr14": 107043718, "chr15": 101991189, "chr16": 90338345, "chr17": 83257441, "chr18": 80373285, "chr19": 58617616, "chr20": 64444167, "chr21": 46709983, "chr22": 50818468, "chrX": 156040895, "chrY": 56887902}
print DicoHumanChromSize


def Sort(Liste):
        Final = []
        for i in Liste:
                if len(Final) == 0:
                        Final.append(i)
                else:
                        c = 0
                        Place = False
                        Begin = int(i[0])
                        for j in Final:
                                BeginJ = int(j[0])
                                if Begin<=BeginJ:
                                        Final.insert(c, i)
                                        Place = True
                                        break
                                c+=1
                        if Place == False:
                                Final.append(i)
        return Final




def GetNonCodingRegions(Liste, NameChrom, DicoChrom):
	ListeNonCoding = []
	print NameChrom
	if NameChrom in DicoChrom.keys():
		print NameChrom
		NewBorn = Liste[0][0]
		ListePetite = [str(1), str(NewBorn)]
		ListeNonCoding.append(ListePetite)
		c = 1
		for i in range(len(Liste)-1):
			if int(Liste[i+1][0])<=int(Liste[i][1]):
				continue
			else:
				BorneMoins = int(Liste[i][1])+1
				BornePlus = int(Liste[i+1][0])-1
				Lala = [str(BorneMoins), str(BornePlus)]
				ListeNonCoding.append(Lala)
		if NameChrom!="chrY":
			BorneMoins = int(Liste[len(Liste)-1][1])+1
			BornePlus = DicoChrom[NameChrom]
			Lala = [str(BorneMoins), str(BornePlus)]
			ListeNonCoding.append(Lala)
			print Lala
	return ListeNonCoding
		







def RemoveInside(Liste):
        c = 1
        #print Liste
        while c<len(Liste):
                if int(Liste[c][1])<=int(Liste[c-1][1]):
                        del Liste[c]
                else:
                        c+=1
        return Liste




def GetGenesPosition(File):
	Dico = {}
	for i in File:
		lolo = i.split()
		#print lolo[0]
		chrom = lolo[0].split("_")
		if len(chrom) == 1:
			BonChrom = chrom[0]
			PosInit = lolo[1]
			PosEnd = lolo[2]
			liste = [PosInit, PosEnd]
			if BonChrom not in Dico.keys():
				Dico[BonChrom] = []
				Dico[BonChrom].append(liste)
			else:
				Dico[BonChrom].append(liste)
	return Dico

def CreatDicoSorted(Dico, DicoHumanChromSize):
	NewDico = {}
	for i in Dico.keys():
		Liste = Dico[i]
		ListeSorted = Sort(Liste)
		print len(ListeSorted)
		ListeWithoutInside = RemoveInside(ListeSorted)
		#print ListeWithoutInside
		print len(ListeWithoutInside)
		ListeNonCoding = GetNonCodingRegions(ListeWithoutInside, i, DicoHumanChromSize)
		print len(ListeNonCoding)
		NewDico[i] = ListeNonCoding
	return NewDico


def PrintFile(Dico):
	F = open("NonCodingRegions", "w")
	for i in Dico.keys():
		for j in Dico[i]:
			F.write(i)
			for k in j:
				F.write(" "+k)
			F.write("\n")
	F.close()

Genes = openFile("GenesPositions")
Dico = GetGenesPosition(Genes)
DicoNc = CreatDicoSorted(Dico, DicoHumanChromSize)
PrintFile(DicoNc)

















