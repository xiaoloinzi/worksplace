# encoding=utf-8
import re


def login(username,userpwd):
    if username == '' or userpwd == '':
        return {"massage":"The user name and password can not be empty","status":0}
    # if not re.match('^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\\d{8}$',username):
    #     return {"massage":"Mobile phone number does not meet the requirements","status":0}
    if len(userpwd) < 8 or  len(userpwd) > 12:
        return {"massage":"The user password is incorrect","status":0}
    if not re.match("^(?=.*?[A-Za-z]+)(?=.*?[0-9]+)(?=.*?[A-Z]).*$",userpwd):
        return {"massage":"The user password is incorrect","status":0}
    else:
        return {"massage":"user password is correct","status":1,"username":username,"userpwd":userpwd}

# if __name__ == "__main__":
#     print login('18834133049',"2111s12A12192")
    # login(186089979095,"B1234567")
    # login("aaaaa")
    # login("A111")
    # login("Addddddd9999")
    # login("@@@@@@@@@@@@")
    # login("11111111111")
    # login("11111中111111")