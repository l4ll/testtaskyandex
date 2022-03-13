import pandas as pd
db= pd.read_csv("pp-complete.csv")
db=db.fillna('none')
db['31, Unnamed: 8, ALDRICH DRIVE, WILLEN, MILTON KEYNES, MILTON KEYNES.1'] = (db['31']+', '+db['Unnamed: 8']+', '+db['ALDRICH DRIVE']+', '+db['WILLEN']+', '+db['MILTON KEYNES']+', '+db['MILTON KEYNES.1']+', '+db['MILTON KEYNES.2'])
db=db.sort_values(by='31, Unnamed: 8, ALDRICH DRIVE, WILLEN, MILTON KEYNES, MILTON KEYNES.1')
series=db['31, Unnamed: 8, ALDRICH DRIVE, WILLEN, MILTON KEYNES, MILTON KEYNES.1']
series=series.squeeze(axis=0)
a="31, Unnamed: 8, ALDRICH DRIVE, WILLEN, MILTON KEYNES, MILTON KEYNES.1"
series.loc[len(series.index)]=a
series=series.sort_values()
for i in range(1000):
    if series[i+1]!=series[i]:
        series=series.drop(labels=[i])
        i-=1
        