# coding: utf-8
import json
with open(r'./IMDb_data/IMDb2006-2015.json', 'r+') as f:
    movie_dict = json.load(f)
i = 0
movie_to_actors={}
actor_to_movies={}
while (movie_dict.has_key(str(i))):
    print i
    try:
        movie_id = movie_dict[str(i)]["imdbID"]
        actors_name = movie_dict[str(i)]["Actors"].encode("UTF-8").split(', ')
    except:
        i += 1
        continue
    movie_to_actors[movie_id] = actors_name
    for name in actors_name:
        if actor_to_movies.has_key(name):
            actor_to_movies[name].append(movie_id)
        else:
            actor_to_movies[name] = [movie_id]
    i += 1
with open("bipartitegraph.json", "w+") as f:
    json.dump({'movie_to_actors':movie_to_actors,'actor_to_movies':actor_to_movies}, f, indent=4, separators=(',', ':'), sort_keys=False)
