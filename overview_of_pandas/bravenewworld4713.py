import pandas as pd

# read the Excel workbook into a Pandas dataframe


videos = pd.read_excel(r'C:\WiseOwl\overview_of_pandas\Most-viewed videos.xlsx')

# show just the video names of the top 5

top_five = videos.head(5)

print(top_five)

print(top_five["Video"])

# sort a dataframe by one or more columns

sorted_videos = videos.sort_values(

by=['Publication date'],

ascending=[False]

)

print(sorted_videos.iloc[:, -2:])
