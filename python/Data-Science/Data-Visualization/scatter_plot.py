import matplotlib.pyplot as plt
import pandas as pd
presidents_df = pd.read_csv('https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')

# plt.scatter(presidents_df['height'], presidents_df['age'],
#    marker='<',
#    color='b')
# plt.xlabel('height');
# plt.ylabel('age')
# plt.title('U.S. presidents')
# plt.show()

presidents_df.plot(kind = 'scatter',
  x = 'height',
  y = 'age',
  title = 'U.S. presidents')
plt.show()