import pandas as pd, numpy as np, webbrowser

# to read the dataset into a data table using pandas
df = pd.read_csv("ratings.csv")

# convert the running list of user ratings into a matrix the "pivot table" function
ratings_df = pd.pivot_table(df, index="userId", columns="movieId", aggfunc=np.max)

#  create a web page view of the data easy viewing
html = ratings_df.to_html(na_rep="")

# save the html to a temporary file
with open("review_matrix.html", "w") as f:
    f.write(html)

# open the web page in our web browser
full_filename = "C:/Users/Zakariya'u/Dropbox/Web_Engine_Project/Implementation/lyndaRS/create_review_matrix.html"
webbrowser.open("file://{}".format(full_filename))
