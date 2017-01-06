from urllib.request import urlopen
import sys

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

data = urlopen(target_url)
xList = []
labels = []
for line in data:
	row = line.decode('utf8').strip().split(',')
	xList.append(row)
	
sys.stdout.write("Number of Rows of Data = " + str(len(xList)) + "\n")
sys.stdout.write("Number of Rows of Data = " + str(len(xList[1])))