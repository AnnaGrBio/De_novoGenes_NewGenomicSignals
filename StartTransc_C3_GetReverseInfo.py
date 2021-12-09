import cv2
import os
os.chdir("Folder")
import random
from Bio import SeqIO

def openFile(NameFile):
    F=open(NameFile, "r")
    L=F.readlines()
    return L  


def MakeDicoContigs(F):
	D = {}
	for i in F:
		ligne = i.split("\n")
		Total = ligne[0].split("_")
		D[Total[0]] = int(Total[1])
	return D

def MakeDicoTRanscripts(F):
	D = {}
	for i in F:
		ligne = i.split("\n")
		Total = ligne[0].split(" ")
		#print Total
		Liste = [int(Total[1]), int(Total[2])]
		D[Total[0]] = Liste
	return D


def MakeFinalFileReverse(Dtranscript, Dcontig):
	NewDico = {}
	ListeNegative = []
	for i in Dtranscript.keys():
		ligne = i.split("_")
		Name = ligne[0]
		Present = False
		for j in Dcontig.keys():
			if j == Name:
				SizeContig = Dcontig[j]
				ListeORF = Dtranscript[i]
				DebORF = ListeORF[0]
				EndORF = ListeORF[1]
				R5prime = SizeContig-DebORF
				R3prime = EndORF
				L = [R5prime, R3prime]
				#print L
				#print NewSize
				#print "************"
				NewDico[i]=L
				Present = False
				break
	#print len(NewDico)
	return NewDico


def MakeFinalFileForward(Dtranscript, Dcontig):
        NewDico = {}
        ListeNegative = []
        for i in Dtranscript.keys():
                ligne = i.split("_")
                Name = ligne[0]
                Present = False
                for j in Dcontig.keys():
                        if j == Name:
                                SizeContig = Dcontig[j]
                                ListeORF = Dtranscript[i]
                                DebORF = ListeORF[0]
                                EndORF = ListeORF[1]
                                R5prime = DebORF
                                R3prime = SizeContig-EndORF
                                L = [R5prime, R3prime]
                                #print L
                                NewDico[i]=L
                                Present = False
                                break
	#print len(NewDico)
        return NewDico





def MakeFile(D1, D2):
	F = open("ORF_5_3_prime_size", "w")
	for i in D1.keys():
		F.write(i)
		for j in D1[i]:
			F.write(" "+str(j))
		F.write("\n")
	for i in D2.keys():
                F.write(i)
                for j in D2[i]:
                        F.write(" "+str(j))
                F.write("\n")
	F.close()








ContigSize = openFile("FileContigsSize")
DicoContig = MakeDicoContigs(ContigSize)

TranscriptReverse = openFile("ListeReverse5PrimeSize")
DicoTranscriptsRev = MakeDicoTRanscripts(TranscriptReverse)

DicoReverse = MakeFinalFileReverse(DicoTranscriptsRev, DicoContig)

TranscriptForward = openFile("ListeForward5PrimeSize")
DicoTranscriptsFor = MakeDicoTRanscripts(TranscriptForward)

DicoForward = MakeFinalFileForward(DicoTranscriptsFor, DicoContig)

MakeFile(DicoForward, DicoReverse)
