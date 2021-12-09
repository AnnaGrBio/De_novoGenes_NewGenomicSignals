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

DicoChrom = {"chr1": C1, "chr2":C2, "chr3":C3, "chr4":C4, "chr5":C5, "chr6":C6, "chr7":C7, "chr8":C8, "chr9":C9, "chr10":C10, "chr11":C11, "chr12":C12, "chr13":C13, "chr14":C14, "chr15":C15, "chr16":C16, "chr17":C17, "chr18":C18, "chr19":C19, "chr20":C20, "chr21":C21, "chr22":C22, "chrX":CX, "chrY":CY}

def MakeFile(Dico, Genes, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14, C15, C16, C17, C18, C19, C20, C21, C22, CX, CY):
	DicoGenesBefore = {}
	DicoGenesAfter = {}
	DicoPseudogenesBefore = {}
	DicoPseudogenesAfter = {}
	DicoNcRNABefore = {}
	DicoNcRNAAfter = {}
	for i in Genes:
		ligne = i.split()
		if ligne[0] in Dico.keys():
			Beg = int(ligne[1])
			End = int(ligne[2])
			Name = ligne[3]
			Categorie = ligne[4]
			Direction = ligne[5]
			LeChrom = Dico[ligne[0]]
			if Direction == "+":
				Before = LeChrom[Beg-100:Beg+100]
				After = LeChrom[End-100:End+100]
			else:
				Before = LeChrom[End-100:End+100]
				After = LeChrom[Beg-100:Beg+100]
			if Categorie == "ncRNA_gene":
				DicoNcRNABefore[Name+"_"+Direction] = Before
				DicoNcRNAAfter[Name+"_"+Direction] = After
			elif Categorie == "pseudogene":
				DicoPseudogenesBefore[Name+"_"+Direction] = Before
				DicoPseudogenesAfter[Name+"_"+Direction] = After
			else:
				DicoGenesBefore[Name+"_"+Direction] = Before
				DicoGenesAfter[Name+"_"+Direction] = After
	F = open("Genes200BeforeCorePromoter", "w")
	for i in DicoGenesBefore.keys():
		F.write(">"+i+"\n")
		F.write(DicoGenesBefore[i]+"\n")
	F.close()
        F = open("Pseudogenes200BeforeCorePromoter", "w")
        for i in DicoPseudogenesBefore.keys():
                F.write(">"+i+"\n")
                F.write(DicoPseudogenesBefore[i]+"\n")
        F.close()
        F = open("NcRNAgenes200BeforeCorePromoter", "w")
        for i in DicoNcRNABefore.keys():
                F.write(">"+i+"\n")
                F.write(DicoNcRNABefore[i]+"\n")
        F.close()









GenesPositions = openFile("AllGenesPos")
MakeFile(DicoChrom, GenesPositions, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14, C15, C16, C17, C18, C19, C20, C21, C22, CX, CY)
