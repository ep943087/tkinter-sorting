from tkinter import *
from hsl import *
import math
import random

delay = 1

class Sort(Canvas):
	def __init__(self,root,width,height):
		super().__init__(root,width=width,height=height,background="white")
		self.lst = []
		self.drawtype = "Lines"
		self.drawLst = []
		self.mode = "Bubble"
		self.i = 0
		self.speed = 1
		self.solving = False
		self.size = 100
		self.initLst()
		self.after(delay,self.update)
	def initSortVar(self):
		if(self.mode=="Bubble"):
			self.i = 0
			self.last = self.size-1		
		elif(self.mode=="Select"):
			self.i = 0
			self.j = 0
			self.s = 0
		elif(self.mode=="Insert"):
			self.i = 0
			self.j = 0
		elif(self.mode=="Quick"):
			self.tmp = [];
			self.low_high = [];
			for i in self.lst:
				self.tmp.append(i);
			self.temp_quick_sort(0,self.size-1);
			self.x = 0;
			self.low = self.low_high[self.x][0]
			self.high = self.low_high[self.x][1]
			self.i = self.low;
			self.j = self.low;
			self.pivot = self.lst[self.high];
		elif(self.mode=="Merge"):
			self.low_high = [];
			self.temp_merge_sort(0,self.size-1);
			self.x = 0;
			self.low = self.low_high[self.x][0];
			self.high = self.low_high[self.x][1];
			self.mid = (self.low+self.high)//2;
			self.i = self.low;
			self.j = self.mid+1;
			self.m = 0;
			self.n = self.low;
			self.tmp = [];
		
	def initLst(self):
		self.solving = False;
		tmp = [];
		for i in range(1,self.size+1):
			tmp.append(i);
		self.lst = [];
		for i in range(1,self.size+1):
			r = random.randint(0,len(tmp)-1);
			h = tmp[r];
			tmp.pop(r);
			self.lst.append(h);
		self.initSortVar();
	def set_speed(self,value):
		self.speed = value;

	def set_size(self,value):
		self.stop();
		self.size = value;
		self.initLst();
	def set_mode(self,value):
		self.mode = value;
		self.stop();
		self.initLst();
	def set_drawtype(self,value):
		self.drawtype=value;
	def start(self):
		self.solving = True;
	def stop(self):
		self.solving = False;
	def swap(self,i,j):
		x = self.lst[i];
		self.lst[i] = self.lst[j];
		self.lst[j] = x;
	def sort(self):
		if(not(self.solving)):
			return;
		if(self.mode=="Bubble"):
			self.bubble_sort();
		elif(self.mode=="Select"):
			self.select_sort();
		elif(self.mode=="Insert"):
			self.insert_sort();
		elif(self.mode=="Quick"):
			self.quick_sort();
		elif(self.mode=="Merge"):
			self.merge_sort();
		else:
			print(self.mode);

	def temp_partition(self,low,high):
		j = low;
		pivot = self.tmp[high];
		for i in range(low,high):
			if(self.tmp[i]<pivot):
				self.swap_tmp(i,j);
				j+=1;
		self.swap_tmp(j,high);
		return j;
	def swap_tmp(self,i,j):
		x = self.tmp[i];
		self.tmp[i] = self.tmp[j];
		self.tmp[j] = x;
	def temp_quick_sort(self,low,high):
		if(low<high):
			self.low_high.append((low,high));
			j = self.temp_partition(low,high);
			self.temp_quick_sort(low,j-1);
			self.temp_quick_sort(j+1,high);
	def temp_merge_sort(self,low,high):
		if(low<high):
			mid = (low+high)//2;
			self.temp_merge_sort(low,mid);
			self.temp_merge_sort(mid+1,high);
			self.low_high.append((low,high));	

	def bubble_sort(self):
		if(self.last>=0):
			if(self.i<self.last):
				if(self.lst[self.i]>self.lst[self.i+1]):
					self.swap(self.i,self.i+1)
				self.i+=1;
			else:
				self.i = 0;
				self.last-=1;
		else:
			self.solving = False;
	def select_sort(self):
		if(self.i<self.size):
			if(self.j<self.size):
				if(self.lst[self.j]<self.lst[self.s]):
					self.s = self.j;
				self.j+=1;
			else:
				self.swap(self.s,self.i);
				self.i+=1;
				self.j = self.i;
				self.s = self.i;								
		else:
			self.solving = False;
	def insert_sort(self):
		if(self.i<self.size):
			if(self.j>0 and self.lst[self.j-1]>self.lst[self.j]):
				self.swap(self.j-1,self.j);
				self.j-=1;
			else:
				self.i+=1;
				self.j = self.i;
		else:
			self.solving = False;
	def quick_sort(self):
		if(self.x<len(self.low_high)):
			if(self.i<self.high):
				if(self.lst[self.i]<self.pivot):
					self.swap(self.i,self.j);
					self.j += 1;
				self.i += 1;
			else:
				self.swap(self.j,self.high);
				self.x += 1;
				if(self.x==len(self.low_high)):
					self.solving = False;
					return;
				else:
					self.low = self.low_high[self.x][0];
					self.high = self.low_high[self.x][1];
					self.i = self.low;
					self.j = self.low;
					self.pivot = self.lst[self.high];
		else:
			self.solving = False;
	def merge_sort(self):
		if(self.x<len(self.low_high)):
			if(self.i<=self.mid and self.j<=self.high):
				if(self.lst[self.i]<self.lst[self.j]):
					self.tmp.append(self.lst[self.i]);
					self.i += 1;
				else:
					self.tmp.append(self.lst[self.j]);
					self.j += 1;
			elif(self.i<=self.mid):
				self.tmp.append(self.lst[self.i]);
				self.i+=1;
			elif(self.j<=self.high):
				self.tmp.append(self.lst[self.j]);
				self.j+=1;
			elif(self.n<=self.high):
				self.lst[self.n] = self.tmp[self.m];
				self.n+=1;
				self.m+=1;
			else:
				self.x += 1;
				if(self.x==len(self.low_high)):
					self.solving = False;
					return;
				self.low = self.low_high[self.x][0];
				self.high = self.low_high[self.x][1];	
				self.mid = (self.low+self.high)//2;
				self.i = self.low;
				self.j = self.mid+1;
				self.m = 0;
				self.n = self.low;
				self.si = self.high-self.low+1;					
				self.tmp = [];
		else:
			self.solving = False;

	def drawRectangles(self):
		w = self.winfo_width()/self.size;
		h = self.winfo_height()/self.size*.8;
		width = self.winfo_width();
		height= self.winfo_height();
		for i in range(self.size):
			self.choose_color(i);
			t = self.create_rectangle(i*w,height-self.lst[i]*h,i*w+w,height,fill=self.color,outline="");
			self.drawLst.append(t);

	def drawConnectLines(self):
		w = self.winfo_width()/self.size;
		h = self.winfo_height()/self.size*.8;
		width = self.winfo_width();
		height= self.winfo_height();
		for i in range(self.size-1):
			self.choose_color(i);
			t = self.create_line(i*w,height-self.lst[i]*h,i*w+w,height-self.lst[i+1]*h,fill=self.color,width=3);
			self.drawLst.append(t);
	def drawSpiral(self):
		width = self.winfo_width();
		height = self.winfo_height();
		cx = width/2;
		cy = height/2;
		angle = 0;
		for i in self.lst:
			self.choose_color(i);
			x = cx + (i*.5)*math.cos(angle);
			y = cy + (i*.5)*math.sin(angle);
			t = self.create_circle(x,y,2,self.color);
			self.drawLst.append(t);
			angle+=math.pi/50;
			
	def drawScatter(self):
		w = self.winfo_width()/self.size;
		h = self.winfo_height()/self.size;
		width = self.winfo_width();
		height= self.winfo_height();
		for i in range(self.size-1):
			self.choose_color(i);
			t = self.create_circle(i*w+w,height-self.lst[i]*h,2,self.color);
			self.drawLst.append(t);
	def drawColor(self):
		w = self.winfo_width()/self.size;
		h = self.winfo_height()/self.size;
		height = self.winfo_height();
		for i in range(self.size):
			self.color = "";
			self.choose_color(i);
			if(self.color=="black" or not self.solving):
				h = 360*self.lst[i]/self.size;
				self.color = hsl_hex(h,1,.4);
			t = self.create_rectangle(i*w,height-self.lst[i]*w,i*w+w,height,fill=self.color,outline="");
			self.drawLst.append(t);
			
	def create_circle(self,x,y,r,color):
		x0 = x-r;
		y0 = y-r;
		x1 = x+r;
		y1 = y+r;
		return self.create_oval(x0,y0,x1,y1,fill=color,outline="");
	def choose_color(self,i):
		self.color = "black";
		if(self.mode=="Bubble" and i==self.i):
			self.color = "red";
			if(self.drawtype=="Color"):
				self.color = self['background'];
		elif(self.mode=="Select" and i==self.s):
			self.color = "blue";
			if(self.drawtype=="Color"):
				self.color = self['background'];
		elif(self.mode=="Select" and i==self.j):
			self.color="red";
			if(self.drawtype=="Color"):
				self.color = self['background'];
		elif(self.mode=="Insert" and i==self.j):
			self.color="red";
			if(self.drawtype=="Color"):
				self.color = self['background'];
		elif(self.mode=="Quick" and (i==self.i or i==self.j)):
			self.color = "red";
			if(self.drawtype=="Color"):
				self.color = self['background'];
		elif(self.mode=="Merge" and i==self.i and self.n==self.low):
			self.color = "red";
			if(self.drawtype=="Color"):
				self.color = self['background'];
		elif(self.mode=="Merge" and i==self.j and self.n==self.low):
			self.color = "blue";
			if(self.drawtype=="Color"):
				self.color = self['background'];
		elif(self.mode=="Merge" and i==self.n and self.m>0):
			self.color = "#00ff00";
			if(self.drawtype=="Color"):
				self.color = self['background'];
		if(not self.solving):
			self.color = "black";	
			if(self.drawtype=="Color"):
				self.color = self['background'];
	def draw(self):
		if(len(self.drawLst)>0):
			for d in self.drawLst:
				self.delete(d);
		self.drawLst = [];
		
		if(self.drawtype=="Rectangle"):
			self.drawRectangles();
		elif(self.drawtype=="Lines"):
			self.drawConnectLines();
		elif(self.drawtype=="Spiral"):
			self.drawSpiral();
		elif(self.drawtype=="Scatter"):
			self.drawScatter();
		elif(self.drawtype=="Color"):
			self.drawColor();
	def update(self):
		for i in range(self.speed):
			self.sort();

		self.draw();
		self.after(delay,self.update);

