import turtle
class wall:
	def __init__(self,pos1,pos2):
		self._pos1=pos1
		self._pos2=pos2
		self.t=turtle.Turtle()
		
		self.t.penup()
		self.t.goto(self._pos1)
		self.t.pendown()
		self.t.goto(self._pos2)
		self.t.hideturtle()
		self._x1=self._pos1[0]
		self._y1=self._pos1[1]
		self._x2=self._pos2[0]
		self._y2=self._pos2[1]
		
	def collision_check(self,turtle):
		self._turtlex=turtle.xcor()
		self._turtley=turtle.ycor()
		self._dist=(((self._x1-self._x2)**2+(self._y1-self._y2)**2)**0.5)
		self._dist2=(((self._x1-self._turtlex)**2+(self._y1-self._turtley)**2)**0.5)
		self._dist3=(((self._turtlex-self._x2)**2+(self._turtley-self._y2)**2)**0.5)
		if(self._dist2+self._dist3==self._dist):
			
			return True
		

def main():
	w=turtle.Screen()
	w.tracer(0,0)
	walls=[]
	x=wall((100,-200),(100,200))
	#for i in walls:
	#	if (i.collision_check(player)==True):
	#		w.background("red")
	w.tracer(1,10)
	player=turtle.Turtle()
	while (True):
		player.fd(1)
		if (x.collision_check(player)):
			w.bgcolor("red")
	w.exitonclick()

if __name__=='__main__':
	main()	
