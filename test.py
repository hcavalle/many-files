for i in range (1, 5000):
    f = open(str(i) + '.out', 'w')
    print "writing file " + str(i) + ".out"
    f.write(str(i))
    f.close()


