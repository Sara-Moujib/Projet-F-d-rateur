import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from time import strftime
from datetime import datetime


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
            chatBoxQuotidien.insert(END, "Bot: " + res + '\n\n')
            chatBoxQuotidien.config(state=DISABLED)
            chatBoxQuotidien.yview(END)
        else:
            messagebox.showerror("Message d'erreur","vous ne pouvez pas envoyer un empty message") 
       
    rootQuotidien = Tk()
    rootQuotidien.title("Suivi Quotidien")
    rootQuotidien.iconbitmap("C:/Users/ERRAKI-OTMAN/Downloads/ENSIAS-tr.ico")
    rootQuotidien.geometry("400x500")
    rootQuotidien.resizable(width=FALSE, height=FALSE)
    chatBoxQuotidien = Text(rootQuotidien, bd=0, bg="white", height="8", width="50", font="Arial")

    chatBoxQuotidien.config(state=DISABLED)
    sendQuotidienButton = Button(rootQuotidien, font=("Verdana",12,'bold'), text="send", width="12", height=5,
                    bd=0, bg="green", activebackground="#3c9d9b",fg='#ffffff',
                    command= sendQuotidien )
    EntryBoxQuotidien = Text(rootQuotidien, bd=0, bg="white",width="29", height="5", font="Arial")

    chatBoxQuotidien.place(x=6,y=6, height=386, width=370)
    EntryBoxQuotidien.place(x=128, y=401, height=40, width=265)
    sendQuotidienButton.place(x=6, y=401, height=40)

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
        
            chatBoxUrgence.insert(END, "Aida: " + res + '\n\n')
            chatBoxUrgence.config(state=DISABLED)
            chatBoxUrgence.yview(END)
            
        else:
             messagebox.showerror("Message d'erreur","vous ne pouvez pas envoyer un empty message")   
 
    
    rootUrgence = Tk()
    rootUrgence.title("Cas d'urgence: appelez le 150")
    rootUrgence.iconbitmap("C:/Users/ERRAKI-OTMAN/Downloads/ENSIAS-tr.ico")
    rootUrgence.geometry("400x500")
    rootUrgence.resizable(width=FALSE, height=FALSE)
    chatBoxUrgence = Text(rootUrgence, bd=0, bg="white", height="8", width="50", font="Arial")
    chatBoxUrgence.config(state=DISABLED)
    sendUrgence = Button(rootUrgence, font=("Verdana",12,'bold'), text="send", width="12", height=5,
                    bd=0, bg="red", activebackground="#3c9d9b",fg='#ffffff',
                    command= sendUrgence)
    EntryBoxUrgence = Text(rootUrgence, bd=0, bg="white",width="29", height="5", font="Arial")
    chatBoxUrgence.place(x=6,y=6, height=386, width=370)
    EntryBoxUrgence.place(x=128, y=401, height=40, width=265)
    sendUrgence.place(x=6, y=401, height=40)
    

    

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
        
            chatBoxQuestion.insert(END, "Aida: " + res + '\n\n')
            chatBoxQuestion.config(state=DISABLED)
            chatBoxQuestion.yview(END)
            
        else:
             messagebox.showerror("Message d'erreur","vous ne pouvez pas envoyer un empty message")   
 
    
    rootQuestion = Tk()
    rootQuestion.title("Questions Générales")
    rootQuestion.iconbitmap("C:/Users/ERRAKI-OTMAN/Downloads/ENSIAS-tr.ico")
    rootQuestion.geometry("400x500")
    rootQuestion.resizable(width=FALSE, height=FALSE)
    chatBoxQuestion = Text(rootQuestion, bd=0, bg="white", height="8", width="50", font="Arial")
    chatBoxQuestion.config(state=DISABLED)
    sendQuestionButton = Button(rootQuestion, font=("Verdana",12,'bold'), text="send", width="12", height=5,
                    bd=0, bg="blue", activebackground="#3c9d9b",fg='#ffffff',
                    command= sendQuestion)
    EntryBoxQuestion = Text(rootQuestion, bd=0, bg="white",width="29", height="5", font="Arial")
    chatBoxQuestion.place(x=6,y=6, height=386, width=370)
    EntryBoxQuestion.place(x=128, y=401, height=40, width=265)
    sendQuestionButton.place(x=6, y=401, height=40)


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
            res = trainPeriodique.getResponse(ints, intents)
            ChatBox.insert(END, "Aida: " + res + '\n\n')
            ChatBox.config(state=DISABLED)
            ChatBox.yview(END)
        else:
         
            messagebox.showerror("Message d'erreur","vous ne pouvez pas envoyer un empty message")   
 
    
    rootPeriodique = Tk()
    rootPeriodique.title("Suivi Périodique")
    rootPeriodique.iconbitmap("C:/Users/ERRAKI-OTMAN/Downloads/ENSIAS-tr.ico")
    rootPeriodique.geometry("400x500")
    rootPeriodique.resizable(width=FALSE, height=FALSE)
    ChatBox = Text(rootPeriodique, bd=0, bg="white", height="8", width="50", font="Arial")
    ChatBox.config(state=DISABLED)
    sendPeriodiqueButton = Button(rootPeriodique, font=("Verdana",12,'bold'), text="send", width="12", height=5,
                    bd=0, bg="violet", activebackground="#3c9d9b",fg='#ffffff',
                    command= sendPeriodique )
    EntryBoxPeriodique = Text(rootPeriodique, bd=0, bg="white",width="29", height="5", font="Arial")
    ChatBox.place(x=6,y=6, height=386, width=370)
    EntryBoxPeriodique.place(x=128, y=401, height=40, width=265)
    sendPeriodiqueButton.place(x=6, y=401, height=40) 

    
#########################################################################################"
boolm=True
def protectEye():
    global boolm
  
    if(boolm):
        ChatBox.config(bg="black")
        Disclaimer.config(bg="black")
        Disclaimer.config(foreground="white")
        
        
        boolm=False
    else:    
        ChatBox.config(bg="white")
        Disclaimer.config(bg="white")
        Disclaimer.config(foreground="black")
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
Espace=Label(ChatBox,text="",background="white").grid(row=0,column=0)
#Espace=Label(ChatBox,text="       ",background="white").grid(row=1,column=0)

Espace=Label(ChatBox,text="",background="white").grid(row=1,column=1)

Urgence=Button(ChatBox, font=("Verdana",12,'bold'), text=" Cas Urgence", width="13", height=5,
                    bd=0, bg="red", activebackground="#3c9d9b",fg='#ffffff',command=openUrgence ).grid(row=2,column=0,columnspan=2,padx=10)
#Espace=Label(ChatBox,background="white").grid(row=2,column=3)                  
Quotidien=Button(ChatBox, font=("Verdana",12,'bold'), text="Suivi Quotidien ", width="14", height=5,
                    bd=0, bg="green", activebackground="#3c9d9b",fg='#ffffff',command=openQuotidien ).grid(row=2,column=4,columnspan=2,rowspan=2)
#Espace=Label(ChatBox,text="",background="white").grid(row=2,column=7)
Espace=Label(ChatBox,background="white").grid(row=5,column=2)                   
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