import cv2
import os
import matplotlib.pyplot as plt
import glob
import numpy as np
from natsort import natsorted

#動画ファイルの読み込み
file_name = u"images/bld.mp4"
v = cv2.VideoCapture(file_name)

#スクリーンキャプチャを保存するディレクトリ
dir_name = "screen_caps"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

#フレーム数を取得
frame_count = int(v.get(7))
for i in range(frame_count):
    _, frame = v.read()
    cv2.imwrite(dir_name+ "/" + str(i) + ".png", frame)

file_list=glob.glob('./screen_caps/*')
y=[]
count=0
for path in natsorted(file_list):
    im=cv2.imread(path)
    a=im.mean()
    y=y+[a]
    count+=1
x = np.arange(0,count)
plt.plot(x,y)
plt.xlabel("frame")
plt.ylabel("bightness value")
plt.title("Pulse")
plt.show()