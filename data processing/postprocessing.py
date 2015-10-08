import sys
CLASS_1 = ""
CLASS_0 = ""
def preprocess_data():
    inputFile = sys.argv[1]
    method = sys.argv[2]
    classes = sys.argv[3]
    if classes.upper() == "SENTIMENT":
        CLASS_1 = "POSITIVE"
        CLASS_0 = "NEGATIVE"
        #print("donr")
    if classes.upper() == "EMAIL":
        CLASS_1 = "SPAM"
        CLASS_0 = "HAM"
    if method == "SVM":
        outputFile = open(inputFile + "_post", 'w')
        for line in open(inputFile, 'r'):
            if float(line.rstrip()) > 0: 
                outputFile.write( CLASS_1 + "\n")
            if float(line.rstrip()) < 0: 
                outputFile.write( CLASS_0 + "\n")
    if method == "MEGAM":
        outputFile = open(inputFile + "_post", 'w')
        for line in open(inputFile, 'r'):
            if line.rstrip().split()[0] == "1": 
                outputFile.write( CLASS_1+ "\n")
            else: 
                outputFile.write( CLASS_0+ "\n")

preprocess_data()
