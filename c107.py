import pandas as pd
import csv
import plotly_express
df = pd.read_csv("data.csv")
print(df.groupby("level")["attempt"].mean())
barGraph = plotly_express.bar(df,x=df.groupby("level")["attempt"].mean()
                                ,y=["Level 1","Level 2","Level 3","Level 4"]
                                ,orientation="h")
barGraph.show()
#import plotly.graph_objects as pgo
