'''varone = ''

varone = 'hello'

print(varone)

tempvar = varone

print(tempvar)

varone = ''

print(varone)

print(tempvar + 'tempvar')'''

my_func = lambda x : x**2
print(my_func(4))

L = [ 0 , 10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
res = L [:: -1]
print(res)

words = [' one ', ' one ', ' two ', ' three ', ' three ', ' two ']
#unique = set(words)
#unique.add('five')
used = set()
unique = [x for x in words if x not in used and (used.add(x) or True)]
print(unique)


def extendList(val, list=[]):
    list.append(val)
    return list


list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('a')

print("list1 = %s" % list1)
print("list2 = %s" % list2)
print("list3 = %s" % list3)

r = []
un = [j for j in words if not (j in r or r.append(j)) ]
print(un)
print(type(r))
