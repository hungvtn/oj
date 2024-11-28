import os, shutil
from random import randint
from pathlib import Path
from time import sleep


nameProblem = 'hello'
numTest = 20

def mkTest(pathFolder, nameProblem):
    with open(f"{pathFolder}/{nameProblem}.inp", 'w') as g:
        a = randint(10, 100)
        b = randint(10, 100)
        g.write(f'{a} {b}\n')
    with open(f"{pathFolder}/{nameProblem}.out", 'w') as g:
        g.write(f'{a + b}\n')


pathFolder = f'test/{nameProblem}'
if (os.path.isdir(pathFolder)):
    shutil.rmtree(pathFolder)
os.mkdir(pathFolder)
    

for i in range(1, numTest + 1):
    pathFolder = f'test/{nameProblem}/test'
    if (i < 10):
        pathFolder += '0' + str(i)
    else:
        pathFolder += str(i)
    p = Path(pathFolder)
    p.mkdir(exist_ok = 1)
    # make test
    mkTest(pathFolder, nameProblem)
    
    