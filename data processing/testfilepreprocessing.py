import sys

def preprocess():
	outputfile = open(sys.argv[2],"w")
	method = sys.argv[3]
	separator = " "
	if method.upper() == "SVM":
		separator = ":"
	for line in open(sys.argv[1],"r"):
		feat = {}
		features = line.rstrip().split() 
		outputfile.write("1")
		featureList = features
		for x in featureList:
			featName, featCnt = x.split(":")
			feat[int(featName) + 1] = featCnt 
		for f in sorted(feat):
			outputfile.write(" " + str(f) + separator +feat[f])
		outputfile.write("\n")
if __name__ == '__main__':
	preprocess()
