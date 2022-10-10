from statsmodels.graphics.mosaicplot import mosaic
fig, ax = plt.subplots(figsize=(a, b))
props = {}
col_dic = {colname1: color1, colname2: color2, colname3: color3}
for x, col in col_dic.items():
    for y in rowarray:
        props[(x, y)] = {"color": col}
mosaic(data=data, index=data.index, properties=props, ax=ax)
plt.show()
