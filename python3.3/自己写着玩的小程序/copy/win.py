import wx

def opener(event):
    '定义事件'
    file=open(filename.GetValue())
    contents.SetValue(file.read())
    file.close()

def save(event):
    '定义事件'
    file=open(filename.GetValue(),'w')
    file.write(contents.GetValue())
    file.close()
    
app=wx.App()
win=wx.Frame(None,title='Simple editor',size=(410,335))
bkg=wx.Panel(win)

openbtn=wx.Button(bkg,label='open')
openbtn.Bind(wx.EVT_BUTTON,opener)

savebtn=wx.Button(bkg,label='save')
savebtn.Bind(wx.EVT_BUTTON,save)

filename=wx.TextCtrl(bkg)
contents=wx.TextCtrl(bkg,style=wx.TE_MULTILINE|wx.HSCROLL)

hbox=wx.BoxSizer()
hbox.Add(filename,proportion=1,flag=wx.EXPAND)
hbox.Add(openbtn,proportion=0,flag=wx.LEFT,border=5)
hbox.Add(savebtn,proportion=0,flag=wx.LEFT,border=5)

vbox=wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox,proportion=0,flag=wx.EXPAND|wx.ALL,border=5)
vbox.Add(contents,proportion=1,
         flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT,border=5)

bkg.SetSizer(vbox)
win.Show()
app.MainLoop()
