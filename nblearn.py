
import sys
import math
import timeit

POSITIVE_RANGE = [7,8,9,10]
NEGATIVE_RANGE = [1,2,3,4]

global classes
global currentClass 
global numOfDocuments 
global vocab 
class LearnData:
    def __init__(self, name):
        self.name = name
        self.wordFrequency ={}
        self.totalNumOfWords = 0;
        #self.uniqueNumOfWords = 0;
        self.numOfOccurrences = 0;
        self.probWordGivenClass ={}
        self.probClass = 0;
def learn():
    #start = timeit.default_timer()
    numOfDocuments = 0
    vocab = set()
    currentClass = ""
    classes = {}
    for line in open(sys.argv[1],"r"):
        className, words = line.rstrip().split(None,1)
        words = words.split()
        numOfDocuments += 1
        if className.isdigit():
            if int(className) in POSITIVE_RANGE:
                currentClass = "POSITIVE"
            if int(className) in NEGATIVE_RANGE:
                currentClass = "NEGATIVE"
        else:
            currentClass = className.upper()
        
        if currentClass not in classes:
                classes[currentClass] = LearnData(currentClass)
            
        classes[currentClass].numOfOccurrences+=1   
        for w in words:
            currWord = w.split(":")[0]
            currVal = int (w.split(":")[1])
            vocab.add(currWord)
            frequencies = classes[currentClass].wordFrequency
            if currWord in frequencies:
                frequencies[currWord] += currVal
            else:
                frequencies[currWord] = 1
            classes[currentClass].totalNumOfWords += currVal
            
    for currClass in classes:
        classes[currClass].probClass = math.log(classes[currClass].numOfOccurrences) - math.log(numOfDocuments)
        
    for word in vocab:
        for currClass in classes:
            if word in classes[currClass].wordFrequency:
                classes[currClass].probWordGivenClass[word] = math.log(classes[currClass].wordFrequency[word] + 1) - math.log(int (classes[currClass].totalNumOfWords) + len(vocab))
            else:
                classes[currClass].probWordGivenClass[word] = - math.log(classes[currClass].totalNumOfWords + len(vocab))
            #print(word, currClass, classes[currClass].probWordGivenClass[word])
    output = open(sys.argv[2], "w+")
    output.write("VocabSize: " + str(len(vocab)))
    output.write("\n")
    for currClass in classes:
        output.write(currClass+ " " +  str(classes[currClass].probClass) + " " + str(classes[currClass].totalNumOfWords))
        output.write("\n")
    output.write("FEATURE_NAME CLASS1PROB CLASS2PROB")  
    output.write("\n")
    for word in vocab:
        toWrite = word
        for currClass in classes:  
            toWrite += " "   + str(classes[currClass].probWordGivenClass[word])
        output.write(toWrite)
        output.write("\n")     
    
    #stop = timeit.default_timer()
    #print(stop - start) 

if __name__ == '__main__':
    learn()
