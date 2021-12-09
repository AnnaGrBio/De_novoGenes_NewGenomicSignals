import os
os.chdir("Folder")
import random

def openFile(NameFile):
    F=open(NameFile, "r")
    L=F.readlines()
    return L  

#ncRNA_gene

def GetGenes(File):
    NbGenes = 0
    NcRNAgenes = 0
    NbPseudo = 0
    c = 100
    Liste = []
    for i in File:
        if i[0]!="#":
            ligne = i.split()
            Categorie = ligne[2]
            if Categorie == "gene" or Categorie == "ncRNA_gene" or Categorie == "pseudogene":
                NomChrom = "chr"+ligne[0]
                PosBegin = ligne[3]
                PosEnd = ligne[4]
                Sens = ligne[6]
                TotalName = ligne[8].split(";")
                HalfTotalName = TotalName[0].split(":")
                Name = HalfTotalName[1]
                Phrase = NomChrom+" "+PosBegin+" "+PosEnd+" "+Name+" "+Categorie+" "+Sens+" "+"\n"
                Liste += Phrase
                if Categorie == "ncRNA_gene":
                    NcRNAgenes += 1
                elif Categorie == "pseudogene":
                    NbPseudo +=1
                elif Categorie == "gene":
                    NbGenes+=1
    print NbGenes
    print NcRNAgenes
    print NbPseudo
            #print ligne[2]
            #c += 1
            #if c>1000:
                #break
    NewFile = open("AllGenesPos", "w")
    for i in Liste:
        NewFile.write(i)
    NewFile.close()

FichierGtf = openFile("Homo_sapiens.GRCh38.102.chr.gff3")
GetGenes(FichierGtf)
