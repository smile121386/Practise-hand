import shutil
import os


def get_all_path(open_file_path):
    rootdir = open_file_path
    path_list = []
    list1 = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(list1)):
        com_path = os.path.join(rootdir, list1[i])
        # print(com_path)
        if os.path.isfile(com_path):
            path_list.append(com_path)
        if os.path.isdir(com_path):
            path_list.extend(get_all_path(com_path))
    # print(path_list)
    return path_list


def movefile(file_path_list, to_path):
    if os.path.exists(to_path):
        for i in file_path_list:
            shutil.copy(i, to_path)
    else:
        os.mkdir(to_path)
        for i in file_path_list:
            shutil.copy(i, to_path)


file_list = get_all_path(r'D:\q')
movefile(file_list, r'D:\qq')
