import cv2
import os
os.chdir("Folder")
import random
from Bio import SeqIO
from Bio import motifs
from Bio.Alphabet import IUPAC
from Bio.Seq import Seq
import random
from multiprocessing import Pool
#from random import *


def openFile(NameFile):
    F=open(NameFile, "r")
    L=F.readlines()
    return L  

def GetSize(F1, F2, F3, F4):
	D5 = {}
	D3 = {}
	for i in F1:
		ligne = i.split("\n")
		ligne = ligne[0]
		if len(ligne)>0 and ligne[0] == ">":
			Name = ligne[1:]
		else:
			taille = len(ligne)-1
			if taille == 0:
				print ligne
			D5[Name] = taille
        for i in F2:
                ligne = i.split("\n")
                ligne = ligne[0]
                if len(ligne)>0 and ligne[0] == ">":
                        Name = ligne[1:]
                else:
                        taille = len(ligne)-1
                        D3[Name] = taille
        for i in F3:
                ligne = i.split("\n")
                ligne = ligne[0]
                if len(ligne)>0 and ligne[0] == ">":
                        Name = ligne[1:]
                else:
                        taille = len(ligne)-1
                        D5[Name] = taille
        for i in F4:
                ligne = i.split("\n")
                ligne = ligne[0]
                if len(ligne)>0 and ligne[0] == ">":
                        Name = ligne[1:]
                else:
                        taille = len(ligne)-1
                        D3[Name] = taille
	print D5["MSTRG.6616.9_4_+"]
	print D3["ENSG00000183520_+"]
	return D5, D3




def MakeFile(Denovo5, Denovo3, Gene5, Gene3, DicoTaille5, DicoTaille3):
	NbMotifs = 0
	debut = -1
	F = open("DataForAveragePhylofact", "w")
	F.write("Name"+","+"UTRregion"+","+"Category"+","+"SIzeUTR"+","+"NbTotalMotifs"+","+"NbTotalMotifsDivSize"+"\n")
	for elt in Denovo5:
		if elt[0] == ">":
			debut +=1
                        if debut >0:
				if Taille == "NA" or Taille == 0:
					Div = "NA"
				else:
					Div = float(NbMotifs)/float(Taille)
                                F.write(Gene+","+"5UTR"+","+"DeNovoGene"+","+str(Taille)+","+str(NbMotifs)+","+str(Div)+"\n")
                                NbMotifs = 0

			ligne = elt.split("\n")
			Gene = ligne[0][1:]
			if Gene in DicoTaille5.keys():
				Taille = DicoTaille5[Gene]
			else:
				Taille = "NA"
			
		else:
			NbMotifs +=1
	F.write(Gene+","+"5UTR"+","+"DeNovoGene"+","+str(Taille)+","+str(NbMotifs)+","+str(Div)+"\n")
        NbMotifs = 0
        debut = -1
        for elt in Denovo3:
                if elt[0] == ">":
                        debut +=1
                        if debut >0:
                                if Taille == "NA" or Taille == 0:
                                        Div = "NA"
                                else:
                                        Div = float(NbMotifs)/float(Taille)

                                F.write(Gene+","+"3UTR"+","+"DeNovoGene"+","+str(Taille)+","+str(NbMotifs)+","+str(Div)+"\n")
                                NbMotifs = 0

                        ligne = elt.split("\n")
                        Gene = ligne[0][1:]
                        if Gene in DicoTaille3.keys():
                                Taille = DicoTaille3[Gene]
                        else:
                                Taille = "NA"
                        
                else:
                        NbMotifs +=1
        F.write(Gene+","+"3UTR"+","+"DeNovoGene"+","+str(Taille)+","+str(NbMotifs)+","+str(Div)+"\n")
        NbMotifs = 0
        debut = -1
        for elt in Gene5:
                if elt[0] == ">":
                        debut +=1
                        if debut >0:
                                if Taille == "NA" or Taille == 0:
                                        Div = "NA"
                                else:
                                        Div = float(NbMotifs)/float(Taille)

                                F.write(Gene+","+"5UTR"+","+"Gene"+","+str(Taille)+","+str(NbMotifs)+","+str(Div)+"\n")
                                NbMotifs = 0

                        ligne = elt.split("\n")
                        Gene = ligne[0][1:]
                        if Gene in DicoTaille5.keys():
                                Taille = DicoTaille5[Gene]
                        else:
                                Taille = "NA"
                        
                else:
                        NbMotifs +=1
        F.write(Gene+","+"5UTR"+","+"Gene"+","+str(Taille)+","+str(NbMotifs)+","+str(Div)+"\n")
        NbMotifs = 0
        debut = -1
        for elt in Gene3:
                if elt[0] == ">":
                        debut +=1
                        if debut >0:
                                if Taille == "NA" or Taille == 0:
                                        Div = "NA"
                                else:
                                        Div = float(NbMotifs)/float(Taille)

                                F.write(Gene+","+"3UTR"+","+"Gene"+","+str(Taille)+","+str(NbMotifs)+","+str(Div)+"\n")
                                NbMotifs = 0

                        ligne = elt.split("\n")
                        Gene = ligne[0][1:]
                        if Gene in DicoTaille3.keys():
                                Taille = DicoTaille3[Gene]
                        else:
                                Taille = "NA"
                        
                else:
                        NbMotifs +=1
        F.write(Gene+","+"3UTR"+","+"Gene"+","+str(Taille)+","+str(NbMotifs)+","+str(Div)+"\n")
	F.close()





Denovo5 = openFile("DeNovo5PhylofactSorted")
Denovo3 = openFile("DeNovo3PhylofactSorted")
Gene5 = openFile("Gene5PhylofactSorted")
Gene3 = openFile("Gene3PhylofactSorted")

TailleDeNovo5 = openFile("Region5primeDeNovoGenes")
TailleDeNovo3 = openFile("Region3primeDeNovoGenes")
TailleGene5 = openFile("Region5primeGenesOneByGene.fa")
TailleGene3 = openFile("Region3primeGenesOneByGene.fa")



D5, D3 = GetSize(TailleDeNovo5, TailleDeNovo3, TailleGene5, TailleGene3)

MakeFile(Denovo5, Denovo3, Gene5, Gene3, D5, D3)
