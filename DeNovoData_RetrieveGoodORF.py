import cv2
import os
os.chdir("Folder")
import random
from Bio import SeqIO

def openFile(NameFile):
    F=open(NameFile, "r")
    L=F.readlines()
    return L  




def GetSequences(File):
	Dico = {}
	it = SeqIO.parse(File, 'fasta')
	while True:
    		try:
        		seqRecord = next(it)
			Sequence = seqRecord.seq
			S = ""
			for i in Sequence:
				S += i
			Dico[seqRecord.id] = S
    		except StopIteration:
        		break
	return Dico


def MakeFile(File, Dico):
	ListeChrom = ["chr1", "chr2", "chr3", "chr4", "chr5", "chr6", "chr7", "chr8", "chr9", "chr10", "chr11", "chr12","chr13", "chr14", "chr15", "chr16", "chr17", "chr18", "chr19", "chr20", "chr21", "chr22", "chrX", "chrY"]
	DicoFinal = {}
	NbGood = 0
	for i in Dico.keys():
		for j in File:
			ligne = j.split(",")
                        if ligne[0] == i:
                                Lala = ligne[1].split("_")
                                if len(Lala) == 1:
                                        LeChrom = Lala[0][1:len(Lala[0])-1]
                                else:
                                        LeChrom = Lala[0][1:]
                                if LeChrom in ListeChrom:
                                        DicoFinal[i] = Dico[i]
					NbGood +=1
                                break
	print NbGood
	F = open("DeNovoNucFinal.fa", "w")
	for i in DicoFinal.keys():
		F.write(">"+i+"\n")
		F.write(DicoFinal[i]+"\n")
	F.close()


File = openFile("CorrespondanceFinal2")
DeNovoGeneSeq = openFile("hsapiens.orfs.dna.fa")
D = GetSequences("hsapiens.orfs.dna.fa")
MakeFile(File, D)

