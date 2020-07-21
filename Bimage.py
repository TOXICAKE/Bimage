#coding=utf-8
from PIL import Image
import sys
import os
Version="V1.1"
OptionNum=1
def Help():
    print("***************************************")
    print("*                Bimage               *")
    print("*           Devloped by N0P3          *")
    print("***************************************")
    print("["+Version+"]  ---- Help ----")
    print("")
    print(" [-d]+[Folder path]: Open the dir.")
    print(r'  \_[-p]+[Positon]: The position of target pixel. e.g. Bimage.py -d test -p "0,0"')
    print("")
    print(" [-g]+[gif path]: Open the gif.")
    print(r'  \_[-o]+[Output folder path]: The Output folder path. e.g. Bimage.py -g test.gif -o Output')
    print("")
    print(' [-b]+[Binary string]: Binary transfer character. e.g. Bimage.py -b "1001110 110000 1010000 110011"')
    print("")
    print(' [-s]+[String]: String transfer Binary. e.g. Bimage.py -s "Hello"')
    print("")
def error():
    print("ERROR: Can't find '"+sys.argv[OptionNum]+"',please use '-h' to check.")
    return
def GetNextArgv():
    global OptionNum
    OptionNum+=1
    try:
        result=sys.argv[OptionNum]
        return result
    except:
        print("ERROR: More parameters needed.")
        exit(0)
def SplitGif():
    GifPath=GetNextArgv()
    SaveDir=GetNextArgv()
    if SaveDir == '-o':
        SaveDir=GetNextArgv()
    else:
        print("ERROR: Need output file name.")
        exit(0)
    try:
        img = Image.open(GifPath)
    except:
        print("ERROR: No such file or directory: '"+GifPath+"'.")
        exit(0)
    GifPath=os.path.dirname(os.path.abspath(GifPath))
    try:
        os.mkdir(GifPath+'/'+SaveDir)
    except:
        print("ERROR: The directory already exists.")
        exit(0)
    try:
        i = 0
        while True:
            img.seek(i)
            img.save(GifPath+'/'+SaveDir+'/'+str(i)+'.png')
            i = i +1
    except:
        pass
    print('Finished.Total: '+str(i))
def ImportDir():
    index=0
    binstr=""
    divide=True
    RefColor=[0,0,0]
    _x=''
    _y=''
    x=0
    y=0
    DirPath=GetNextArgv()
    position=GetNextArgv()
    if position=='-p':
        position=GetNextArgv()
        for i in position:
            if divide :   
                if i==',' :
                    divide=False
                else:
                    _x+=i
            else:
                _y+=i
        if divide :
            print("ERROR: Syntax error. Please check your parameters.")
        try:
            x=int(_x)
            y=int(_y)
        except:
            print("ERROR: Parameters error.")
    else:
        print("ERROR: Need position.")
        exit(0)
    images = os.listdir(DirPath)
    try:
        images.sort(key=lambda la:int(la.split('.')[0]))
        print("Reference Image: "+images[0])
    except:
        print("Reference Image: "+images[0])
    try:
        img = Image.open(DirPath+'/'+images[0],'r')
        pixel = img.load()#导入像素
    except:
        print("ERROR: The folder contains non-image files.")
        exit(0)
    for i in range(0,3):
        RefColor[i]=pixel[x,y][i]
    for ImgName in images:
        diff=False
        try:
            img = Image.open(DirPath+'/'+ImgName,'r')
        except:
            print("ERROR: The folder contains non-image files.")
            exit(0)
        pixel = img.load()
        for i in range(0,3):
            check = pixel[x,y][i]
            if check != RefColor[i]:
                diff=True
        if diff:
            binstr+='0'
        else:
            binstr+='1'
        index+=1
        print(ImgName)
        if (index) % 8 == 0:
            binstr+=' '
    print('Bin: "'+binstr+'"')
    print('or')
    print('Bin: "',end='')
    for i in binstr:
        if i =='1':
            print('0',end='')
        elif i == '0':
            print('1',end='')
        else:
            print(' ',end='')
    print('"')
    return
def InputBin():
    BinStr=GetNextArgv()
    print(Bin2Str(BinStr))
    return
def InputStr():
    Str=GetNextArgv()
    print('"'+Str2Bin(Str)+'"')
    return
def Str2Bin(_str):
    return ' '.join([bin(ord(c)). replace('0b','') for c in _str])
def Bin2Str(_str):
    return ''.join([chr(i) for i in [int(b, 2) for b in _str.split(' ')]])
OptionSwitch={
    '-d': ImportDir,
    '-b': InputBin,
    '-s': InputStr,
    '-g': SplitGif,
    '-h': Help,
    }
try:
    Option=sys.argv[OptionNum]
except:
    Help()
    exit(0)
OptionSwitch.get(Option,error)()
