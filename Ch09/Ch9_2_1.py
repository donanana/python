import pandas as pd

dists = {"name": ["中正區", "板橋區", "桃園區", "北屯區", 
                   "安南區", "三民區", "大安區", "永和區", 
                   "八德區", "前鎮區", "鳳山區", 
                   "信義區", "新店區"],
         "population": [159598, 551452, 441287, 275207,
                        192327, 343203, 309835, 222531,
                        198473, 189623, 359125, 
                        225561, 302070],
         "city": ["台北市", "新北市", "桃園市", "台中市",
                  "台南市", "高雄市", "台北市", "新北市",
                  "桃園市", "高雄市", "高雄市",
                  "台北市", "新北市"]}
df = pd.DataFrame(dists) 
print(df)
df.to_html("Ch9_2_1.html")