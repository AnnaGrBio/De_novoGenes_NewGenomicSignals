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


def MakeList(File, seuil):
	Liste = []
	LPM = ["+", "-"]
	for i in File:
		if i[0] == ">":
			Sens = random.choice(LPM)
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


NonCoding = openFile("NonCodingRegionMotifsPoll2")
LNonCoding = MakeList(NonCoding, 0.8)
MakeFinalFile(LNonCoding, "NonCodingPoll2Sorted")

Intron = openFile("IntronMotifsPoll2")
LIntron = MakeList(Intron, 0.8)
MakeFinalFile(LIntron, "IntronPoll2Sorted")
