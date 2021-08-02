# one.py

def func():
    print("FUNC() IN ONE.PY")

print("TOP LEVEL IN ONE.PY")

def func1():
    pass

def func2():
    pass

# In Python there is a builtin variable called `name`.
if __name__ == "__main__":
#     print('ONE.PY is being run directly!')
# else:
#     print('ONE.PY has been imported!')
    func1()
    func2()
