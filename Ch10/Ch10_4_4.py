import pandas as pd

data = [100, 110, 150, 170, 190, 200, 220]
s = pd.Series(data)
s.plot(kind="bar", rot=0)