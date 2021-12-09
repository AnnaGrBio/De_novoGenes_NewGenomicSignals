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

def RetrieveSens(S):
	ListElts = S.split(",")
	return ListElts[8]



def MakeList(File, seuil):
	Liste = []
	for i in File:
		if i[0] == ">":
			Sens = RetrieveSens(i)
			Liste.append(i)
		else:
			ListElmts = i.split("\n")
			CorrectListElmts = ListElmts[0].split(" ")
			Pos = int(CorrectListElmts[1])
			Value = float(CorrectListElmts[2])
			if Value>=seuil:
				if Sens == "+" and Pos>0:
					Liste.append(i)
				if Sens =="-" and Pos<0:
					Liste.append(i)
	return Liste

def MakeFinalFile(Liste, Name):
	F = open(Name, "w")
	for i in Liste:
		F.write(i)
	F.close()


DeNovo = openFile("DeNovoCoreMotifsPoll2")
LDeNovo = MakeList(DeNovo, 0.8)
MakeFinalFile(LDeNovo, "DeNovoCoreMotifsPoll2Sorted")
