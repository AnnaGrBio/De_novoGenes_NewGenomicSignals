import os
os.chdir("Folder")
import random

def openFile(NameFile):
    F=open(NameFile, "r")
    L=F.readlines()
    return L  



def MakeNewFile(File):
	F = open("NcRNAstandardised.fa", "w")
	Name = ""
	Seq = ""
	for i in File:
		if i[0] == ">":
			if Name != "":
				if len(Seq)<=1000:
					F.write(Name)
					F.write(Seq+"\n")
			Name = i
			Seq = ""
		else:
			ligne = i.split("\n")[0]
			Seq+=ligne
	if len(Seq)<=1000:
		F.write(Name)
		F.write(Seq)
	F.close()



NewFile = openFile("Homo_sapiens.GRCh38.ncrna.fa")
MakeNewFile(NewFile)
