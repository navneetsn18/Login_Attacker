import webbrowser,time
import pyautogui as pg
url=""
url=input("Enter the url: ")
email="testingfornsn@gmail.com"
uname="Navneet Singh Negi"
contactno="7011710907"
gender="Male"
Country="India"
date="18"
month="Sept"
year="1999"
employeeid="1713114026"
loc="New Delhi"

webbrowser.open(url)
time.sleep(3)
#Change this with the x,y coordinates of 
pg.click(514,622)
time.sleep(20)
#Click next page
pg.click(430,513)
#click Proceed page
pg.click(1255,477)
#Start page
pg.click(529,307)
#Email Field
pg.click(458,304)
pg.typewrite(email)
pg.press("tab")
pg.typewrite(uname)
pg.press("tab")
pg.typewrite(contactno)
pg.press("tab")
pg.typewrite(gender)
pg.press("tab")
pg.typewrite(Country)
pg.press("tab")
pg.typewrite(month)
pg.press("tab")
pg.typewrite(date)
pg.press("tab")
pg.typewrite(year)
pg.press("tab")
pg.typewrite(employeeid)
pg.press("tab")
pg.typewrite(loc)
pg.press("tab")
#click terms and condition button
pg.click(174,740)
#click next button
pg.click(1247,819)
print("Now keep calm and do your work.")