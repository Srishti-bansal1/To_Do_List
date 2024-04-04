class To_Do_List:
    _id : int
    title : str
    description : str
    status : str

    def __init__(self,_id,title,description,status):
        self._id = _id
        self.title = title
        self.description = description
        self.status = status