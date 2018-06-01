from pymongo import MongoClient
from bson.objectid import ObjectId 


# 通訊類型
# from enum import Enum, IntEnum, unique
#
# try:
#     @unique
#     class OPERATION(Enum):
#         MSG = 0
#         NUMCHANGE = 1
#         ISALIVE = 2
#         CONNECT = 3
#         CHANGEPWD = 4
#         PWDCHANGE = 5
#         LOGIN = 6
# except ValueError as e:
#     print(e)
#
# spliteTag = '$@~&*^$'


class DataBaseChatRoom:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)  # 比较常用
        self.database = self.client["ChatRoom"]  # SQL: Database Name
        self.collection = self.database["user"]  # SQL: Table Name

    def loadData(self):
        cursor = self.collection.find({})
        data = [d for d in cursor]
        return data

    # delete user by uname
    # dbChatRoom.deleteUser(['A'])
    def deleteUser(self, unameList=None):
        for n in unameList:
            self.collection.delete_one(n)
        return 'successful'

    # insert user
    # dbChatRoom.insertUser(uname='A', upwd='A')
    def insertUser(self, uname=None, upwd=None):
        self.collection.insert_one({ "uname":uname, "upwd":upwd })
        return 'successful'

    def updataUser(self, uname=None, upwd=None):
        user = self.collection.find_one({'uname': uname})
        user['upwd'] = upwd
        self.collection.save(user)
        return 'successful'

    # check checkUserExist
    def checkUserExist(self, uname='A'):
        return bool(self.collection.find({'uname': uname}).count())

    # query user bu uname
    # dbChatRoom.queryByuname(uname='A', upwd='A')
    def queryByuname(self, uname='A', upwd='A'):
        return self.collection.find({'uname': uname, 'upwd': upwd}).sort('uname')

    # Init database
    # dbChatRoom.Initdatabase()
    def Initdatabase(self):
        userList = []
        userList.append({'uname': 'A', 'upwd': 'A'})
        userList.append({'uname': 'B', 'upwd': 'B'})
        userList.append({'uname': 'C', 'upwd': 'C'})
        userList.append({'uname': 'D', 'upwd': 'D'})
        userList.append({'uname': 'E', 'upwd': 'E'})
        self.collection.insert_many(userList)

    def colseClient(self):
        self.client.close()


def main():
    dbChatRoom = DataBaseChatRoom()
    dbChatRoom.Initdatabase()
    dbChatRoom.colseClient()


if __name__ == "__main__":
    main()
