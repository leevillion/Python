import os

class Searchfile:

    '查找指定盘符下指定文件'

    def __init__(self,file_name):
        #self.drive=drive
        self.file_name=file_name
        self.position=[]  #存放目标文件完全路径

    def search(self,search_dir):
        '递归查找'

        if os.path.isdir(search_dir):
            try:
                filename=os.listdir(search_dir)
                #d=search_dir
                for i in filename:
                    if self.file_name==i:
                        self.position.append(os.path.join(search_dir,i))
                        return os.path.join(search_dir,i)
                        #print(os.path.join(search_dir,i))
                    else:
                        self.search(os.path.join(search_dir,i))
            except:
                print(os.path.split(search_dir))


##c=Searchfile('FA_安装包_20121119')
##c.search('E:\\')








