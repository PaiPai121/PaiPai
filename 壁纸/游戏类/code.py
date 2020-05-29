import os
import random
 
names = ['.jpg','.png'] # 需要随机替换的后缀名列表
 
def test(path):
    files = os.listdir(path)  # 获取当前目录的所有文件及文件夹
    t= 0
    i=0
    for file in files:
        t+=1
        file_path = os.path.join(path, file)  # 获取绝对路径
        if os.path.isdir(file_path):  # 判断是否是文件夹
            test(file_path)  # 如果是文件夹，就递归调用自己
        else:
            #print(file_path)
            extension_name = os.path.splitext(file_path)  # 将文件的绝对路径中的后缀名分离出来
            print(extension_name)
            if extension_name[1] in names:
                print(path+"\\" + str(i)+extension_name[1])
                #os.rename(file_path, path + "\\" + str(i) + extension_name[1])  # 对文件进行重命名
                os.rename(file_path, path + "\\" + str(i) + '.jpg') 
                i+=1
                print(i)

test(r"D:\GH\MyWeb\MyWeb\壁纸\游戏类")