estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


def iterateDictionary(estudiantes):
    for x in range(len(estudiantes)):
     print("first_name  "+estudiantes[x]['first_name']+", last_name  "+estudiantes[x]['last_name'])

iterateDictionary(estudiantes)

