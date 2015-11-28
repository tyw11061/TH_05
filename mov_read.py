#-*- coding:utf-8 -*-
import numpy
import cv2
import sys


def error(cap):
    if not cap.isOpened():#ビデオファイルを読み込めたか確認
        print ("ファイルのオープンに失敗しました")
        return

    else:
        print ("ファイルの読み込みに成功しました")

def main(): #メイン処理を行う部分
    if len(sys.argv) < 2: #対象となるビデオが入力されていない場合
        print ("Error -　ビデオファイルが入力されていません")
        return

    cap = cv2.VideoCapture()
    cap.open(sys.argv[1])#ビデオファイルを開く

    error(cap)#ファイルの読み込みが成功したかチェックする

    width  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)#ビデオの大きさの入手
    print(width, height)
   


    while True:
        (rv,im) =cap.read()
        if not rv:
            break
        cv2.imshow('frame',im)
        cv2.waitKey(0)

main()
