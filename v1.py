'''
v1.py
2023/2/21完成
此程式為Facebook "Basketball FRVR" 的外掛
遊戲連結: https://www.facebook.com/gaming/play/800772590062226/

使用方法：
Step 01. 登入Facebook並載入此遊戲畫面
Step 02. 執行此程式並將畫面跳回上步驟所開的畫面

註：本程式會需要取得您的螢幕截圖以及游標的控制權，因此在使用此外掛時無法同時使用本台電腦做其他事情
'''

import numpy as np
import cv2
import matplotlib
from matplotlib import pyplot as plt
import pyautogui
import time

for i in range(1000):
    print("This is the %d round"%(i+1))
    time.sleep(3.5)
    pyautogui.screenshot("screenshot/00.jpg")
    image = cv2.imread('screenshot/00.jpg')
    rgb=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    lower=np.array([240,222,101])
    upper=np.array([253,230,200]) #[247,225,106]~[210,191,90]
    output0=cv2.inRange(rgb,lower,upper)
    kernel=cv2.getStructuringElement(cv2.MORPH_RECT, (20,20))
    output0=cv2.dilate(output0,kernel)
    output0=cv2.erode(output0, kernel)
    contours, hierarchy = cv2.findContours(output0,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    area=0
    x0=0
    y0=0
    for contour in contours:
        if (area<cv2.contourArea(contour)):
           area = cv2.contourArea(contour)
           x0, y0, w0, h0 = cv2.boundingRect(contour)   #取得座標與長寬尺寸
           #print("the first pic bug x:",x0," y:",y0," w:",w0," h:",h0)
    if (h0<70 or x0==0): #畫面不在籃框頁面的情況
        break
    print("the first pic x:",x0," y:",y0," w:",w0," h:",h0)
    for ttt in range(1):
        
        for j in range(60): 
            time.sleep(0.01)
            pyautogui.screenshot("screenshot/%d.jpg"%j)
            now=time.time()*1000
            imagenew = cv2.imread('screenshot/%d.jpg'%j)
            rgbnew=cv2.cvtColor(imagenew, cv2.COLOR_BGR2RGB)
            outputnew=cv2.inRange(rgbnew,lower,upper)
            kernel=cv2.getStructuringElement(cv2.MORPH_RECT, (20,20)) #原本是(11,11)
            outputnew=cv2.dilate(outputnew,kernel)
            outputnew=cv2.erode(outputnew, kernel)
            contours, hierarchy = cv2.findContours(outputnew,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            area=0
            if (j==0):
                x=[]
                y=[]
                h=[]
            for contour in contours:
                if (area<cv2.contourArea(contour)):
                    area = cv2.contourArea(contour)
                    xx, yy, ww, hh = cv2.boundingRect(contour)   #取得座標與長寬尺寸\
            x.append(xx)
            y.append(yy)
            h.append(hh)
            #print("the",j,"pic x:",x[j]," y:",y[j]," w:",ww," h:",h[j])
            '''plt.imshow(cv2.cvtColor(outputnew, cv2.COLOR_BGR2RGB))
            cv2.imshow('super cool huh JIMMY',outputnew)
            cv2.waitKey(0)
            cv2.destroyAllWindows'''
            if (hh<70 or xx==0): #畫面不在籃框頁面的情況
                break
            if (x0==x[0]): #籃框不動的情況
                pyautogui.moveTo(1408, 1502, duration = 0.5)
                pyautogui.dragTo(1405+(x[0]+89-1405)*0.8, (y[0]+35-(y[0]-900)*0.9), duration=0.25+y[0]*0.00006, button='left')
                break
            if (j>=2):
                if (x[j-2]<x[j-1] and x[j-1]>x[j] and x[j-1]>1565): #開始往左
                    time.sleep(3.4) #3.5 2.95
                    pyautogui.moveTo(1408, 1502, duration = 0.5)
                    pyautogui.dragTo(1408, (y[0]+35-(y[0]-900)*0.85), duration=0.25+y[0]*0.00006, button='left') #35,0.9 892 991middle
                    break
        if (hh<70 or xx==0): #畫面不在籃框頁面的情況
            break
        print("Max:",max(x),x.index(max(x)),"Min:",min(x),x.index(min(x)))
        #print("Speed:",(max(x)-min(x))/(x.index(max(x))-x.index(min(x)))*0.1)
        print(x)
        print("Running time:",time.time()*1000-now)
        '''if(x0==x[0]):
            break'''
        
        