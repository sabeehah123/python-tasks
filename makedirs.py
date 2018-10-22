def pymkdirs():
    import os
    root_path = '/Users/Admin/PycharmProjects/helloworld/'
    folders = ['dir1', 'dir2', 'dir3']
    for folder in folders:
        os.mkdir(os.path.join(root_path, folder))

pymkdir()