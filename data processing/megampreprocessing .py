import sys

def preprocess():
	outputfile = open(sys.argv[2],"w")
	for line in open(sys.argv[1],"r", encoding="utf-8"):
		feat = {}
		result, features = line.rstrip().split(None, 1) 
		if result.isdigit() and int(result) >= 7:
			outputfile.write("1" )
		if result.isdigit() and int(result) <= 4:
			outputfile.write("0")
		if result in ["HAM", "NEGATIVE"]:
			outputfile.write("0" )
		if result in ["SPAM", "POSITIVE"]:
			outputfile.write("1")
		featureList = features.split()
		for x in featureList:
			featName, featCnt = x.split(":")
			feat[int(featName) + 1] = featCnt 
		
		for f in sorted(feat):
			outputfile.write(" " + str(f) + " " +feat[f])
		outputfile.write("\n")
if __name__ == '__main__':
	preprocess()
