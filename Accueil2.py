import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from time import strftime
from datetime import datetime
from unidecode import unidecode

import json
import pickle
from nltk.stem import WordNetLemmatizer
import numpy as np
import tensorflow
from keras.models import load_model
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
import QuestionGenerale.chatbot as chatQuestion
import QuestionGenerale.train_chatbot as trainQuestion
 

import CasUrgence.chatbot as chatUrgence
import CasUrgence.train_chatbot as trainUrgence

import SuiviPeriodique.chatbot as chatPeriodique
import SuiviPeriodique.train_chatbot as trainPeriodique


import SuiviQuotidien.chatbot as chatQuotidien
import SuiviQuotidien.train_chatbot as trainQuotidien


###########################################################################################
#                   Définition des fonctions des nouvelles fenêtres                       #
###########################################################################################




##########################################################################################

def openQuotidien():
    #lemmatizer = WordNetLemmatizer()
    trainQuotidien.trainChatBot()
    intents = json.loads(open('SuiviQuotidien/intents.json').read())
   
    
    def sendQuotidien():
        msg = EntryBoxQuotidien.get("1.0",'end-1c').strip()
        EntryBoxQuotidien.delete("0.0",END)

        if msg != '':
            chatBoxQuotidien.config(state=NORMAL)
            chatBoxQuotidien.insert(END, "Vous: " + msg + '\n\n')
            chatBoxQuotidien.config(foreground="#446665", font=("Verdana", 12 ))
            ints =chatQuotidien.predict_class(msg)
            res = chatQuotidien.getResponse(ints, intents)
            chatBoxQuotidien.insert(END, "Aida: " + unidecode(res) + '\n')
            timing=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            chatBoxQuotidien.insert(END, timing + '\n\n')
            chatBoxQuotidien.config(state=DISABLED)
            chatBoxQuotidien.yview(END)
        else:
            messagebox.showerror("Message d'erreur","vous ne pouvez pas envoyer un empty message") 
    trainQuotidien.trainChatBot()   
    rootQuotidien = Tk()
    rootQuotidien.title("Suivi Quotidien")
    rootQuotidien.iconbitmap("C:/Users/ERRAKI-OTMAN/Downloads/ENSIAS-tr.ico")
    rootQuotidien.geometry("400x500")
    rootQuotidien.resizable(width=FALSE, height=FALSE)
    scrollbar = Scrollbar(rootQuotidien)
    if(boolm):
        chatBoxQuotidien = Text(rootQuotidien, bd=0, bg="white", height="8", width="50", font="Arial",yscrollcommand = scrollbar.set)
        chatBoxQuotidien.config(foreground="black")
        rootQuotidien.config(bg="white")
    else:
        chatBoxQuotidien = Text(rootQuotidien, bd=0, bg="black", height="8", width="50", font="Arial",yscrollcommand = scrollbar.set)
        chatBoxQuotidien.config(foreground="white")
        rootQuotidien.config(bg="black")
    

    chatBoxQuotidien.config(state=DISABLED)
    sendQuotidienButton = Button(rootQuotidien, font=("Verdana",12,'bold'), text="send", width="12", height=5,
                    bd=0, bg="green", activebackground="#3c9d9b",fg='#ffffff',
                    command= sendQuotidien )
    EntryBoxQuotidien = Text(rootQuotidien, bd=0, bg="white",width="29", height="5", font="Arial")

    chatBoxQuotidien.place(x=6,y=6, height=386, width=370)
    EntryBoxQuotidien.place(x=128, y=401, height=40, width=250)
    sendQuotidienButton.place(x=6, y=401, height=40)
    scrollbar.config(command = chatBoxQuotidien.yview )
    scrollbar.place(x=376,y=6, height=386)
    chatBoxQuotidien.config(state=NORMAL)
    chatBoxQuotidien.insert(END, "Aida: " + "Bonjour, nous allons faire notre suivi quotidien" + '\n\n')
    chatBoxQuotidien.config(state=DISABLED)

##################################################################################################################

def openUrgence():
    
    intents = json.loads(open('CasUrgence/intents.json').read())
    
    trainUrgence.trainChatBot()
    def sendUrgence():
       
        msg = EntryBoxUrgence.get("1.0",'end-1c').strip()
        EntryBoxUrgence.delete("0.0",END)
        if msg != '':
            chatBoxUrgence.config(state=NORMAL)
            chatBoxUrgence.insert(END, "Vous: " + msg + '\n\n')
            chatBoxUrgence.config(foreground="#446665", font=("Verdana", 12 ))
    
            ints =chatUrgence.predict_class(msg)
            res = chatUrgence.getResponse(ints, intents)
        
            chatBoxUrgence.insert(END, "Aida: " + res.enocode("utf-8") + '\n')
            timing=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            chatBoxUrgence.insert(END, timing + '\n\n')
            chatBoxUrgence.config(state=DISABLED)
            chatBoxUrgence.yview(END)
            
        else:
             messagebox.showerror("Message d'erreur","vous ne pouvez pas envoyer un empty message")   
 
    
    rootUrgence = Tk()
    rootUrgence.title("Cas d'urgence: appelez le 150")
    rootUrgence.iconbitmap("C:/Users/ERRAKI-OTMAN/Downloads/ENSIAS-tr.ico")
    rootUrgence.geometry("400x500")
    rootUrgence.resizable(width=FALSE, height=FALSE)
    scrollbar = Scrollbar(rootUrgence)
    if(boolm):
        chatBoxUrgence = Text(rootUrgence, bd=0, bg="white", height="8", width="50", font="Arial",yscrollcommand = scrollbar.set)
        
        chatBoxUrgence.config(foreground="black")
        rootUrgence.config(bg="white")
    else:
         chatBoxUrgence = Text(rootUrgence, bd=0, bg="black", height="8", width="50", font="Arial",yscrollcommand = scrollbar.set)
         chatBoxUrgence.config(foreground="white")
         rootUrgence.config(bg="black")
    
    chatBoxUrgence.config(state=DISABLED)
    sendUrgence = Button(rootUrgence, font=("Verdana",12,'bold'), text="send", width="12", height=5,
                    bd=0, bg="red", activebackground="#3c9d9b",fg='#ffffff',
                    command= sendUrgence)
    EntryBoxUrgence = Text(rootUrgence, bd=0, bg="white",width="29", height="5", font="Arial")
    chatBoxUrgence.place(x=6,y=6, height=386, width=370)
    EntryBoxUrgence.place(x=128, y=401, height=40, width=250)
    sendUrgence.place(x=6, y=401, height=40)
    scrollbar.config(command = chatBoxUrgence.yview )
    scrollbar.place(x=376,y=6, height=386)
    chatBoxUrgence.config(state=NORMAL)
    chatBoxUrgence.insert(END, "Aida: " + "Bonjour,Quel est votre cas d'urgence? (Appelez le 115)" + '\n\n')
    chatBoxUrgence.config(state=DISABLED)
    

##################################################################################################################""""


def openQuestion():
    
    intents = json.loads(open('QuestionGenerale/intents.json').read())
    trainQuestion.trainChatBot()
    def sendQuestion():
       
        msg = EntryBoxQuestion.get("1.0",'end-1c').strip()
        EntryBoxQuestion.delete("0.0",END)
        if msg != '':
            chatBoxQuestion.config(state=NORMAL)
            chatBoxQuestion.insert(END, "Vous: " + msg + '\n\n')
            chatBoxQuestion.config(foreground="#446665", font=("Verdana", 12 ))
    
            ints =chatQuestion.predict_class(msg)
            res = chatQuestion.getResponse(ints, intents)
        
            chatBoxQuestion.insert(END, "Aida: " + res + '\n')
            timing=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            chatBoxQuestion.insert(END, timing + '\n\n')
            chatBoxQuestion.config(state=DISABLED)
            chatBoxQuestion.yview(END)
            
        else:
             messagebox.showerror("Message d'erreur","vous ne pouvez pas envoyer un empty message")   
 
    
    rootQuestion = Tk()
    rootQuestion.title("Questions Générales")
    rootQuestion.iconbitmap("C:/Users/ERRAKI-OTMAN/Downloads/ENSIAS-tr.ico")
    rootQuestion.geometry("400x500")
    rootQuestion.resizable(width=FALSE, height=FALSE)
    scrollbar = Scrollbar(rootQuestion)
    if(boolm):
        chatBoxQuestion = Text(rootQuestion, bd=0, bg="white", height="8", width="50", font="Arial",yscrollcommand = scrollbar.set)
        chatBoxQuestion.config(foreground="black")
        rootQuestion.config(bg="white")
    else:
         chatBoxQuestion = Text(rootQuestion, bd=0, bg="black", height="8", width="50", font="Arial",yscrollcommand = scrollbar.set)
         chatBoxQuestion.config(foreground="white")
         rootQuestion.config(bg="black")
    
    chatBoxQuestion.config(state=DISABLED)
    sendQuestionButton = Button(rootQuestion, font=("Verdana",12,'bold'), text="send", width="12", height=5,
                    bd=0, bg="blue", activebackground="#3c9d9b",fg='#ffffff',
                    command= sendQuestion)
    EntryBoxQuestion = Text(rootQuestion, bd=0, bg="white",width="29", height="5", font="Arial")
    chatBoxQuestion.place(x=6,y=6, height=386, width=370)
    EntryBoxQuestion.place(x=128, y=401, height=40, width=250)
    sendQuestionButton.place(x=6, y=401, height=40)
    
    
    scrollbar.config(command = chatBoxQuestion.yview )
    scrollbar.place(x=376,y=6, height=386)
    chatBoxQuestion.config(state=NORMAL)
    chatBoxQuestion.insert(END, "Aida: " + "Bonjour,Quelle est votre question?" + '\n\n')
    chatBoxQuestion.config(state=DISABLED)
###############################################################################################
def openPeriodique():
    
    
    trainPeriodique.trainChatBot()
    def sendPeriodique():
        
    
        msg = EntryBoxPeriodique.get("1.0",'end-1c').strip()
        EntryBoxPeriodique.delete("0.0",END)
   

        if msg != '':
            ChatBox.config(state=NORMAL)
            ChatBox.insert(END, "Vous: " + msg + '\n\n')
            ChatBox.config(foreground="#446665", font=("Verdana", 12 ))
    
            ints =chatPeriodique.predict_class(msg)
            res = trainPeriodique.getResponse(ints,intents).enocode("utf-8")
            ChatBox.insert(END, "Aida: " + res + '\n')
            timing=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ChatBox.insert(END, timing + '\n\n')
            ChatBox.config(state=DISABLED)
            ChatBox.yview(END)
        else:
         
            messagebox.showerror("Message d'erreur","vous ne pouvez pas envoyer un empty message")   
 
    
    rootPeriodique = Tk()
    rootPeriodique.title("Suivi Périodique")
    rootPeriodique.iconbitmap("C:/Users/ERRAKI-OTMAN/Downloads/ENSIAS-tr.ico")
    rootPeriodique.geometry("400x500")
    rootPeriodique.resizable(width=FALSE, height=FALSE)
    scrollbar = Scrollbar(rootPeriodique)
    if(boolm):
        ChatBox = Text(rootPeriodique, bd=0, bg="white", height="8", width="50", font="Arial")
        ChatBox.config(foreground="black")
        rootPeriodique.config(bg="white")
    else:
         ChatBox = Text(rootPeriodique, bd=0, bg="black", height="8", width="50", font="Arial")
         ChatBox.config(foreground="white")
         rootPeriodique.config(bg="black")
    ChatBox.config(state=DISABLED)
    sendPeriodiqueButton = Button(rootPeriodique, font=("Verdana",12,'bold'), text="send", width="12", height=5,
                    bd=0, bg="violet", activebackground="#3c9d9b",fg='#ffffff',
                    command= sendPeriodique )             
    EntryBoxPeriodique = Text(rootPeriodique, bd=0, bg="white",width="29", height="5", font="Arial")   
    ChatBox.place(x=6,y=6, height=386, width=370)
    EntryBoxPeriodique.place(x=128, y=401, height=40, width=250)
    scrollbar = Scrollbar(rootPeriodique, command=ChatBox.yview, cursor="heart")
    ChatBox['yscrollcommand'] = scrollbar.set
    sendPeriodiqueButton.place(x=6, y=401, height=40) 
    scrollbar.config(command = ChatBox.yview )
    scrollbar.place(x=376,y=6, height=386)
    ChatBox.config(state=NORMAL)
    ChatBox.insert(END, "Aida: " + "Bonjour, nous allons faire notre suivi périodique" + '\n\n')
    ChatBox.config(state=DISABLED)
#########################################################################################"
boolm=True
def protectEye():
    global boolm
  
    if(boolm):
        ChatBox.config(bg="black")
        Disclaimer.config(bg="black")
        Disclaimer.config(foreground="white")
        Espace1.config(background="black")
        Espace2.config(background="black")
        Espace3.config(background="black")
        
        boolm=False
    else:    
        ChatBox.config(bg="white")
        Disclaimer.config(bg="white")
        Disclaimer.config(foreground="black")
        Espace1.config(background="white")
        Espace2.config(background="white")
        Espace3.config(background="white")
        boolm=True


############################################################################################    


   
root = Tk()
root.title("Aida-ChatAida")
root.iconbitmap("C:/Users/ERRAKI-OTMAN/Downloads/ENSIAS-tr.ico")
root.geometry("500x600")
root.resizable(width=FALSE, height=FALSE)

ChatBox = Text(root, bd=0, bg="white", height="8", width="50", font="Arial")

ChatBox.config(state=DISABLED)
ChatBox.place(x=6,y=6, height=580, width=470)

photo =ImageTk.PhotoImage(Image.open("C:/Users/ERRAKI-OTMAN/Downloads/eye-modeNuit.png"))
ButtonNuit=Button(root,image=photo,command=protectEye).pack(side=TOP, anchor=NW,pady=5,padx=5)

timing=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
TimeLabel=Label(root,text=timing,background="violet").pack(side=TOP,anchor=NE)
accueilImage=ImageTk.PhotoImage(Image.open("bienvenue.png"))
ImageLabel=Label(ChatBox,image=accueilImage).grid(row=0,column=3)
#Bienvenue=Label(ChatBox,text="Bienvenue",background="white").grid(row=0,column=3)
Espace1=Label(ChatBox,text="",background="white")
Espace1.grid(row=0,column=0)
#Espace=Label(ChatBox,text="       ",background="white").grid(row=1,column=0)

Espace2=Label(ChatBox,text="",background="white")
Espace2.grid(row=1,column=1)

Urgence=Button(ChatBox, font=("Verdana",12,'bold'), text=" Cas Urgence", width="13", height=5,
                    bd=0, bg="red", activebackground="#3c9d9b",fg='#ffffff',command=openUrgence ).grid(row=2,column=0,columnspan=2,padx=10)
#Espace=Label(ChatBox,background="white").grid(row=2,column=3)                  
Quotidien=Button(ChatBox, font=("Verdana",12,'bold'), text="Suivi Quotidien ", width="14", height=5,
                    bd=0, bg="green", activebackground="#3c9d9b",fg='#ffffff',command=openQuotidien ).grid(row=2,column=4,columnspan=2,rowspan=2)
#Espace=Label(ChatBox,text="",background="white").grid(row=2,column=7)
Espace3=Label(ChatBox,background="white") 
Espace3.grid(row=5,column=2)                  
Periodique=Button(ChatBox, font=("Verdana",12,'bold'), text="Suivi Périodique", width="13", height=5,
                    bd=0, bg="violet", activebackground="#3c9d9b",fg='#ffffff',command=openPeriodique).grid(row=6,column=0,columnspan=2,rowspan=2)
#Espace=Label(ChatBox,text="",background="white").grid(row=6,column=3)
General=Button(ChatBox, font=("Verdana",12,'bold'), text="Question Générale", width="14", height=5,
                    bd=0, bg="blue", activebackground="#3c9d9b",fg='#ffffff',command=openQuestion).grid(row=6,column=4,columnspan=2,rowspan=2)

#Espace=Label(ChatBox,text="",background="white").grid(row=6,column=7)

Disclaimer = Text(ChatBox, bd=0, bg="white", height="8", width="50", font="Arial")


Disclaimer.place(x=6,y=460, height=120, width=470)
Disclaimer.config(state=NORMAL)
            
Disclaimer.insert(END, "     Aida-ChatBot est  un assistant  développé par  des"+'\n' +"élèves  de    l'ENSIAS,  cet   assistant   est dédié   aux"+'\n' +"personnes diabétiques mais Les informations délivrées dans cette  application sont à  caractère institutionnel"+'\n' "et  ne se substituent  en aucun cas à  un avis médical."  '\n\n')
Disclaimer.config(foreground="black", font=("Verdana", 12 ))
Disclaimer.config(state=DISABLED)


#Disclaimer2=Text(ChatBox, bd=0, bg="white", height="8", width="50", font="Arial")
#Disclaimer2.place(x=6,y=460, height=120, width=470)
#Disclaimer2.config(state=NORMAL)
            
#Disclaimer.insert(END, "     Aida-ChatBot est  un assistant  développé par  des"+'\n' +"élèves  de    l'ENSIAS,  cet   assistant   est dédié   aux"+'\n' +"personnes diabétiques mais Les informations délivrées dans cette  application sont à  caractère institutionnel"+'\n' "et  ne se substituent  en aucun cas à  un avis médical."  '\n\n')
#Disclaimer.config(foreground="red", font=("Verdana", 12 ))
# Disclaimer.config(state=DISABLED)

root.mainloop()