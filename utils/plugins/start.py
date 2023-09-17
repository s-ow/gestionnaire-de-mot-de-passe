def createmdpfile():
    with open('mdps.txt', 'a+') as filemdp:
        filemdp.seek(0)
        content = filemdp.read()

        if not content:
            filemdp.write("{" + "}")