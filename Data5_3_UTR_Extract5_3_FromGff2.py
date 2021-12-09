import os
os.chdir("Folder")
import random

def openFile(NameFile):
    F=open(NameFile, "r")
    L=F.readlines()
    return L  




def GetGenes(File):
    ListePourFichier = []
    c = 100
    InAGene = False
    NbWithoutCDS = 0
    for i in File:
        if i[0]!="#":
            ligne = i.split()
            Categorie = ligne[2]
            if Categorie == "gene":
                NomChrom = "chr"+ligne[0]
                PosBeginGene = ligne[3]
                PosEndGene = ligne[4]
                Sens = ligne[6]
                TotalName = ligne[8].split(";")
                HalfTotalName = TotalName[0].split(":")
                Name = HalfTotalName[1]
                InAGene = True
            elif Categorie == "five_prime_UTR" and InAGene == True:
                Debut5prime = ligne[3]
                Fin5prime = ligne[4]
                Taille5prime = int(Fin5prime)-int(Debut5prime)
                NomTranscript = ligne[8].split(":")
                NomTranscript = NomTranscript[1]
                Phrase = NomChrom+","+Name+","+NomTranscript+","+str(PosBeginGene)+"_"+str(PosEndGene)+","+Sens+","+str(Taille5prime)+","+str(Debut5prime)+","+str(Fin5prime)+","+"NA"+","+"NA"+","+"NA"+"\n"
                ListePourFichier.append(Phrase)
            elif Categorie == "three_prime_UTR" and InAGene == True:
                Debut3prime = ligne[3]
                Fin3prime = ligne[4]
                Taille3prime = int(Fin3prime)-int(Debut3prime)
                NomTranscript = ligne[8].split(":")
                NomTranscript = NomTranscript[1]
                Phrase = NomChrom+","+Name+","+NomTranscript+","+str(PosBeginGene)+"_"+str(PosEndGene)+","+Sens+","+"NA"+","+"NA"+","+"NA"+","+str(Taille3prime)+","+str(Debut3prime)+","+str(Fin3prime)+"\n"
                ListePourFichier.append(Phrase)
        else:
            InAGene = False
    F = open("DataHumanGenes_5_3_prime", "w")
    F.write("NameChrom"+","+"NameGene"+","+"TranscriptName"+","+"PosBeginGene"+"_"+"PosEndGene"+","+"direction"+","+"Size5prime"+","+"Begin5prime"+","+"End5prime"+","+"Size3prime"+","+"Begin3prime"+","+"End3prime"+"\n")
    for i in ListePourFichier:   
        F.write(i)
    F.close()
    print NbWithoutCDS

                    



FichierGtf = openFile("Homo_sapiens.GRCh38.102.chr.gff3")
GetGenes(FichierGtf)
