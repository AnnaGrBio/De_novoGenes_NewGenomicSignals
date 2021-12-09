import cv2
import os
os.chdir("Folder
    ")
import random
from Bio import SeqIO
import random
#from random import *


def openFile(NameFile):
    F=open(NameFile, "r")
    L=F.readlines()
    return L  




def GetSequences(File):
	Dico = {}
	it = SeqIO.parse(File, 'fasta')
	while True:
    		try:
        		seqRecord = next(it)
        		Name = seqRecord.id
			#print(len(seqRecord.seq))
			lala = seqRecord.seq
			S = ""
			for i in lala:
				S+=i
			Dico[Name] = S
    		except StopIteration:
        		break
	return Dico



def RetrieveNbPositions(File):
	D = {}
	for i in File:
		ligne = i.split("\n")
		All = ligne[0].split()
		#print len(All)
		D[All[0]] = []
		for i in All[1:]:
			D[All[0]].append(int(i))
		#print len(D[All[0]])
	return D

def Choisir(Seq, Size):
	Debut = random.randint(0, len(Seq)-Size)
	Fin = Debut+Size
	SeqFinal = Seq[Debut:Fin]
	#print Debut
	#print Fin
	#print len(Seq)
	#print len(SeqFinal)
	return SeqFinal



def MakeRandom(DicoSeq,DicoDeNovo, NomChrom, ListeTaille):
	Nb = len(ListeTaille)
	print Nb
	ListeNoms = []
	for i in DicoSeq.keys():
		ListeNoms.append(i)
	Compteur = 0
	ListeSequences = []
	while Nb>0:
		Taille = 200
		#print Taille
		C = True
		while C == True:
			NameSeq = random.choice(ListeNoms)
			ligne = NameSeq.split("_")
			Beg = int(ligne[3])
			End = int(ligne[4])
			LongueSeq = DicoSeq[NameSeq]
			#print len(LongueSeq)
			if len(LongueSeq)>Taille and "N" not in LongueSeq:
				DeNovoInside = False
				for i in DicoDeNovo[NomChrom]:
					Deb = int(i[0])
					Fin = int(i[1])
					if Fin>=Beg and Fin<=End:
						DeNovoInside = True
						#print (str(Deb)+" "+str(Fin)+" "+str(Beg)+" "+str(End))
						break
					elif Deb>=Beg and Deb<=End:
						DeNovoInside = True
						break
					elif Deb>=Beg and Fin<=End:
						DeNovoInside = True
						break
				if DeNovoInside == False:
					C =False
		PetiteSeq = Choisir(LongueSeq, Taille)
		ListeSequences.append(PetiteSeq)
		Compteur +=1
		Nb-=1
	print len(ListeSequences)
	print ListeSequences
	return ListeSequences



def MakeFile(DicoChrom,DicoDeNovo, DicoC1, DicoC2, DicoC3, DicoC4,DicoC5, DicoC6, DicoC7, DicoC8, DicoC9, DicoC10, DicoC11, DicoC12, DicoC13, DicoC14, DicoC15, DicoC16, DicoC17, DicoC18, DicoC19, DicoC20, DicoC21, DicoC22, DicoCX, DicoCY):
	DicoFinal = {}
	F = open("Intron200Random.fa", "w")
	for i in DicoChrom.keys():
		if i == "chr1":
			print "Chr1"
			ListeTaille = DicoChrom[i]
			SeqsC1 = MakeRandom(DicoC1, DicoDeNovo,"chr1",  ListeTaille)
			c = 0
			for j in SeqsC1:
				#print i
				F.write(">chr1_"+str(c)+"\n")
				F.write(j+"\n")
				c+=1
		elif i == "chr2":
			print "Chr2"
                        ListeTaille = DicoChrom[i]
                        SeqsC2 = MakeRandom(DicoC2, DicoDeNovo,"chr2",  ListeTaille)
                        c = 0
                        for j in SeqsC2:
                                #print i
                                F.write(">chr2_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1
		elif i == "chr3":
			print "Chr3"
                        ListeTaille = DicoChrom[i]
                        SeqsC3 = MakeRandom(DicoC3, DicoDeNovo,"chr3",  ListeTaille)
                        c = 0
                        for j in SeqsC3:
                                #print i
                                F.write(">chr3_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1
		elif i == "chr4":
                        ListeTaille = DicoChrom[i]
                        SeqsC4 = MakeRandom(DicoC4, DicoDeNovo,"chr4",  ListeTaille)
                        c = 0
                        for j in SeqsC4:
                                #print i
                                F.write(">chr4_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1
		elif i == "chr5":
                        ListeTaille = DicoChrom[i]
                        SeqsC5 = MakeRandom(DicoC5, DicoDeNovo,"chr5",  ListeTaille)
                        c = 0
                        for j in SeqsC5:
                                #print i
                                F.write(">chr5_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1				
		elif i == "chr6":
                        ListeTaille = DicoChrom[i]
                        SeqsC6 = MakeRandom(DicoC6, DicoDeNovo,"chr6",  ListeTaille)
                        c = 0
                        for j in SeqsC6:
                                #print i
                                F.write(">chr6_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1				
		elif i == "chr7":
                        ListeTaille = DicoChrom[i]
                        SeqsC7 = MakeRandom(DicoC7, DicoDeNovo,"chr7",  ListeTaille)
                        c = 0
                        for j in SeqsC7:
                                #print i
                                F.write(">chr7_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1				
		elif i == "chr8":
                        ListeTaille = DicoChrom[i]
                        SeqsC8 = MakeRandom(DicoC8, DicoDeNovo,"chr8",  ListeTaille)
                        c = 0
                        for j in SeqsC8:
                                #print i
                                F.write(">chr8_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1				
		elif i == "chr9":
                        ListeTaille = DicoChrom[i]
                        SeqsC9 = MakeRandom(DicoC9, DicoDeNovo,"chr9",  ListeTaille)
                        c = 0
                        for j in SeqsC9:
                                #print i
                                F.write(">chr9_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1				
		elif i == "chr10":
                        ListeTaille = DicoChrom[i]
                        SeqsC10 = MakeRandom(DicoC10, DicoDeNovo,"chr10",  ListeTaille)
                        c = 0
                        for j in SeqsC10:
                                #print i
                                F.write(">chr10_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1				
		elif i == "chr11":
                        ListeTaille = DicoChrom[i]
                        SeqsC11 = MakeRandom(DicoC11, DicoDeNovo,"chr11",  ListeTaille)
                        c = 0
                        for j in SeqsC11:
                                #print i
                                F.write(">chr11_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1				
		elif i == "chr12":
                        ListeTaille = DicoChrom[i]
                        SeqsC12 = MakeRandom(DicoC12, DicoDeNovo,"chr12",  ListeTaille)
                        c = 0
                        for j in SeqsC12:
                                #print i
                                F.write(">chr12_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1				
		elif i == "chr13":
                        ListeTaille = DicoChrom[i]
                        SeqsC13 = MakeRandom(DicoC13, DicoDeNovo,"chr13",  ListeTaille)
                        c = 0
                        for j in SeqsC13:
                                #print i
                                F.write(">chr13_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1				
		elif i == "chr14":
                        ListeTaille = DicoChrom[i]
                        SeqsC14 = MakeRandom(DicoC14, DicoDeNovo,"chr14",  ListeTaille)
                        c = 0
                        for j in SeqsC14:
                                #print i
                                F.write(">chr14_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1				
		elif i == "chr15":
                        ListeTaille = DicoChrom[i]
                        SeqsC15 = MakeRandom(DicoC15, DicoDeNovo,"chr15",  ListeTaille)
                        c = 0
                        for j in SeqsC15:
                                #print i
                                F.write(">chr15_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1
		elif i == "chr16":
                        ListeTaille = DicoChrom[i]
                        SeqsC16 = MakeRandom(DicoC16, DicoDeNovo,"chr16",  ListeTaille)
                        c = 0
                        for j in SeqsC16:
                                #print i
                                F.write(">chr16_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1
		elif i == "chr17":
                        ListeTaille = DicoChrom[i]
                        SeqsC17 = MakeRandom(DicoC17, DicoDeNovo,"chr17",  ListeTaille)
                        c = 0
                        for j in SeqsC17:
                                #print i
                                F.write(">chr17_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1				
		elif i == "chr18":
                        ListeTaille = DicoChrom[i]
                        SeqsC18 = MakeRandom(DicoC18, DicoDeNovo,"chr18",  ListeTaille)
                        c = 0
                        for j in SeqsC18:
                                #print i
                                F.write(">chr18_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1				
		elif i == "chr19":
                        ListeTaille = DicoChrom[i]
                        SeqsC19 = MakeRandom(DicoC19, DicoDeNovo,"chr19",  ListeTaille)
                        c = 0
                        for j in SeqsC19:
                                #print i
                                F.write(">chr19_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1				
		elif i == "chr20":
                        ListeTaille = DicoChrom[i]
                        SeqsC20 = MakeRandom(DicoC20, DicoDeNovo,"chr20",  ListeTaille)
                        c = 0
                        for j in SeqsC20:
                                #print i
                                F.write(">chr20_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1				
		elif i == "chr21":
                        ListeTaille = DicoChrom[i]
                        SeqsC21 = MakeRandom(DicoC21, DicoDeNovo,"chr21",  ListeTaille)
                        c = 0
                        for j in SeqsC21:
                                #print i
                                F.write(">chr21_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1				
		elif i == "chr22":
                        ListeTaille = DicoChrom[i]
                        SeqsC22 = MakeRandom(DicoC22, DicoDeNovo,"chr22",  ListeTaille)
                        c = 0
                        for j in SeqsC22:
                                #print i
                                F.write(">chr22_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1				
		elif i == "chrX":
                        ListeTaille = DicoChrom[i]
                        SeqsCX = MakeRandom(DicoCX, DicoDeNovo,"chrX",  ListeTaille)
                        c = 0
                        for j in SeqsCX:
                                #print i
                                F.write(">chrX_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1				
		elif i == "chrY":
                        ListeTaille = DicoChrom[i]
                        SeqsCY = MakeRandom(DicoCY, DicoDeNovo,"chrY",  ListeTaille)
                        c = 0
                        for j in SeqsCY:
                                #print i
                                F.write(">chrY_"+str(c)+"\n")
                                F.write(j+"\n")
				c+=1				
	F.close()				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
def MakeDicoCorre(File):
	Dico = {}
	for i in File:
		ligne = i.split(",")
		Chrom = ligne[1][1:len(ligne[1])-1]
		Begin = int(ligne[2])
		End = int(ligne[3])
		Liste = [Begin, End]
		if Chrom not in Dico.keys():
			Dico[Chrom] = []
		Dico[Chrom].append(Liste)
	return Dico





Corres = openFile("CorrespondanceFinal2")
DicoDeNovoPos = MakeDicoCorre(Corres)
PosFile = openFile("DeNovo_Special_Size_Chrom")
DAllPos = RetrieveNbPositions(PosFile)
DicoC1 = GetSequences("Intron_chr1")
DicoC2 = GetSequences("Intron_chr2")
DicoC3 = GetSequences("Intron_chr3")
DicoC4 = GetSequences("Intron_chr4")
DicoC5 = GetSequences("Intron_chr5")
DicoC6 = GetSequences("Intron_chr6")
DicoC7 = GetSequences("Intron_chr7")
DicoC8 = GetSequences("Intron_chr8")
DicoC9 = GetSequences("Intron_chr9")
DicoC10 = GetSequences("Intron_chr10")
DicoC11= GetSequences("Intron_chr11")
DicoC12 = GetSequences("Intron_chr12")
DicoC13 = GetSequences("Intron_chr13")
DicoC14 = GetSequences("Intron_chr14")
DicoC15 = GetSequences("Intron_chr15")
DicoC16 = GetSequences("Intron_chr16")
DicoC17 = GetSequences("Intron_chr17")
DicoC18 = GetSequences("Intron_chr18")
DicoC19 = GetSequences("Intron_chr19")
DicoC20 = GetSequences("Intron_chr20")
DicoC21 = GetSequences("Intron_chr21")
DicoC22 = GetSequences("Intron_chr22")
DicoCX = GetSequences("Intron_chrX")
DicoCY = GetSequences("Intron_chrY")

print "Beginning"
MakeFile(DAllPos,DicoDeNovoPos, DicoC1, DicoC2, DicoC3, DicoC4, DicoC5, DicoC6, DicoC7, DicoC8, DicoC9, DicoC10, DicoC11, DicoC12, DicoC13, DicoC14, DicoC15, DicoC16, DicoC17, DicoC18,DicoC19, DicoC20, DicoC21, DicoC22, DicoCX, DicoCY)






















