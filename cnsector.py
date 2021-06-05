class point :
    def __init__ (self,x,y):
        self.x=x
        self.y=y
    def drow(self) :
        print ("drow")
    def print1(self):
        print ('print')


point1 = point(10,20)
point1.x=11
print (point1.x)
point1.drow()
"exarsice"
class point :
    def __init__ (self,name):
        self.name=name
    def drow (self):
        print (f'hai iam {self.name}')



point1= point('akhil')
point1.drow()

















