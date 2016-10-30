import re
import json
f = open(r'./IMDb_data/IMDb2006-2015.json', 'r+')
for line in f:
    movie_detail_list=line.split('}')
movie_to_actors={}
actor_to_movies={}
for i in movie_detail_list:
    if re.search('\S', i):
        movie_id=re.findall('"imdbID":"(tt[0-9]*?)"',i)[0]
        actors_name=re.findall('"Actors":"(.*?)"',i)[0].split(', ')
        movie_to_actors[movie_id]=actors_name
        for name in actors_name:
            if actor_to_movies.has_key(name):
                actor_to_movies[name].append(movie_id)
            else:
                actor_to_movies[name]=[movie_id]
bipartitegraph={'movie_to_actors':movie_to_actors,'actor_to_movies':actor_to_movies}
