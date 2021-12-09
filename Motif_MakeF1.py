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


def MakeDicoAllMotifs(File):
	Dico = {}
	NbMotifs = 0
	for elt in File:
		if elt[0] == ">":
			if NbMotifs in Dico.keys():
				Dico[NbMotifs]+=1
			else:
				Dico[NbMotifs]=1
			NbMotifs = 0
		else:
			NbMotifs +=1
	return Dico



def MakeFinalFile(Ddenovo, Dgene, Dncrna, Dpseudogene, Dnoncoding, Dintron):
	F =open("DataNbGenesVsNbMotifs", "w")
	F.write("Category"+","+"NbGeneWithXmotifs"+","+"NbMotifs"+"\n")
	for i in Ddenovo.keys():
		#print i
		F.write("DeNovoGene"+","+str(Ddenovo[i])+","+str(i)+"\n")
	for i in Dgene.keys():
		F.write("Gene"+","+str(Dgene[i])+","+str(i)+"\n")
	for i in Dncrna.keys():
		F.write("NonCodingRNA"+","+str(Dncrna[i])+","+str(i)+"\n")
	for i in Dpseudogene.keys():
		F.write("Pseudogene"+","+str(Dpseudogene[i])+","+str(i)+"\n")
	for i in Dnoncoding.keys():
		F.write("NonCodingRegion"+","+str(Dnoncoding[i])+","+str(i)+"\n")
	for i in Dintron.keys():
		F.write("IntronicRegion"+","+str(Dintron[i])+","+str(i)+"\n")
	F.close()


Denovo = openFile("DeNovoGenesMotifsBeforeSorted")
Gene = openFile("GenesMotifsBeforeSorted")
Ncrna = openFile("NcRNAMotifsBeforeSorted")
Pseudogene = openFile("PseudogenesMotifsBeforeSorted")
Noncoding = openFile("RandomNonCodingMotifsSorted")
Intron = openFile("RandomIntronMotifsSorted")

Ddenovo = MakeDicoAllMotifs(Denovo)
#print Ddenovo
Dgene = MakeDicoAllMotifs(Gene)
Dncrna = MakeDicoAllMotifs(Ncrna)
Dpseudogene = MakeDicoAllMotifs(Pseudogene)
Dnoncoding = MakeDicoAllMotifs(Noncoding)
Dintron = MakeDicoAllMotifs(Intron)

MakeFinalFile(Ddenovo, Dgene, Dncrna, Dpseudogene, Dnoncoding, Dintron)
