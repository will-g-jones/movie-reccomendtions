#Program to recommend similar movies based on the description, and return the name of the most similar movie.

#Loads space and imports the md english analysis tool.
import spacy
nlp = spacy.load('en_core_web_md')

#this section will define the list of movies and the comparator value, which will be used to find the most similar movie, and a placeholder to track this movie title.
movie_list = []
comparator_value = 0
most_similar_movie_title = ""

with open('movies.txt', 'r+') as inventory_file:
    for line in inventory_file:
        line = line.strip("\n")
        movie_list.append(line)

#This defines the movie to compare.
movie_watched = u"""Planet Hulk  :Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle
and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."""

#This will take the movie watched and include only the description
movie_to_compare = nlp(movie_watched[14::])
#this will iterate through each movie in the movie_list, and first select only the description of the movie
for movie in movie_list:
    movie_desc = nlp(movie[9::])
    
    #This will measure the similarity between the description of the hulk movie and each other movie.
    similarity = nlp(movie_desc).similarity(movie_to_compare)

    #This will check the similarity aagainst the comparator value, which starts at 0. If the similarity value is higher, the new value is saved and the
    #movie name is recored. Should another movie description tested have higher similarity, this will be overwritten.
    if similarity > comparator_value:
        comparator_value = similarity
        most_similar_movie_title = movie[0:7]
    else:
        continue

#This will print the next recommened movie based on the similarity.
print(f"The movie we think you'd enjoy the most is: {most_similar_movie_title}")