#-*-<coding=UTF-8>-*-
import wx
import os

class GuiMainFrame(wx.Frame):
    
    def __init__(self):
        wx.Frame.__init__(self,parent=None,id=-1,title="",pos=wx.DefaultPosition,size=wx.DefaultSize)
        panel = wx.Panel(self)
        panel.SetBackgroundColour("White")

        #menu bar
        menubar = wx.MenuBar()
        
        #File menu
        fileMenu = wx.Menu()
        fileMenu.Append(-1,"&Open","")
        menubar.Append(fileMenu,"&File")
        self.Bind(wx.EVT_MENU,self.OnFileOpen)

        #Edit menu
        editMenu = wx.Menu()
        editMenu.Append(-1,"&Copy","")
        menubar.Append(editMenu,"&Edit")

        #Help/About menu
        helpMenu = wx.Menu()
        helpMenu.Append(-1,"About","")
        menubar.Append(helpMenu,"&Help")
        
        #调用SetMenuBar，使其在框架中显示出来
        self.SetMenuBar(menubar)
        
        #添加工具栏,注意：用toolbar = wx.ToolBar()创建不行，会被其它的控件盖掉，这是为什么?
        #toolbar = wx.ToolBar(self)
        toolbar = self.CreateToolBar()
        tsize = (24,24)
        new_bmp = wx.ArtProvider.GetBitmap(wx.ART_NEW,wx.ART_TOOLBAR,tsize)
        toolbar.AddSimpleTool(-1,new_bmp,"Long Help for 'New'")
        toolbar.Realize()
        
        #添加状态栏
        statusbar = self.CreateStatusBar()

    def OnFileOpen(self,event):
        #创建标准文件对话框
        dialog = wx.FileDialog(self,"Open file...",os.getcwd(),style=wx.OPEN,wildcard="*.py")
        #这里有个概念：模态对话框和非模态对话框. 它们主要的差别在于模态对话框会阻塞其它事件的响应,
        #而非模态对话框显示时,还可以进行其它的操作. 此处是模态对话框显示. 其返回值有wx.ID_OK,wx.ID_CANEL;
        if dialog.ShowModal() == wx.ID_OK:
            self.filename = dialog.GetPath()
            self.OnFileRead()
            #在TopWindow中更新标题为文件名.
            self.SetTitle(self.filename)
        #销毁对话框,释放资源.
        dialog.Destroy()

    def OnFileRead(self):
        if self.filename:
            try:
                fd = open(self.filename,'r')
                line = fd.read()
                #这里只是在终端显示文件内容. 可以实现在多行文本控件中显示. 这是下一步的工作.
                print line
                fd.close()
            except:
                wx.MessageBox("%s is not a match file." %self.filename,"oops!",style=wx.OK|wx.ICON_EXCLAMATION)

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = GuiMainFrame()
    frame.Show()
    app.MainLoop()
