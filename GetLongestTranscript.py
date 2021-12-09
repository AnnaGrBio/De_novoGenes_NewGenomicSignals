import cv2
import os
os.chdir("Folder")
import random
from Bio import SeqIO


def GetSequences(File):
        Dico = {}
        it = SeqIO.parse(File, 'fasta')
        while True:
                try:
                        seqRecord = next(it)
                        #print(len(seqRecord.seq))
                        S = ""
                        for i in seqRecord.seq:
                                S +=i
                        #print S
                        Dico[seqRecord.id] = S
                except StopIteration:
                        break
        return Dico

def DicoTranscript(File):
	Dico = {}
	for i in File:
		if i[0] == ">":
			ligne = i.split()
			TranscriptName = ligne[0][1:]
			Haber = ligne[3].split(".")
			Haber2 = Haber[0].split(":")
			GeneName = Haber2[1]
			Dico[TranscriptName] = GeneName
	return Dico

def GetLongest(Liste):
	Taille = 0
	Seq = ""
	for i in Liste:
		if len(i)>Taille:
			Taille = len(i)
			Seq = i
	return Seq


def LongestTranscript(gene, DicoTrans, DicoSeqs):
	ListeSeqs = []
	for i in DicoTrans.keys():
		if DicoTrans[i] == gene:
			Seq = DicoSeqs[i]
			ListeSeqs.append(Seq)
	Seq = GetLongest(ListeSeqs)
	return Seq



def BuildSeqDico(DicoSequences, DicoTranscriptCorres):
	DicoFinal = {}
	ListeGenes = []
	for i in DicoTranscriptCorres.keys():
		Gene = DicoTranscriptCorres[i]
		if Gene not in ListeGenes:
			ListeGenes.append(Gene)
	for i in ListeGenes:
		L = LongestTranscript(i, DicoTranscriptCorres,DicoSequences)
		DicoFinal[i] = L
	return DicoFinal




def openFile(NameFile):
    F=open(NameFile, "r")
    L=F.readlines()
    return L 


def BuildFinalFile(Dico, Name):
	F = open(Name, "w")
	for i in Dico.keys():
		F.write(">"+i+"\n")
		F.write(Dico[i]+"\n")
	F.close()



DicoSeqs = GetSequences("Homo_sapiens.GRCh38.cds.all.fa")
Seq = openFile("Homo_sapiens.GRCh38.cds.all.fa")
DicoCorres = DicoTranscript(Seq)
DicoFinal = BuildSeqDico(DicoSeqs, DicoCorres)
BuildFinalFile(DicoFinal, "GenesLongestTranscripts")


DicoSeqs = GetSequences("Homo_sapiens.GRCh38.ncrna.fa")
Seq = openFile("Homo_sapiens.GRCh38.ncrna.fa")
DicoCorres = DicoTranscript(Seq)
DicoFinal = BuildSeqDico(DicoSeqs, DicoCorres)
BuildFinalFile(DicoFinal, "NcRNALongestTranscripts")








