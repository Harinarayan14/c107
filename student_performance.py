import pandas as pd
import csv
import plotly_express
df = pd.read_csv("data.csv")
student_id = input("Enter Student's Id")
dfLoc = df.loc[df["student_id"]==student_id]
barGraph = plotly_express.bar(df,x=dfLoc.groupby("level")["attempt"].mean()
                                ,y=["Level 1","Level 2","Level 3","Level 4"]
                                ,orientation="h")
barGraph.show()