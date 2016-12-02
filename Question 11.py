class Node(object):
      def __init__(self, value):
          self.value=value
          self.next=None
          self.prev=None

class List(object):
      def __init__(self):
          self.head=None
          self.tail=None
      def insert(self,n,x):
          if n!=None:
              x.next=n.next
              n.next=x
              x.prev=n
              if x.next!=None:
                  x.next.prev=x              
          if self.head==None:
              self.head=self.tail=x
              x.prev=x.next=None
          elif self.tail==n:
              self.tail=x             
      def remove(self, n):
          """ this function is the double linked list node delete function """
          if n.prev != None:
              n.prev.next
              # if the previous node is not equal to anything then it checks te next node
          else:
              self.head = n.next
              # heads to the next node
          if next != None:
              n.next.prev
              # if the next node isnt equal to anything then it will check the previous node
          else:
              self.tail = n.prev
              # else the previous node is equal to nothing
      def display(self):
          values=[]
          n=self.head
          while n!=None:
              values.append(str(n.value))
              n=n.next
          print ("List: ",",".join(values))
          
if __name__ == '__main__':
      l=List()
      l.insert(None, Node(4))
      l.insert(l.head,Node(6))
      l.insert(l.head,Node(8))
      l.display()
