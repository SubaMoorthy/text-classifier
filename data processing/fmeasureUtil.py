import sys

def calculateFMeasure():
    correctlyClassified = {}
    actualCount = {}
    predictedCount = {}
    classes = [sys.argv[3], sys.argv[4]]
    with open(sys.argv[1],"r") as resultF, open(sys.argv[2],"r") as correctF:
        results = resultF.read().split("\n")
        correctly = correctF.read().split("\n")
        for i in range (0, len(correctly)-1):
            print(i)
            result = results[i]
            correct = correctly[i]

            #if correct == "+1" or correct == "1":
             #       correct = classes[0]
            #else:
             #       correct = classes[1]
            if result == correct:
                if result in correctlyClassified:
                    correctlyClassified[result] +=1
                else:
                    correctlyClassified[result] = 1
            
            if result in predictedCount:
                    predictedCount[result] +=1
            else:
                    predictedCount[result] = 1
        
            if correct in actualCount:
                    actualCount[correct] +=1
            else:
                    actualCount[correct] = 1
    
    
                   
    for c in classes:
        print(c)
        precision = correctlyClassified[c]/predictedCount[c]
        recall = correctlyClassified[c]/actualCount[c]
        fscore = (2*precision*recall)/(precision+recall)
        print("precision: " + str(precision))
        print("recall: " + str(recall))
        print("f score: " + str(fscore))
if __name__ == '__main__':
    calculateFMeasure()
