from ast import Index
from operator import indexOf
from sqlite3 import DataError
from unittest import result
from urllib import response
import urllib.request as request
import json

src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

# 這邊用json load 進來，畢竟我們知道他是json格式
with request.urlopen(src) as response:
    data = json.load(response)

# 發現總共有57個地點資料
Date_list = data["result"]["results"]

#print(Date_list[0]["xpostDate"]) #測試印日期用

# 來用for迴圈把所有照xpostDate篩選條件 <= 2015 都拿出來
# 景點名稱,區域,經度,緯度,第一張圖檔網址

# 先處理日期問題
# 試著抓xpostDate的前四個字再轉成數字篩選 
#print(Date_list[0]["xpostDate"][0:4])

# for date in Date_list:
#     # 篩選出 > = 2015的年份
#     # 你已經是個成熟的年份了，可以做篩選了
#         year = int(date["xpostDate"][0:4])
#         if year < 2015:
#             continue
        

#         # 處理首張圖片區
#         # 最終印出是要打 "https" + first_pic[1]
#         pic = date["file"]
#         first_pic = pic.split("https")
        

#         # 處理區域地址三字區
#         #以下區域的其中一個：
#         # 中正區、萬華區、中山區、大同區、大安區、松山區、信義區、
#         # 士林區、文山區、北投區、內湖區、南港區。
#         area = date["address"]
#         target_area = area.split(" ")

#         longitude = date["longitude"]
#         latitude = date["latitude"]



        
#         print(date["stitle"] + ",",target_area[2][0:3] +",", longitude + "," , latitude + ",","https" + first_pic[1])
        


# print(len(date)) 取出資料長度是21個

# 把變數命名更明確點，
# date 改成 travel

with open("data.csv" , mode = "w" , encoding = "utf-8") as file:
    for travel in Date_list:
    # 篩選出 > = 2015的年份
    # 你已經是個成熟的年份了，可以做篩選了
        year = int(travel["xpostDate"][0:4])
        if year < 2015:
            continue
        

        # 處理首張圖片區
        # 最終印出是要打 "https" + first_pic[1]
        pic = travel["file"]
        first_pic = pic.split("https")
        

        # 處理區域地址三字區
        #以下區域的其中一個：
        # 中正區、萬華區、中山區、大同區、大安區、松山區、信義區、
        # 士林區、文山區、北投區、內湖區、南港區。
        area = travel["address"]
        target_area = area.split(" ")

        longitude = travel["longitude"]
        latitude = travel["latitude"]
        
        
        file.write(travel["stitle"] + ","+ target_area[2][0:3] +","+ longitude + "," + latitude + "," + "https" + first_pic[1] +"\n") 
    






# # index取物(先不採用)
# for date in Date_list:
#     date.index(["xpostDate"])
#     print(date)

# for_index = Date_list[0]["xpostDate"]
# pick = for_index.index("xpostDate")
# print(pick)



# # 取第一張圖片 OK ，到時要再看看用迴圈取出大家的第一張圖片
# pic = Date_list[0]["file"]
# first_pic = pic.split(".jpg")
# print(first_pic[1] + ".jpg")


# rank = sorted(date["xpostDate"]) #額他只有排序字串而已，不要裡這邊
# print(rank)



# for Date in Date_list:
#     print(Date["stitle"],",",Date["xpostDate"],",",Date["address"],",",Date["longitude"],",",Date["latitude"],",",Date["file"])



# 決定針對每個有要求的做變數計算，再去print

# 作業有要求要取 <= 2015 的日期，要研究一下
# 而且是以日期做篩選取出目標資料的，還有其他條件要看
# 除了日期，還有必須是三個字，並且為以下區域的其中一個：
# 中正區、萬華區、中山區、大同區、大安區、松山區、信義區、
# 士林區、文山區、北投區、內湖區、南港區。



# 作業是要求CSV格式，能用 + \n做換行，然後\n前不要打我平時程式排版空格，會顯示出來的。
# with open("data.csv" , mode = "w" , encoding = "utf-8") as file:
#     for date in Date_list: #這裡記得改正確的變數
#         file.write(Date["xpostDate"]+",")  #這裡記得改成要的正確內容