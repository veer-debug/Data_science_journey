from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API

class NLPApp:
    
    def __init__(self):
        self.dob=Database()
        self.api=API()
        
        
        self.root=Tk()
        self.root.title("Nlp App")
        self.root.iconbitmap(r'C:\Users\theve\OneDrive\Desktop\DATA-S\05_GUI\resorces\logo.ico')
        self.root.geometry('400x520')
        self.root.config(bg="light green")
        self.login_gui()
        
        self.root.mainloop()
        
        
    
    
    def login_gui(self):
        self.clear()
        heading=Label(self.root,text='NLPApp',bg='light green',fg='black')
        heading.pack(pady=20)
        heading.config(font=('verdana',24,'bold'))
        
        labeli=Label(self.root,text="Enter Email")
        labeli.pack(pady=10)
        
        self.email_input=Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=4)

        labeli2=Label(self.root,text="Enter Password")
        labeli2.pack(pady=10)
        
        self.password_input=Entry(self.root,width=50,show="*")
        self.password_input.pack(pady=(5,10),ipady=4)
        
        login_btn=Button(self.root,text="Login",width=30,height=2,command=self.perform_login)
        login_btn.pack(pady=(10,10))
        
        labeli3=Label(self.root,text="Not a member ")
        labeli3.pack(pady=10)
        
        redirect_btn=Button(self.root,text="Register",width=30,height=2,command=self.register_gui)
        redirect_btn.pack(pady=(10,10))
        
        
    def register_gui(self):
        self.clear()
        
        heading=Label(self.root,text='NLPApp',bg='light green',fg='black')
        heading.pack(pady=20)
        heading.config(font=('verdana',24,'bold'))
        
        labeli=Label(self.root,text="Enter Name")
        labeli.pack(pady=10)
        
        self.name_input=Entry(self.root,width=50)
        self.name_input.pack(pady=(5,10),ipady=4)

        labeli2=Label(self.root,text="Enter email")
        labeli2.pack(pady=10)
        
        self.email_input=Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=4)
        
        labeli4=Label(self.root,text="Enter password")
        labeli4.pack(pady=10)
        
        self.password_input=Entry(self.root,width=50,show="*")
        self.password_input.pack(pady=(5,10),ipady=4)
        
        register_btn=Button(self.root,text="Register",width=30,height=2,command=self.perform_register)
        register_btn.pack(pady=(10,10))
        
        labeli3=Label(self.root,text="Alredy a member ")
        labeli3.pack(pady=10)
        
        redirect_btn=Button(self.root,text="Login Now",width=30,height=2,command=self.login_gui)
        redirect_btn.pack(pady=(10,10))
        
        
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
            
    def perform_register(self):
        name=self.name_input.get()
        email=self.email_input.get()
        password=self.password_input.get()
        respons=self.dob.add_data(name,email,password)
        
        if respons:
            messagebox.showinfo('Success',"Registration success")
            
        else:
            messagebox.showerror('Error',"Email alredy exist")
    def perform_login(self):
        email=self.email_input.get()
        password=self.password_input.get()
        
        responce=self.dob.search(email,password)    
        if responce:
            messagebox.showinfo('Success',"Login Succesful")
            self.home_gui()
        else:
            messagebox.showerror('Error',"Envlid User")
    
    
    def home_gui(self):
        self.clear()
        heading=Label(self.root,text='NLPApp',bg='light green',fg='black')
        heading.pack(pady=20)
        heading.config(font=('verdana',24,'bold'))
        
        
        sentiment_btn=Button(self.root,text="Sentiment Analysis",width=30,height=2,command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10,10))
        
        ner_btn=Button(self.root,text="Name Entry Recognition",width=30,height=2,command=self.ner_gui)
        ner_btn.pack(pady=(10,10))
        
        emotion_btn=Button(self.root,text="EmotionPrediction",width=30,height=2,command=self.emotion_gui)
        emotion_btn.pack(pady=(10,10))
        
        logout_btn=Button(self.root,text="Log out",width=30,height=2,command=self.login_gui)
        logout_btn.pack(pady=(10,10))
        
    def sentiment_gui(self):
        self.clear()
        heading=Label(self.root,text='NLPApp',bg='light green',fg='black')
        heading.pack(pady=20)
        heading.config(font=('verdana',24,'bold'))

        heading1=Label(self.root,text='SENTIMENT',bg='light green',fg='black')
        heading1.pack(pady=10)
        heading1.config(font=('verdana',24))
        
        self.labeli=Label(self.root,text="Enter password")
        self.labeli.pack(pady=10)
        
        self.sentiment_input=Entry(self.root,width=50)
        self.sentiment_input.pack(pady=(5,10),ipady=4)
        
        sentiment_btn=Button(self.root,text="Sentiment Analysis",width=30,height=2,command=self.do_sentiment)
        sentiment_btn.pack(pady=(10,10))
        
        
        self.result=Label(self.root,text="",bg='light green',fg='white')
        self.result.pack(pady=10)
        self.result.config(font=('verdana',16))
        
        sentiment_btn=Button(self.root,text="Go Back",width=30,height=2,command=self.home_gui)
        sentiment_btn.pack(pady=(10,10))
        
        
        
        
        
    def ner_gui(self):
        self.clear()
        heading=Label(self.root,text='NLPApp',bg='light green',fg='black')
        heading.pack(pady=20)
        heading.config(font=('verdana',24,'bold'))

        heading1=Label(self.root,text='NER',bg='light green',fg='black')
        heading1.pack(pady=10)
        heading1.config(font=('verdana',24))
        
        
        
        
    def emotion_gui(self):
        self.clear()
        heading=Label(self.root,text='NLPApp',bg='light green',fg='black')
        heading.pack(pady=20)
        heading.config(font=('verdana',24,'bold'))
        
        heading1=Label(self.root,text='Emotion',bg='light green',fg='black')
        heading1.pack(pady=10)
        heading1.config(font=('verdana',24))
        
        
    def do_sentiment(self):
        txt=self.sentiment_input.get()
        result=self.api.sentiment_analysis(txt)
        txt=""
        for i in result['sentiment']:
            txt=txt+i+" -> "+str(result['sentiment'][i])+'\n'
                
        self.result['text']=txt
        
        
        
    
    
nlp=NLPApp()