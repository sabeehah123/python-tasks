def user():
    from pathlib import Path
    import socket
    import os
    print("Home folder location: ")
    print(str(Path.home()))
    print("Hostname of machine: ")
    print(socket.gethostname())
    print("Current working directory: ")
    print(os.getcwd())
user()