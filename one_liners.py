# Creating objects
myInf = type('myInf',(object,),{'__repr__':lambda self: 'bazinga'})
'''
type[0] is the object name (seen when doing `myInf`)
type[1] is i dont know dont mess with it
type[2] is a dictionary with `propertyName:propertyValue`s
'''

# if else (also runs print if the program is being run (not imported or anything else))
print('hi') if __name__ == '__main__' else None

# list
[ord(x) for x in 'hello world']
# list with if
[ord(x) for x in 'hello world' if not x == 'o']
# list with if else
[ord(x) if not x == 'o' else 'kachow' for x in 'hello world']

# list comprehension with 2 fors
[x+y for x in range(1,10) for y in range (10,20)]

# dict
{str(a):a*a for a in range(10)}
# dict with if
{str(i):True for i in range(10) if not i == 3}
# dict with if else
{str(x):(x*2 if not x == 3 else "walahi") for x in range(10)}

# functions
def sayhello(name): print('hello',name)
# lambda (not really a function)
sayhello = lambda name: print('hello',name) # will return None
# multi-line functions (just dont - it doesnt even count really)
exec('def say2hellos(name1,name2):\n\tprint("hello",name1)\n\tprint("wassup",name2)')

# get input or default (I put it in a function so it wouldn't automatically run)
getname = lambda: input('Your name: ') or 'Marcus'

# here's a one-liner quine (sorta)
_='_=%r;print(_%%_)';print(_%_)

# heres the := operator in python 3.7
(globals().update({'example':27}) or globals()['example']) # returns 27
# heres an example of it as a lambda function 
setglobal = lambda name,value: globals().update({name:value}) or globals()[name]
# you can also get or set a variable like so
globals().get("is_this_defined", (globals().update({'is_this_defined':'it is now'}) or globals()['is_this_defined']))

# this dumb shit
print("hi",[(print("hi",i) or i+1) for i in range(10)].__len__())