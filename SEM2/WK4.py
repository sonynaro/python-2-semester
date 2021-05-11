setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''

stmt = 'func_one(100)'

timeit.timeit(stmt,setup,number=100000)