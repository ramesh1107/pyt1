
import os

'''path = '/Users/Ramesh/Pgms/python/day24'
f= '/Users/Ramesh/Pgms/python/day24/tes.txt'
isExist = os.path.exists(path)
isFile =os.path.isfile(f)
print(f"the path is - {isExist}")
print(f"the file is - {isFile}")
'''


with open ('/Users/Ramesh/Pgms/python/day24/test.txt', mode ="w") as file:
    file.write("\nhello kris wanna have fun with me")
with open ('/Users/Ramesh/Pgms/python/day24/test.txt', mode ="r") as file:
    cont= file.read()
    print(cont)
    
