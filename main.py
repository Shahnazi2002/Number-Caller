import tkinter as tk
from playsound import playsound
window = tk.Tk()

window.title("نوبت شمار گویا")

window.geometry("500x400")
window.resizable(False, False)

nobat = 1

nobat_display = tk.Label(text=str(nobat).zfill(2), bg="Cyan", font=("Arial", 120, "bold"))
nobat_display.place(relx=0.25, rely=0, relwidth=0.5, relheight=0.5)

def nobat_minus():
    global nobat
    if nobat > 1:
        nobat -= 1
    nobat_display.config(text=str(nobat).zfill(2))
minus = tk.Button(text="-", bd=10, font=("Arial", 80), command=nobat_minus).place(relx=0, rely=0, relwidth=0.25, relheight=0.6)

def nobat_plus():
    global nobat
    if nobat < 99:
        nobat += 1
    nobat_display.config(text=str(nobat).zfill(2))
plus = tk.Button(text="+", bd=10, font=("Arial", 80), command=nobat_plus).place(relx=0.75, rely=0, relwidth=0.25, relheight=0.6)

def nobat_call():
    playsound("audios/0.mp3")
    if nobat < 20 or nobat%10 == 0:
        playsound(f"audios/{nobat}.mp3")
    else:
        playsound(f"audios/{nobat//10}.mp3")
        playsound("audios/o.mp3")
        playsound(f"audios/{nobat%10}.mp3")
def nobat_next():
    nobat_plus()
    nobat_call()

call_current = tk.Button(text="اعلام نوبت فعلی", bd=6, font=("Tahoma", 14), command=nobat_call).place(relx=0.25, rely=0.5, relwidth=0.5, relheight=0.1)
call_next = tk.Button(text="بعدی", bd=16, font=("Tahoma", 40, "bold"), command=nobat_next).place(relx=0, rely=0.6, relwidth=1, relheight=0.4)

window.mainloop()