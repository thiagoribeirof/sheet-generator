import customtkinter as ctk
import tkinter as tk
from datetime import datetime
import backend

# Official documentation of customtkinter https://customtkinter.tomschimansky.com/documentation/color

MODE = "Dark"
THEME = "green"
ctk.set_appearance_mode(MODE) # Supported modes : Light, Dark, System
ctk.set_default_color_theme(THEME)  # Themes: "blue" (standard), "green", "dark-blue"
dimensions = "1024x768" #width x height

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(dimensions)
        self.title("Sheet Generator")

        #add widgets (buttons, textboxes, etc)
        self.Welcomelabel = ctk.CTkLabel(self, text="Bem-vindo ao gerador de planilha!", 
                                    fg_color="transparent", text_color="darkgrey")
        self.Welcomelabel.place(x=420, y=5)

        self.Portarialabel = ctk.CTkLabel(self, text="Nº da Portaria:", 
                                    fg_color="transparent", text_color="darkgrey")
        self.Portarialabel.place(x=15, y=70)
        
        self.PortariaEntry = ctk.CTkEntry(self, placeholder_text="ex: 0515")
        self.PortariaEntry.place(x=120, y=70)
        
        self.Vazao = ctk.CTkLabel(self, text="Vazão:", 
                                    fg_color="transparent", text_color="darkgrey")
        self.Vazao.place(x=15, y=140)
        
        self.VazaoEntry = ctk.CTkEntry(self, placeholder_text="ex: 15.3")
        self.VazaoEntry.place(x=120, y=140)

        self.TempoCaptacao = ctk.CTkLabel(self, text="Tempo máximo de captação:", 
                                    fg_color="transparent", text_color="darkgrey", wraplength=101, justify="left")
        self.TempoCaptacao.place(x=15, y=205)
        
        self.TempoCaptacaoEntry = ctk.CTkEntry(self, placeholder_text="em horas/dia. ex: 12")
        self.TempoCaptacaoEntry.place(x=120, y=210)


        self.DataInstalacao = ctk.CTkLabel(self, text="Data de instalação:", 
                                    fg_color="transparent", text_color="darkgrey", wraplength=101, justify="left")
        self.DataInstalacao.place(x=15, y=280)
        
        self.DataInstalacaoEntry = ctk.CTkEntry(self, placeholder_text="ex: 25/07/2020")
        self.DataInstalacaoEntry.place(x=120, y=280)

        self.DataFim = ctk.CTkLabel(self, text="Data fim da leitura:", 
                                    fg_color="transparent", text_color="darkgrey", wraplength=101, justify="left")
        self.DataFim.place(x=15, y=350)
        
        self.DataFimEntry = ctk.CTkEntry(self, placeholder_text="ex: 25/10/2022")
        self.DataFimEntry.place(x=120, y=350)

        self.DataFim = ctk.CTkLabel(self, text="Frequência:", 
                                    fg_color="transparent", text_color="darkgrey", wraplength=101, justify="left")
        self.DataFim.place(x=15, y=420)

        self.Frequencia = tk.StringVar(value="DIARIO")
 
        self.DiarioRadioButton = ctk.CTkRadioButton(self,
                                  text="Diario",
                                  variable=self.Frequencia,
                                            value="DIARIO")
        self.DiarioRadioButton.place(x=150, y=420)

        self.SemanalRadioButton = ctk.CTkRadioButton(self,
                                  text="Semanal",
                                  variable=self.Frequencia,
                                            value="SEMANAL")
        self.SemanalRadioButton.place(x=300, y=420)

        self.QuinzenalRadioButton = ctk.CTkRadioButton(self,
                                  text="Quinzenal",
                                  variable=self.Frequencia,
                                            value="QUINZENAL")
        self.QuinzenalRadioButton.place(x=450, y=420)

        self.MensalRadioButton = ctk.CTkRadioButton(self,
                                  text="Mensal",
                                  variable=self.Frequencia,
                                            value="MENSAL")
        self.MensalRadioButton.place(x=600, y=420)


        self.sendButton = ctk.CTkButton(self, command=self.getData, text="Gerar Planilha")
        self.sendButton.place(x=400, y=500)

        

        #methods 
    def getData(self):
            portaria = self.PortariaEntry.get()
            vazao = float(self.VazaoEntry.get())
            tempoCaptacao = float(self.TempoCaptacaoEntry.get())
            dataInstalacao = datetime.strptime(self.DataInstalacaoEntry.get(), '%d/%m/%Y').date()
            dataFim = datetime.strptime(self.DataFimEntry.get(), '%d/%m/%Y').date()
            frequencia = self.Frequencia.get()
            backend.createDataframe(portaria=portaria, vazao=vazao, tempoCaptacao=tempoCaptacao, dataInstalacao=dataInstalacao, 
                                    dataFim=dataFim, frequencia=frequencia)
              
    


app = App()  #instance of App object. The app.configure(attribute=value) method can change and configure all attributes.
# ex: app.configure(fg_color="red") would set the background to red
app.resizable(False, False)


app.mainloop() #calls the main loop of the app. In resume, it'll keep the app running


