import tkinter as tk

window = tk.Tk()
window.title("Approximate Pattern Matching")
#window.resizable(height=False)
window.geometry("900x600")
window.resizable(width=False, height=False)



frame2 = tk.Frame(master=window, height=100, bg="yellow")
frame2.pack(fill=tk.X)

#frm_entry = tk.Frame(master=frame2)
lbl_input = tk.Label(master=frame2,text="Input:")
lbl_input.place(x=0, y=0)
ent_temperature = tk.Entry(master=frame2, width=10)
ent_temperature.place(x=100,y=0)

lbl_search = tk.Label(master=frame2,text="Searched Word:")
lbl_search.place(x=200, y=0)
ent_temperature = tk.Entry(master=frame2, width=10)
ent_temperature.place(x=300,y=0)



frame1 = tk.Frame(master=window, height=500, bg="red")
frame1.pack(fill=tk.X)


canvas = tk.Canvas(frame1, width=800, height=500, borderwidth=0, highlightthickness=0,
                   bg="black")
canvas.grid()

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle

word="patata"
for x in range(1,5):
    for y in range(1,len(word)+1):
        canvas.create_circle(y*100, x*100, 25, fill="blue", outline="#DDD", width=2)



window.mainloop()