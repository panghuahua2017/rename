import time,os
path = "/Users/apple/同步空间/娃/日期未修正" #待搜索的目录路径
file_list = os.listdir(path) #遍历path里的所有文件名
count = len(file_list)
print(f'文件夹{path}里共有{count}个文件')
chongming = []
for file in file_list:
    cur_path = os.path.join(path, file)
    print(file, end='')
    if 'DS_Store' in cur_path:
        print(',这是mac系统文件')
    else:
        imgPath = cur_path
        ImageDate = time.localtime(os.stat(imgPath).st_mtime)
        c_time = time.strftime("%Y-%m-%d %H点%M分%S秒",ImageDate)
        print(f'｜创建时间：{c_time}',end='')
        filetype = file.split('.')[-1] #提取文件后缀名
        new_name = c_time+'.'+filetype

        file_list = os.listdir(path) #再次获取文件夹里的文件名，用于比对是否重复

        if new_name in file_list:
            print(f'｜已有同名文件')
            chongming.append(file)
        else:
            os.chdir(path)
            os.rename(file, new_name)
            print('｜已重命名')

print(f'执行完毕，重命名失败文件:{chongming}')