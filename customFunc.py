import pandas as pd
import os

# pandas를 사용하여 csv 파일 읽은 후 추가할 유저가 파일내에 없다면 추가
def saveUsersToCSV(usr_nm, _nick):
    data = [[], []]
    if not os.path.isfile("./user_list.csv"):
        data = [["웨르끼"], ["웨르끼"]]
        dataframe = pd.DataFrame(data)
        dataframe.to_csv("./user_list.csv", header=False, index=False, encoding="utf-8-sig")
    user_list = pd.read_csv("./user_list.csv")

    usr = list(user_list.columns.values)
    nickname = list(user_list.values[0])
    if not usr.count(usr_nm) > 0:
        usr.append(usr_nm)
        nickname.append(_nick)
        data = [usr, nickname]
        print(data)
        dataframe = pd.DataFrame(data)
        dataframe.to_csv("./user_list.csv", header=False, index=False, encoding="utf-8-sig")
        return True
    else:
        print("이미 있음")
        return False

# 유저들의 모든 캐릭터 업데이트
def updateAllCharacters():
    return 0