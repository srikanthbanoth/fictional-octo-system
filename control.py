'''
    control flow statementa
    if ...elif...else(optional)

    python for iterate over the sequence
'''

names=['banoth','srikanth']

for name in names:
    print(name)

'''
When you modify a collection while
iterating either copy it or create new collection
'''
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

for key,value in users.copy().items():
    if value=='inactive':
        del users[key]
#iterating over an copy and deleting from the main collection

print(users)


#create a new collection

active_users={}
for key,value in users.items():
    if value=='active':
        active_users[key]=value

print(active_users)

print(list(range(10)))

#pass does nothing
def match_reqcode(status):
    match status:
        case 200:
            return 'Ok Request'
        case _:
            return 'Default Request'

print(match_reqcode(200))
print(match_reqcode(201))
