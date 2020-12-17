# import Tkinter modules
import tkinter as tk
import tkinter.scrolledtext as st
from tkinter import messagebox
# import classes
from components.menu import MenuBar
from classes.dictionary import Dictionary


class MainPage(tk.Frame):
    def __init__(self, parent, user):
        # gui window settings
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("EasyWords v.1 | Hello "+ user.getUsername())
        self.parent.resizable(False, False)
        # centering the windows
        self.parent.geometry("{}x{}+{}+{}".format(705, 500, int((self.parent.winfo_screenwidth()/2) - (705/2)), int((self.parent.winfo_screenheight()/2) - (500/2))))
        # create MenuBar Object
        self.menubar = MenuBar(self.parent)
        self.parent.config(menu=self.menubar)
        # create Dictionary Object
        self.dictionary = Dictionary()

        ##### Components/Widgets
        # (Sidebar Frame)
        self.sidebarFrame = tk.Frame(parent, relief="sunken",borderwidth=0.5, padx=10,  pady=10)
        self.getDefinitionsBtn = tk.Button(self.sidebarFrame, width=30, text ="Get Definitions", command=lambda : self.mainEventController("definitions"))
        self.getSynonymsBtn = tk.Button(self.sidebarFrame, width=30,text ="Get Synonyms", command=lambda : self.mainEventController("synonyms"))
        self.getAntonymsBtn = tk.Button(self.sidebarFrame, width=30,text ="Get Antonyms", command=lambda : self.mainEventController("antonyms"))
        self.getRhymesBtn = tk.Button(self.sidebarFrame, width=30,text ="Get Rhymes", command=lambda : self.mainEventController("rhymes"))
        self.getSuggestionWordsBtn = tk.Button(self.sidebarFrame, width=30,text ="Get Suggestions Words", command=lambda : self.mainEventController("suggestionWords"))
        self.getSoundLikeWordsBtn = tk.Button(self.sidebarFrame, width=30,text ="Get Sound Like Words", command=lambda : self.mainEventController("soundLikeWords"))
        
        # (Searchbar Frame)
        self.searchbarFrame = tk.Frame(parent, relief="sunken",borderwidth=0.5, padx=10,  pady=10)
        self.searchLabel = tk.Label(self.searchbarFrame, text=user.getUsername()+", Serch by typing below")
        self.searchWordEntry = tk.Entry(self.searchbarFrame, width=40)
        self.searchBtn = tk.Button(self.searchbarFrame, width=20, text="Search", command=lambda : self.mainEventController("definitions"))
        self.searchErrorLabel = tk.Label(self.searchbarFrame, text="", fg="red")
        
        # (Result Frame)
        self.resultFrame = tk.Frame(parent, relief="sunken",borderwidth=0.5, padx=10, pady=10)
        self.resultLabel = tk.Label(self.resultFrame, text="Results :", font=("Arial 10 bold"), pady=5)
        self.ResultsTextArea = st.ScrolledText(self.resultFrame, padx=5, pady=5, width = 53, height = 20, font = ("Arial", 11)) 
        self.ResultsTextArea.insert(tk.INSERT,"Search word's data by typing above in the field...") 
        self.ResultsTextArea.configure(state='disabled')
        
        ##### layout
        # (Sidebar Frame)
        self.getDefinitionsBtn.grid(pady=5)
        self.getSynonymsBtn.grid(pady=5)
        self.getAntonymsBtn.grid(pady=5)
        self.getRhymesBtn.grid(pady=5)
        self.getSuggestionWordsBtn.grid(pady=5)
        self.getSoundLikeWordsBtn.grid(pady=5)

        # (Searchbar Frame)
        self.searchLabel.grid(row=0,column=0, sticky="w")
        self.searchWordEntry.focus()
        self.searchWordEntry.grid(row=1, column=0, ipady=3)
        self.searchBtn.grid(row=1,column=1,padx=10)
        self.searchErrorLabel.grid(row=2, column=0,sticky="w")

        # (Result Frame)
        self.resultLabel.grid(sticky="w")
        self.ResultsTextArea.grid()

        ##### Frames Layout:
        self.sidebarFrame.grid(row=0, column=0, rowspan=2, sticky="n")
        self.searchbarFrame.grid(row=0, column=1,  sticky="n")
        self.resultFrame.grid(row=1,column=1, sticky="w")

    # function to set tittle in result's textarea
    def setResultsTextAreaTitle(self, title):
        self.ResultsTextArea.configure(state='normal')
        self.ResultsTextArea.delete('1.0', tk.END)
        self.ResultsTextArea.insert(tk.INSERT,title + "\n" + "\n")

    # function to validate search field text
    def validateSearchText(self, searchText):
        if searchText == "":
            messagebox.showinfo("Alert !!!", "Search field cannot be empty. Please enter valid text in serch field and try again")
            self.searchErrorLabel['text'] = 'Enter Valid Text'
            return False
        else:
            self.searchErrorLabel['text'] = ""
            return True

    ##### EVENTS
    # method to controll all the events of GUI
    def mainEventController(self, eventName):
        isSearchValid = self.validateSearchText(self.searchWordEntry.get())
        self.dictionary.setSearchWord(self.searchWordEntry.get())
        # events responses
        if isSearchValid and eventName == "definitions":
            self.definitionsEvent()
        elif isSearchValid and eventName == "synonyms":
            self.synonymsEvent()
        elif isSearchValid and eventName == "antonyms":
            self.antonymsEvent()
        elif isSearchValid and eventName == "rhymes":
            self.rhymesEvent()
        elif isSearchValid and eventName == "suggestionWords":
            self.suggestionWordsEvent()
        elif isSearchValid and eventName == "soundLikeWords":
            self.soundLikeWordsEvent()
        self.ResultsTextArea.configure(state='disabled')

    # method to get and set definitions
    def definitionsEvent(self):
        self.setResultsTextAreaTitle("Definitions : ")
        # get and set definition's list
        for definition in self.dictionary.getDefinitionsList():
            self.ResultsTextArea.insert(tk.INSERT, definition + "\n" + "\n" )
    
    # method to get and set synonyms
    def synonymsEvent(self):
        self.setResultsTextAreaTitle("Synonyms : ")
        # get and set synonyms's list
        for synonym in self.dictionary.getSynonymsList():
            self.ResultsTextArea.insert(tk.INSERT, synonym + "\n" + "\n" )

    # method to get and set antonyms
    def antonymsEvent(self):
        self.setResultsTextAreaTitle("Antonyms : ")
        # get and set antonyms's list
        for antonyms in self.dictionary.getAntonymsList():
            self.ResultsTextArea.insert(tk.INSERT, antonyms + "\n" + "\n" )

    # method to get and set rhymes
    def rhymesEvent(self):
        self.setResultsTextAreaTitle("Rhymes : ")
        # get and set rhymes's list
        for rhymes in self.dictionary.getRhymesList():
            self.ResultsTextArea.insert(tk.INSERT, rhymes + "\n" + "\n" )

    # method to get and set suggestion words
    def suggestionWordsEvent(self):
        self.setResultsTextAreaTitle("Suggestion Words : ")
        # get and set suggestion words's list
        for suggestionWord in self.dictionary.getSuggestionWordsList():
            self.ResultsTextArea.insert(tk.INSERT, suggestionWord + "\n" + "\n" )
    
    # method to get and set sound like words
    def soundLikeWordsEvent(self):
        self.setResultsTextAreaTitle("Sound Like Words : ")
        # get and set sound like words's list
        for soundLikeWord in self.dictionary.getSoundLikeWordsList():
            self.ResultsTextArea.insert(tk.INSERT, soundLikeWord + "\n" + "\n" )