'''
What this program actually does: it's not important shut up

Why it's cool:
    utilizing the power of my inline_with-inator, i can do this:
        with x:
            print(something)
    like this:
        inline_with(x,lambda: print(something))

Yes but why?
see line 43 and behold

Okay so what does the program do tho?
Well there are some comments but the gist of it is that every time it's run, it... i cant even explain it
'''

import random

strlist = list('marcus weinberger')

def inline_with(ctx, fn): # here's the function that lets u do it
    with ctx:
        return fn()

class Test(object): # example object with context
    def __init__(self, rdict):
        self.rdict = rdict
    def __enter__(self):
        for x in self.rdict:
            globals()[self.rdict[x]] = x
    def __exit__(self, *args):
        for x in self.rdict:
            del globals()[self.rdict[x]]

tryExcept = (type('TE',(object,),{'__enter__':lambda s:None,'__exit__':lambda *args:True}))() # try/except using with

ctxList = []
while len(ctxList) < 5:
    ctx = Test({random.choice(strlist):random.choice(strlist)})
    ctxList.append(ctx) # making a bunch of test objects with context

a = [inline_with(ctx,lambda: inline_with(tryExcept, lambda: print(globals()[random.choice(strlist)]))) for ctx in ctxList] # and tadaa


'''
PS: https://stackoverflow.com/a/57315502/8291579 ETA SON
'''