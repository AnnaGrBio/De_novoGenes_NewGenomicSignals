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





def GetFirstDico(FileGene, FileDeNovo):
	DFamily = {}
	DDomain = {}
	DRepeat = {}
	DDisordered = {}
	DCoiledCoil = {}
	for i in FileGene:
		if i[0]!="#" and len(i)>1:
			ligne = i.split()
			NameElt = ligne[6]
			Type = ligne[7]
			if float(ligne[12])<0.05:
				if Type == "Family":
					if NameElt not in DFamily.keys():
						DFamily[NameElt] = [1, 0]
					else:
						DFamily[NameElt][0]+=1
				elif Type == "Domain":
					if NameElt not in DDomain.keys():
						DDomain[NameElt] = [1, 0]
					else:
						DDomain[NameElt][0]+=1
				elif Type == "Repeat":
					if NameElt not in DRepeat.keys():
						DRepeat[NameElt] = [1, 0]
					else:
						DRepeat[NameElt][0]+=1
				elif Type == "Disordered":
					if NameElt not in DDisordered.keys():
						DDisordered[NameElt] = [1, 0]
					else:
						DDisordered[NameElt][0]+=1
				elif Type == "Coiled-coil":
					if NameElt not in DCoiledCoil.keys():
						DCoiledCoil[NameElt] = [0, 1]
					else:
						DCoiledCoil[NameElt][0] +=1
	for i in FileDeNovo:
                if i[0]!="#" and len(i)>1:
                        ligne = i.split()
                        NameElt = ligne[6]
                        Type = ligne[7]
                        if float(ligne[12])<0.05:
                                if Type == "Family":
                                        if NameElt not in DFamily.keys():
                                                DFamily[NameElt] = [0, 1]
                                        else:
                                                DFamily[NameElt][1]+=1
                                elif Type == "Domain":
                                        if NameElt not in DDomain.keys():
                                                DDomain[NameElt] = [0, 1]
                                        else:
                                                DDomain[NameElt][1]+=1
                                elif Type == "Repeat":
                                        if NameElt not in DRepeat.keys():
                                                DRepeat[NameElt] = [0, 1]
                                        else:
                                                DRepeat[NameElt][1]+=1
                                elif Type == "Disordered":
                                        if NameElt not in DDisordered.keys():
                                                DDisordered[NameElt] = [0, 1]
                                        else:
                                                DDisordered[NameElt][1]+=1
                                elif Type == "Coiled-coil":
                                        if NameElt not in DCoiledCoil.keys():
                                                DCoiledCoil[NameElt] = [0, 1]
                                        else:
                                                DCoiledCoil[NameElt][1] +=1
	F = open("Data_Domain", "w")
	F.write("NameDomain"+","+"Category"+","+"NbDomain"+"\n")
	for i in DDomain.keys():
		F.write(i+","+"Gene"+","+str(DDomain[i][0])+"\n")
		F.write(i+","+"DeNovoGene"+","+str(DDomain[i][1])+"\n")
	F.close()
        F = open("Data_Family", "w")
        F.write("NameFamily"+","+"Category"+","+"NbFamily"+"\n")
        for i in DFamily.keys():
                F.write(i+","+"Gene"+","+str(DFamily[i][0])+"\n")
                F.write(i+","+"DeNovoGene"+","+str(DFamily[i][1])+"\n")
        F.close()
        F = open("Data_Repeat", "w")
        F.write("NameRepeat"+","+"Category"+","+"NbRepeat"+"\n")
        for i in DRepeat.keys():
                F.write(i+","+"Gene"+","+str(DRepeat[i][0])+"\n")
                F.write(i+","+"DeNovoGene"+","+str(DRepeat[i][1])+"\n")
        F.close()
        F = open("Data_Disordered", "w")
        F.write("NameDisordered"+","+"Category"+","+"NbDisordered"+"\n")
        for i in DDisordered.keys():
                F.write(i+","+"Gene"+","+str(DDisordered[i][0])+"\n")
                F.write(i+","+"DeNovoGene"+","+str(DDisordered[i][1])+"\n")
        F.close()
        F = open("Data_CoiledCoil", "w")
        F.write("NameCoiledCoil"+","+"Category"+","+"NbCoiledCoil"+"\n")
        for i in DCoiledCoil.keys():
                F.write(i+","+"Gene"+","+str(DCoiledCoil[i][0])+"\n")
                F.write(i+","+"DeNovoGene"+","+str(DCoiledCoil[i][1])+"\n")
        F.close()








Genes = openFile("HumanGenesProt.fa.pfam")

DeNovoGenes = openFile("DeNovoGenesProt.fa.pfam")

GetFirstDico(Genes, DeNovoGenes)
