import sys
import timeit

global numOfDocuments 
global vocabSize

class Classify:
    def __init__(self, name):
        self.name = name
        self.totalNumOfWords = 0;
        self.probWordGivenClass ={}
        self.probClass = 0;
        
def classify():
    #start = timeit.default_timer()
    classes = []
    modelfile = open(sys.argv[1],"r")
    vocabSize = int(modelfile.readline().split()[1])
    # for CLASS 1
    className, prob, count = modelfile.readline().split()
    newClass = Classify(className)
    newClass.probClass = float(prob)
    newClass.totalNumOfWords = int(count)
    classes.append(newClass)
    
    # for CLASS 2
    className, prob, count = modelfile.readline().split()
    newClass = Classify(className)
    newClass.probClass = float(prob)
    newClass.totalNumOfWords = int (count)
    classes.append(newClass)
    
    #read the heading n skip it
    modelfile.readline()
    for line in modelfile:
        wordProb = line.split()
        for currClass in classes:
            currClass.probWordGivenClass[wordProb[0]] = float(wordProb[classes.index(currClass )+1])
    modelfile.close()
    testfile = open(sys.argv[2],"r")
    #outputfile = open(sys.argv[2]+".out","w")
    for line in testfile:
        words = line.rstrip().split()
        max_probability, maxClass = None, ""
        for currClass in classes:
            classProb = currClass.probClass
            for w in words:
                #print(w)
                word_freq = (int) (w.split(":")[1])
                curr_word = w.split(":")[0]
                if curr_word in currClass.probWordGivenClass:
                    classProb += currClass.probWordGivenClass[curr_word] * word_freq
                #else:
                 #   classProb += - math.log10(classes[currClass].totalNumOfWords + vocabSize)
                    
            if(max_probability == None or max_probability < classProb):
                max_probability, maxClass = classProb, currClass.name
                
    
        print(maxClass)
	#outputfile.write(maxClass)
        #outputfile.write("\n");
    #stop = timeit.default_timer()
    #print(stop - start) 

if __name__ == '__main__':
    classify()
