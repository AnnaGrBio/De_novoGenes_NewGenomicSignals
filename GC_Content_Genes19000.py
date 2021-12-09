
import os
os.chdir("Folder")
import random

def openFile(NameFile):
    F=open(NameFile, "r")
    L=F.readlines()
    return L  


def GetOneSeqByGene(File):
        Dico = {}
        from Bio.Seq import Seq
        c = 0
        for i in File:
                if i[0] == ">":
                        ligne = i.split("\n")
                        Name = ligne[0]
                        Name = Name[1:]
                        Name = Name.split("_")
                        Name = Name[0]+"_"+Name[2]
                else:
                        Liste = i.split("\n")
                        Sequence = Liste[0]
                        Dico[Name] = Sequence
			print Name
			print Sequence

        return Dico

def MakeFinalFile(Dico, Name):
        F = open(Name, "w")
        for i in Dico.keys():
                F.write(">"+i+"\n")
                F.write(Dico[i]+"\n")
        F.close()

DataGene5 = openFile("Region5primeGenes")
DicoGene5 = GetOneSeqByGene(DataGene5)

MakeFinalFile(DicoGene5, "Region5primeGenesOneByGene.fa")

DataGene3 = openFile("Region3primeGenes")
DicoGene3 = GetOneSeqByGene(DataGene3)

MakeFinalFile(DicoGene3, "Region3primeGenesOneByGene.fa")



