import pymongo


#------------input-------------


#-----------class-----------

class Dictionary:
    def __init__(self,db,collection):
        self.client = pymongo.MongoClient()
        self.Database = self.client[db]
        self.collection =self.Database[collection]
        
    def change_db(self,db,collection):
        self.Database =self.client[db]
        self.collection =self.Database[collection]
        
    def Add_word(self,Word,details):
        meaning,catagory,command,synom = details # detila =meaning,catagory,command,Synom
        self.collection.insert_one({'Word':Word,'Meaning':meaning,'Catagory':catagory,'Command':command,'Synom':synom})
                                                #cataagory = verb,noun,pronoun    command = (module,function name)
    def Find(self,Word):
        
        result =  self.collection.find_one({'Word':Word})
        if result ==None:
            self.New_word(Word)
        else:
            return result
    def Exist(self,word):
        result  =self.collection.find_one({'Word':word})
        if result != None:
            return True
        else: 
            return False

    def Update(self,query,item):
        self.collection.update_one(query,{"$set": item})
    def display(self):
        for i in self.collection.find({}):
            print(i)




if __name__ == '__main__':
    Dictionary = Dictionary('Dictionary','Words')
    Dictionary.display()
    
