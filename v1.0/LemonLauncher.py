# This is a python for LemonLauncher window.
import tkinter
import tkinter.messagebox as msgbox
import minecraft_launcher_lib as mc
import data
import webbrowser
import time

GamesList = ['游戏列表', '1.17', '1.19']
UserList = ['HymnFo', 'HymnFoF13']
GameDirectory = ''


def StartGame():
    TimeNow = time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime())
    print(TimeNow+'[INFO]run minecraft')
    msgbox.showinfo('[LemonLauncher]', '游戏启动指令已发出，\n请耐心等待游戏启动')


def GameInstall():
    pass


def GameInstaller(self):
    mc.install.install_minecraft_version(self, data.minecraft_directory)


def MicrosoftLogin():
    Login_Microsoft = tkinter.Tk()
    TellUser = tkinter.Label(Login_Microsoft, text='尊敬的Minecraft玩家，您选择了Microsoft登录，\n稍后会打开浏览器，进行登录，\n我们只获取Minecraft'
                                                   '信息，不会保存您的密码')
    TellUser.pack()
    a = mc.microsoft_account.get_login_url(client_id="0e9621ea-900a-436e-a8a5-92c5bd41d938",
                                           redirect_uri="https://login.live.com/oauth20_desktop.srf")
    print(a)
    webbrowser.open(a)
    Login_Microsoft.mainloop()


def login():
    LoginWin = tkinter.Tk()
    LoginWin.title('添加游戏账户')
    LoginWin.geometry('300x450')
    LoginWin.resizable(False, False)
    LoginMicrosoft = tkinter.Button(LoginWin, text='微软登录', command=MicrosoftLogin)
    LoginMicrosoft.pack()
    LoginWin.mainloop()


# 新用户LemonLauncher使用向导
def NewUserWinDelete():
    msgbox.showerror('error',
                     'You can\'t close the guide on this way.\n你不能这样关闭此向导，它可以帮助你设置LemonLauncher。')


def SaveGameDirectory():
    global GameDirectorySettingEntry
    global Temporary_GameDirectory
    now = GameDirectorySettingEntry.get()
    Temporary_GameDirectory = now


def close_():
    global NewUser
    NewUser.destroy()


if data.OpenWar == 0:
    NewUser = tkinter.Tk()
    NewUser.title('LemonLauncher guide')
    NewUser.geometry('225x250')
    NewUser.resizable(False, False)
    NewUser.protocol("WM_DELETE_WINDOW", NewUserWinDelete)
    TellNewUser = tkinter.Label(NewUser, text='这是一个LemonLauncher的向导，\n别担心，只是设置Launcher！', bg='white')
    TellNewUser.pack()
    GameDirectorySettingLabel = tkinter.Label(NewUser, text='设置游戏根目录(谨慎设置！)')
    GameDirectorySettingLabel.pack(anchor='w')
    GameDirectorySettingEntry = tkinter.Entry(NewUser)
    GameDirectorySettingEntry.pack(anchor='e')
    GameDirectorySettingButton = tkinter.Button(NewUser, text='保存游戏根目录', command=SaveGameDirectory)
    GameDirectorySettingButton.pack()
    close = tkinter.Button(NewUser, text='close', command=close_)
    close.pack()
    NewUser.mainloop()

root = tkinter.Tk()

root.title('LemonLauncher')
root.geometry('300x450')
root.resizable(False, False)
'''root组件定义'''
var = tkinter.StringVar()
var.set(GamesList[0])
GameOption = tkinter.OptionMenu(root, var, *GamesList)
GameOption.pack()
LoginButton = tkinter.Button(root, text='添加游戏账户', command=login, bd=0)
LoginButton.pack()
var_UserList = tkinter.StringVar()
UserList = tkinter.OptionMenu(root, var_UserList, *UserList)
UserList.pack()
StartGame = tkinter.Button(root, text='启动游戏', command=StartGame)
StartGame.pack()
testButton = tkinter.Button(root, text='test', command=GameInstall)
testButton.pack()

root.mainloop()
