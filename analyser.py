import pandas as pd
df=pd.read_csv('ipl_2024_deliveries.csv')
index=0
rcbballs=0
freqdict={}
extradict={}
wicket=0
while index<len(df):
    if df.loc[index,'batting_team']=='RCB':
        rcbballs+=1
        run=df.loc[index,'runs_of_bat']+df.loc[index,'legbyes']+df.loc[index,'byes']
        extras=df.loc[index,'wide']+df.loc[index,'noballs']
        if pd.notna(df.loc[index, 'wicket_type']):
            wicket+=1
        if run in freqdict:
            freqdict[run]+=1
        else:
            freqdict[run]=1
        if extras in extradict:
            extradict[extras]+=1
        else:
            extradict[extras]=1
    index+=1

print(rcbballs,extradict,wicket,freqdict)