def getline(file_path):
    '获得行生成器'
    f=open(file_path)
    for line in f.readlines():
        yield line
    yield '\n'
def getblock(file_path):
    '获得完整SQL语句'
    block=[]
    a=[]
    for i in getline(file_path):
        if i.strip():
            block.append(i.strip('\n'))
            if block[-1][-1]!=';':
                a.append(i.strip('\n'))
                del block[-1]
            elif block[-1][-1]==';':
                del block[-1]
                a.append(i.strip('\n'))
                block.append(''.join(a).strip())
                del a[:]
    return block

def main(file_path,target_path):
    f=open(target_path,'w')
    for text in getblock(file_path):
        f.write(text)
        f.write('\n')
    f.close()

if __name__=='__main__':
    main('E:\\Sequence_FINUPDATE_NUMBER.sql','E:\\1.sql')
