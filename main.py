import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the CSV file
netflix_df = pd.read_csv('netflix_data.csv')

# Step 2: Filter the data to remove TV shows
netflix_subset = netflix_df[netflix_df['type'] != 'TV Show']

# Step 3: Subset the Netflix movie data
netflix_movies = netflix_subset[["title", "country", "genre", "release_year", "duration"]]

# Step 4: Filter movies shorter than 60 minutes
short_movies = netflix_movies[netflix_movies['duration'] < 60]

# Inspect the result
print(short_movies.head())

# Step 5: Assign colors to genre groups
colors = []
for index, row in netflix_movies.iterrows():
    if "Children" in row['genre']:
        colors.append('blue')
    elif "Documentaries" in row['genre']:
        colors.append('green')
    elif "Stand-Up" in row['genre']:
        colors.append('red')
    else:
        colors.append('black')
    

# Step 6: Create scatter plot
fig = plt.figure(figsize = (10, 6))
plt.scatter(netflix_movies['release_year'], netflix_movies['duration'], c =colors, alpha =0.5)
plt.xlabel('Release year')
plt.ylabel('Duration (min)')
plt.title('Movie Duration by Year of Release')
plt.show()

# Step 7: Answer the question
answer = "no"
print("Are we certain that movies are getting shorter?", answer)