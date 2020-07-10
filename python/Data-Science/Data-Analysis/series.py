#o entanto, é possível fazer isso em pandas.
# A biblioteca do pandas é construída sobre o numpy,
# o que significa que muitos recursos, métodos e funções são compartilhados.

import pandas as pd

series = pd.Series({'a': 1, 'b': 2, 'c':3})
print(series['a'])