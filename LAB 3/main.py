class Node:
    def __init__(self, name, add):
        self.range = 250
        self.add = add
        self.id = name
        self.neighbors = []
        self.sending = False
        self.receiving = False
        
    def receive(self, sender):
        if self.receiving == False:
            print(f'{self.id} is receiving from {sender.id}')
            self.receiving = True
        else:
            print('HIDDEN TERMINAL: Collision detected. Node is already receiving.')
   
    def transmit(self, receiver):
        print(f'{self.id} is transmitting to {receiver.id}')
        if receiver not in self.neighbors:
            print('Node out of range')
        else:
            for node in self.neighbors:
                if node.sending == True:
                    print('EXPOSED TERMINAL: Collision detected. Node is already sending.')
                    self.sending = True
                    break
            if self.sending == False:
                self.sending = True
                receiver.receive(self)
                
def main():
    A = Node('A', 450)
    B = Node('B', 850)
    C = Node('C', 650)
    D = Node('D', 1050)
    
    for i in [B, C, D]:
        if abs(i.add - A.add) < A.range:
            A.neighbors.append(i)
            i.neighbors.append(A)
    
    for i in [C,D]:
        if abs(i.add - B.add) < B.range:
            B.neighbors.append(i)
            i.neighbors.append(B)
            
    if abs(C.add - D.add) < C.range:
        C.neighbors.append(D)
        D.neighbors.append(C)
    
    B.transmit(C)
    A.transmit(D)
    A.transmit(C)
    C.transmit(A)
    
    
if __name__=='__main__':
    main()