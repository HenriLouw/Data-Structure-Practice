class Treenode:
    def __init__(self,data):
        self.data = data            
        self.children = []                         
        self.parent = None
    
    def add_child(self, child):                 #function that adds children to the tree
        child.parent = self                     #Child is an instance of the treenode class and setting the parent property equal to self
        self.children.append(child)             #Appending child to children

    def get_level(self):                        #function that gets specific child level
        level = 0                               
        p = self.parent                         #setting variable p equal to self.parent as we know parent level is 0
        while p:                                #While loop that increases parent level everytime p is not equal to None
            level += 1
            p = p.parent
        return level                            #returns level




    def print_tree(self):                               #Print function that prints the Parents and Children of the tree
        spaces = ' ' * self.get_level() * 3             #Creating spaces for each level of the tree and multiplying it with 3
        prefix = spaces + '|__' if self.parent else ''  #Creating underscores and spaces for each child and parent in the tree except the Root of the tree
        print(prefix + self.data)                       
        if self.children:                       
            for child in self.children:                 #Traversing through all the children in the tree and printing each child
                child.print_tree()




def build_tree():                               #creating a function for building the tree
    root = Treenode('Electronics')              #setting the instance of Treenode equal to the root

    laptop = Treenode('Laptop')                 #setting the instance of Treenode 'Laptop' equal to the variable laptop
    laptop.add_child(Treenode('Mac'))
    laptop.add_child(Treenode('Thinkpad'))

    cellphone = Treenode('Cell Phone')
    cellphone.add_child(Treenode('Iphone'))  
    cellphone.add_child(Treenode('Vivo'))        

    tv = Treenode('Tv')
    tv.add_child(Treenode('Samsung'))
    tv.add_child(Treenode('LG'))

    root.add_child(laptop)                      #Add the children to root of the tree
    root.add_child(cellphone)
    root.add_child(tv)


    # print(tv.get_level())

    return root

root = build_tree()
root.print_tree()