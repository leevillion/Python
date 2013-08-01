import os
import shutil
os.remove('D:\website\TMI\bin\\web.config')

shutil.copyfile('D:\website\TMI\bin\\BAF.TMI.Application.BLL.dll',
                'D:\website\TMI\\BAF.TMI.Application.BLL.dll')
shutil.copyfile('D:\website\TMI\bin\\BAF.TMI.Application.Common.dll',
                'D:\website\TMI\\BAF.TMI.Application.Common.dll')
shutil.copyfile('D:\website\TMI\bin\\BAF.TMI.Application.DAL.dll',
                'D:\website\TMI\\BAF.TMI.Application.DAL.dll')
shutil.copyfile('D:\website\TMI\bin\\BAF.TMI.Application.Entity.dll',
                'D:\website\TMI\\BAF.TMI.Application.Entity.dll')
shutil.copyfile('D:\website\TMI\bin\\BAF.TMI.Application.Model.dll',
                'D:\website\TMI\\BAF.TMI.Application.Model.dll')
shutil.copyfile('D:\website\TMI\bin\\BAF.TMI.Application.Web.dll',
                'D:\website\TMI\\BAF.TMI.Application.Web.dll')
shutil.copyfile('D:\website\TMI\bin\\BAF.TMI.Application.SearchObject.dll',
                'D:\website\TMI\\BAF.TMI.Application.SearchObject.dll')

