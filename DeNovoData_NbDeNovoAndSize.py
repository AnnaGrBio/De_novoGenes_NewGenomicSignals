import cv2
import os
os.chdir("Folder")
import random
from Bio import SeqIO

def openFile(NameFile):
    F=open(NameFile, "r")
    L=F.readlines()
    return L  




def GetSequencesSize(File):
	Dico = {}
	it = SeqIO.parse(File, 'fasta')
	while True:
    		try:
        		seqRecord = next(it)
        		#print(seqRecord.id)
			#print(len(seqRecord.seq))
			Dico[seqRecord.id] = len(seqRecord.seq)
    		except StopIteration:
        		break
	return Dico


def SearcChromAndSize(File, Dico, LeName):
	DicoFinal = {"chr1" : [],"chr2" : [],"chr3" : [],"chr4" : [],"chr5" : [],"chr6" : [],"chr7" : [],"chr8" : [],"chr9" : [],"chr10" : [],"chr11" : [],"chr12" : [],"chr13" : [],"chr14" : [],"chr15" : [],"chr16" : [], "chr17" : [],"chr18" : [],"chr19" : [],"chr20" : [],"chr21" : [],"chr22" : [],"chrX" : [],"chrY" : []}
	NbNot = 0
	NbGood = 0
	NbNonGood = 0
	for i in Dico.keys():
		B = "N"
		for j in File:
			ligne = j.split(",")
			if ligne[0] == i:
				B = "O"
				Lala = ligne[1].split("_")
				if len(Lala) == 1:
					LeChrom = Lala[0][1:len(Lala[0])-1]
				else:
					LeChrom = Lala[0][1:]
				if LeChrom in DicoFinal.keys():
					DicoFinal[LeChrom].append(Dico[i])
					NbGood+=1
				else:
					print LeChrom
					NbNonGood +=1
				break
		if B == "N":
			NbNot +=1
	print NbNot
	print NbGood
	print NbNonGood
	F = open(LeName, "w")
	for i in DicoFinal.keys():
		F.write(str(i))
		for j in DicoFinal[i]:
			F.write(" "+str(j))
		F.write("\n")


File = openFile("CorrespondanceFinal2")
DeNovoGeneSeq = openFile("hsapiens.orfs.dna.fa")
D = GetSequencesSize("hsapiens.orfs.dna.fa")
SearcChromAndSize(File, D, "DeNovo_Size_Chrom")

File = openFile("SpecialCorres200")
D = GetSequencesSize("hsapiens.orfs.dna.fa")
SearcChromAndSize(File, D, "DeNovo_Special_Size_Chrom")

