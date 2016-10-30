import py_compile
for i in range(8):
    py_compile.compile("get_movie_data_"+ str(i)+".py")