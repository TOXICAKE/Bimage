# ! python3
#coding=utf-8
from PIL import Image
import re
import sys
import os
Version="V2.1"
OptionNum=1
def Help():
    print("***************************************")
    print("*                Bimage               *")
    print("*           Devloped by N0P3          *")
    print("***************************************")
    print("["+Version+"]  ---- Help ----")
    print("")
    print(" [-d]+[Folder path]: Open the dir.")
    print(r'  \_[-p]+[Positon]: The position of target pixel. e.g. Python3 Bimage.py -d test -p "0,0"')
    print("")
    print(" [-g]+[gif path]: Open the gif.")
    print(r'  \_[-o]+[Output folder path]: The Output folder path. e.g. Python3 Bimage.py -g test.gif -o Output')
    print("")
    print(" [-i]+[Image path]: Open the image.")
    print(r'  \_[-size]+[Little image size]: The size of first little image.')
    print(r'       \_[-p]+[Positon]: The position of target pixel. e.g. Python3 Bimage.py -i test.png -size "63,61" -p "34,47"')
    print("")
    print(' [-b]+[Binary string]: Binary transfer character. e.g. Python3 Bimage.py -b "1001110 110000 1010000 110011"')
    print("")
    print(' [-s]+[String]: String transfer Binary. e.g. Python3 Bimage.py -s "Hello"')
    print("")
def error():
    print("ERROR: Can't find '"+sys.argv[OptionNum]+"',please use '-h' to check.")
    return
def GetNextArgv(Stop=True):
    global OptionNum
    OptionNum+=1
    try:
        result=sys.argv[OptionNum]
        return result
    except:
        if Stop:
            print("ERROR: More parameters needed.")
            exit(0)
        else:
            return "ERROR"
def SplitBin(_str,_bit):
    s_str=re.findall(r'.{'+str(_bit)+'}',_str)
    result = ""
    for char in s_str :
        result += chr(int(char,2))
    return result
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
def InputImage():
    x=0
    y=0
    _x=''
    _y=''
    hight=0
    width=0
    _hight=''
    _width=''
    divide=True
    RefColor=[0,0,0]
    ImagePath=GetNextArgv()
    size=GetNextArgv()
    if size =='-size':
            size=GetNextArgv()
            for i in size:
                if divide :   
                    if i==',' :
                        divide=False
                    else:
                        _width+=i
                else:
                    _hight+=i
            if divide :
                print("ERROR: Syntax error. Please check your parameters.")
                exit(0)
            try:
                width=int(_width)
                hight=int(_hight)
            except:
                print("ERROR: '-size',Parameters error.")
                exit(0)
    else:
            print('ERROR: Need "-size"')
            exit(0)
    divide=True
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
                exit(0)
            try:
                x=int(_x)
                y=int(_y)
            except:
                print("ERROR: '-p',Parameters error.")
                exit(0)
    else:
        print("ERROR: Need position.")
        exit(0)
    Zero=GetNextArgv(False)
    ZeroX=0
    ZeroY=0
    if Zero=="-z":
        divide=True
        _ZeroX=''
        _ZeroY=''
        Zero=GetNextArgv()
        for i in Zero:
            if divide :   
                if i==',' :
                    divide=False
                else:
                    _ZeroX+=i
            else:
                _ZeroY+=i
        if divide :
            print("ERROR: Syntax error. Please check your parameters.")
            exit(0)
        try:
            ZeroX=int(_ZeroX)
            ZeroY=int(_ZeroY)
        except:
            print("ERROR: '-p',Parameters error.")
            exit(0)
    try:
        img=Image.open(ImagePath,'r')
    except:
        print("ERROR: Can't load this image '"+ImagePath+"'")
        exit(0)
    pixel=img.load()
    width=width-ZeroX
    hight=hight-ZeroY
    x=x-ZeroX
    y=y-ZeroY
    ImageWidth=img.size[0]
    ImageHight=img.size[1]
    ZoneNumX=(ImageWidth-ZeroX)/width
    ZoneNumY=(ImageHight-ZeroY)/hight
    print("ZoneNumX:"+str(int(ZoneNumX)))
    print("ZoneNumY:"+str(int(ZoneNumY)))
    NowX=ZeroX+x
    NowY=ZeroY+y
    index=0
    binstr=''
    for i in range(0,3):
        RefColor[i]=pixel[NowX,NowY][i]
    for i in range(0,int(ZoneNumY)):
        for j in range(0,int(ZoneNumX)):
            NowX=ZeroX+width*j+x
            NowY=ZeroY+hight*i+y
            diff=False
            print("Pixel:"+str(NowX)+","+str(NowY)+"|"+str(j)+","+str(i),end='')
            for k in range(0,3):
                check = pixel[NowX,NowY][k]
                if check != RefColor[k]:
                    diff=True
            print("|")
            if diff:
                binstr+='0'
            else:
                binstr+='1'
            index+=1
            if (index) % 8 == 0:
                binstr+=' '
    print('Bin: '+binstr)
    print('or')
    print('Bin: ',end='')
    for i in binstr:
        if i =='1':
            print('0',end='')
        elif i == '0':
            print('1',end='')
        else:
            print(' ',end='')
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
            exit(0)
        try:
            x=int(_x)
            y=int(_y)
        except:
            print("ERROR: Parameters error.")
            exit(0)
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
        if (index) % 8 == 0:
            binstr+=' '
    print('Bin: '+binstr)
    print('or')
    print('Bin: ',end='')
    for i in binstr:
        if i =='1':
            print('0',end='')
        elif i == '0':
            print('1',end='')
        else:
            print(' ',end='')
    return
def InputBin():
    BinStr=GetNextArgv()
    print('Result: '+Bin2Str(BinStr))
    return
def InputStr():
    Str=GetNextArgv()
    print('"'+Str2Bin(Str)+'"')
    return
def Str2Bin(_str):
    return ' '.join([bin(ord(c)). replace('0b','') for c in _str])
def Bin2Str(_str):
    try:
        return ''.join([chr(i) for i in [int(b, 2) for b in _str.split(' ')]])
    except:
        print('Result: '+SplitBin(_str,6))
        print('or')
        print('Result: '+SplitBin(_str,7))
        print('or')
        return SplitBin(_str,8)
OptionSwitch={
    '-d': ImportDir,
    '-b': InputBin,
    '-s': InputStr,
    '-g': SplitGif,
    '-h': Help,
    '-i': InputImage,
    }
try:
    Option=sys.argv[OptionNum]
except:
    Help()
    exit(0)
OptionSwitch.get(Option,error)()
