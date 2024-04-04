from to_do_list import To_Do_List
global count
count = 1
class List_detail:

    detail_list : [To_Do_List]

    def __init__(self):
        self.detail_list = []

    def addDetail(self,l:To_Do_List)-> bool:
        self.detail_list.append(l)
        return True

    def updateDetail(self,l:dict)-> bool:
        for i in range(len(self.detail_list)):
            if self.detail_list[i] != None:
                if self.detail_list[i]._id == l["id"]:
                    if l.get('title'):
                        self.detail_list[i].title = l["title"]
                    if l.get("description"):
                        self.detail_list[i].description = l["description"]
                    if l.get("status"):
                        self.detail_list[i].status = l["status"]
        return {"id" : self.detail_list[i]._id,"title":self.detail_list[i].title,"description":self.detail_list[i].description,"status":self.detail_list[i].status}


    def deleteDetail(self,_id)-> bool:
        for i in range(len(self.detail_list)):
            if self.detail_list[i]._id == _id:
                self.detail_list[i] = None
                return True

    def getDetail(self,_id)-> str:
        for i in range(len(self.detail_list)):
            if self.detail_list[i] == None:
                continue
            if self.detail_list[i]._id == _id:
                return {"id" : self.detail_list[i]._id,"title":self.detail_list[i].title,"description":self.detail_list[i].description,"status":self.detail_list[i].status}

    def getAllDetails(self)->[To_Do_List]:
        return self.detail_list


to_do_list = List_detail()
_title = input("enter the title:")
_description = input("enter the description:")
_status = input("enter the status:")
list1 = To_Do_List(count,_title,_description,_status)
count +=1
to_do_list.addDetail(list1)

list2 = To_Do_List(count,"b","abc","incomplete")
count +=1
to_do_list.addDetail(list2)

for el in to_do_list.getAllDetails():
    print(el._id," ",el.title," ",el.description," ",el.status)


to_do_list.deleteDetail(1)

for el in to_do_list.getAllDetails():
    if el == None:
        continue
    print(el._id," ",el.title," ",el.description," ",el.status)

particular_list = to_do_list.getDetail(2)
print(particular_list)

l = {"id" : 2,"title":"z"}
updated_list = to_do_list.updateDetail(l)
print(updated_list)

for el in to_do_list.getAllDetails():
    if el == None:
        continue
    print(el._id," ",el.title," ",el.description," ",el.status)

