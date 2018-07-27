"""
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
step = int( len(img) / useCPU )

def main():
    mulchProcess(useCPU=useCPU, step= step)

def changeToGray( number: int , length: int ):
    start = time.time()
    endPoint = number + length if number + length < len(img)  else  len(img) - 1
    part_height = img[ number : endPoint ]
    for width in part_height:
        width[...] = np.tile((width * [0.3, 0.59, 0.11]).sum(axis=1), (3, 1)).T
    return number, part_height

def mulchProcess(useCPU: int, step: int):
    index_list = [ i for i in range(0, len(img), step)  if i < len(img) ]
    start = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=useCPU) as executer:
        fs = [ executer.submit(changeToGray, i, step) for i in index_list ]
        for future in concurrent.futures.as_completed(fs):
            line_number = future.result()[0]
            part_height  = future.result()[1]
            img[line_number:line_number+len(part_height)] = part_height
    finish = time.time()-start
    print(str(finish))


if __name__ == '__main__':
    main()