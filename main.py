import AccountDB
file = AccountDB.AccountDB("account.db")
while True:
    print('*'*10+'帳號管理資料庫'+'*'*10)
    print()
    print("1. 新增帳號")
    print("2. 登入帳號")
    print("3. 變更密碼")
    print("4. 刪除帳號")
    print("5. 關閉程式")
    print()

    #Judge Type in
    while True:
        decision = input("請輸入您的選擇：")
        if decision in "12345": break

    #Run Order
    if decision == "1":
        if file.add(input("請輸入您的帳號："),input("請輸入您的密碼：")):
            print("\n帳號新增成功！")
        else:print("\n帳號已經存在！")
    elif decision == "2":
        if file.login(input("請輸入您的帳號："),input("請輸入您的密碼：")):print("\n登入成功！")
        else:print("\n帳號或密碼錯誤！")
    elif decision == "3":
        if file.ChangePassword(input("請輸入您的帳號："),input("請輸入您的密碼："),input("請輸入您的新密碼：")):
            print("\n密碼更改成功！")
        else:print("\n帳號或密碼錯誤！")
    elif decision == "4":
        if file.AccountDeletion(input("請輸入您的帳號："),input("請輸入您的密碼：")):
            print("\n帳號刪除成功！")
        else:print("\n帳號或密碼錯誤！")
    else:
        print("感謝您的使用！")
        break

    print("\n")
