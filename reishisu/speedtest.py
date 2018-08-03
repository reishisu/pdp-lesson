"""
※これはただグレースケール化の速度を計測するためのファイルです
並列で画像をモノクロにする
画像をコマンドライン引数の第1引数で渡しておく
コア数をコマンドライン引数の第2引数で指定
例）python Monochrome.py 画像.png 4とか
事前に
  pip install opencv-python
  pip install matplotlib
  pip install futures
をしておく
"""
import concurrent.futures
import matplotlib.pyplot as plt
import numpy as np
import cv2
import common
import sys
import os
import time

img = common.getRGBImage( sys.argv[1] )
useCPU = int( sys.argv[2] )

def main():
    mulchProcess(useCPU=useCPU)

def changeToGray( number: int, width: np.ndarray ):
    return number, np.tile((width * [0.3, 0.59, 0.11]).sum(axis=1),(3, 1)).T


def mulchProcess(useCPU: int):
    start = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=useCPU) as executer:
        fs = [ executer.submit(changeToGray, i, width) for width, i in zip( img, range(len(img)) ) ]
        for future in concurrent.futures.as_completed(fs):
            img[future.result()[0]] = future.result()[1]
    finish = time.time()-start
    print(str(finish) + "秒かかりました！！")


if __name__ == '__main__':
    main()