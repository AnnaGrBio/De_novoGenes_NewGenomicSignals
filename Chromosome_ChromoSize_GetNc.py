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




##############################################  Get Non COding regions #####################

def MakeDicoNonCoding(File):
	Dico = {}
	for i in File:
		ligne = i.split("\n")
		lala = ligne[0].split()
		if lala[0] not in Dico.keys():
			Dico[lala[0]] = []
			Beg = int(lala[1])
			End = int(lala[2])
			l = [Beg, End]
			Dico[lala[0]].append(l)
		else:
			Beg = int(lala[1])
                        End = int(lala[2])
                        l = [Beg, End]
                        Dico[lala[0]].append(l)
	return Dico



def GetRegions(FastaChrom, NomChrom, DicoPos, Type):
	F = open(Type+"_"+NomChrom, "w")
	c = 1
	for i in DicoPos.keys():
		if i == NomChrom:
			Region = DicoPos[i]
			for j in Region:
				Beg = j[0]
				End = j[1]
				Nom = Type+"_"+NomChrom+"_"+str(c)+"_"+str(Beg)+"_"+str(End)
				Seq = FastaChrom[Beg:End-1]
				F.write(">"+Nom+"\n")
				F.write(Seq+"\n")
				c+=1


NcRegionsPos = openFile("NonCodingRegionsPosition")
DicoNc = MakeDicoNonCoding(NcRegionsPos)

IntronPos = openFile("IntronsPositionsWithoutEnd")
DicoIntron = MakeDicoNonCoding(IntronPos)
#print DicoIntron


GetRegions(C1, "chr1", DicoNc, "NonCoding")
GetRegions(C1, "chr1", DicoIntron, "Intron")


GetRegions(C2, "chr2", DicoNc, "NonCoding")
GetRegions(C2, "chr2", DicoIntron, "Intron")

GetRegions(C3, "chr3", DicoNc, "NonCoding")
GetRegions(C3, "chr3", DicoIntron, "Intron")

GetRegions(C4, "chr4", DicoNc, "NonCoding")
GetRegions(C4, "chr4", DicoIntron, "Intron")

GetRegions(C5, "chr5", DicoNc, "NonCoding")
GetRegions(C5, "chr5", DicoIntron, "Intron")

GetRegions(C6, "chr6", DicoNc, "NonCoding")
GetRegions(C6, "chr6", DicoIntron, "Intron")

GetRegions(C7, "chr7", DicoNc, "NonCoding")
GetRegions(C7, "chr7", DicoIntron, "Intron")

GetRegions(C8, "chr8", DicoNc, "NonCoding")
GetRegions(C8, "chr8", DicoIntron, "Intron")

GetRegions(C9, "chr9", DicoNc, "NonCoding")
GetRegions(C9, "chr9", DicoIntron, "Intron")

GetRegions(C10, "chr10", DicoNc, "NonCoding")
GetRegions(C10, "chr10", DicoIntron, "Intron")

GetRegions(C11, "chr11", DicoNc, "NonCoding")
GetRegions(C11, "chr11", DicoIntron, "Intron")

GetRegions(C12, "chr12", DicoNc, "NonCoding")
GetRegions(C12, "chr12", DicoIntron, "Intron")

GetRegions(C13, "chr13", DicoNc, "NonCoding")
GetRegions(C13, "chr13", DicoIntron, "Intron")

GetRegions(C14, "chr14", DicoNc, "NonCoding")
GetRegions(C14, "chr14", DicoIntron, "Intron")

GetRegions(C15, "chr15", DicoNc, "NonCoding")
GetRegions(C15, "chr15", DicoIntron, "Intron")

GetRegions(C16, "chr16", DicoNc, "NonCoding")
GetRegions(C16, "chr16", DicoIntron, "Intron")

GetRegions(C17, "chr17", DicoNc, "NonCoding")
GetRegions(C17, "chr17", DicoIntron, "Intron")

GetRegions(C18, "chr18", DicoNc, "NonCoding")
GetRegions(C18, "chr18", DicoIntron, "Intron")

GetRegions(C19, "chr19", DicoNc, "NonCoding")
GetRegions(C19, "chr19", DicoIntron, "Intron")

GetRegions(C20, "chr20", DicoNc, "NonCoding")
GetRegions(C20, "chr20", DicoIntron, "Intron")

GetRegions(C21, "chr21", DicoNc, "NonCoding")
GetRegions(C21, "chr21", DicoIntron, "Intron")

GetRegions(C22, "chr22", DicoNc, "NonCoding")
GetRegions(C22, "chr22", DicoIntron, "Intron")

GetRegions(CX, "chrX", DicoNc, "NonCoding")
GetRegions(CX, "chrX", DicoIntron, "Intron")

GetRegions(CY, "chrY", DicoNc, "NonCoding")
GetRegions(CY, "chrY", DicoIntron, "Intron")



