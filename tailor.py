import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as msg
import os
import PyPDF2

class App(tk.Tk):
  def __init__(self):
    super().__init__()

    self.geometry('400x600+500+100')
    
    self.title('PDF Birleştirici')
    self.columnconfigure(0, weight=1)
    self.rowconfigure(0, weight=0)
    self.rowconfigure(1, weight=1)
    self.rowconfigure(2, weight=1)
    self.rowconfigure(3, weight=0)

    self.create_widgets()

    self.filetypes= [('PDF', '*.pdf')] # , ('All files', '*.*')
    self.directory = str()
    self.inputs_paths = list()

  def create_widgets(self):
    self.button_inputs = tk.Button(self, text='Dosya yükle', height=3, command=self.button_inputs_handler)
    self.listbox = tk.Listbox(self, bg='white', font=("Courier", 16, "italic"))
    self.button_up = tk.Button(self, text='Yukarı', width=5, command=self.button_up_click_handler)
    self.button_down = tk.Button(self, text='Aşağı', width=5, command=self.button_down_click_handler)
    self.button_delete = tk.Button(self, text='Sil', width=5, command=self.button_delete_click_handler)
    self.button_merge = tk.Button(self, text="BİRLEŞTİR", height=3, command=self.button_merge_handler)
    
    self.button_inputs.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW, padx=8, pady=8)
    self.listbox.grid(row=1, column=0, rowspan=3, sticky=tk.NSEW, padx=8, pady=8)
    self.button_up.grid(row=1, column=1, sticky=tk.S, padx=8, pady=8)
    self.button_down.grid(row=2, column=1, sticky=tk.N, padx=8, pady=8)
    self.button_delete.grid(row=3, column=1, sticky=tk.S, padx=8, pady=8)
    self.button_merge.grid(row=4, column=0, columnspan=2, sticky=tk.NSEW, padx=8, pady=8)


  def button_delete_click_handler(self):
    if len(self.listbox.curselection()) == 0:
      return
    
    (selected_index, )  = self.listbox.curselection()

    self.listbox.delete(selected_index)
    
    if selected_index == self.listbox.size():
      self.listbox.select_set(selected_index-1)
    else:
      self.listbox.select_set(selected_index)

  def button_down_click_handler(self):
    if len(self.listbox.curselection()) == 0:
      return
    
    (selected_index, )  = self.listbox.curselection()
    if selected_index == self.listbox.size()-1:
      return

    selected_item_text = self.listbox.get(selected_index)
    self.listbox.delete(selected_index)
    self.listbox.insert(selected_index+1, selected_item_text)
    self.listbox.select_set(selected_index+1)

  def button_up_click_handler(self):
    if len(self.listbox.curselection()) == 0:
      return
    
    (selected_index, )  = self.listbox.curselection()
    if selected_index == 0:
      return

    selected_item_text = self.listbox.get(selected_index)
    self.listbox.delete(selected_index)
    self.listbox.insert(selected_index-1, selected_item_text)
    self.listbox.select_set(selected_index-1)

    
  def button_inputs_handler(self):
    self.inputs_paths = fd.askopenfilenames(filetypes=self.filetypes)
    if len(self.inputs_paths) == 0:
      return

    for path in self.inputs_paths:
      head, tail = os.path.split(path)
      self.listbox.insert(tk.END, tail)

    self.directory = head + '/'
    
  def button_merge_handler(self):
    merge_file = PyPDF2.PdfFileMerger()

    for path in self.listbox.get(0, tk.END):
      merge_file.append(PyPDF2.PdfFileReader(self.directory + path, 'rb'))

    output_path = fd.asksaveasfilename(filetypes=self.filetypes)
    
    if not output_path:
      return
    
    try:
      merge_file.write(output_path)
      msg.showinfo('TEBRİKLER!', message='Dosyalar başarılı bir şekilde birleştirilmiştir.')
      
    except Exception as e:
      msg.showerror('HATA', message=e)
    
    
if __name__ == "__main__":
  app = App()
  
  try:
    # call a dummy dialog with an impossible option to initialize the file
    # dialog without really getting a dialog window; this will throw a
    # TclError, so we need a try...except :
    try:
        app.tk.call('tk_getOpenFile', '-foobarbaz')
    except tk.TclError:
        pass
    # now set the magic variables accordingly
    app.tk.call('set', '::tk::dialog::file::showHiddenBtn', '1')
    app.tk.call('set', '::tk::dialog::file::showHiddenVar', '0')
  except:
    pass

  app.mainloop()