import matplotlib.pyplot as plt
import pandas as pd
iris = pd.read_csv('https://sololearn.com/uploads/files/iris.csv')

iris.hist()
plt.show()
