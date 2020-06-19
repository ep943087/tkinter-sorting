def hsl_rgb(h,s,l):
	c = (1-abs(2*l-1))*s;
	hp = h/60;
	x = c * (1-abs(hp%2-1));
	if(h<60):
		r,g,b =  c,x,0;
	elif(h<120):
		r,g,b =  x,c,0;
	elif(h<180):
		r,g,b = 0,c,x;
	elif(h<240):
		r,g,b =  0,x,c;
	elif(h<300):
		r,g,b = x,0,c;
	elif(h<=360):
		r,g,b =  c,0,x;
	m = l-c/2;
	r,g,b =  (r+m)*255,(g+m)*255,(b+m)*255;
	return int(r),int(g),int(b);

def get_hex_char(n):
	if n<=9:
		return str(n);
	else:
		return chr(n+55);

def dec_hex(d):
	str = "";
	while(d>0):
		str += get_hex_char(d%16);
		d = int(d/16);
	if(len(str)==0):
		return "00";
	elif(len(str)==1):
		return "0"+str;
	else:
		return str[::-1];

def rgb_hex(r,b,g):
	return "#"+dec_hex(r)+dec_hex(b)+dec_hex(g);

def hsl_hex(h,s,l):
	r,g,b = hsl_rgb(h,s,l);
	return rgb_hex(r,g,b);
	
def main():
	print(rgb_hex(255,0,0));
	print(hsl_hex(120,.4,.5));
	print(hsl_hex(300,.4,.5));
if __name__ == "__main__":
	main();
