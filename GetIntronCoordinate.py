import os
os.chdir("Folder")
import random

def openFile(NameFile):
    F=open(NameFile, "r")
    L=F.readlines()
    return L  


def GetDeNovoTranscritpsNames(F):
	Dico = {}
	for i in F:
		ligne = i.split(" ")
		Name =ligne[0]
		Name = Name.split("_")
		Name = Name[0]
		Lolo = i.split(",")
		Chrom = Lolo[1][1:len(Lolo[1])-1]
		Dico[Name]=Chrom
	return Dico

def GetIntrons(GTF, DicoName):
	Dico = {}
	c = 0
	for i in GTF:
		if i[0] != "#":
			ligne = i.split()
			if ligne[2] == "transcript":
				Name = ligne[11][1:len(ligne[11])-2]
				if Name in DicoName.keys():
					Chrom = DicoName[Name]
					Compteur = c+1
					while True:
						ligne2 = GTF[Compteur].split()
						if ligne2[2] == "exon":
							Begin = ligne2[3]
							End = ligne2[4]
							if Name in Dico.keys():
								Dico[Name].append((Begin, End, Chrom))
							else:
								Dico[Name] = [(Begin, End, Chrom)]
						else:
							break
						Compteur += 1
		c+=1
	print len(Dico)
	return Dico

def MakeFinalFiles(Dico):
    F2 = open("CoordDeNovoIntron", "w")
    F2.write("TranscriptName"+","+"Chrom"+","+"IntronBegin"+","+"IntronEnd"+"\n")
    for i in Dico.keys():
        TranscriptName = i
        NbIntrons = len(Dico[i])-1
        if NbIntrons>0:
            for j in range(len(Dico[i])-1):
                Suivant = Dico[i][j+1]
                Avant = Dico[i][j]
		BegIntron = int(Avant[1])+1
		EndIntron = int(Suivant[0])-1
		Chrom = Dico[i][j][2]
                F2.write(TranscriptName+","+Chrom+","+str(BegIntron)+","+str(EndIntron)+"\n")
    F2.close()

               
                
        

Corres3 = openFile("CorrespondanceFinal3")
DicoNameDeNovo = GetDeNovoTranscritpsNames(Corres3)
GTF = openFile("Hsapiens.merged.gtf")

Dico = GetIntrons(GTF, DicoNameDeNovo)
MakeFinalFiles(Dico)







