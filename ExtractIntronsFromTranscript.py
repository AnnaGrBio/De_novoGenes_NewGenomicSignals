import os
os.chdir("Folder")
import random

def openFile(NameFile):
    F=open(NameFile, "r")
    L=F.readlines()
    return L  

#ncRNA_gene



def GetAllTranscriptsExons(FileGTF):
    DicoExons = {}
    PositionInFile = 0
    for i in FileGTF:
        if i[0] != "#":
            ligne = i.split()
            if ligne[2] == "gene":
                Compteur = PositionInFile+1
                while True:
                    ligneNew = FileGTF[Compteur].split()
                    if len(ligneNew)>2:
                        if ligneNew[2] == "exon":
                            PosBegin = ligneNew[3]
                            PosEnd = ligneNew[4]
                            Block = ligneNew[8].split(";")
                            Block = Block[0].split(":")
                            Transcript = Block[1]
                            #print Transcript
                            if Transcript in DicoExons.keys():
                                DicoExons[Transcript].append((PosBegin, PosEnd))
                            else:
                                DicoExons[Transcript] = [(PosBegin, PosEnd)]
                    else:   
                        #print ligneNew
                        break
                        
                   
                    Compteur+=1   
        PositionInFile +=1    
        #if len(DicoExons.keys())>100:
            #break
    return  DicoExons 

def MakeFinalFiles(Dico):
    F1 = open("NbIntronsByExons", "w")
    F1.write("TranscriptName"+","+"NbIntrons"+"\n")
    F2 = open("IntronsSize", "w")
    F2.write("TranscriptName"+","+"IntronSize"+"\n")
    for i in Dico.keys():
        TranscriptName = i
        NbIntrons = len(Dico[i])-1
        F1.write(TranscriptName+","+str(NbIntrons)+"\n")
        #print TranscriptName
        #print Dico[i]
        if NbIntrons>0:
            for j in range(len(Dico[i])-1):
                Suivant = Dico[i][j+1]
                Avant = Dico[i][j]
                SizeIntron = int(Suivant[0])-int(Avant[1])-2
                F2.write(TranscriptName+","+str(SizeIntron)+"\n")
        print "**********"
        

               
                
        

FichierGtf = openFile("Homo_sapiens.GRCh38.102.chr.gff3")
DicoExon = GetAllTranscriptsExons(FichierGtf)
MakeFinalFiles(DicoExon)












