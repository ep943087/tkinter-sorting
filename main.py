from sort import *
from tkinter import *

root = Tk()
root.title("Sorting Simulation")
root.geometry("408x430")
root.resizable(False,False)

mySort = Sort(root,400,400);
mySort.grid(row=2,column=0,columnspan=7);

start_btn = Button(root,text="Start",command=mySort.start);
start_btn.grid(row=1,column=0);

scramble_btn = Button(root,text="Scramble",command=mySort.initLst);
scramble_btn.grid(row=1,column=1);

stop_btn = Button(root,text="Stop",command=mySort.stop);
stop_btn.grid(row=1,column=2);


size_options = [
	"100",
	"200",
	"300",
	"400",
	"500"
]

so = StringVar();
so.set(size_options[0]);

def update_size(e):
	global so;
	mySort.set_size(int(so.get()));

def update_mode(e):
	global mo;
	mySort.set_mode(mo.get());

def update_speed(e):
	global spo;
	mySort.set_speed(int(spo.get()));

def update_draw(e):
	global do;
	mySort.set_drawtype(do.get());

#Label(root,text="Size:").grid(row=1,column=4,sticky=E);
size_button = OptionMenu(root,so,*size_options,command=update_size)
size_button.grid(row=1,column=3);

mode_options = [
	"Bubble",
	"Select",
	"Insert",
	"Merge",
	"Quick"
]	

mo = StringVar();
mo.set(mode_options[0]);

mode_button = OptionMenu(root,mo,*mode_options,command=update_mode);
mode_button.grid(row=1,column=4);

speed_options = [
	"1",
	"5",
	"10",
	"15",
	"20",
	"25",
	"30",
]

spo = StringVar();
spo.set(speed_options[0]);

speed_button = OptionMenu(root,spo,*speed_options,command=update_speed);
speed_button.grid(row=1,column=5);

draw_options = [
	"Lines",
	"Rectangle",
	"Spiral",
	"Scatter",
	"Color"
]

do = StringVar();
do.set(draw_options[0]);

draw_button = OptionMenu(root,do,*draw_options,command=update_draw);
draw_button.grid(row=1,column=6);

root.mainloop();
