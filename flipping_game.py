#!/usr/bin/env python
# coding: utf-8

# In[5]:


from random import *
from turtle import *
from turtle import Screen, Turtle


# In[6]:


pip install opencv-python


# In[7]:


import os,cv2,random


# In[8]:


#每一個小格的寬度
w_box=100
#一行和一列總共:8×8=64格
n_box=8
#每一個格子內的數字0~31，有一對，總共64個
num_labels = list(range(32)) * 2
#64個小格子
hide = [True] * 64

#狀態字典
state = {'mark': None}

        
img = [] #圖片串列 
# 讀取圖片函式
def read_directory(directory_name):
    #讀取所有圖片，directory_name為資料夾名稱
    for filename in os.listdir(r"./"+directory_name):
        img.append(filename)
        
read_directory("picture")
image=random.sample(img,1)
for i in image:
    bt21_image=bgpic('%s'%i)

    
#畫一個小方格函式
def square(x, y):
    up()
    goto(x, y)
    down()
    #網格線顏色為白色，背景顏色為紫色
    color('white', '#B399FF')
    begin_fill()
    #用“_”代替臨時性i
    for _ in range(4):
        forward(w_box) #邊長小格子的寬度
        left(90)
    end_fill()

    
#索引函式
def index(x, y):
    return int((x + w_box*n_box//2) // w_box + ((y + w_box*n_box/2) // w_box) * n_box)


#x和y座標計數函式
def xy(count):
    return (count % n_box) * w_box - w_box*n_box//2, (count // n_box) * w_box - w_box*n_box/2


#顯示標籤
def tap(x, y):
    spot = index(x, y) #第二次按下去的值
    mark = state['mark'] #按下去的值
    #判斷為None、按同一點、數字不同
    if mark is None or mark == spot or num_labels[mark] != num_labels[spot]: 
        state['mark'] = spot
    #判斷為答對
    else: 
        #將答對的格子隱藏
        hide[mark] = False 
        hide[spot] = False 
        state['mark'] = None 

        
#繪畫的總函式
def draw():
    clear()
    goto(0, 0)
#載入背景圖片
    shape(bt21_image)

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark'] 

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y+2)
        #顯示數字的顏色
        color('white')
        write(num_labels[mark], font=('Arial',25, 'normal'))

    update()
    #計時器，100毫秒
    ontimer(draw, 100)

def main():
    while True:
        #將num_labels隨機排序
        shuffle(num_labels)
        #遊戲視窗大小設定
        setup(w_box*n_box+20, w_box*n_box+20, 500, 100)
        #畫筆隱藏
        hideturtle()
        #一次性畫出格子
        tracer(False)
        #調出點選螢幕函式
        onscreenclick(tap)
        #調出繪畫函式
        draw()
        done()
        clear()
        continue

if __name__ == "__main__":
        main()

