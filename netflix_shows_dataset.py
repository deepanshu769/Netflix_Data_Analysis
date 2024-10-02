import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Loading the dataset
data = pd.read_csv("C:/Git hub code/vs code/Kaggel project/netflix_titles.csv")
data.sample(5)
# Dropping unnecessary columns
data.drop(["show_id", "description"], axis=1, inplace=True)
# Checking shape and columns of the dataset
data.shape
data.columns
# Checking for null values
print("Null values per column:")
# Filling missing values in 'country' with mode
country_mode = data["country"].mode()[0]
data["country"].fillna(country_mode, inplace=True)
# Filling missing values in 'date_added' with mode
mode_data = data["date_added"].mode()[0]
data["date_added"].fillna(mode_data, inplace=True)
# Filling missing values in 'rating' with mode
rating_mode = data["rating"].mode()[0]
data["rating"].fillna(rating_mode, inplace=True)
# Filling missing values in 'duration' with mode
duration_mode = data["duration"].mode()[0]
data["duration"].fillna(duration_mode, inplace=True)
# Filling missing values in 'listed_in', 'director', and 'cast' with 'not mentioned'
data["listed_in"].fillna("not mentioned", inplace=True)
data["director"].fillna("not mentioned", inplace=True)
data["cast"].fillna("not mentioned", inplace=True)
# Replace rating categories with standardized values
data["rating"] = data["rating"].replace({
    "TV-PG": "PG", "TV-MA": "MA", "TV-Y7-FV": "PG", "TV-Y7": "PG",
    "TV-14": "PG-13", "R": "R", "TV-Y": "G", "NR": "NR", 
    "PG-13": "PG-13", "UR": "UR", "TV-G": "G", "PG": "PG", 
    "G": "G", "NC-17": "NC-17"
})
# Removing commas from 'date_added'
data["date_added"] = data["date_added"].str.replace(",", "", regex=False)
# Converting 'date_added' to datetime format
data["date_added"] = pd.to_datetime(data["date_added"], format="mixed")
# Extracting year, month, and day from 'date_added'
data["year_added"] = data["date_added"].dt.year
data["month_added"] = data["date_added"].dt.month_name()
data["day_added"] = data["date_added"].dt.day
# Extracting the first value from 'listed_in' column
data["listed_in"] = data["listed_in"].apply(lambda x: x.split(",")[0])
# Remove rows where 'cast' is 'not mentioned'
data = data[data["cast"] != "not mentioned"]
# Extracting the first value from 'cast' as 'lead_actor'
data["lead_actor"] = data["cast"].apply(lambda x: x.split(",")[0])
# Dropping unnecessary columns
data.drop(["date_added", "cast"], axis=1, inplace=True)
# Final dataframe sample
print("Sample Data:", data.sample(5))
# Dataframe with types equal to "Movie"
movies_data = data[data["type"] == "Movie"].copy()
# Extracting numerical part of 'duration' and saving it to 'duration_min' column
movies_data["duration_min"] = movies_data["duration"].apply(lambda x: int(x.split(" ")[0]))
# Dropping 'duration' column
movies_data.drop(["duration"], axis=1, inplace=True)
# Sample movie data
print("Movies Data Sample:", movies_data.head(5))
# Dataframe with types equal to "TV Show"
tv_show_data = data[data["type"] == "TV Show"].copy()
# Extracting numerical part of 'duration' and saving it to 'duration_season' column
tv_show_data["duration_season"] = tv_show_data["duration"].apply(lambda x: int(x.split(" ")[0]))
# Dropping 'duration' column
tv_show_data.drop(["duration"], axis=1, inplace=True)
# Sample TV Show data
print("TV Show Data Sample:", tv_show_data.head(5))
# Count of unique values in 'listed_in' (genres)
print("Top 5 genres:", data["listed_in"].value_counts().head(5))
# Count of unique values in 'rating' column
print("Top 5 ratings:", data["rating"].value_counts().head(5))
# Count of unique values in 'release_year' column
print("Top 5 release years:", data["release_year"].value_counts().head(5))
# Count of unique values in 'country' column
print("Top 5 countries:", data["country"].value_counts().head(5))
print(data)
# count of unique values in the genre column 
print("Top 5 genres:", data["listed_in"].value_counts().head(5))
# setting polt style to ticket
sns.set_style("ticks")
# no of tv shows and movies avaiable  on netflix
fig,ax=plt.subplots(figsize=(12,6))
ax=sns.countplot(data=data,x="type",color="#00FFFF"
                 ,order=data["type"].value_counts().index)
ax.set_title(
    "no.of tv shows and movies avaiable on netflix")
ax.bar_label(ax.containers[0],fontsize=15)
plt.show()
# no of shows in each rating category
fig,ax=plt.subplots(figsize=(12,6))
ax=sns.countplot(data=data,x="rating",color="#00FFFF",
                 order=data["rating"].value_counts().index)
ax.set_title("no.of shows in each rating category")
ax.bar_label(ax.containers[0],fontsize=10)
plt.show()
# no of shows upload on netflix in each year
fig,ax=plt.subplots(figsize=(12,6))
ax=sns.countplot(data=data,x="year_added",color="Green",
                 order=data["year_added"].value_counts().index)
ax.set_title("no.of shows upload on netflix in each year")
ax.bar_label(ax.containers[0],fontsize=15)
plt.show()
# no of shows upload on netflix in each month
fig,ax=plt.subplots(figsize=(12,6))
ax=sns.countplot(data=data,x="month_added",color="#E50914",
                 order=data["month_added"].value_counts().index)
ax.set_title("no.of shows upload on netflix in each month")
plt.show()
# no of shows upload on netflix in each day
fig,ax=plt.subplots(figsize=(12,6))
ax=sns.countplot(data=data,x="day_added",color="#FF69B4",
                 order=data["day_added"].value_counts().index)
ax.set_title("no.of shows upload on netflix in each day")
ax.bar_label(ax.containers[0],fontsize=10)
plt.show()
# no of moives ralsed on netflix in each genre
fig,ax=plt.subplots(figsize=(12,6))
ax=sns.countplot(data=data,x="listed_in",color="Red",
                 order=data["listed_in"].value_counts().index)
ax.set_title("no.of moives ralsed on netflix in each genre")
ax.bar_label(ax.containers[0],fontsize=10)
plt.show()
# no of movies for a lead actor on netflix
actor_count_movies=movies_data["lead_actor"].value_counts().head()
fig,ax=plt.subplots(figsize=(12,6))
ax=sns.barplot(x=actor_count_movies.index,
               y=actor_count_movies.values,color="Blue")
ax.set_title("no of Movies for a lead actor on netflix")
ax.tick_params(axis="x",rotation=90)
ax.bar_label(ax.containers[0],fontsize=10)
plt.show()
# no of tv shows for a lead actor on netflix
actor_count_tv_show=tv_show_data["lead_actor"].value_counts().head()
fig,ax=plt.subplots(figsize=(12,6))
ax=sns.barplot(x=actor_count_tv_show.index,
               y=actor_count_tv_show.values,color="#c81b91")
ax.set_title("no of tv shows for a lead actor on netflix")
ax.tick_params(axis="x",rotation=90)
ax.bar_label(ax.containers[0],fontsize=10)
plt.show()
# avg.length of movies in each Genre
genre_duration=movies_data.groupby("listed_in")["duration_min"].mean().sort_values(ascending=False).head(10)
fig,ax=plt.subplots(figsize=(12,6))
ax=sns.barplot(x=genre_duration.index,
               y=genre_duration.values,color="#96EC2B")
ax.set_title("avg.length of movies in each Genre")
ax.tick_params(axis="x",rotation=90)
ax.bar_label(ax.containers[0],fontsize=10)
plt.show()
# length of TV shows in each genre
genre_duration_tv_show=tv_show_data.groupby("listed_in")["duration_season"].mean().sort_values(ascending=False).head(10)
fig,ax=plt.subplots(figsize=(12,6))
ax=sns.barplot(x=genre_duration_tv_show.index,
               y=genre_duration_tv_show.values,
               color="#FF69B4")
ax.set_title("length of TV shows in each genre")
ax.tick_params(axis="x",rotation=90)
ax.bar_label(ax.containers[0],fontsize=10)
plt.show()
# duration of length of movies on netflix
fig,ax=plt.subplots(figsize=(12,6))
ax=sns.kdeplot(data=movies_data,x="duration_min"
                ,color="#2B35EC",fill=True)
ax.set_title("duration of length of movies on netflix")
plt.show()
# distribution of seasons of tv shows on netflix
fig,ax=plt.subplots(figsize=(12,6))
ax=sns.kdeplot(data=tv_show_data,x="duration_season",
                color="#FF69B4",fill=True)
ax.set_title("distribution of seasons of tv shows on netflix")
plt.show()