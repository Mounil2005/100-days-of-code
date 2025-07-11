import tkinter as tk
import math

root = tk.Tk()

BG_COLOR = "#121212"
BTN_COLOR = "#03026f"
SCI_BTN_COLOR = "#008080"
TEXT_COLOR = "#ffffff"


root.configure(bg="#f0f0f0")
root.title("Scientific Calculator")

root.geometry("400x600")


entry=tk.Entry(root,width=20,font=("Arial",24),borderwidth=5,relief="ridge", justify='right')




entry.grid(row=0,column=0, columnspan=5, padx=10,pady=20)

def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)


def click(symbol):
    current=entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current+symbol)

buttons = [
    ('7',1,0), ('8',1,1) ,('9',1,2),('/',1,3),
    ('4',2,0),('5',2,1),('6',2,2),('*',2,3),
    ('1',3,0),('2',3,1),('3',3,2),('-',3,3),
    ('0',4,0),('.',4,1),('+',4,2),('=',4,3),
    ('C',5,0)
]



sci_buttons = [
    ('√', 'sqrt('),
    ('log', 'log('),
    ('sin', 'sin('),
    ('cos', 'cos('),
    ('tan', 'tan('),
    ('π', str(math.pi)),
    ('e', str(math.e)),
    ('^', '**'),
    ('(', '('),
    (')', ')'),
    ('toDeg', 'toDeg('),
    ('toRad', 'toRad(')
]


sci_start_row = 6
cols = 4

for (text, row, col) in buttons:
    if text == "=":
        btn=tk.Button(root,text=text, width=10, height=2, bg="#add8e6", fg="#121212",font=("Arial",14),command=lambda: evaluate())
        
    elif text=='C':
        btn=tk.Button(root,text=text, width=32, height=2, bg="#d1a24c", fg="#111111", font=("Arial",14),command=lambda: entry.delete(0,tk.END))
        btn.grid(row=row,column=col,columnspan=4,padx=5,pady=5)
        continue
    else:
        btn=tk.Button(root, text=text, width=10, height=2, bg=BTN_COLOR, fg=TEXT_COLOR, font=("Arial",14),command=lambda t=text: click(t))
    
    btn.grid(row=row, column=col, padx=5, pady=5)




for i, (label, value) in enumerate(sci_buttons):
    row = sci_start_row + i // cols
    col = i % cols

    btn = tk.Button(root, text=label, width=10, height=2, bg=SCI_BTN_COLOR, fg=TEXT_COLOR,
                    font=("Arial", 14), command=lambda v=value: click(v))
    
    btn.grid(row=row, column=col, padx=5, pady=5)



def evaluate():
    try:
        expression=entry.get()

        safe_dict=math.__dict__.copy()
        safe_dict["toDeg"]=math.degrees
        safe_dict["toRad"]=math.radians

        result=eval(expression, {"__builtins__":None},safe_dict)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except: 
        entry.delete(0, tk.END)
        entry.insert(0,"Error")


root.mainloop()

