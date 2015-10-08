import sys
import os

CLASS_1 = "HAM"
CLASS_2 = "SPAM"

enron = ["enron1", "enron2", "enron3", "enron4"]

def convertToPDF():
    vocab = {}
    currentClass = ""
    listofWords = {}
    pdfString = ""
    pdfList = []
    files = []
    i=0
    for word in open("../data/email/enron.vocab", "r", encoding="latin1"):
        if(len(word)) > 0:
            vocab[word.rstrip()] = i
            i += 1
    count = 0
    #print(len(vocab))
    dirName = "../data/test/spam_or_ham_test"
    output = open("../data/email_nb_test.data", 'w')  
    for filename in os.listdir(dirName):
        file_path = dirName+ "/" + filename
        if filename == ".DS_Store":
            continue
        files.append(file_path)

        #currentClass = ""
    files = sorted(files)
    for filename in files:
        count += 1
        #if "ham" in filename:
         #   currentClass = CLASS_1
        #elif "spam" in filename:
         #   currentClass = CLASS_2
        #else:
        #currentClass = ""
        #file_path = dirName+ "/" + filename
        #if filename == ".DS_Store":
         #   continue
        infile = open(filename,"r", encoding="latin1")
        # reset words for each file
        listofWords = {}
        pdfString = ""

	
        for line in infile:
            words = line.rstrip().split()
            for word in words:
                #print(word)
                if word in vocab:
                    wordNum = vocab[word]
                    if wordNum in listofWords:
                        listofWords[wordNum] = listofWords.get(wordNum) + 1
                    else:
                        listofWords[wordNum] = 1
                        
        if currentClass == "":
            pdfString = ""
        else:
            pdfString = currentClass + " "
        for wordNum in listofWords:
            pdfString += str(wordNum) + ":" + str(listofWords[wordNum])+ " "
        
        pdfList.append(pdfString)
        
 
    for item in pdfList:
        output.write(item)
        output.write("\n")
    
    
    
if __name__ == '__main__':
    convertToPDF()
