class Pyqueuue:
    def __init__(self,size=20):
        self.queue=[]
        self.size=size
        self.end=-1
    def IN(self,element):
        if self.end <self.size-1:
            self.queue.append(element)
            self.end+=1
        else:
            raise"the queue is full"
    def OUT (self):
        if self.end!=-1:
            element=self.queue[0]
            self.queue=self.queue[1:]
            self.end-=1
            return element
        else:
            raise"the queue is empty"
    def End(self):
        return self.end
    def empty (self):
        self.queue=[]
        self.end=-1
if __name__ =="__main__":
    queue=Pyqueuue()
    for i in range(10):
        queue.IN(i)
    print queue.End()
    for i in range(10):
        print queue.OUT()
    for i in range(21):
        queue.IN(i)
         
    