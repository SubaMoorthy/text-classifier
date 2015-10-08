import sys

def preprocess_sentiment_data():
    inputFile = sys.argv[1]
    method = sys.argv[2]
    if method == "BAYES":
        outputFile = open(inputFile + "_test", 'w')
        resultFile = open(inputFile + "_result", 'w')
        for line in open(inputFile, 'r'):
            result, features = line.split(None, 1) 
            if result.isdigit() and int(result) >= 7:
                resultFile.write("POSITIVE" + "\n")
            elif result.isdigit() and int(result) <= 4:
                resultFile.write("NEGATIVE" + "\n")
            else: 
                resultFile.write(result + "\n")
            outputFile.write(features)
        outputFile.close()
    if method == "SVM":
        outputFile = open(inputFile + "_train", 'w')
        resultFile = open(inputFile + "_result", 'w')
        for line in open(inputFile, 'r'):
            result, features = line.rstrip().split(None, 1) 
            if result.isdigit() and int(result) >= 7:
                resultFile.write("POSITIVE" + "\n")
            elif result.isdigit() and int(result) <= 4:
                resultFile.write("NEGATIVE" + "\n")
            elif result == "+1":
                resultFile.write("SPAM" + "\n")
            elif result == "-1":
                resultFile.write("HAM" + "\n")
            else: 
                resultFile.write(result + "\n")
            outputFile.write("1" + " " + features + "\n")
preprocess_sentiment_data()
