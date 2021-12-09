import cv2
import os
os.chdir("Folder")
import random
from Bio import SeqIO

def openFile(NameFile):
    F=open(NameFile, "r")
    L=F.readlines()
    return L  



def RetrieveSizes(F):
	D = {}
	for i in F:
		ligne = i.split("\n")
		Data = ligne[0].split(" ")
		L = [Data[1], Data[2]]
		D[Data[0]] = L
	return D

def MakeFile(Corres, Dico):
	ListeLignes = []
	for i in Corres:
		ligne = i.split("\n")
		Data = ligne[0].split(",")
		Name = Data[0]
		Present = False
		for j in Dico.keys():
			if j == Name:
				R5 = Dico[j][0]
				R3=Dico[j][1]
				Data.append(R5)
				Data.append(R3)
				ListeLignes.append(Data)
				Present = True
				break
		if Present == False:
			print "shit"
	F = open("CorrespondanceFinal3", "w")
	for i in ListeLignes:
		F.write(i[0])
		for elt in i[1:]:
			F.write(","+elt)
		F.write("\n")
	F.close()






Corres2 = openFile("CorrespondanceFinal2")
Sizes = openFile("ORF_5_3_prime_size")
DicoSizes = RetrieveSizes(Sizes)
MakeFile(Corres2, DicoSizes)

