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


def GetSequenceSize(File):
        Dico = {}
        it = SeqIO.parse(File, 'fasta')
        while True:
                try:
                        seqRecord = next(it)
                        #print(len(seqRecord.seq))
                        S = ""
                        for i in seqRecord.seq:
                                S +=i
                        Size = len(S)
                        Dico[seqRecord.id] = Size
                except StopIteration:
                        break
        return Dico




def GetFirstDico(File):
	D = {}
	#ListeElts = []
	for i in File:
		if i[0]!="#" and len(i)>1:
			ligne = i.split()
			Name = ligne[0]
			#if ligne[7] not in ListeElts:
				#ListeElts.append(ligne[7])
			NameDomainAndType = ligne[7]+"_"+ligne[5]+"_"+ligne[6]
			if float(ligne[12])<0.05:
				if Name not in D.keys():
					D[Name] = {NameDomainAndType:1}
				else:
					Present = False
					for Domain in D[Name].keys():
						if NameDomainAndType == Domain:
							D[Name][Domain] += 1
							Present = True
							break
					if Present == False:
						D[Name][NameDomainAndType] = 1
	#print ListeElts
	return D


def RetrieveData(Name, Dico, size):
	NbUniq = 0
	NbTotal = 0
	for i in Dico.keys():
		ligne = i.split("_")
		if ligne[0] == Name:
			NbUniq += 1
			NbTotal += Dico[i]
	NbUniqDivSize = float(NbUniq)/float(size)
	NbTotalDivSize = float(NbTotal)/float(size)
	return NbTotal, NbUniq, NbTotalDivSize, NbUniqDivSize


def MakeFileNbElementsByGene(DicoDeNovoDomain, DicoDeNovoSize, DicoGeneDomain, DicoGeneSize, NameFile):
	F = open(NameFile, "w")
	F.write("GeneName"+","+"category"+","+"size"+","+"NbFamily"+","+"NbFamilyDivSize"+","+"NbUniqFamily"+","+"NbUniqFamilyDivSize"+","+"NbDomain"+","+"NbDomainDivSize"+","+"NbUniqDomain"+","+"NbUniqDomainDivSize"+","+"NbMotif"+","+"NbMotifDivSize"+","+"NbUniqMotif"+","+"NbUniqMotifDivSize"+","+"NbRepeat"+","+"NbRepeatDivSize"+","+"NbUniqRepeat"+","+"NbUniqRepeatDivSize"+","+"NbDisordered"+","+"NbDisorderedDivSize"+","+"NbUniqDisordered"+","+"NbUniqDisorderedDivSize"+","+"NbCoiled-coil"+","+"NbCOiled-coilDivSize"+","+"NbUniqCoiled-coil"+","+"NbUniqCoiled-coilDivSize"+"\n")
	for i in DicoDeNovoDomain.keys():
		Subdic = DicoDeNovoDomain[i]
		Size = DicoDeNovoSize[i]
		TotalFamily, UniqFamily, TotalFamilyDivSize, UniqFamilyDivSize = RetrieveData("Family", Subdic, Size)
		TotalDomain, UniqDomain, TotalDomainDivSize, UniqDomainDivSize = RetrieveData("Domain", Subdic, Size)
		TotalMotif, UniqMotif, TotalMotifDivSize, UniqMotifDivSize = RetrieveData("Motif", Subdic, Size)
		TotalRepeat, UniqRepeat, TotalRepeatDivSize, UniqRepeatDivSize = RetrieveData("Repeat", Subdic, Size)
		TotalDisordered, UniqDisordered, TotalDisorderedDivSize, UniqDisorderedDivSize = RetrieveData("Disordered", Subdic, Size)
		TotalCoiledCoil, UniqCoiledCoil, TotalCoiledCoilDivSize, UniqCoiledCoilDivSize = RetrieveData("Coiled-coil", Subdic, Size)
		F.write(i+","+"DeNovoGene"+","+str(Size)+","+str(TotalFamily)+","+str(TotalFamilyDivSize)+","+str(UniqFamily)+","+str(UniqFamilyDivSize)+","+str(TotalDomain)+","+str(TotalDomainDivSize)+","+str(UniqDomain)+","+str(UniqDomainDivSize)+","+str(TotalMotif)+","+str(TotalMotifDivSize)+","+str(UniqMotif)+","+str(UniqMotifDivSize)+","+str(TotalRepeat)+","+str(TotalRepeatDivSize)+","+str(UniqRepeat)+","+str(UniqRepeatDivSize)+","+str(TotalDisordered)+","+str(TotalDisorderedDivSize)+","+str(UniqDisordered)+","+str(UniqDisorderedDivSize)+","+str(TotalCoiledCoil)+","+str(TotalCoiledCoilDivSize)+","+str(UniqCoiledCoil)+","+str(UniqCoiledCoilDivSize)+"\n")

        for i in DicoGeneDomain.keys():
                Subdic = DicoGeneDomain[i]
                Size = DicoGeneSize[i]
                TotalFamily, UniqFamily, TotalFamilyDivSize, UniqFamilyDivSize = RetrieveData("Family", Subdic, Size)
                TotalDomain, UniqDomain, TotalDomainDivSize, UniqDomainDivSize = RetrieveData("Domain", Subdic, Size)
                TotalMotif, UniqMotif, TotalMotifDivSize, UniqMotifDivSize = RetrieveData("Motif", Subdic, Size)
                TotalRepeat, UniqRepeat, TotalRepeatDivSize, UniqRepeatDivSize = RetrieveData("Repeat", Subdic, Size)
                TotalDisordered, UniqDisordered, TotalDisorderedDivSize, UniqDisorderedDivSize = RetrieveData("Disordered", Subdic, Size)
                TotalCoiledCoil, UniqCoiledCoil, TotalCoiledCoilDivSize, UniqCoiledCoilDivSize = RetrieveData("Coiled-coil", Subdic, Size)
                F.write(i+","+"Gene"+","+str(Size)+","+str(TotalFamily)+","+str(TotalFamilyDivSize)+","+str(UniqFamily)+","+str(UniqFamilyDivSize)+","+str(TotalDomain)+","+str(TotalDomainDivSize)+","+str(UniqDomain)+","+str(UniqDomainDivSize)+","+str(TotalMotif)+","+str(TotalMotifDivSize)+","+str(UniqMotif)+","+str(UniqMotifDivSize)+","+str(TotalRepeat)+","+str(TotalRepeatDivSize)+","+str(UniqRepeat)+","+str(UniqRepeatDivSize)+","+str(TotalDisordered)+","+str(TotalDisorderedDivSize)+","+str(UniqDisordered)+","+str(UniqDisorderedDivSize)+","+str(TotalCoiledCoil)+","+str(TotalCoiledCoilDivSize)+","+str(UniqCoiledCoil)+","+str(UniqCoiledCoilDivSize)+"\n")
	F.close()

Genes = openFile("HumanGenesProt.fa.pfam")
DicoTailleGene = GetSequenceSize("HumanGenesProt.fa")
DicoDomainGene = GetFirstDico(Genes)

DeNovoGenes = openFile("DeNovoGenesProt.fa.pfam")
DicoTailleDeNovo = GetSequenceSize("DeNovoGenesProt.fa")
DicoDomainDeNovoGene = GetFirstDico(DeNovoGenes)

MakeFileNbElementsByGene(DicoDomainDeNovoGene, DicoTailleDeNovo, DicoDomainGene, DicoTailleGene, "DataDomains.rst")
