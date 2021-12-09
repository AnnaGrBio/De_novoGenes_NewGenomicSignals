import os
os.chdir("Folder")
import random

def openFile(NameFile):
    F=open(NameFile, "r")
    L=F.readlines()
    return L  


def GetGCdeNovo(File):
	Dico = {}
        from Bio.Seq import Seq
	c = 0
        for i in File:
                if i[0] == ">":
			ligne = i.split("\n")
			Name = ligne[0]
			Name = Name[1:]
			Name = Name.split("_")
			Name = Name[0]+"_"+Name[1]
                else:
                        Liste = i.split("\n")
                        Sequence = Liste[0]
			TailleSeq = len(Sequence)
			if TailleSeq > 6:
				NbGC = 0
				for j in Sequence:
					if j == "G" or j == "C":
						NbGC+=1
				PourcGC = float(100)*float(NbGC)/float(TailleSeq)
				Dico[Name] = [TailleSeq, PourcGC]
	return Dico


def GetGCGene(File):
        Dico = {}
        from Bio.Seq import Seq
        c = 0
        for i in File:
                if i[0] == ">":
                        ligne = i.split("\n")
                        Name = ligne[0]
                        Name = Name[1:]
                        Name = Name.split("_")
                        Name = Name[0]+"_"+Name[1]
                else:
                        Liste = i.split("\n")
                        Sequence = Liste[0]
                        TailleSeq = len(Sequence)
                        if TailleSeq > 6:
                                NbGC = 0
                                for j in Sequence:
                                        if j == "G" or j == "C":
                                                NbGC+=1
                                PourcGC = float(100)*float(NbGC)/float(TailleSeq)
                                Dico[Name] = [TailleSeq, PourcGC]
        return Dico

def MakeFinalFile(DicoDeNovo, DicoGene, Corres, Name):
	F = open(Name, "w")
	F.write("Category"+","+"ClassAge"+","+"Classpos"+","+"SizeSeq"+","+"PercGC"+"\n")
	for i in DicoGene.keys():
		Name = i
		Size = DicoGene[i][0]
		PercGC = DicoGene[i][1]
		F.write("Gene"+","+"NA"+","+"NA"+","+str(Size)+","+str(PercGC)+"\n")
	for i in DicoDeNovo.keys():
		Name = i
		Size = DicoDeNovo[i][0]
		PercGC = DicoDeNovo[i][1]
		for j in Corres:
			ligne = j.split(",")
			OtherName = ligne[0]
			Pos = ligne[6]
			Age = ligne[7]
			if OtherName == Name:
				F.write("DeNovo"+","+Age+","+Pos+","+str(Size)+","+str(PercGC)+"\n")
				break
	F.close()



DataDeNovo5 = openFile("Region5primeDeNovoGenes")
DicoDeNovo5 = GetGCdeNovo(DataDeNovo5)

DataDeNovo3 = openFile("Region3primeDeNovoGenes")
DicoDeNovo3 = GetGCdeNovo(DataDeNovo3)


DataGene5 = openFile("Region5primeGenes")
DicoGene5 = GetGCGene(DataGene5)

DataGene3 = openFile("Region3primeGenes")
DicoGene3 = GetGCGene(DataGene3)


Corres3 = openFile("CorrespondanceFinal3")

MakeFinalFile(DicoDeNovo5, DicoGene5, Corres3, "RstGC5primeUTR")
MakeFinalFile(DicoDeNovo3, DicoGene3, Corres3, "RstGC3primeUTR")

