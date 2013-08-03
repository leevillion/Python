import os,csv,re
from find_file import Searchfile

class Getsqlinfo(Searchfile):

    def __init__(self,file_name):
        self.scriptfile_name={}
        self.sql_name={}  #存储脚本文件，键值对
        #super(Match,self).__init__()
        Searchfile.__init__(self,file_name)

    def get_filename(self,drive):
        '获得script子文件内容'
        self.search(drive)
        self.file_path=self.position[0]

        for prefilename in os.listdir(self.file_path):
            if os.path.isdir(os.path.join(self.file_path,prefilename)):
                self.scriptfile_name[prefilename]=os.listdir(self.file_path+'\\'+prefilename)
            else:
                self.scriptfile_name[prefilename]=prefilename

    def get_scriptname(self,drive):
        self.get_filename(drive)
        for i in self.scriptfile_name['scripts']:
            self.sql_name[i]=os.listdir(self.position[0]+'\\'+'scripts'+'\\'+i)

class Getcsvinfo:

    def __init__(self):
        self.csv=[]
        self.csv_scripts=[] #存储csv文件中脚本路径值
        self.count=2

    def get_csv(self,file_path):
        f=open(file_path)
        c=csv.reader(f)
        for line in c:
            self.csv.append(line)
        while self.count<len(self.csv)-7:
            self.csv_scripts.append(self.csv[self.count][4])
            self.count+=1



def match():

    M=Getsqlinfo('FA_安装包_20121119')
    M.get_scriptname('E:\\')
    N=Getcsvinfo()
    N.get_csv('E:\\release.csv')

    match_pattern=re.compile(r'.*\\(.*)\\(.*\.[a-z]{3})') #生成匹配模式对象
    for member in N.csv_scripts:
        match_result=match_pattern.match(member)
        if match_result:
            if match_result.group(1) in M.sql_name and match_result.group(2) in M.sql_name[match_result.group(1)]:
                pass
            else:
                print(match_result.group(1)+'\\'+match_result.group(2))

if __name__=='__main__':
    match()





