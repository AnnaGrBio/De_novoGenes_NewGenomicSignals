import os
os.chdir("Folder")
import random

def openFile(NameFile):
    F=open(NameFile, "r")
    L=F.readlines()
    return L  





def MakeCorresFile(File):
    Dico = {}
    for i in File:
        ligne = i.split(",")
        Name = ligne[0]
        Position = ligne[6]
        Direction = ligne[8]
        if Direction == ".":
            Direction = "+"
        if Position == "0" or Position =="1" or Position == "2":
            Position = "Intergenic"
            Age = "I"+ ligne[7][1:len(ligne[7])-1]
            L = [Position, Age,Direction]
            Dico[Name]=L
        elif Position == "3" or Position == "4":
            Position = "Intronic"
            Age = "I"+ ligne[7][1:len(ligne[7])-1]
            L = [Position, Age,Direction]
            Dico[Name]=L
        else:
            Position = "Exonic"
            Age = "I"+ ligne[7][1:len(ligne[7])-1]
            L = [Position, Age,Direction]
            Dico[Name]=L
    return Dico




def MakeDicoORFs(File):
    DicoForward = {}
    DicoReverse = {}
    Seq = ""
    NameGene = ""
    c=0
    for i in File:
        #c+=1
        #if c>200:
            #break
        ligne = i.split("\n")[0]
        if ligne[0] == ">":
            if len(NameGene)>0:
                if Reverse == True:
                    if NameGene in DicoReverse.keys():
                        DicoReverse[NameGene].append(len(Seq))
                    else:
                        DicoReverse[NameGene] = [len(Seq)]
                elif Reverse == False:
                    if NameGene in DicoForward.keys():
                        DicoForward[NameGene].append(len(Seq))
                    else:
                        DicoForward[NameGene] = [len(Seq)]
            Seq = ""
            if "REVERSE SENSE" in ligne:
                Reverse=True
            else:
                Reverse=False
            Name = ligne.split(" ")[0][1:]
            NameGene = Name.split("_")[0]
        else:
            Seq+=ligne
    if Reverse == True:
        if NameGene in DicoReverse.keys():
            DicoReverse[NameGene].append(len(Seq))
        else:
            DicoReverse[NameGene] = [len(Seq)]
    elif Reverse == False:
        if NameGene in DicoForward.keys():
            DicoForward[NameGene].append(len(Seq))
        else:
            DicoForward[NameGene] = [len(Seq)]
    return DicoForward, DicoReverse


def GetMax(Liste):
    Max = 0
    for i in Liste:
        if int(i)>Max:
            Max = i
    return Max

def GetTotal(Liste):
    T = 0
    for i in Liste:
        T+=int(i)
    return T


def CalcPTI(Liste):
    highest = GetMax(Liste)
    Total = GetTotal(Liste)
    PTI = float(highest)/float(Total)
    return PTI


def GetPTI(DicoInfoDeNovo, DicoForward, DicoReverse):
    DicoFinal = {}
    print len(DicoInfoDeNovo)
    c=0
    for NameDeNovo in DicoInfoDeNovo.keys():
        NameGene = NameDeNovo.split("_")[0]
        ListeInfo = DicoInfoDeNovo[NameDeNovo]
        Direction = ListeInfo[2]
        if Direction == "+":   
            if NameGene in DicoForward.keys():
                PTI = CalcPTI(DicoForward[NameGene])
                ListeInfo.append(PTI)
                DicoFinal[NameDeNovo]=ListeInfo
        else:
            if NameGene in DicoReverse.keys():
                PTI = CalcPTI(DicoReverse[NameGene])
                ListeInfo.append(PTI)
                DicoFinal[NameDeNovo]=ListeInfo
        c+=1
        print c
    F = open("Data_PTI.txt", "w")
    F.write("Name,Position,Age,Direction,PTI"+"\n")
    for i in DicoFinal.keys():
        F.write(i)
        Liste = DicoFinal[i]
        for j in Liste:
            F.write(","+str(j))
        F.write("\n")
    F.close()




Corres = openFile("CorrespondanceFinal3")
DicoInfoDeNovo = MakeCorresFile(Corres)

AllORFs = openFile("hsapiens_merged_orfs.fa")
DicoForward, DicoReverse = MakeDicoORFs(AllORFs)
GetPTI(DicoInfoDeNovo, DicoForward, DicoReverse)
