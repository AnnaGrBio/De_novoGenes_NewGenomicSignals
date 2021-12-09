import cv2
import os
os.chdir("Folder")
import random
from Bio import SeqIO

def openFile(NameFile):
    F=open(NameFile, "r")
    L=F.readlines()
    return L  




def GetSequencesLen(File):
	Dico = {}
	it = SeqIO.parse(File, 'fasta')
	while True:
    		try:
        		seqRecord = next(it)
			Sequence = seqRecord.seq
			Taille = len(Sequence)
			Dico[seqRecord.id] = Taille
    		except StopIteration:
        		break
	F = open("FileContigsSize", "w")
	for i in Dico.keys():
		F.write(str(i)+"_"+str(Dico[i])+"\n")
	F.close()





D = GetSequencesLen("Hsapiens_merged.fa")

