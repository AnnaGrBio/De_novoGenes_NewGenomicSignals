import cv2
import os
from Bio.Seq import Seq
os.chdir("Folder")
import random

def openFile(NameFile):
    F=open(NameFile, "r")
    L=F.readlines()
    return L  






def BuildFile(F, NomFile):
	f = open(NomFile, "w")
	for i in F:
		ligne = i.split("\n")
		Liste = ligne[0].split(" ")
		f.write(">"+Liste[0]+"\n")
		f.write(Liste[5]+"\n")
	f.close()

def Traduire(File, FutureFile):
	from Bio.Seq import Seq
	f = open(FutureFile, "w")
	for i in File:
		if i[0] == ">":
			f.write(i)
		else:
			Liste = i.split("\n")
			Sequence = Liste[0]
			coding_dna = Seq(Sequence)
			Prot = coding_dna.translate()
			p = str(Prot)
			f.write(p+("\n"))
	f.close()





F = openFile("DeNovoGenes.fa")
Traduire(F, "DeNovoGenesProt.fa")


F2 = openFile("GenesLongestTranscriptFinal")
Traduire(F2, "HumanGenesProt.fa")

