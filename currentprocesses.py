def process():
    import os
    import psutil
    print(psutil.pids())
    print(os.getpid())
    print(os.system('C:/Users/Admin'))
    f = open("C:\ProcessList.txt")
    plist = f.read
    print(plist)
process()