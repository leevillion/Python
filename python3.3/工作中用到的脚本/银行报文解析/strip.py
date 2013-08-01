class Tripspace:
    def getline(self,file_path):
        '获得行生成器'
        f=open(file_path)
        for line in f.readlines():
            yield line
        yield '\n'
    def getblock(self,file_path):
        '去除空格'
        block=[]
        for i in self.getline(file_path):
            if i.strip():
                block.append(i[:-1])
        return ''.join(block)

    def main(self,file_path,target_path):
        f=open(target_path,'w')
        text=self.getblock(file_path)
        f.write(text)
        f.close()
##if __name__=='__main__':
##    main('E:\Code\GitHub\Python\python3.2\工作中用到的脚本\银行报文解析\ICBC\\ICBC1.xml',
##           'E:\Code\GitHub\Python\python3.2\工作中用到的脚本\银行报文解析\ICBC\\ICBC2.xml')
