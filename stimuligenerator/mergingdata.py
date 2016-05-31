import pandas as pd

mtdata = pd.read_csv('worker information from MT.csv')
qualtricsdata = pd.read_csv('Sharing_Game_Study2.csv')

mtdata['WorkerID'] = mtdata['WorkerID'].str.extract(r'(\S*)', expand=False)
qualtricsdata['WorkerID'] = qualtricsdata['WorkerID'].str.extract(r'(\S*)', expand=False)

qualtricsdata = qualtricsdata.loc[qualtricsdata['WorkerID'].str.len() > 5]
mtdata = mtdata.loc[mtdata['WorkerID'].str.len() > 5]

data = pd.merge(qualtricsdata,mtdata, on = 'WorkerID')

data.to_csv('merged.csv')