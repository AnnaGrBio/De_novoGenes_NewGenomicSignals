
import os
os.chdir("Folder")
import random

def openFile(NameFile):
    F=open(NameFile, "r")
    L=F.readlines()
    return L  



def GetMotifList(Data):
    c = 0
    Dico = {}
    for i in Data[1:]:
        ligne = i.split("\n")[0]
        ligne = ligne.split("	")
        Name = ligne[0]
        Motif = ligne[1]
        if Name[0:5] == "ENSG0":
	    NbFound = 0
	    MotifPresent = False
	    for j in Dico.keys():
		PresentName = j.split("_")[0]
		if PresentName == Name:
		    NbFound+=1
		    if Dico[j] == Motif:
			MotifPresent = True
	    if MotifPresent == False:
		NewNb = str(NbFound+1)
		NewMotifName = Name+"_"+NewNb
	        Dico[NewMotifName] = Motif
    print len(Dico)
    return Dico
        
        
def GetDicoSeq(File):
    Dico = {}
    for i in File:
        if len(i)>1:
            ligne = i.split("\n")[0]
            if ligne[0]==">":
                Name = ligne[1:]
            else:
                Seq = ligne
		NewSeq = ""
		for i in Seq:
		    if i == "T":
			NewSeq+="U"
		    else:
			NewSeq+=i
                Dico[Name] = NewSeq
                Seq = ""
                Name = ""
    return Dico


def MakeCorresFile(File):
    Dico = {}
    for i in File:
        ligne = i.split(",")
        Name = ligne[0]
        Position = ligne[6]
        if Position == "0" or Position =="1" or Position == "2":
            Position = "Intergenic"
            Age = "I"+ ligne[7][1:len(ligne[7])-1]
            L = [Position, Age]
            Dico[Name]=L
        elif Position == "3" or Position == "4":
            Position = "Intronic"
            Age = "I"+ ligne[7][1:len(ligne[7])-1]
            L = [Position, Age]
            Dico[Name]=L
        else:
            Position = "Exonic"
            Age = "I"+ ligne[7][1:len(ligne[7])-1]
            L = [Position, Age]
            Dico[Name]=L
    return Dico


def MakeInfoFile(DicoSeqDeNovo, DicoSeqGene, DicoMotif, DicoCorres, NameFile1, NameFile2):
    BigDicoFinal = {}
    for i in DicoSeqDeNovo.keys():
        Loulou = i.split("_")
        NameDeNovo = Loulou[0]+"_"+Loulou[1]
        SequenceGene = DicoSeqDeNovo[i]
        SizeSeq = len(SequenceGene)
        if NameDeNovo in DicoCorres.keys():
            DicoGene = {}
            Position = DicoCorres[NameDeNovo][0]
            Age = DicoCorres[NameDeNovo][1]
            for NameMotif in DicoMotif:
                Motif = DicoMotif[NameMotif]
                NbMotif = SequenceGene.count(Motif)
                DicoGene[NameMotif] = NbMotif
            NewName=NameDeNovo+","+Position+","+Age+","+str(SizeSeq)
            BigDicoFinal[NewName] = DicoGene
    for i in DicoSeqGene.keys():
        NameGene = i.split("_")[0]
        SequenceGene = DicoSeqGene[i]
        SizeSeq = len(SequenceGene)
        DicoGene = {}
        for NameMotif in DicoMotif:
            Motif = DicoMotif[NameMotif]
            NbMotif = SequenceGene.count(Motif)
            DicoGene[NameMotif] = NbMotif
        NewName=NameGene+","+"EstablishedGene"+","+"-"","+str(SizeSeq)
        BigDicoFinal[NewName] = DicoGene
    F = open(NameFile1, "w")
    F.write("Name,Category,Age,Size,NbUniqMotifs,NbUniqMotifsPerSize,TotalMotifNumber,NbTotalMotifNumberPerSize"+"\n")
    for i in BigDicoFinal.keys():
        Data = i.split(",")
        DicoFromGene = BigDicoFinal[i]
        Name = Data[0]
        Category = Data[1]
        Age = Data[2]
        Size = int(Data[3])
        NbUniqMotifs = 0
        for j in DicoFromGene.keys():
            if DicoFromGene[j] >=1:
                NbUniqMotifs+=1
        TotalMotifNumber = 0
        for j in DicoFromGene.keys():
            TotalMotifNumber+=DicoFromGene[j]
        NbUniqMotifsPerSize = float(NbUniqMotifs)/float(Size)
        NbTotalMotifPerSize = float(TotalMotifNumber)/float(Size)
        F.write(Name+","+Category+","+Age+","+str(Size)+","+str(NbUniqMotifs)+","+str(NbUniqMotifsPerSize)+","+str(TotalMotifNumber)+","+str(NbTotalMotifPerSize)+"\n")
    F.close
    F = open(NameFile2, "w")
    F.write("Name,Category,Age,Size")
    ListeNameMotifs = []
    for i in BigDicoFinal.keys():
        for j in BigDicoFinal[i].keys():
            ListeNameMotifs.append(j)
        break
    for i in ListeNameMotifs:
        F.write(","+i)
    F.write("\n")
    for i in BigDicoFinal.keys():
        Data = i.split(",")
        DicoFromGene = BigDicoFinal[i]
        Name = Data[0]
        Category = Data[1]
        Age = Data[2]
        Size = int(Data[3])
        F.write(Name+","+Category+","+Age+","+str(Size))
        for Motifs in ListeNameMotifs:
            NbMotifs = str(DicoFromGene[Motifs])
            F.write(","+NbMotifs)
        F.write("\n")
    F.close()
    
    
    
            
                
                
    
        
ListeMotifs = openFile("ATtRACT_database.txt")
DicoMotifs = GetMotifList(ListeMotifs)

DeNovo5UTR=openFile("Region5primeDeNovoGenes")
DeNovo3UTR=openFile("Region3primeDeNovoGenes")
Gene5UTR = openFile("Region5primeGenesOneByGene.fa")
Gene3UTR = openFile("Region3primeGenesOneByGene.fa")



DicoDeNovo5UTR = GetDicoSeq(DeNovo5UTR)
DicoDeNovo3UTR = GetDicoSeq(DeNovo3UTR)
DicoGene5UTR = GetDicoSeq(Gene5UTR)
DicoGene3UTR = GetDicoSeq(Gene3UTR)


Corres = openFile("CorrespondanceFinal3")
DicoCorres = MakeCorresFile(Corres)

TestDeNovo=openFile("TestDeNovo")
TestGene = openFile("TestGene")
DicoTestDeNovo=GetDicoSeq(TestDeNovo)
DicoTestGene = GetDicoSeq(TestGene)
#MakeInfoFile(DicoTestDeNovo, DicoTestGene, DicoMotifs, DicoCorres, "lala", "lolo")

MakeInfoFile(DicoDeNovo5UTR, DicoGene5UTR, DicoMotifs, DicoCorres, "TotalNbMotifs_5UTR.txt", "MotifsDistribution_5UTR.txt")
MakeInfoFile(DicoDeNovo3UTR, DicoGene3UTR, DicoMotifs, DicoCorres, "TotalNbMotifs_3UTR.txt", "MotifsDistribution_3UTR.txt")


