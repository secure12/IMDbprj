#!/usr/bin/env python3
import requests
import json

def IMDb_query_url(id):
    # the returned query url for id='tt0407887' should be 'http://www.omdbapi.com/?i=tt0407887&plot=short&r=json'
    return 'http://www.omdbapi.com/?i='+id+'&plot=short&r=json'

def get_movie_ids(input_file):
    # the returned list should like ['tt0407887', 'tt1212123', ... ]
    id_list = []
    with open(input_file, 'r') as f:
        for line in f:
            id_list.append(line[:-1])
    return id_list
    
def get_all_data(in_file, out_file):
    movie_data_dict = {}
    movie_ids = get_movie_ids(in_file)

    id_counter = 0
    session = requests.Session()
    for id in movie_ids:

        url = IMDb_query_url(id)
        print id_counter, url
        # start writing your code here
        # get movie data using the session.get(url).json()
        try:
            movie_data = session.get(url).json()
            # you may need to handle some exceptions here
        
            movie_data_dict[id_counter] = movie_data
            id_counter += 1
        except:
            print "get", url, "failed!"

        # don't change any code below this line
        with open(out_file, 'w+') as f:
            json.dump(movie_data_dict, f)
        
if __name__ == '__main__':
    # don't change any code below this line
    movie_id_file = r'../IMDbIDCrawler/movie_ids06-15'
    movie_data_file = 'IMDb2006-2015.json'
    get_all_data(movie_id_file, movie_data_file)
