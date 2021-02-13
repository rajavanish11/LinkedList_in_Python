##########create node class:#########################################################
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

##############create linklist class:##################################################
class LL:
    def __inti__(self):
        self.head=None

    ############# Traverse(Print linklist):###########################################
    def traverese(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.next
            

     ############################### Insert from Head:##############################
    def add_head(self,value):
        new_node=Node(value)    #create a new node calling Node Class
        new_node.next=self.head
        self.head=new_node


   
    ############################ Insert from Tail:####################################

    def add_tail(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node


    ####################### Insert after any value: ##############################
    def add_after(self,after,value):
        temp=self.head
        while temp is not None:
            if temp.data==after:
                break
            temp=temp.next
        if temp is None:
            print("Not Found")
        else:
            new_node=Node(value)
            new_node.next=temp.next
            temp.next=new_node

            

    ################################# Delete from tail: ########################

    def remove_tail(self):
        if self.head is None:
            print("List empty")

        else:
            temp=self.head
            if temp.next is None:
                self.head=None
            else:
                while temp.next.next is not None:
                    temp=tenp.next
                temp.next=None


    ####################### Delete from Head: ###########################
    def remove_head(self):
        if self.head is None:
            print("List Empty")

        else:
            self.head=seld.head.next


    ################# Delete by value: ##################################

    def remove(self,value):
        if self.head.data==value:
            return self.revome_head()  #calling remove_head function
        temp=self.head
        while temp.next is not None:
            if temp.next.data==value:
                break
            temp=temp.next
        if temp.next is None:
            print("Not there")

        else:
            temp.next=temp.next.next


    ##################### SEARCH by value: ###############################
    def search(self,value):
        temp=self.head
        pos=0
        while temp is not None:
            if temp.data==value:
                return pos
            pos+=1
            temp=temp.next
        return "Not found"

    
   #### ############# Replace maximaum number by given number ###########
    def replace_max(self,value):
        maximum=self.head
        temp=self.head
        while temp.data>maximum.data:
            maximum=temp
            temp=temp.next
        maximum.data=value


   ################## Reverse linkedlist: #################################
    def reverse(self):
        prev_node=None
        curr_node=self.head
        while curr_node is not None:
            next_node=curr_node.next
            curr_node.next=prev_node
            prev_node=next_node
        self.head=prev_node

#########################################################################            
                     
#L=LL()                      #Create linklist class
#L.traverse()                #Traverse(Print linkedlist)
#L.add_head(value)           #Insert from Head
#L.add_tail(value)           #Insert from Tail
#add_after(after,value)      #Insert after any value
#L.remove_tail()             #Delete from Tail
#L.remove_head()             #Delete from Head
#L.remove(value)             #Delete by value
#L.search(value)             #SEARCH by value
#L.replace_max(value)        #Replace maximaum number by given number
#L.reverse()                 #Reverse linklist 
#
#
