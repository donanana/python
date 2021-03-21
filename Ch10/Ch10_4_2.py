import pandas as pd

dists = {"name": ["Zhongzheng", "Banqiao", "Taoyuan", "Beitun", 
                   "Annan", "Sanmin", "Daan", "Yonghe", 
                   "Bade", "Cianjhen", "Fengshan", 
                   "Xinyi", "Xindian"],
         "population": [159598, 551452, 441287, 275207,
                        192327, 343203, 309835, 222531,
                        198473, 189623, 359125, 
                        225561, 302070]}
df = pd.DataFrame(dists)
print(df) 
df.to_html("Ch10_4_2_01.html")
df.plot()

df2 = pd.DataFrame(dists, 
                   columns=["population"],
                   index=dists["name"])
print(df2)
df2.to_html("Ch10_4_2_02.html")
df2.plot()