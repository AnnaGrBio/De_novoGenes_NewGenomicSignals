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


def MakeListeAllMotifs(F1, F2):
	ListeTRfactor = []
	ListePoll2 = []
	for i in F1:
		ligne = i.split()
		if i[0] != ">":
			if ligne[0] not in ListeTRfactor:
				ListeTRfactor.append(ligne[0])
        for i in F2:
                ligne = i.split()
                if i[0] != ">":
                        if ligne[0] not in ListePoll2:
                                ListePoll2.append(ligne[0])
	return ListeTRfactor, ListePoll2


def MakeFinalFile(DeNovo1, DeNovo2, Gene1, Gene2, Pseudogene1, Pseudogene2, NcRNA1, NcRNA2, Intron1, Intron2, NonCoding1, NonCoding2):
	DicoFinalLtr = {}
	DicoFinalPoll2 = {}
	TailleDeNovo = 23126
	TailleGene = 21445
	TaillePseudogene = 15200
	TailleNcRNA = 23934
	TailleIntron = 23135
	TailleNonCoding = 23135
	for i in DeNovo1:
		if i[0] != ">":
			Name = i.split()
			Name = Name[0]
			if Name in DicoFinalLtr.keys():
				DicoFinalLtr[Name][0]+=1
			else:
				DicoFinalLtr[Name] = [1,0,0,0,0,0]

        for i in DeNovo2:
                if i[0] != ">":
                        Name = i.split()
                        Name = Name[0]
                        if Name in DicoFinalPoll2.keys():
                                DicoFinalPoll2[Name][0]+=1
                        else:
                                DicoFinalPoll2[Name] = [1,0,0,0,0,0]
	print "aaa"
        for i in Gene1:
                if i[0] != ">":
                        Name = i.split()
                        Name = Name[0]
                        if Name in DicoFinalLtr.keys():
                                DicoFinalLtr[Name][1]+=1
                        else:
                                DicoFinalLtr[Name] = [0,1,0,0,0,0]

        for i in Gene2:
                if i[0] != ">":
                        Name = i.split()
                        Name = Name[0]
                        if Name in DicoFinalPoll2.keys():
                                DicoFinalPoll2[Name][1]+=1
                        else:
                                DicoFinalPoll2[Name] = [0,1,0,0,0,0]
        print "aaa"
        for i in Pseudogene1:
                if i[0] != ">":
                        Name = i.split()
                        Name = Name[0]
                        if Name in DicoFinalLtr.keys():
                                DicoFinalLtr[Name][2]+=1
                        else:
                                DicoFinalLtr[Name] = [0,0,1,0,0,0]

        for i in Pseudogene2:
                if i[0] != ">":
                        Name = i.split()
                        Name = Name[0]
                        if Name in DicoFinalPoll2.keys():
                                DicoFinalPoll2[Name][2]+=1
                        else:
                                DicoFinalPoll2[Name] = [0,0,1,0,0,0]
        print "aaa"
        for i in NcRNA1:
                if i[0] != ">":
                        Name = i.split()
                        Name = Name[0]
                        if Name in DicoFinalLtr.keys():
                                DicoFinalLtr[Name][3]+=1
                        else:
                                DicoFinalLtr[Name] = [0,0,0,1,0,0]

        for i in NcRNA2:
                if i[0] != ">":
                        Name = i.split()
                        Name = Name[0]
                        if Name in DicoFinalPoll2.keys():
                                DicoFinalPoll2[Name][3]+=1
                        else:
                                DicoFinalPoll2[Name] = [0,0,0,1,0,0]
        print "aaa"
        for i in Intron1:
                if i[0] != ">":
                        Name = i.split()
                        Name = Name[0]
                        if Name in DicoFinalLtr.keys():
                                DicoFinalLtr[Name][4]+=1
                        else:
                                DicoFinalLtr[Name] = [0,0,0,0,1,0]

        for i in Intron2:
                if i[0] != ">":
                        Name = i.split()
                        Name = Name[0]
                        if Name in DicoFinalPoll2.keys():
                                DicoFinalPoll2[Name][4]+=1
                        else:
                                DicoFinalPoll2[Name] = [0,0,0,0,1,0]
        print "aaa"
        for i in NonCoding1:
                if i[0] != ">":
                        Name = i.split()
                        Name = Name[0]
                        if Name in DicoFinalLtr.keys():
                                DicoFinalLtr[Name][5]+=1
                        else:
                                DicoFinalLtr[Name] = [0,0,0,0,0,1]

        for i in NonCoding2:
                if i[0] != ">":
                        Name = i.split()
                        Name = Name[0]
                        if Name in DicoFinalPoll2.keys():
                                DicoFinalPoll2[Name][5]+=1
                        else:
                                DicoFinalPoll2[Name] = [0,0,0,0,0,1]
        print "aaa"

	for i in DicoFinalLtr.keys():
		Liste = DicoFinalLtr[i]
		Elt0 = float(Liste[0])/float(TailleDeNovo)
		Elt1 = float(Liste[1])/float(TailleGene)
                Elt2 = float(Liste[2])/float(TaillePseudogene)
                Elt3 = float(Liste[3])/float(TailleNcRNA)
                Elt4 = float(Liste[4])/float(TailleIntron)
                Elt5 = float(Liste[5])/float(TailleNonCoding)
		NewListe = [Elt0, Elt1, Elt2, Elt3, Elt4, Elt5]
		DicoFinalLtr[i] = NewListe
        for i in DicoFinalPoll2.keys():
                Liste = DicoFinalPoll2[i]
                Elt0 = float(Liste[0])/float(TailleDeNovo)
                Elt1 = float(Liste[1])/float(TailleGene)
                Elt2 = float(Liste[2])/float(TaillePseudogene)
                Elt3 = float(Liste[3])/float(TailleNcRNA)
                Elt4 = float(Liste[4])/float(TailleIntron)
                Elt5 = float(Liste[5])/float(TailleNonCoding)
                NewListe = [Elt0, Elt1, Elt2, Elt3, Elt4, Elt5]
                DicoFinalPoll2[i] = NewListe
	F = open("DataForMatrix", "w")
	F.write("MotifName"+","+"DeNovoGene"+","+"Gene"+","+"Pseudogene"+","+"NcRNA"+","+"Intron"+","+"NcRegion"+"\n")
	for i in DicoFinalLtr.keys():
		Liste = DicoFinalLtr[i]
		F.write(i)
		for j in Liste:
			F.write(","+str(j))
		F.write("\n")
        for i in DicoFinalPoll2.keys():
                Liste = DicoFinalPoll2[i]
                F.write(i)
                for j in Liste:
                        F.write(","+str(j))
                F.write("\n")
	F.close()





DeNovo1 = openFile("DeNovoMotifsSorted")
DeNovo2 = openFile("DeNovoPoll2Sorted")

Gene1 = openFile("GenesMotifsSorted")
Gene2 = openFile("GenePoll2Sorted")

Pseudogene1 = openFile("PseudogenesMotifsSorted")
Pseudogene2 = openFile("PseudogenesPoll2Sorted")

NcRNA1 = openFile("NcRNAMotifsSorted")
NcRNA2 = openFile("NcRNAPoll2Sorted")

Intron1 = openFile("IntronMotifsSorted")
Intron2 = openFile("IntronPoll2Sorted")

NonCoding1 = openFile("NonCodingMotifsSorted")
NonCoding2 = openFile("NonCodingPoll2Sorted")

#Ltr, Lpol2 = MakeListeAllMotifs(DeNovo1, DeNovo2)

MakeFinalFile(DeNovo1, DeNovo2, Gene1, Gene2, Pseudogene1, Pseudogene2, NcRNA1, NcRNA2, Intron1, Intron2, NonCoding1, NonCoding2)
