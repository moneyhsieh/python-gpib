# -*- coding: UTF-8 -*-
x = range(10) # 橫軸的數據 
y = [i*i for i in x] # 縱軸的數據 
pl.plot(x, y) # 調用pylab的plot函數繪製曲線 
pl.show # 顯示繪製出的圖
