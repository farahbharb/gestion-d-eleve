from PyQt5.uic import *
from PyQt5.QtWidgets  import*
from numpy import array
app=QApplication([]) 
w=loadUi("note.ui")
w.show()
#btaff
def affichier():
    nph="note.txt"  
    f=open(nph,"a")
    f.close()
    f=open(nph,"r")
    w.aff.clear()
    ch=f.readline()
    while ch!="":
        w.aff.addItem(ch[:len(ch)-1])
        ch=f.readline()
    f.close()
#btajo
def ajouter():
    nph="note.txt"
    pre=w.pre.text()
    nom=w.nom.text()
    dc1=w.dc1.text()
    dc2=w.dc2.text()
    ds=w.ds.text()
    if not(len(pre)==0 or len(nom)==0) and dc1.isdecimal() and dc2.isdecimal() and ds.isdecimal():
        #cherche de l'eleve si il est dans la liste
        f=open(nph,"r")
        t=True
        ch=f.readline()
        chpre=ch[:ch.find(" ")]
        ch=ch[ch.find(" ")+1:]
        chnom=ch[:ch.find(" ")]
        while ch!="" and t:
            if chpre==pre and chnom==nom:
                t=False
            else:
                ch=f.readline()
                chpre=ch[:ch.find(" ")]
                ch=ch[ch.find(" ")+1:]
                chnom=ch[:ch.find(" ")]
        f.close()
        #
        if t:
            f=open(nph,"a")
            moy=(float(dc1)+float(dc2)+float(ds)*2)/4
            f.write(pre+" "+nom+" "+str(moy)+"\n")
            w.pre.clear()
            w.nom.clear()
            w.dc1.clear()
            w.dc2.clear()
            w.ds.clear()
            w.aff.addItem(pre+" "+nom+" "+str(moy))
            f.close()
        else:
            QMessageBox.critical(w,"attention","cette eleve est deja dans la liste \n si vous voulliez modifier les donnees cliquer sur boutton modifier")
    else:
        QMessageBox.critical(w,"erreur","verifier de votre donnner")
#btmodi
def modifier():
    nph="note.txt"
    pre=w.pre.text()
    nom=w.nom.text()
    dc1=w.dc1.text()
    dc2=w.dc2.text()
    ds=w.ds.text()
    t=array([dict()]*100)
    n=remplirt(nph,t)
    for i in range(n):
        if pre==t[i]["pre"] and nom==t[i]["nom"]:
            t[i]["moy"]=(float(dc1)+float(dc2)+float(ds)*2)/4
    remplirf(nph,t,n)
    f=open(nph,"r")
    w.aff.clear()
    ch=f.readline()
    while ch!="":
        w.aff.addItem(ch[:len(ch)-1])
        ch=f.readline()
    f.close()
        
#btsupp
def supprimer():
    nph="note.txt"
    pre=w.pre.text()
    nom=w.nom.text()
    dc1=w.dc1.text()
    dc2=w.dc2.text()
    ds=w.ds.text()
    t=array([dict()]*100)
    n=remplirt(nph,t)
    for i in range(n):
        if pre==t[i]["pre"] and nom==t[i]["nom"]:
            t[i]["pre"]=""
            t[i]["nom"]=""
            t[i]["moy"]=""
    f=open(nph,"w")
    for i in range(n):
        if not(t[i]["pre"]=="" and t[i]["nom"]==""):
            ch=t[i]["pre"]+" "+t[i]["nom"]+" "+str(t[i]["moy"])
            f.write(ch+"\n")
    f.close()
    f=open(nph,"r")
    w.aff.clear()
    ch=f.readline()
    while ch!="":
        w.aff.addItem(ch[:len(ch)-1])
        ch=f.readline()
    f.close()
#bttri
def trie():
    if w.btnc.isChecked()==w.btndc.isChecked():
        QMessageBox.critical(w,"erreur","choisir un trie  croi ou decroi")
    else:
        nph="note.txt"  
        t=array([dict()]*100)
        n=remplirt(nph,t)
        if w.btnc.isChecked():
            triec(t,n)
        else:
            triedc(t,n)
        remplirf(nph,t,n)
        f=open(nph,"r")
        w.aff.clear()
        ch=f.readline()
        ch=ch[:len(ch)-1]
        while ch!="":
            w.aff.addItem(ch)
            ch=f.readline()
            ch=ch[:len(ch)-1]
        f.close()
    
#remplir fichier
def remplirf(nph,t,n):
    f=open(nph,"w")
    for i in range(n):
        ch=t[i]["pre"]+" "+t[i]["nom"]+" "+str(t[i]["moy"])
        f.write(ch+"\n")
    f.close()
#remplir le tableau
def remplirt(nph,t):
    f=open(nph,"r")
    i=0
    ch=f.readline()
    while ch!="":
        t[i]=dict()
        t[i]["pre"]=ch[:ch.find(" ")]
        ch=ch[ch.find(" ")+1:]
        t[i]["nom"]=ch[:ch.find(" ")]
        ch=ch[ch.find(" ")+1:]
        t[i]["moy"]=ch[:ch.find(" ")]
        ch=ch[ch.find(" ")+1:]
        i=i+1
        ch=f.readline()
    f.close()
    return i

#trie
def triec(t,n):
    for i in range(n-1):
        p=i
        for j in range(i+1,n):
            if float(t[j]["moy"])<=float(t[p]["moy"]):
                p=j
        if p!=i:
            aux=t[i]
            t[i]=t[p]
            t[p]=aux
        
def triedc(t,n):
    for i in range(n-1):
        p=i
        for j in range(i+1,n):
            if float(t[j]["moy"])>=float(t[p]["moy"]):
                p=j
        if p!=i:
            aux=t[i]
            t[i]=t[p]
            t[p]=aux
        
    
    
    
    
w.btnaff.clicked.connect(affichier)
w.btnaj.clicked.connect(ajouter)
w.btnmod.clicked.connect(modifier)
w.btnsup.clicked.connect(supprimer)
w.btntrie.clicked.connect(trie)
app.exec_()



