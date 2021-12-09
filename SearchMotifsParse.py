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








def GetSequences(File):
        DicoSeq = {}
        it = SeqIO.parse(File, 'fasta', alphabet=IUPAC.unambiguous_dna)
        while True:
                try:
                        seqRecord = next(it)
                        #print(seqRecord.id)
                        #print(len(seqRecord.seq))
                        lala = seqRecord.seq
                        S = ""
                        for i in lala:
                                S+=i
                        #print SeqRecord(Seq("ACGT"))
                        DicoSeq[seqRecord.id] = lala
                except StopIteration:
                        break
        return DicoSeq


def ReadMotifFile(File, Dico):
	FinalDico = {}
	for Name in Dico.keys():
		Seq = Dico[Name]
		fh = open(File)
		FinalDico[Name] = []
		#print Name
		for m in motifs.parse(fh, "jaspar"):
			#print m.consensus
			m.pseudocounts = motifs.jaspar.calculate_pseudocounts(m)
			#print m.pseudocounts
			pssm = m.pssm
			#print pssm
			max_score = pssm.max
			#print max_score
			min_score = pssm.min
			#print min_score
			abs_score_threshold = (max_score - min_score) * 0.8 + min_score
			#print abs_score_threshold
			for position, score in pssm.search(Seq,threshold=abs_score_threshold):
				rel_score = (score - min_score) / (max_score - min_score)
				#print m.name
				#print position
				#print rel_score
				L = [m.name, position, rel_score]
				FinalDico[Name].append(L)
				#print(m.name+" "+"Position %d: score = %5.3f, rel. score = %5.3f" % (position, score, rel_score))
		#break
	return FinalDico







def MakeSeveral(Dico, Fmotifs):
	ListeD = []
	LFinale = []
	NbSeqs = len(Dico)
	NbSeqBySubDico = int(NbSeqs/60)
	#print NbSeqBySubDico
	c = 1
	NbDic = 1
	d = {}
	for Seqs in Dico.keys():
		d[Seqs] = Dico[Seqs]
		if c == NbSeqBySubDico:
			ListeD.append(d)
			NbDic+=1
			c = 0
			d = {}
		c+=1
	if len(d)!=0:
		ListeD.append(d)
	for i in ListeD:
		Tup = (Fmotifs, i)
		LFinale.append(Tup)
	#print len(LFinale)
	return LFinale


#	L.append((File, D1), 60....)
# 20 Dico D1 - D20	return the L	


def wrapper(x):
	File, Dico = x
	D = ReadMotifFile(File, Dico)
	return D


def Multiproc(L):
	Taille = len(L)
	p = Pool(Taille)
	Results = p.map(wrapper, L)
	p.close()
	p.join()
	print len(Results)
	DFinal = {}
	for i in Results:
		for j in i:
			DFinal[j] =i[j]
	return DFinal
	#join the 60 dic from the Results list


def MakeFinalFile(Name, FinalDico):
	NewFile = open(Name, "w")
        for Name in FinalDico.keys():
                NewFile.write(">"+Name+"\n")
                for Data in FinalDico[Name]:
                        for i in Data:
                                NewFile.write(str(i)+" ")
                        NewFile.write("\n")
        NewFile.close()



DicoSeqs = GetSequences("Pseudogenes200Before")
ListeToParse = MakeSeveral(DicoSeqs, "PhylofactJaspar.txt")
TotalDic = Multiproc(ListeToParse)
MakeFinalFile("PseudogenePhylofactMotifs", TotalDic)

#ReadMotifFile("JASPAR2020_CORE_vertebrates_non-redundant_pfms_jaspar.txt", DicoSeqs)
