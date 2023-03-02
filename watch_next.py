# imported the spacy libraries and use 'en_core_web_md' as it is a large dataset
import spacy
nlp = spacy.load('en_core_web_md')

# the movie that suggestions for a similar movie should come from
planet_hulk = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator"
nlp_planet_hulk = nlp(planet_hulk)

# created an empty list called movies
movies = []

# reads from movies.txt
with open('movies.txt', 'r') as f:
    for line in f:
        movies.append(line[9::])
        
        # split and strip to make the lines readable
        '''line = line.split()
        line[2] = line[2].strip(':')
        movies.append(line[2::])'''

# created a function called watch_next
def watch_next(x):
    # created another list called ratings that gets similarity through spacy
    ratings = []

    # goes through the movies
    for movie in movies:
        similarity = nlp(movie).similarity(nlp_planet_hulk)
        ratings.append(similarity)

    # fetches the index of the most similar movie
    most_similar_movies = max(ratings)
    index = ratings.index(most_similar_movies)

    return print(f"based on what you've liked and previously watched, the suggested movie is {index + 1}. And the description is: {movies[index]}")

#run function
watch_next(nlp_planet_hulk)