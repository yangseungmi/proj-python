import os
##print('listdir:',os.listdir(os.getcwd()))
##print('isdir:',os.path.isdir('/Users/mac/Documents/IdeaProject/proj-python/python'))

for dname in os.listdir(os.getcwd()):
    print(os.path.join(os.getcwd(),dname))