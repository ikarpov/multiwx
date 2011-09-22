from multiprocessing import Process, Queue

import wx
class MyFrame(wx.Frame):
    """ We simply derive a new class of Frame. """
    def __init__(self, parent, title, queue):
        wx.Frame.__init__(self, parent, title=title, size=(200,100))
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.button = wx.Button(self, label='Send Text!')
        self.button.Bind(wx.EVT_BUTTON, self.OnButton)
        self.queue = queue
        self.Show(True)

    def OnButton(self,e):
        self.queue.put('button!')

    def OnClose(self,e):
        q.close()
        self.Destroy()

def start_app(queue):
    app = wx.App(False)
    frame = MyFrame(None, 'Menu', queue)
    app.MainLoop()

if __name__ == '__main__':
    q = Queue() # create a queue object to talk to the window
    p = Process(target=start_app, args=(q,)) # create the window process
    p.start() # start the window process
    while q:
        print q.get() # get stuff from the queue
    p.join()
