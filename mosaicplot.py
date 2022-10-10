from statsmodels.graphics.mosaicplot import mosaic
fig, ax = plt.subplots(figsize=(a, b))

props = {}
col_dic = {colname1: color1, colname2: color2, colname3: color3}
gb = data.groupby([cols, rows])[index].count()
for x, col in col_dic.items():
    for y in rowarray:
        props[(x, y)] = {"color": col}

mosaic(data=data, index=data.index, labelizer=lambda k: gb[k], properties=props, ax=ax)
plt.show()


##### ex. train data, employment type & income type #####
from statsmodels.graphics.mosaicplot import mosaic
fig, ax = plt.subplots(figsize=(10, 10))

props = {}
col_dic = {"정규직": "powderblue", "기타": "lightblue", "계약직": "lightskyblue", "일용직": "deepskyblue"}
gb = train.groupby(["employment_type", "income_type"])["application_id"].count()
for x, col in col_dic.items():
  for y in data["income_type"].unique():
    props[(x, y)] = {"color": col}

mosaic(data=train, index=["employment_type", "income_type"], labelizer=lambda k: gb[k], properties=props, ax=ax)
plt.show()
