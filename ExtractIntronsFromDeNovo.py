import os
os.chdir("Folder")
import random

def openFile(NameFile):
    F=open(NameFile, "r")
    L=F.readlines()
    return L  


def GetDeNovoTranscritpsNames(F):
	Liste = []
	for i in F:
		ligne = i.split(" ")
		Name =ligne[0]
		Name = Name.split("_")
		Name = Name[0]
		Liste.append(Name)
	return Liste

def GetIntrons(GTF, Liste):
	Dico = {}
	c = 0
	for i in GTF:
		if i[0] != "#":
			ligne = i.split()
			if ligne[2] == "transcript":
				Name = ligne[11][1:len(ligne[11])-2]
				if Name in Liste:
					Compteur = c+1
					while True:
						ligne2 = GTF[Compteur].split()
						if ligne2[2] == "exon":
							Begin = ligne2[3]
							End = ligne2[4]
							if Name in Dico.keys():
								Dico[Name].append((Begin, End))
							else:
								Dico[Name] = [(Begin, End)]
						else:
							break
						Compteur += 1
		c+=1
	print len(Dico)
	return Dico

def MakeFinalFiles(Dico):
    F1 = open("NbIntronsByExonsDeNovo", "w")
    F1.write("TranscriptName"+","+"NbIntrons"+"\n")
    F2 = open("IntronsSizeDeNovo", "w")
    F2.write("TranscriptName"+","+"IntronSize"+"\n")
    for i in Dico.keys():
        TranscriptName = i
        NbIntrons = len(Dico[i])-1
        F1.write(TranscriptName+","+str(NbIntrons)+"\n")
        #print TranscriptName
        #print Dico[i]
        if NbIntrons>0:
            for j in range(len(Dico[i])-1):
                Suivant = Dico[i][j+1]
                Avant = Dico[i][j]
                SizeIntron = int(Suivant[0])-int(Avant[1])-2
                F2.write(TranscriptName+","+str(SizeIntron)+"\n")
        

               
                
        

Corres3 = openFile("CorrespondanceFinal3")
NameDeNovo = GetDeNovoTranscritpsNames(Corres3)
GTF = openFile("Hsapiens.merged.gtf")

Dico = GetIntrons(GTF, NameDeNovo)
MakeFinalFiles(Dico)







