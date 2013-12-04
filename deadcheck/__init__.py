from deadcheck import Deadcheck
d = Deadcheck('<url>')
d.process()
for key in d.getAll().keys():
    for element in d.getAll()[key]:
        print str(key) + ' --- ' + element.get()[0] + ' -- > ' + str(element.isBroken()) + ' ---- > ' + str(element.isProcessed())