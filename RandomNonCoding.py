import cv2
import os
os.chdir("Folder")
import random
from Bio import SeqIO
import random
#from random import *


def openFile(NameFile):
    F=open(NameFile, "r")
    L=F.readlines()
    return L  




def GetSequences(File):
	Liste = []
	it = SeqIO.parse(File, 'fasta')
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
			Liste.append(S)
    		except StopIteration:
        		break
	return Liste



def RetrieveNbPositions(File):
	D = {}
	for i in File:
		ligne = i.split("\n")
		All = ligne[0].split()
		#print len(All)
		D[All[0]] = []
		for i in All[1:]:
			D[All[0]].append(int(i))
		#print len(D[All[0]])
	return D

def Choisir(Seq, Size):
	Debut = random.randint(0, len(Seq)-Size)
	Fin = Debut+Size
	SeqFinal = Seq[Debut:Fin]
	#print Debut
	#print Fin
	#print len(Seq)
	#print len(SeqFinal)
	return SeqFinal



def MakeRandom(ListeSeq, ListeTaille):
	Nb = len(ListeTaille)
	print Nb
	Compteur = 0
	ListeSequences = []
	while Nb>0:
		Taille = ListeTaille[Compteur]
		#print Taille
		C = True
		while C == True:
			LongueSeq = random.choice(ListeSeq)
			#print len(LongueSeq)
			if len(LongueSeq)>Taille and "N" not in LongueSeq:
				C = False
		PetiteSeq = Choisir(LongueSeq, Taille)
		ListeSequences.append(PetiteSeq)
		Compteur +=1
		Nb-=1
	print len(ListeSequences)
	return ListeSequences



def MakeFile(DicoChrom, ListeC1, ListeC2, ListeC3, ListeC4, ListeC5, ListeC6, ListeC7, ListeC8, ListeC9, ListeC10, ListeC11, ListeC12, ListeC13, ListeC14, ListeC15, ListeC16, ListeC17, ListeC18, ListeC19, ListeC20, ListeC21, ListeC22, ListeCX, ListeCY):
	DicoFinal = {}
	F = open("NonCodingRandom.fa", "w")
	for i in DicoChrom.keys():
		if i == "chr1":
			ListeTaille = DicoChrom[i]
			SeqsC1 = MakeRandom(ListeC1, ListeTaille)
			c = 0
			for j in SeqsC1:
				#print i
				F.write(">chr1_"+str(c)+"\n")
				F.write(j+"\n")
				c+=1
		elif i == "chr2":
                        ListeTaille = DicoChrom[i]
                        SeqsC2 = MakeRandom(ListeC2, ListeTaille)
                        c = 0
                        for j in SeqsC2:
                                #print i
                                F.write(">chr2_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1
		elif i == "chr3":
                        ListeTaille = DicoChrom[i]
                        SeqsC3 = MakeRandom(ListeC3, ListeTaille)
                        c = 0
                        for j in SeqsC3:
                                #print i
                                F.write(">chr3_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1
		elif i == "chr4":
                        ListeTaille = DicoChrom[i]
                        SeqsC4 = MakeRandom(ListeC4, ListeTaille)
                        c = 0
                        for j in SeqsC4:
                                #print i
                                F.write(">chr4_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1
		elif i == "chr5":
                        ListeTaille = DicoChrom[i]
                        SeqsC5 = MakeRandom(ListeC5, ListeTaille)
                        c = 0
                        for j in SeqsC5:
                                #print i
                                F.write(">chr5_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1				
		elif i == "chr6":
                        ListeTaille = DicoChrom[i]
                        SeqsC6 = MakeRandom(ListeC6, ListeTaille)
                        c = 0
                        for j in SeqsC6:
                                #print i
                                F.write(">chr6_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1				
		elif i == "chr7":
                        ListeTaille = DicoChrom[i]
                        SeqsC7 = MakeRandom(ListeC7, ListeTaille)
                        c = 0
                        for j in SeqsC7:
                                #print i
                                F.write(">chr7_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1				
		elif i == "chr8":
                        ListeTaille = DicoChrom[i]
                        SeqsC8 = MakeRandom(ListeC8, ListeTaille)
                        c = 0
                        for j in SeqsC8:
                                #print i
                                F.write(">chr8_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1				
		elif i == "chr9":
                        ListeTaille = DicoChrom[i]
                        SeqsC9 = MakeRandom(ListeC9, ListeTaille)
                        c = 0
                        for j in SeqsC9:
                                #print i
                                F.write(">chr9_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1				
		elif i == "chr10":
                        ListeTaille = DicoChrom[i]
                        SeqsC10 = MakeRandom(ListeC10, ListeTaille)
                        c = 0
                        for j in SeqsC10:
                                #print i
                                F.write(">chr10_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1				
		elif i == "chr11":
                        ListeTaille = DicoChrom[i]
                        SeqsC11 = MakeRandom(ListeC11, ListeTaille)
                        c = 0
                        for j in SeqsC11:
                                #print i
                                F.write(">chr11_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1				
		elif i == "chr12":
                        ListeTaille = DicoChrom[i]
                        SeqsC12 = MakeRandom(ListeC12, ListeTaille)
                        c = 0
                        for j in SeqsC12:
                                #print i
                                F.write(">chr12_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1				
		elif i == "chr13":
                        ListeTaille = DicoChrom[i]
                        SeqsC13 = MakeRandom(ListeC13, ListeTaille)
                        c = 0
                        for j in SeqsC13:
                                #print i
                                F.write(">chr13_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1				
		elif i == "chr14":
                        ListeTaille = DicoChrom[i]
                        SeqsC14 = MakeRandom(ListeC14, ListeTaille)
                        c = 0
                        for j in SeqsC14:
                                #print i
                                F.write(">chr14_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1				
		elif i == "chr15":
                        ListeTaille = DicoChrom[i]
                        SeqsC15 = MakeRandom(ListeC15, ListeTaille)
                        c = 0
                        for j in SeqsC15:
                                #print i
                                F.write(">chr15_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1
		elif i == "chr16":
                        ListeTaille = DicoChrom[i]
                        SeqsC16 = MakeRandom(ListeC16, ListeTaille)
                        c = 0
                        for j in SeqsC16:
                                #print i
                                F.write(">chr16_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1
		elif i == "chr17":
                        ListeTaille = DicoChrom[i]
                        SeqsC17 = MakeRandom(ListeC17, ListeTaille)
                        c = 0
                        for j in SeqsC17:
                                #print i
                                F.write(">chr17_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1				
		elif i == "chr18":
                        ListeTaille = DicoChrom[i]
                        SeqsC18 = MakeRandom(ListeC18, ListeTaille)
                        c = 0
                        for j in SeqsC18:
                                #print i
                                F.write(">chr18_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1				
		elif i == "chr19":
                        ListeTaille = DicoChrom[i]
                        SeqsC19 = MakeRandom(ListeC19, ListeTaille)
                        c = 0
                        for j in SeqsC19:
                                #print i
                                F.write(">chr19_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1				
		elif i == "chr20":
                        ListeTaille = DicoChrom[i]
                        SeqsC20 = MakeRandom(ListeC20, ListeTaille)
                        c = 0
                        for j in SeqsC20:
                                #print i
                                F.write(">chr20_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1				
		elif i == "chr21":
                        ListeTaille = DicoChrom[i]
                        SeqsC21 = MakeRandom(ListeC21, ListeTaille)
                        c = 0
                        for j in SeqsC21:
                                #print i
                                F.write(">chr21_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1				
		elif i == "chr22":
                        ListeTaille = DicoChrom[i]
                        SeqsC22 = MakeRandom(ListeC22, ListeTaille)
                        c = 0
                        for j in SeqsC22:
                                #print i
                                F.write(">chr22_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1				
		elif i == "chrX":
                        ListeTaille = DicoChrom[i]
                        SeqsCX = MakeRandom(ListeCX, ListeTaille)
                        c = 0
                        for j in SeqsCX:
                                #print i
                                F.write(">chrX_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1				
		elif i == "chrY":
                        ListeTaille = DicoChrom[i]
                        SeqsCY = MakeRandom(ListeCY, ListeTaille)
                        c = 0
                        for j in SeqsCY:
                                #print i
                                F.write(">chrY_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1				
	F.close()				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				

PosFile = openFile("DeNovo_Size_Chrom")
DAllPos = RetrieveNbPositions(PosFile)
ListeC1 = GetSequences("NonCoding_chr1")
ListeC2 = GetSequences("NonCoding_chr2")
ListeC3 = GetSequences("NonCoding_chr3")
ListeC4 = GetSequences("NonCoding_chr4")
ListeC5 = GetSequences("NonCoding_chr5")
ListeC6 = GetSequences("NonCoding_chr6")
ListeC7 = GetSequences("NonCoding_chr7")
ListeC8 = GetSequences("NonCoding_chr8")
ListeC9 = GetSequences("NonCoding_chr9")
ListeC10 = GetSequences("NonCoding_chr10")
ListeC11= GetSequences("NonCoding_chr11")
ListeC12 = GetSequences("NonCoding_chr12")
ListeC13 = GetSequences("NonCoding_chr13")
ListeC14 = GetSequences("NonCoding_chr14")
ListeC15 = GetSequences("NonCoding_chr15")
ListeC16 = GetSequences("NonCoding_chr16")
ListeC17 = GetSequences("NonCoding_chr17")
ListeC18 = GetSequences("NonCoding_chr18")
ListeC19 = GetSequences("NonCoding_chr19")
ListeC20 = GetSequences("NonCoding_chr20")
ListeC21 = GetSequences("NonCoding_chr21")
ListeC22 = GetSequences("NonCoding_chr22")
ListeCX = GetSequences("NonCoding_chrX")
ListeCY = GetSequences("NonCoding_chrY")
MakeFile(DAllPos, ListeC1, ListeC2, ListeC3, ListeC4, ListeC5, ListeC6, ListeC7, ListeC8, ListeC9, ListeC10, ListeC11, ListeC12, ListeC13, ListeC14, ListeC15, ListeC16, ListeC17, ListeC18, ListeC19, ListeC20, ListeC21, ListeC22, ListeCX, ListeCY)






















