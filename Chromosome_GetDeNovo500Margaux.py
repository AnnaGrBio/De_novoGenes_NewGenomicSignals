import cv2
import os
os.chdir("Folder")
import random

def openFile(NameFile):
    F=open(NameFile, "r")
    L=F.readlines()
    return L  

def PrintLenChrom(File, name):
	print name
	Nb = 0
	for i in File:
		if i[0] != ">":
			if len(i)>0:
				Nb+=len(i)-1
	print Nb


def RecoverChrom(File):
	Ch = ""
	for i in File:
		if i[0]!= ">":
			if len(i)>0:
				Ch += i[0:len(i)-1]
	#print len(Ch)
	#print Ch[0:2000]
	return Ch


Chr1 = openFile("Homo_sapiens.GRCh38.dna.chromosome.1.fa")
#PrintLenChrom(Chr1, "Chrom 1")
C1 = RecoverChrom(Chr1)

Chr2 = openFile("Homo_sapiens.GRCh38.dna.chromosome.2.fa")
#PrintLenChrom(Chr2, "Chrom 2")
C2 = RecoverChrom(Chr2)

Chr3 = openFile("Homo_sapiens.GRCh38.dna.chromosome.3.fa")
#PrintLenChrom(Chr3, "Chrom 3")
C3 = RecoverChrom(Chr3)

Chr4 = openFile("Homo_sapiens.GRCh38.dna.chromosome.4.fa")
#PrintLenChrom(Chr4, "Chrom 4")
C4 = RecoverChrom(Chr4)

Chr5 = openFile("Homo_sapiens.GRCh38.dna.chromosome.5.fa")
#PrintLenChrom(Chr5, "Chrom 5")
C5 = RecoverChrom(Chr5)

Chr6 = openFile("Homo_sapiens.GRCh38.dna.chromosome.6.fa")
#PrintLenChrom(Chr6, "Chrom 6")
C6 = RecoverChrom(Chr6)

Chr7 = openFile("Homo_sapiens.GRCh38.dna.chromosome.7.fa")
#PrintLenChrom(Chr7, "Chrom 7")
C7 = RecoverChrom(Chr7)

Chr8 = openFile("Homo_sapiens.GRCh38.dna.chromosome.8.fa")
#PrintLenChrom(Chr8, "Chrom 8")
C8 = RecoverChrom(Chr8)

Chr9 = openFile("Homo_sapiens.GRCh38.dna.chromosome.9.fa")
#PrintLenChrom(Chr9, "Chrom 9")
C9 = RecoverChrom(Chr9)

Chr10 = openFile("Homo_sapiens.GRCh38.dna.chromosome.10.fa")
#PrintLenChrom(Chr10, "Chrom 10")
C10 = RecoverChrom(Chr10)

Chr11 = openFile("Homo_sapiens.GRCh38.dna.chromosome.11.fa")
#PrintLenChrom(Chr11, "Chrom 11")
C11 = RecoverChrom(Chr11)

Chr12 = openFile("Homo_sapiens.GRCh38.dna.chromosome.12.fa")
#PrintLenChrom(Chr12, "Chrom 12")
C12 = RecoverChrom(Chr12)

Chr13 = openFile("Homo_sapiens.GRCh38.dna.chromosome.13.fa")
#PrintLenChrom(Chr13, "Chrom 13")
C13 = RecoverChrom(Chr13)

Chr14 = openFile("Homo_sapiens.GRCh38.dna.chromosome.14.fa")
#PrintLenChrom(Chr14, "Chrom 14")
C14 = RecoverChrom(Chr14)

Chr15 = openFile("Homo_sapiens.GRCh38.dna.chromosome.15.fa")
#PrintLenChrom(Chr15, "Chrom 15")
C15 = RecoverChrom(Chr15)

Chr16 = openFile("Homo_sapiens.GRCh38.dna.chromosome.16.fa")
#PrintLenChrom(Chr16, "Chrom 16")
C16 = RecoverChrom(Chr16)

Chr17 = openFile("Homo_sapiens.GRCh38.dna.chromosome.17.fa")
#PrintLenChrom(Chr17, "Chrom 17")
C17 = RecoverChrom(Chr17)

Chr18 = openFile("Homo_sapiens.GRCh38.dna.chromosome.18.fa")
#PrintLenChrom(Chr18, "Chrom 18")
C18 = RecoverChrom(Chr18)

Chr19 = openFile("Homo_sapiens.GRCh38.dna.chromosome.19.fa")
#PrintLenChrom(Chr19, "Chrom 19")
C19 = RecoverChrom(Chr19)

Chr20 = openFile("Homo_sapiens.GRCh38.dna.chromosome.20.fa")
#PrintLenChrom(Chr20, "Chrom 20")
C20 = RecoverChrom(Chr20)

Chr21 = openFile("Homo_sapiens.GRCh38.dna.chromosome.21.fa")
#PrintLenChrom(Chr21, "Chrom 21")
C21 = RecoverChrom(Chr21)

Chr22 = openFile("Homo_sapiens.GRCh38.dna.chromosome.22.fa")
#PrintLenChrom(Chr22, "Chrom 22")
C22 = RecoverChrom(Chr22)

ChrX = openFile("Homo_sapiens.GRCh38.dna.chromosome.X.fa")
#PrintLenChrom(ChrX, "Chrom X")
CX = RecoverChrom(ChrX)

ChrY = openFile("Homo_sapiens.GRCh38.dna.chromosome.Y.fa")
#PrintLenChrom(ChrY, "Chrom Y")
CY = RecoverChrom(ChrY)


def SeeDoublons(D1, D2):
	ListeDoublons = []
	ListeGood = []
	for Name1 in D1.keys():
		Doublons = False
		Seq1 = D1[Name1]
		Seq2 = D2[Name1]
		for Name2 in D1.keys():
			SeqNext1 = D1[Name2]
			SeqNext2 = D2[Name2]
			if Seq1 == SeqNext1 and Seq2 == SeqNext2:
				if Name1 != Name2:
					L = [Name1, Name2]
					ListeDoublons.append(L)
					Doublons  =True
					break
		if Doublons == False:
			ListeGood.append(Name1)
	ListToKeep = []
	for i in ListeDoublons:
		if i[0] in ListToKeep or i[1] in ListToKeep:
			continue
		else:
			ListToKeep.append(i[0])
	print len(ListToKeep)
	print len(ListeGood)
	print len(ListeDoublons)
	return ListeGood, ListToKeep, ListeDoublons


def SearchORF(D, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14, C15, C16, C17, C18, C19, C20, C21, C22, CX, CY):
	DicoChrom = {"chr1": C1, "chr2":C2, "chr3":C3, "chr4":C4, "chr5":C5, "chr6":C6, "chr7":C7, "chr8":C8, "chr9":C9, "chr10":C10, "chr11":C11, "chr12":C12, "chr13":C13, "chr14":C14, "chr15":C15, "chr16":C16, "chr17":C17, "chr18":C18, "chr19":C19, "chr20":C20, "chr21":C21, "chr22":C22, "chrX":CX, "chrY":CY}
	DicoAllSeqBefore = {}
	DicoAllSeqAfter = {}
	for i in D:
		Chrom = D[i][0]
		IntervBefore = D[i][1]
		IntervAfter = D[i][2]
		SeqChrom = DicoChrom[Chrom]
		SeqBefore = SeqChrom[IntervBefore[0]:IntervBefore[1]]
		DicoAllSeqBefore[i] = SeqBefore
		SeqAfter = SeqChrom[IntervAfter[0]:IntervAfter[1]]
		DicoAllSeqAfter[i] = SeqAfter
	ListeGood, ListToKeep, ListeDoublons = SeeDoublons(DicoAllSeqBefore, DicoAllSeqAfter)
	F = open("Sequences1000BeforeDeNovoGeneMargaux", "w")
	for i in ListeGood:
		F.write(">"+i)
		F.write(DicoAllSeqBefore[i]+str("\n"))
	for i in ListToKeep:
                F.write(">"+i)
                F.write(DicoAllSeqBefore[i]+str("\n"))
	F.close()
	F = open("Sequences1000AfterDeNovoGeneMargaux", "w")
        for i in ListeGood:
                F.write(">"+i)
                F.write(DicoAllSeqAfter[i]+str("\n"))
        for i in ListToKeep:
                F.write(">"+i)
                F.write(DicoAllSeqAfter[i]+str("\n"))
        F.close()






def DicoCorres(File):
    D = {}
    c = 0
    ListeGenesMargaux = ["rna104722_2", "MSTRG.22282.1_3", " rna80857_11", "rna73335_27", "MSTRG.15236.1_7", "MSTRG.7356.1_25", "MSTRG.32955.1_5", "rna161493_2", "MSTRG.29307.1_1", "MSTRG.34141.1_1"]
    for i in File:
        ligne = i.split("\n")
        Elts = ligne[0].split(",")
        if Elts[8] == "+" or Elts[8] == "-":
            Name = Elts[0]
            Chrom = Elts[1][1:len(Elts[1])-1]
            if Elts[8] == "+":
                Begin = int(Elts[2])-int(Elts[9])
                End = int(Elts[3])+int(Elts[10])
                IntervalBegin = [Begin-1000, Begin]
                IntervalEnd = [End, End+1000]
                D[i] = [Chrom, IntervalBegin, IntervalEnd]
            else:
                Begin = int(Elts[3])+int(Elts[9])
                End = int(Elts[2])-int(Elts[10])
                IntervalBegin = [Begin, Begin+1000]
                IntervalEnd = [End-1000, End]
                D[i] = [Chrom, IntervalBegin, IntervalEnd]
    print D
    
    return D

Correspondance = openFile("CorrespondanceMargaux")
D =DicoCorres(Correspondance)



SearchORF(D, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14, C15, C16, C17, C18, C19, C20, C21, C22, CX, CY)
