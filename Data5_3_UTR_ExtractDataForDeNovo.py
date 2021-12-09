import os
os.chdir("Folder")
import random

def openFile(NameFile):
    F=open(NameFile, "r")
    L=F.readlines()
    return L  


def MakeFinalFile(Data):
	ListeFinale = []
	for i in Data:
		ligne = i.split("\n")
		ligne = ligne[0].split(",")
		NameChrom = ligne[1][1:len(ligne[1])-1]
		NameGene = ligne[4][1:len(ligne[4])-1]
		BeginORF = ligne[2]
		EndORF = ligne[3]
		Direction = ligne[8]
		Size5prime = ligne[9]
		Size3prime = ligne[10]
		if Direction == "+":
			Begin5prime = int(BeginORF)-int(Size5prime)
			End5prime = int(BeginORF)-1
			Begin3prime = int(EndORF)+1
			End3prime = int(EndORF)+int(Size3prime)
			L = [NameChrom, NameGene, BeginORF, EndORF, Direction, Size5prime, str(Begin5prime), str(End5prime), Size3prime, str(Begin3prime), str(End3prime)]
			ListeFinale.append(L)
		elif Direction == "-":
                        Begin5prime = int(EndORF)+1
                        End5prime = int(EndORF)+int(Size5prime)
                        Begin3prime = int(BeginORF)-int(Size3prime)
                        End3prime = int(BeginORF)-1
                        L = [NameChrom, NameGene, BeginORF, EndORF, Direction, Size5prime, str(Begin5prime), str(End5prime), Size3prime, str(Begin3prime), str(End3prime)]
                        ListeFinale.append(L)
	F = open("DeNovo_5_3prime", "w")
	F.write("NameChrom"+","+"NameGene"+","+"PosBeginGene"+","+"PosEndGene"+","+"direction"+","+"Size5prime"+","+"Begin5prime"+","+"End5prime"+","+"Size3prime"+","+"Begin3prime"+","+"End3prime"+"\n")
	for i in ListeFinale:
		F.write(i[0])
		for j in i[1:]:
			F.write(","+j)
		F.write("\n")
	F.close()



FileCorres = openFile("CorrespondanceFinal3")
MakeFinalFile(FileCorres)
