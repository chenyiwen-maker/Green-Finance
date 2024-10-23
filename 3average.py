# First, we'll calculate the average score for each province for the three time periods:
# 1. 1990-2000
# 2. 2001-2011
# 3. 2012-2021
#Score.xlsx
# Define the time ranges
import pandas as pd

df = pd.read_excel('data/Score.xlsx')
ranges = {
    "1990-2000": (1990, 2000),
    "2001-2011": (2001, 2011),
    "2012-2021": (2012, 2021)
}

# Create a new dataframe to store the average scores
avg_scores = pd.DataFrame()

for period, (start_year, end_year) in ranges.items():
    avg = df[(df['Time'] >= start_year) & (df['Time'] <= end_year)].groupby('Location')['Score'].mean()
    avg_scores[period] = avg
avg_scores.to_excel('data/3Ave_Score.xlsx')

