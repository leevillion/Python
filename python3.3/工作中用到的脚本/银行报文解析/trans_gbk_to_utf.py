﻿##import codecs,re
##f = codecs.open('E:\Code\GitHub\python3.2\\ABC.xml', 'rb', 'mbcs')
##text = f.read().encode('utf-8')
##text = re.sub(b'encoding="GBK"',b'encoding="UTF-8"',text)
##f.close()
##f = open('E:\Code\GitHub\python3.2\\ABC_utf.xml', 'wb')
##f.write(text)
##f.close()
###print text.decode('utf-8').encode('gbk')




from trans_gbk_to_utf_test import Trans_g_to_u

t=Trans_g_to_u()
t.trans_txt('E:\Code\GitHub\Python\python3.3\自己写着玩的小程序\SAX模块解析XML\\website.txt',
            'E:\Code\GitHub\Python\python3.3\自己写着玩的小程序\SAX模块解析XML\\website2.xml')
