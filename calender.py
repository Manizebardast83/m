import tkinter as tk
from tkcalendar import Calendar
import datetime
root = tk.Tk()
root.title("Calender")
root.geometry("600x600")

events = {'2024-5-12':('tehran','meeting'),
          '2024-8-3' :('Dubai','meeting'),
          '2024-9-22':('LA','holiday')}

cal = Calendar(root, selectmode = "day", year = 2024, month = 12)

for k in events.keys():
    date = datetime.datetime.strptime(k,"%Y-%m-%d").date()
    cal.calevent_create(date,events[k][0],events[k][1])
    
cal.tag_config('holiday', background = 'lightorange',foreground = 'white')
cal.tag_config('meeting', background = 'lightgreen',foreground = 'black')
cal.pack(expand = True, fill = "both")

root.mainloop()