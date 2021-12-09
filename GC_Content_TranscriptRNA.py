import os
os.chdir("Folder")
import random

def openFile(NameFile):
    F=open(NameFile, "r")
    L=F.readlines()
    return L  


def TranscriptDeNovo(File):
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
			NewSeq = ""
			for i in Sequence:
				if i == "T":
					NewSeq+="U"
				else:
					NewSeq+=i
			Dico[Name] = NewSeq
	return Dico


def TranscriptGene(File):
        Dico = {}
        from Bio.Seq import Seq
        c = 0
        for i in File:
                if i[0] == ">":
                        ligne = i.split("\n")
                        Name = ligne[0]
                        Name = Name[1:]
                        Name = Name.split("_")
                        Name = Name[0] +"_"+Name[1]
                else:
                        Liste = i.split("\n")
                        Sequence = Liste[0]
                        NewSeq = ""
                        for i in Sequence:
                                if i == "T":
                                        NewSeq+="U"   
                                else:
                                        NewSeq+=i
			Dico[Name] = NewSeq

        return Dico

def MakeFinalFile(Dico, Name):
	F = open(Name, "w")
	for i in Dico.keys():
		F.write(">"+i+"\n")
		F.write(Dico[i]+"\n")
	F.close()



DataDeNovo5 = openFile("Region5primeDeNovoGenes")
DicoDeNovo5 = TranscriptDeNovo(DataDeNovo5)


DataGene5 = openFile("Region5primeGenes")
DicoGene5 = TranscriptGene(DataGene5)

MakeFinalFile(DicoDeNovo5,"Region5primeUTRDeNovoRNA.fa")
MakeFinalFile(DicoGene5, "Region5primeUTRGeneRNA.fa")

