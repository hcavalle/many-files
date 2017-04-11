import os
from shutil import rmtree

for i in range (0, 10):
    if not os.path.exists(str(i)):
        os.makedirs(str(i))    
    else:
        for n in range (0, 1100):
            file = "{}/{}".format(str(i),str(n))
            f = open(file + '.out', 'w+')
            print "writing file " + str(i) + ".out"
            f.write(str(i))
            f.close()
        # pass
        # rmtree(str(i))


