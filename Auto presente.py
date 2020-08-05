import tkinter as tk

class presente:
    def __init__(self, root):
        self.root = root
        self.root.geometry("100x100")
        self.master_frame = tk.Frame(root)
        self.master_frame.pack(fill=tk.BOTH, expand=True)
        self.root.title("Calculadora")
        btn = tk.Button(self.master_frame, text="Hola")
        btn.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = presente(root)
    root.mainloop()