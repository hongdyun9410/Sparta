from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta



## 코딩 할 준비 ##

target_movie = db.movies.find_one({'title':'매트릭스'})
target_point = target_movie['point']

movies = list(db.movies.find({'point':target_point}))

for movie in movies:
    print(movie['title'])

tartget_update = db.movies.update_one({'title':'매트릭스'},{'$set':{'point':'0'}})
print(tartget_update);