import os

for i in range (1, 1000):
    if not os.path.exists(str(i)):
        os.makedirs(str(i))    
    for n in range (1, 1100):
        file = "{}/{}".format(str(i),str(n))
        f = open(file + '.out', 'w+')
        print "writing file " + str(i) + ".out"
        f.write(str(i))
        f.close()


