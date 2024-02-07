import  hashlib
from os import path
class AccountDB:
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name=name
    def __init__(self,name):
        self.name = name

        # cache for account info
        self.__account_dict = {}
        if path.exists(self.name):
            fin = open(self.name,"rt",encoding="utf-8")
            lines = fin.readlines()
            for line in lines:
                line = line.strip()
                key,value = line.split(":")
                self.__account_dict[key] = value
            fin.close()

    def encrypt(self,string):
        return  hashlib.sha256(string.encode()).hexdigest()

    def add(self,username,password):
        if username not in self.__account_dict.keys():
            encrypt_string = self.encrypt(password)
            self.__account_dict[username] = encrypt_string
            self.savefile()
            return True #account addition success
        else:
            return False

    def login(self,username,password):
        if username in self.__account_dict.keys():
            return True if self.__account_dict[username] == self.encrypt(password) else False
        else:
            return False

    def ChangePassword(self,username,password,new_password):
        if username in self.__account_dict.keys():
            if self.__account_dict[username] == self.encrypt(password):
                self.__account_dict[username] = self.encrypt(new_password)
                self.savefile()
                return True #change success
            else:
                return False
        else:
            return False
        #avoid guess about account info

    def AccountDeletion(self,username,password):
        if username in self.__account_dict.keys():
            if self.__account_dict[username] == self.encrypt(password):
                del self.__account_dict[username]
                self.savefile()
                return True #deletion success
            else:
                return False
        else:
            return False
        # avoid guess about account info

    def savefile(self):
        fout = open(self.name,"wt",encoding="utf-8")
        for i in self.__account_dict.keys():
            print("{}:{}".format(i,self.__account_dict[i]),file=fout)
        fout.close()
        #output cache to the file


if __name__ == "__main__":
    file = AccountDB("account.db")
    status = file.add("robert","1234513213")
    print(status)

    if file.login("robert","1234513213"):
        print("登入成功！")
    else:
        print("登入失敗！")
