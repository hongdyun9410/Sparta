#der == function
#def is_adult(age):
#    if age>20:
#        return print("성인입니다")
#    else:
#        return print("청소년입니다")


#is_adult(30)
#is_adult(15)


##반복문
#fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']
#count =0
#for ff in fruits:
#    if ff =='수박':
#        count += 1

#print(count)

people = [{'name': 'bob', 'age': 20},
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

for person in people:
    if person['age'] <20:
        print(person)