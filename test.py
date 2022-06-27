from tkinter import *
import tkinter.filedialog as fd

root = Tk()

try:
    # call a dummy dialog with an impossible option to initialize the file
    # dialog without really getting a dialog window; this will throw a
    # TclError, so we need a try...except :
    try:
        root.tk.call('tk_getOpenFile', '-foobarbaz')
    except TclError:
        pass
    # now set the magic variables accordingly
    root.tk.call('set', '::tk::dialog::file::showHiddenBtn', '1')
    root.tk.call('set', '::tk::dialog::file::showHiddenVar', '0')
except:
    pass

# a simple callback for testing:
def openfile(event):
    fname = fd.askopenfilename()
    print(fname)
root.bind('<Control-o>', openfile)

root.mainloop()