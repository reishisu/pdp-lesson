import concurrent.futures
import matplotlib.pyplot as plt
import numpy as np
import cv2, sys, os, time

img = cv2.cvtColor(cv2.imread(sys.argv[1]), cv2.COLOR_BGR2RGB)
useCPU = int( sys.argv[2] )
step = int( len(img) / useCPU )

def main():
    """
    メイン関数
    """
    mulchProcess(useCPU= useCPU, step= step)


def changeToGray( number: int, length: int ):
    endPioint = number + length  if number + length < len(img)  else  len(img) - 1
    part_height = img[ number : endPioint-1 ]
    for width in part_height:
         for pixel in width:
             # グレースケールにするする処理
             gray = int(pixel[0]*0.3) + int(pixel[1]*0.59) + int(pixel[2]*0.11)
             pixel[0] = gray # Red
             pixel[1] = gray # Green
             pixel[2] = gray # Blue
    return number, part_height


def mulchProcess(useCPU: int, step: int):
    start = time.time()
    index_list = [ i for i in range(0, len(img), step)  if i < len(img) ]
    with concurrent.futures.ProcessPoolExecutor(max_workers=useCPU) as executer:
        fs = [ executer.submit(changeToGray, i, step) for i in index_list ]
        for future in concurrent.futures.as_completed(fs):
            line_number = future.result()[0]
            part_height  = future.result()[1]
            for i, height in zip( range(line_number, line_number+len(part_height)), part_height ):
                img[i] = height
    print(str( time.time()-start ) + "秒かかりました！！")

if __name__ == '__main__':
    main()

