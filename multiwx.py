import wx
from multiprocessing import Process, Queue

__author__ = "Igor Karpov <ikarpov@cs.utexas.edu>"
__date__ = "2011/09/22"

class MultiFrame(wx.Frame):
    """ A frame with a button """
    def __init__(self, parent, title, queue):
        wx.Frame.__init__(self, parent, title=title, size=(200,100))
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.button = wx.Button(self, label='Send Text!')
        self.button.Bind(wx.EVT_BUTTON, self.OnButton)
        self.queue = queue
        self.Show(True)

    def OnButton(self,e):
        """ when the button is pressed, send something to main process """
        self.queue.put('button!')

    def OnClose(self,e):
        """ when the window is closing, send None to main process """
        print 'closing!'
        self.queue.put(None)
        self.Destroy()

def start_app(queue):
    """ start a wxPython app using queue for multiprocess communication """
    app = wx.App(False)
    frame = MultiFrame(None, 'MultiWx', queue)
    app.MainLoop()

def main():
    """ main function """
    q = Queue() # create a queue object to talk to the window
    p = Process(target=start_app, args=(q,)) # create the window process
    p.start() # start the window process
    while True: # repeat until done
        item = q.get() # get the next item from queue
        if item is None:
            print 'done!' # signal that we are done
            break # break out of the loop
        else:
            print item # print the item from queue
    p.join() # wait for the child process to finish

if __name__ == '__main__':
    main()
