import pandas as pd

df = pd.read_csv("athlete_events.csv").sample(n=50_000, random_state=42)
df.to_csv("athlete_events_sample.csv",index=False)
print(df.shape)
df.head()