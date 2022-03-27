from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# 코딩 시작
#insert
#doc = {'name':'jane','age':30}
#db.users.insert_one(doc)


#select
#same_ages = list(db.users.find({'age':21},{'_id':False}))
#same_ages = list(db.users.find({},{'_id':False}))
#for person in same_ages:
#    print(person)


#select_one
#user = db.users.find_one({'name':'bobby'},{'_id':False})
#print(user)


#UPDATE
#db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

#update_many는 조건이 XX인 경우 모든 XX의 값을 YY로 바꿔줘라
#oracle의 경우 where을 걸지않고 update를 할경우 전부바뀌는게 update_many라고 보면되겟다

#Delete
db.users.delete_one({'name':'bobby'})

#delete_many도 존재한다 위험하다..

# 저장 - 예시
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
same_ages = list(db.users.find({'age':21},{'_id':False}))

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})





