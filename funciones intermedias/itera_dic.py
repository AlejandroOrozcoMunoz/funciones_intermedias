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

def iterateDictionary2(nombre, estudiantes):
    for x in range(len(estudiantes)):
        print(estudiantes[x][nombre])
iterateDictionary2('first_name',estudiantes)
iterateDictionary2('last_name',estudiantes)

def printInfo(some_dict):
    for key in some_dict:
        print(len(some_dict[key]),key)
        for i in range(len(some_dict[key])):
            print(some_dict[key][i])
        print("")

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)

