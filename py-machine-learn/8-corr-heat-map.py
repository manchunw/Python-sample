import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot

# import data file
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

rocksVMines = pd.read_csv(target_url, header=None, prefix=" V")

corMat = DataFrame(rocksVMines.corr())
plot.pcolor(corMat)
plot.show()