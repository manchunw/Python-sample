import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot

# import data file
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

rocksVMines = pd.read_csv(target_url, header=None, prefix=" V")

dataRow2 = rocksVMines.iloc[1,0:60]
dataRow3 = rocksVMines.iloc[2,0:60]
plot.scatter(dataRow2, dataRow3)
plot.xlabel("2nd attribute")
plot.ylabel("3rd attribute")
plot.show()

dataRow21 = rocksVMines.iloc[20,0:60]
plot.scatter(dataRow2, dataRow21)
plot.xlabel("2nd attribute")
plot.ylabel("21st attribute")
plot.show()
