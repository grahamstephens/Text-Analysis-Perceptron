import glob
import codecs
from numpy import array
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize

#converts every line in the file to a string
def toString(file):
    string = ''
    for line in file:
        string += line
    return string

#turns notepad file into list
def wordExtract(direct):
    keywords = []
    fls = open(direct, 'r')
    for line in fls:
        newLine = line.rstrip()
        keywords.append(newLine)
    return array(keywords)

#fileFreq returns the final list of vectors, and also implicitly defines each word's one hot vector
#to be its corresponding index in the txt file
def fileFreq(target, direct):
    
    #words is a list of every word that occurs in the directory
    words = []
    #val will store the number alone
    value = []
    #targetVal holds only values of words in lines
    targetVal = []
    #final vector list to be returned
    vectorList = []
    
    #tokenizes the target file into a list of words
    openF = open(target, 'r')
    fileString = toString(openF)
    keywordList = word_tokenize(fileString)
    #makes targetVal have as many elements as lines, but as zeroes
    for k in range(0, len(keywordList)):
        targetVal.append(0)
    
    #counts the number of times every word in target file occurs in the target directory
    for f in glob.glob(direct):
        #tokenizes the file
        fls = codecs.open(f, 'r', encoding = 'utf-8', errors = 'ignore')
        string = toString(fls)
        tokens = word_tokenize(string)
        fdist = FreqDist(tokens)
        
        words = []
        value = []
        #words is a list of every word in the direct, and value is how many times that word occurs
        for key, val in fdist.items():
            words.append(str(key))
            value.append(val)
            
        #maps every occurrence to its correspondent word in lines    
        for i in range(len(words)):
            for j in range(len(keywordList)):
                if words[i] == keywordList[j]:
                    targetVal[j] += value[i]
                    
        vectorList.append(targetVal)
        #creates a fresh targetVal list of 76 0s
        targetVal = []                    
        for k in range(len(keywordList)):
            targetVal.append(0)
    
    return vectorList

if __name__ == "__main__":
    print(len(fileFreq('C:/Research/Keywords/Absolutist.txt','C:/Research/Dataset/Train1/*.txt')))