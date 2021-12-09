import cv2
import os
os.chdir("Folder")
import random
from Bio import SeqIO


def GetSequences(File):
        Dico = {}
        it = SeqIO.parse(File, 'fasta')
        while True:
                try:
                        seqRecord = next(it)
                        #print(len(seqRecord.seq))
                        S = ""
                        for i in seqRecord.seq:
                                S +=i
                        #print S
			Nom = ""
			for i in seqRecord.id:
				Nom += i
                        Dico[Nom] = S
                except StopIteration:
                        break
        return Dico





def openFile(NameFile):
    F=open(NameFile, "r")
    L=F.readlines()
    return L 


def MakeDicoGood(Seqs, Genes, Name):
	DicoGenesFinal = {}
	DicoPseudo = {}
	DicoNcRNA = {}
	for i in Genes:
		ligne = i.split()
		Nom = ligne[3]
		Cat = ligne[4]
		for j in Seqs.keys():
			if j == Nom:
				if Cat == "gene":
					DicoGenesFinal[j] = Seqs[j]
				elif Cat == "ncRNA_gene":
					DicoNcRNA[j] = Seqs[j]
				else:
					DicoPseudo[j] = Seqs[j]
	print len(DicoGenesFinal)
	print len(DicoPseudo)
	print len(DicoNcRNA)
	F = open(Name, "w")
	for i in DicoGenesFinal.keys():
		F.write(">"+i+"\n")
		F.write(DicoGenesFinal[i]+"\n")
	F.close()



def MakeDicoNcRNA(Seqs, Genes, Name):
        DicoGenesFinal = {}
        DicoPseudo = {}
        DicoNcRNA = {} 
        for i in Genes:
                ligne = i.split()
		#print ligne
                Nom = ligne[3]
                Cat = ligne[4]
                for j in Seqs.keys():
                        if j == Nom:
                                if Cat == "gene":
                                        DicoGenesFinal[j] = Seqs[j]
                                elif Cat == "ncRNA_gene":
                                        DicoNcRNA[j] = Seqs[j]
                                else:
                                        DicoPseudo[j] = Seqs[j]
        print len(DicoGenesFinal)
        print len(DicoPseudo)
        print len(DicoNcRNA) 
        F = open(Name, "w")
        for i in DicoNcRNA.keys():
                F.write(">"+i+"\n")
                F.write(DicoNcRNA[i]+"\n")
        F.close()




Seqs = GetSequences("GenesLongestTranscripts")
GoodGenes = open("AllGenesPos")
MakeDicoGood(Seqs, GoodGenes, "GenesLongestTranscriptFinal")

Seqs = GetSequences("NcRNALongestTranscripts")
GoodGenes = open("AllGenesPos")
MakeDicoNcRNA(Seqs, GoodGenes, "NcRNALongestTranscriptFinal")
