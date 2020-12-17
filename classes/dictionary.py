import requests
import json 

class Dictionary:
    # constructor
    def __init__(self):
        self.__word = ""
        self.__definitions = []
        self.__synonyms = []
        self.__antonyms = []
        self.__rhymes = []
        self.__suggestionWords = []
        self.__soundLikeWords = []

    # method to set word to search data
    def setSearchWord(self, word):
        self.__word = word

    # private method to get all the definitions with api
    def __getDefinitions(self):
        try:
            search_response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/"+self.__word).json()
            data = json.dumps(search_response[0]["meanings"], indent=2, sort_keys=True)
            definitions = json.loads(data)
            self.__definitions.clear()
            for definition in definitions:
                self.__definitions.append(definition["definitions"][0]["definition"])   
        except:
            self.__definitions.clear()
            self.__definitions.append("ERROR!!!\nCould not find definition of given word. Please try again or check your connection.")

    # private method to get all the synonyms with api
    def __getSynonyms(self):
        try:
            synonyms_response = requests.get("https://api.datamuse.com/words?rel_syn="+self.__word).json()
            data = json.dumps(synonyms_response, indent=2, sort_keys=True)
            synonyms = json.loads(data)
            self.__synonyms.clear()
            for synonym in synonyms:
                self.__synonyms.append(synonym["word"])
        except:
            self.__synonyms.clear()
            self.__synonyms.append("ERROR!!!\nCould not find synonyms of given word. Please try again or check your connection.")
    
    # private method to get all the antonyms with api
    def __getAntonyms(self):
        try:
            antonyms_response = requests.get("https://api.datamuse.com/words?rel_ant="+self.__word).json()
            data = json.dumps(antonyms_response, indent=2, sort_keys=True)
            antonyms = json.loads(data)
            self.__antonyms.clear()
            for antonym in antonyms:
                self.__antonyms.append(antonym["word"])
        except:
            self.__antonyms.clear()
            self.__antonyms.append("ERROR!!!\nCould not find synonyms of given word. Please try again or check your connection.")

    # private method to get all the rhymes with api
    def __getRhymes(self):
        try:
            rhymes_response = requests.get("https://api.datamuse.com/words?rel_rhy="+self.__word).json()
            data = json.dumps(rhymes_response, indent=2, sort_keys=True)
            rhymes = json.loads(data)
            self.__rhymes.clear()
            for rhyme in rhymes:
                self.__rhymes.append(rhyme["word"])
        except:
            self.__rhymes.clear()
            self.__rhymes.append("ERROR!!!\nCould not find rhymes of given word. Please try again or check your connection.")

    # private method to get all the suggestions words with api
    def __getSuggestionWords(self):
        try:
            suggestionWords_response = requests.get("https://api.datamuse.com/sug?s="+self.__word).json()
            data = json.dumps(suggestionWords_response, indent=2, sort_keys=True)
            suggestionWords = json.loads(data)
            self.__suggestionWords.clear()
            for suggestionWord in suggestionWords:
                self.__suggestionWords.append(suggestionWord["word"])
        except:
            self.__suggestionWords.clear()
            self.__suggestionWords.append("ERROR!!!\nCould not find any suggestion words for the given word. Please try again or check your connection.")

    # private method to get all the sound like words with api
    def __getSoundLikeWords(self):
        try:
            soundLikeWords_response = requests.get("https://api.datamuse.com/words?sl="+self.__word).json()
            data = json.dumps(soundLikeWords_response, indent=2, sort_keys=True)
            soundLikeWords = json.loads(data)
            self.__soundLikeWords.clear()
            for soundLikeWord in soundLikeWords:
                self.__soundLikeWords.append(soundLikeWord["word"])
        except:
            self.__soundLikeWords.clear()
            self.__soundLikeWords.append("ERROR!!!\nCould not find words with similar sound as given word. Please try again or check your connection.")

    # method to get definitions list
    def getDefinitionsList(self):
        self.__getDefinitions()
        if not self.__definitions:
            self.__definitions.append("Could not find any definition of "+self.__word+".\nPlease search for other word.")
            return self.__definitions
        else:
            return self.__definitions

    # method to get synonyms list
    def getSynonymsList(self):
        self.__getSynonyms()
        if not self.__synonyms:
            self.__synonyms.append("Could not find any synonyms of "+self.__word+".\nPlease search for other word.")
            return self.__synonyms
        else:
            return self.__synonyms

    # method to get antonyms list
    def getAntonymsList(self):
        self.__getAntonyms()
        if not self.__antonyms:
            self.__antonyms.append("Could not find any antonyms of "+self.__word+".\nPlease search for other word.")
            return self.__antonyms
        else:
            return self.__antonyms

    # method to get rhymes list
    def getRhymesList(self):
        self.__getRhymes()
        if not self.__rhymes:
            self.__rhymes.append("Could not find any rhymes of "+self.__word+".\nPlease search for other word.")
            return self.__rhymes
        else:
            return self.__rhymes

    # method to get suggestion words list
    def getSuggestionWordsList(self):
        self.__getSuggestionWords()
        if not self.__suggestionWords:
            self.__suggestionWords.append("Could not find any suggestion words of "+self.__word+".\nPlease search for other word.")
            return self.__suggestionWords
        else:
            return self.__suggestionWords

    # method to get sound like words list
    def getSoundLikeWordsList(self):
        self.__getSoundLikeWords()
        if not self.__soundLikeWords:
            self.__soundLikeWords.append("Could not find words with similar sound as "+self.__word+".\nPlease search for other word.")
            return self.__soundLikeWords
        else:
            return self.__soundLikeWords