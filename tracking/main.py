# tracking with gps and google maps project
import wx
import webbrowser as wbb
import time 

class Window(wx.Frame):
           
    def __init__(self, *args, **kw):
        super(Window, self).__init__(*args, **kw) 
        
        self.InitUI()
        
    def InitUI(self):   

        pnl = wx.Panel(self)
        
        dobtn = wx.Button(pnl,label='Map',pos=(20,20))
        dobtn.Bind(wx.EVT_BUTTON, self.Openbrowser)
        
        cbtn = wx.Button(pnl, label='Close', pos=(150, 160))
        cbtn.Bind(wx.EVT_BUTTON, self.OnClose)

        self.SetSize((250, 200))
        self.SetTitle('pytackGUI')
        self.Centre()
        self.Show(True)          
        
    def OnClose(self, e):
        self.Close(True)                  
    
    def Openbrowser(self, e):
        wbb.open_new('default.html')
        
        
def main():
    
    ex = wx.App()
    Window(None)
    
    ex.MainLoop()    


if __name__ == '__main__':
    main()   
