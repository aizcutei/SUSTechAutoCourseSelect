import tkinter as tk
import requests
import re
import threading
from bs4 import BeautifulSoup

RC = []
OC = []
TSC = []
CSC = []
CMC = []
PC = []
Result = []

system_url = 'http://jwxt.sustc.edu.cn/jsxsd/framework/xsMain.jsp'
cas_url = 'https://cas.sustc.edu.cn/cas/login'
required_course_url = 'http://jwxt.sustc.edu.cn/jsxsd/xsxkkc/bxxkOper'
optional_course_url = 'http://jwxt.sustc.edu.cn/jsxsd/xsxkkc/xxxkOper'
this_semester_course_url = 'http://jwxt.sustc.edu.cn/jsxsd/xsxkkc/bxqjhxkOper'
cross_semester_course_url = 'http://jwxt.sustc.edu.cn/jsxsd/xsxkkc/knjxkOper'
cross_major_course_url = 'http://jwxt.sustc.edu.cn/jsxsd/xsxkkc/fawxkOper'
pubilc_course_url = 'http://jwxt.sustc.edu.cn/jsxsd/xsxkkc/ggxxkxkOper'

def RCinsert():
    Ifhere = True
    classnum = RCInput.get()
    for cla in RC:
        if cla == classnum:
            Ifhere = False
        elif classnum == '':
            Ifhere = False
    if Ifhere:
        RClist.insert('end',classnum)
        RC.append(classnum)
def RCdelete():
    RClist.delete('end')
    if RC:
        RC.pop()

def OCinsert():
    Ifhere = True
    classnum = OCInput.get()
    for cla in OC:
        if cla == classnum:
            Ifhere = False
    if Ifhere:
        OClist.insert('end',classnum)
        OC.append(classnum)
def OCdelete():
    OClist.delete('end')
    if OC:
        OC.pop()

def TSCinsert():
    Ifhere = True
    classnum = TSCInput.get()
    for cla in TSC:
        if cla == classnum:
            Ifhere = False
    if Ifhere:
        TSClist.insert('end',classnum)
        TSC.append(classnum)
def TSCdelete():
    TSClist.delete('end')
    if TSC:
        TSC.pop()

def CSCinsert():
    Ifhere = True
    classnum = CSCInput.get()
    for cla in CSC:
        if cla == classnum:
            Ifhere = False
    if Ifhere:
        CSClist.insert('end',classnum)
        CSC.append(classnum)
def CSCdelete():
    CSClist.delete('end')
    if CSC:
        CSC.pop()

def CMCinsert():
    Ifhere = True
    classnum = CMCInput.get()
    for cla in CMC:
        if cla == classnum:
            Ifhere = False
    if Ifhere:
        CMClist.insert('end',classnum)
        CMC.append(classnum)
def CMCdelete():
    CMClist.delete('end')
    if CMC:
        CMC.pop()

def PCinsert():
    Ifhere = True
    classnum = PCInput.get()
    for cla in PC:
        if cla == classnum:
            Ifhere = False
    if Ifhere:
        PClist.insert('end',classnum)
        PC.append(classnum)
def PCdelete():
    PClist.delete('end')
    if PC:
        PC.pop()

def login():
    username = usernameInput.get()
    password = passwordInput.get()
    session = requests.Session()
    headers={'Accept':'*/*',
             'Accept-Encoding':'gzip,deflate',
             'Accept-Language':'zh-Hans-CN, zh-Hans; q=0.5',
             'Connection':'Keep-Alive',
             'Host':'jwxt.sustc.edu.cn',
             'Referer':'https://cas.sustc.edu.cn/cas/login',
             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
             'X-Requested-With':'XMLHttpRequest'
            }            
    getexecution = session.get(system_url, headers = headers)
    executionSoup = BeautifulSoup(getexecution.content,"html.parser")
    execution = executionSoup.find('input', {'name':'execution'})['value']
    post_data = {'username':username,'password':password,'_eventId':'submit','execution':execution,'geolocation':''}
    session.post(cas_url, data=post_data)
    testlogin = session.get(system_url, headers=headers)
    searchusername = re.search(username,str(testlogin.content),re.M|re.I)
    if searchusername == None:
        tk.Label(window,text="登陆失败").place(x=100,y=200)
    else:
        tk.Label(window,text="登录成功").place(x=100,y=200)

def start():
    #模拟登录
    username = usernameInput.get()
    password = passwordInput.get()
    session = requests.Session()
    headers={'Accept':'*/*',
             'Accept-Encoding':'gzip,deflate',
             'Accept-Language':'zh-Hans-CN, zh-Hans; q=0.5',
             'Connection':'Keep-Alive',
             'Host':'jwxt.sustc.edu.cn',
             'Referer':'https://cas.sustc.edu.cn/cas/login',
             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
             'X-Requested-With':'XMLHttpRequest'
            }            
    getexecution = session.get(system_url, headers = headers)
    executionSoup = BeautifulSoup(getexecution.content,"html.parser")
    execution = executionSoup.find('input', {'name':'execution'})['value']
    post_data = {'username':username,'password':password,'_eventId':'submit','execution':execution,'geolocation':''}
    session.post(cas_url, data=post_data)
    testlogin = session.get(system_url, headers=headers)
    searchusername = re.search(username,str(testlogin.content),re.M|re.I)
    if searchusername == None:
        tk.Label(window,text="登陆失败").place(x=100,y=200)
    else:
        tk.Label(window,text="登录成功").place(x=100,y=200)
    #刷新网页
        #还没写
        #tk.Label(window,text="系统开放").place(x=100,y=200)
    #正式抢课
    session.get('http://jwxt.sustc.edu.cn/jsxsd/xsxk/xsxk_index?jx0502zbid=D102885918754CD79C2E3F167A288A11', headers=headers) #选课系统登录
    params = {'jx0404id':'','xkzy':'','trjf':''}
    if RC:
        for cla in RC:
            params['jx0404id'] = cla
            s = session.get(url=required_course_url,params=params,headers=headers)
            Result.append(s.content)
    if OC:
        for cla in OC:
            params['jx0404id'] = cla
            s = session.get(url=optional_course_url,params=params,headers=headers)
            Result.append(s.content)
    if TSC:
        for cla in TSC:
            params['jx0404id'] = cla
            s = session.get(url=this_semester_course_url,params=params,headers=headers)
            Result.append(s.content)
    if CSC:
        for cla in CSC:
            params['jx0404id'] = cla
            s = session.get(url=cross_semester_course_url,params=params,headers=headers)
            Result.append(s.content)
    if CMC:
        for cla in CMC:
            params['jx0404id'] = cla
            s = session.get(url=cross_major_course_url,params=params,headers=headers)
            Result.append(s.content)
    if PC:
        for cla in PC:
            params['jx0404id'] = cla
            s = session.get(url=pubilc_course_url,params=params,headers=headers)
            Result.append(s.content)
    i = 200
    for r in Result:
        tk.Label(window,text=r).place(x=0,y=i)
        i += 25

window = tk.Tk()
window.geometry('900x700')
tk.Label(window, text='学号').place(x=50,y=50)
tk.Label(window, text='密码').place(x=50,y=100)
usernameInput = tk.Entry(window)
usernameInput.place(x=100,y=50)
passwordInput = tk.Entry(window, show = '*')
passwordInput.place(x=100,y=100)
testlogin = tk.Button(window, text='登录测试',command = login)
testlogin.place(x=80,y=140)
startbutton = tk.Button(window,text='开始抢课',command = start)
startbutton.place(x=160,y=140)

tk.Label(window,text='必修课表').place(x=300,y=50-30)
RClist = tk.Listbox(window)
RClist.place(x=300,y=100-20-30)
RCInput = tk.Entry(window)
RCInput.place(x=300,y=320-20-30)
RCbutton = tk.Button(window,text='加入一项',command = RCinsert)
RCbutton.place(x=300,y=350-20-30)
RCdeletebutton = tk.Button(window,text="删除一项",command = RCdelete)
RCdeletebutton.place(x=400,y=350-20-30)

tk.Label(window,text='选修课表').place(x=500,y=50-30)
OClist = tk.Listbox(window)
OClist.place(x=500,y=100-20-30)
OCInput = tk.Entry(window)
OCInput.place(x=500,y=320-20-30)
OCbutton = tk.Button(window,text='加入一项',command = OCinsert)
OCbutton.place(x=500,y=350-20-30)
OCdeletebutton = tk.Button(window,text="删除一项",command = OCdelete)
OCdeletebutton.place(x=600,y=350-20-30)

tk.Label(window,text='本学期必选课表').place(x=700,y=50-30)
TSClist = tk.Listbox(window)
TSClist.place(x=700,y=100-20-30)
TSCInput = tk.Entry(window)
TSCInput.place(x=700,y=320-20-30)
TSCbutton = tk.Button(window,text='加入一项',command = TSCinsert)
TSCbutton.place(x=700,y=350-20-30)
TSCdeletebutton = tk.Button(window,text="删除一项",command = TSCdelete)
TSCdeletebutton.place(x=800,y=350-20-30)

tk.Label(window,text='跨年级选课').place(x=300,y=350)
CSClist = tk.Listbox(window)
CSClist.place(x=300,y=100+300-20)
CSCInput = tk.Entry(window)
CSCInput.place(x=300,y=320+300-20)
CSCbutton = tk.Button(window,text='加入一项',command = CSCinsert)
CSCbutton.place(x=300,y=350+300-20)
CSCdeletebutton = tk.Button(window,text="删除一项",command = CSCdelete)
CSCdeletebutton.place(x=400,y=350+300-20)

tk.Label(window,text='跨专业选课').place(x=500,y=350)
CMClist = tk.Listbox(window)
CMClist.place(x=500,y=100+300-20)
CMCInput = tk.Entry(window)
CMCInput.place(x=500,y=320+300-20)
CMCbutton = tk.Button(window,text='加入一项',command = CMCinsert)
CMCbutton.place(x=500,y=350+300-20)
CMCdeletebutton = tk.Button(window,text="删除一项",command = CMCdelete)
CMCdeletebutton.place(x=600,y=350+300-20)

tk.Label(window,text='公选课课表').place(x=700,y=350)
PClist = tk.Listbox(window)
PClist.place(x=700,y=100+300-20)
PCInput = tk.Entry(window)
PCInput.place(x=700,y=320+300-20)
PCbutton = tk.Button(window,text='加入一项',command = PCinsert)
PCbutton.place(x=700,y=350+300-20)
PCdeletebutton = tk.Button(window,text="删除一项",command = PCdelete)
PCdeletebutton.place(x=800,y=350+300-20)

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Open')
filemenu.add_command(label='Save')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=window.quit)
window.title("很垃圾的抢课脚本beta")
#window.iconbitmap("")改图标
window.mainloop()