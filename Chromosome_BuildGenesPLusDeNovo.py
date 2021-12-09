import cv2
import os
os.chdir("Folder")
import random

def openFile(NameFile):
    F=open(NameFile, "r")
    L=F.readlines()
    return L 



def MakeFinalOne(Fgene, FDenovo):
	F = open("AllGenesPosANDdeNovo", "w")
	for i in Fgene:
		F.write(i)
	for i in FDenovo:
		ligne = i.split("\n")
		Liste = ligne[0].split(",")
		Chrom = Liste[1][1:len(Liste[1])-1]
		PosBeg = Liste[2]
		PosEnd = Liste[3]
		Name = Liste[0]
		Categorie = "DeNovo"
		Sens = Liste[8]
		Phrase = Chrom+" "+PosBeg+" "+PosEnd+" "+Name+" "+Categorie+" "+Sens+" "+"\n"
		F.write(Phrase)
	F.close()
	
FileGenes = openFile("AllGenesPos")
FileDeNovo = openFile("CorrespondanceFinal2")
MakeFinalOne(FileGenes, FileDeNovo)















