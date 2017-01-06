from urllib.request import urlopen
import sys
import numpy as np
import pylab
import scipy.stats as stats

# import data file
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

data = urlopen(target_url)
xList = []
labels = []
for line in data:
	row = line.decode('utf8').strip().split(',')
	xList.append(row)
nrow = len(xList)
ncol = len(xList[1])
type = [0]*3
colCounts = []
col = 3
colData = []
for row in xList:
	colData.append(float(row[col]))

# show mean and sd
colArray = np.array(colData)
colMean = np.mean(colArray)
colsd = np.std(colArray)
sys.stdout.write("Mean = " + '\t' + str(colMean) + '\t\t' + "Standard Deviation = " + '\t' + str(colsd) + '\n')

# show 4 percentiles
ntiles = 4
percentBdry = []
for i in range(ntiles+1):
	percentBdry.append(np.percentile(colArray, i*100/ntiles))
sys.stdout.write("\nBoundaries for 4 Equal Percentiles\n")
print(percentBdry)
sys.stdout.write("\n")

# show 10 percentiles
ntiles = 10
percentBdry = []
for i in range(ntiles+1):
	percentBdry.append(np.percentile(colArray, i*100/ntiles))
sys.stdout.write("\nBoundaries for 10 Equal Percentiles\n")
print(percentBdry)
sys.stdout.write("\n")

# show unique label values
col = 60
colData = []
for row in xList:
	colData.append(row[col])
unique = set(colData)
sys.stdout.write("Unique Label Values\n")
print(unique)

# show count
catDict = dict(zip(list(unique), range(len(unique))))
catCount = [0]*2
for elt in colData:
	catCount[catDict[elt]] += 1
sys.stdout.write("\nCounts for Each Value of Categorical Label \n")
print(list(unique))
print(catCount)

labels = []
col = 3
colData = []
for row in xList:
	colData.append(float(row[col]))

stats.probplot(colData, dist="norm", plot=pylab)
pylab.show()

sys.stdout.write("Number of Rows of Data = " + str(len(xList)) + "\n")
sys.stdout.write("Number of Rows of Data = " + str(len(xList[1])) + "\n")