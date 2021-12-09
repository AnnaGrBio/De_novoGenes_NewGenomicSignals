import cv2
import os
os.chdir("Folder")
import random
from Bio import SeqIO

def openFile(NameFile):
    F=open(NameFile, "r")
    L=F.readlines()
    return L  




def StoreSeqName(File):
	D = {}
	for i in File:
		if i[0] == ">":
			ligne = i.split()
			#print ligne
			Data1 = int(ligne[1][1:])
			Data2 = int(ligne[3][0:len(ligne[3])-1])
			Name = ligne[0][1:]
			D[Name] = [Data1, Data2]
			#print Data1
			#print Data2
			#print Name
			#break
	return D



def GetDeNovoGenesName(File):
	L = []
	for i in File:
		ligne = i.split(",")
		#print ligne[0]
		L.append(ligne[0])
	return L


def MakeFinalFile1(Dico, Name):
	DicoBons = {}
	DicoReverse = {}
	ListeNot = []
	c = 0
	for i in Name:
		Present = False
		for j in Dico.keys():
			if j == i:
				Present = True
				Data1 = Dico[j][0]
				Data2 = Dico[j][1]
				Liste = [Data1, Data2]
				if Data1<Data2:
					DicoBons[i] = Liste
				else:
					DicoReverse[i] = Liste
				break
		if Present == False:
			ListeNot.append(i)
	F = open("ListeForward5PrimeSize", "w")
	for i in DicoBons.keys():
		F.write(str(i))
		for j in DicoBons[i]:
			F.write(" "+str(j))
		F.write("\n")
	F.close()
	F = open("ListeReverse5PrimeSize", "w")
	for i in DicoReverse.keys():
		F.write(str(i))
		for j in DicoReverse[i]:
			F.write(" "+str(j))
		F.write("\n")
	F.close()
	F = open("ListeNamesNotFound", "w")
	for i in ListeNot:
		F.write(i+"\n")
	F.close()

#D = GetSequencesLen("Hsapiens_merged.fa")

Corres2 = openFile("CorrespondanceFinal2")
L =GetDeNovoGenesName(Corres2)
Seqs = openFile("hsapiens_merged_orfs.fa")
D =StoreSeqName(Seqs)
print "lll"
MakeFinalFile1(D, L)
