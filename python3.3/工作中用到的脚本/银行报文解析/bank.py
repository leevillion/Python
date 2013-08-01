from xml.etree import ElementTree as E
from functools import reduce
from trans_gbk_to_utf_test import Trans_g_to_u

dicter={'BNKACC':'银行帐号','ETYDAT':'交易时间','TRSAMTD':'借方金额','TRSAMTC':'贷方金额',
        'TRSBLV':'余额','RPYACC':'对方帐号','AMTCDR':'借贷标志'}
print('%-15s%-8s%-10s%-10s%-8s%-12s%-15s' % (dicter['BNKACC'],dicter['ETYDAT'],dicter['TRSAMTD'],
        dicter['TRSAMTC'],dicter['AMTCDR'],dicter['TRSBLV'],dicter['RPYACC'],))

TRSAMTD=[]  #保存借方金额
TRSAMTC=[]  #保存贷方金额
perinfo={}  #保存每一笔交易信息


def getinfo(node):
    '获得每个节点的信息并储存'

    if node.tag in dicter:
        #print(dicter[node.tag]+':'+node.text)
        if node.tag=='TRSAMTD':
            TRSAMTD.append(float(node.text)) #将字符串类型转为浮点型，方便reduce计算总额
        elif node.tag=='TRSAMTC':
            TRSAMTC.append(float(node.text))
        perinfo[node.tag]=node.text



def read_file(file_path,target_file):
    global preinfo
    t=Trans_g_to_u()
    t.trans_xml(file_path,target_file)
    tree=E.parse(target_file)
    root=tree.getroot()
    for child in root.findall('SDKRSP'):
        for node in child.getchildren():
            getinfo(node)

        print('%-20s%-10s%-15s%-15s%-12s%-12s%-15s' % (perinfo['BNKACC'],perinfo['ETYDAT'],perinfo['TRSAMTD'],
                perinfo['TRSAMTC'],perinfo['AMTCDR'],perinfo['TRSAMTC'],perinfo['RPYACC'],))

        preinfo={}

    print (reduce(lambda x,y:x+y,TRSAMTD),reduce(lambda x,y:x+y,TRSAMTC))


if __name__=='__main__':
    read_file('E:\Code\GitHub\Python\python3.2\工作中用到的脚本\银行报文解析\ABC\\ABC.xml',
                'E:\Code\GitHub\Python\python3.2\工作中用到的脚本\银行报文解析\ABC\\ABC2.xml')
#a=input('按任意键继续')
