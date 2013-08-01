from xml.dom.minidom import Document


class CreatXML:
    '定义创建XML类，支持添加、赋值方法'
    def __init__(self,file_path):
        self.doc=Document()
        self.path=file_path
    def createnode(self,node):
        return self.doc.createElement(node)
    def addnode_to_father(self,node,father_node):
        '添加节点，与前一节点关联'
        current_node=node
        if father_node is not None:
            father_node.appendChild(current_node)
        else:
            self.doc.appendChild(current_node)
    def setnode_value(self,node,value):
        '值与标签关联'
        node.appendChild(self.doc.createTextNode(value))


if __name__=='__main__':

    '生成测试数据'
    try:
        dict_dat={'BGNDAT':['20120422','20120522','20120622','20120322','20120510'],
                'ENDDAT':['20120422','20120523','20120630','20120429','20120511']}
        bank_xml=CreatXML('E:\Code\GitHub\PythonScript\python3.3\工作中用到的脚本\银行报文生成\\bank.xml')
        root_node=bank_xml.createnode('BAFSDKPGK')
        bank_xml.addnode_to_father(root_node,None)
        first_node=bank_xml.createnode('COMMONINFO')
        bank_xml.addnode_to_father(first_node,root_node)
        first_node_child=bank_xml.createnode('FUNNAM')
        bank_xml.setnode_value(first_node_child,'GetAccountDetail')
        bank_xml.addnode_to_father(first_node_child,first_node)
        first_node_child=bank_xml.createnode('DATTYP')
        bank_xml.addnode_to_father(first_node_child,first_node)
        first_node_child=bank_xml.createnode('FSEQNO')
        bank_xml.setnode_value(first_node_child,'201302600000001')
        bank_xml.addnode_to_father(first_node_child,first_node)
        first_node_child=bank_xml.createnode('BKNBR')
        bank_xml.setnode_value(first_node_child,'CMB')
        bank_xml.addnode_to_father(first_node_child,first_node)

        for i in range(0,5):
            second_node=bank_xml.createnode('SDKREQ')
            bank_xml.addnode_to_father(second_node,root_node)
            second_node_child=bank_xml.createnode('BBKNBR')
            bank_xml.setnode_value(second_node_child,'57')
            bank_xml.addnode_to_father(second_node_child,second_node)
            second_node_child=bank_xml.createnode('BNKACC')
            bank_xml.setnode_value(second_node_child,'571 900288010701')
            bank_xml.addnode_to_father(second_node_child,second_node)
            second_node_child=bank_xml.createnode('BGNDAT')
            bank_xml.setnode_value(second_node_child,dict_dat['BGNDAT'][i])
            bank_xml.addnode_to_father(second_node_child,second_node)
            second_node_child=bank_xml.createnode('ENDDAT')
            bank_xml.setnode_value(second_node_child,dict_dat['ENDDAT'][i])
            bank_xml.addnode_to_father(second_node_child,second_node)
            second_node_child=bank_xml.createnode('LOWAMT')
            bank_xml.addnode_to_father(second_node_child,second_node)
            second_node_child=bank_xml.createnode('HGHAMT')
            bank_xml.addnode_to_father(second_node_child,second_node)
            second_node_child=bank_xml.createnode('AMTCDR')
            bank_xml.addnode_to_father(second_node_child,second_node)
            second_node_child=bank_xml.createnode('STARTTIME')
            bank_xml.addnode_to_father(second_node_child,second_node)
            second_node_child=bank_xml.createnode('NEXTTAG')
            bank_xml.addnode_to_father(second_node_child,second_node)
    except:
        print('error')



    f=open(bank_xml.path,'w')
    #f.write(doc.toprettyxml(encoding="utf-8"))
    bank_xml.doc.writexml(f,encoding='utf-8')
    f.close()

