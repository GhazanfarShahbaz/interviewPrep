class Animal:
    def __init__(self, type):
        self.type = type

    def get(self):
        return self.type
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class linkedList:
    def __init__(self):
        self.head = None

    def add(self,value):
        if not self.head:
            self.head = Node(value, None)
        else:
            parse = self.head
            while(parse.next):
                parse = parse.next
            parse.next = Node(value, None)

    def remove(self, value):
        if self.head.val == value:
            self.head = self.head.next
        else:
            parse = self.head
            while(parse.next.val != value):
                parse = parse.next
            parse.next = parse.next.next

class animalShelter:
    def __init__(self):
        self.shelter = linkedList()

    def push(self, value):
        self.shelter.add(value)

    def enqueu(self):
        animal = self.shelter.head.val
        self.shelter.remove(animal)
        return animal

    def enqueueDog(self):
        parse = self.shelter.head
        if parse and  parse.val.type == "Dog":
            value = parse.val
            self.shelter.remove(value)
            return value
        
        while parse and parse.next.val.type != "Dog" :
            parse = parse.next
        value = None

        if(parse):
            value = parse.next.val
            self.shelter.remove(value)
        return value
    
    def enqueueCat(self):
        parse = self.shelter.head
        if parse and  parse.val.type == "Cat":
            value = parse.val
            self.shelter.remove(value)
            return value
        
        while parse and parse.next.val.type != "Cat" :
            parse = parse.next
        value = None
        
        if(parse):
            value = parse.next.val
            self.shelter.remove(value)
        return value


if __name__ == "__main__":
    shelter = animalShelter()
    shelter.push(Animal("Cat"))
    shelter.push(Animal("Goose"))
    shelter.push(Animal("Goose"))
    shelter.push(Animal("Dog"))
    shelter.push(Animal("Dog"))
    shelter.push(Animal("Dog"))
    shelter.push(Animal("Goose"))
    shelter.push(Animal("Goose"))
    shelter.push(Animal("Goose"))

    

    print(shelter.enqueueDog().type)
    print(shelter.enqueueCat().type)
    print(shelter.enqueu().type)


