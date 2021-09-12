import pandas
import os

outdir = './supermarkets'
if not os.path.exists(outdir):
    os.mkdir(outdir)

fullname_json = os.path.join(outdir, "supermarkets.json")    
df1_json = pandas.read_json(fullname_json)
print(df1_json.head())
