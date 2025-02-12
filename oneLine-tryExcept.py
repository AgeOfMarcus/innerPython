class tryExceptManager:
    def __enter__(self): pass
    def __exit__(self, *args): return True

# initialize it
tryExcept = tryExceptManager()

# if there is an error, the variable wont exist
with tryExcept: testvar = notAFunction()
print('testvar' in globals()) # False

# if there is no error, then the variable is created
with tryExcept: testvar = int(35 / 5)
print('testvar' in globals()) # True
print(testvar) # 7