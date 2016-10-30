f = open("movie_ids06-15", 'r')
l = []
id_count = 0
for line in f:
    if id_count % 10000 == 0:
        l.append(open("movie_ids06-15." + str(len(l)), 'w'))
    id_count += 1
    l[-1].write(line)
