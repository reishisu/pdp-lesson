import concurrent.futures
import matplotlib.pyplot as plt
import numpy as np
import cv2, sys, os, time

img = cv2.cvtColor(cv2.imread(sys.argv[1]), cv2.COLOR_BGR2RGB)
useCPU = int( sys.argv[2] )

def main():
    """
    メイン関数
    """
    mulchProcess(useCPU= useCPU)


def changeToGray( number: int, width: np.ndarray ):
    for pixel in width:
        # グレースケールにするする処理
        gray = int(pixel[0]*0.3) + int(pixel[1]*0.59) + int(pixel[2]*0.11)
        pixel[0] = gray # Red
        pixel[1] = gray # Green
        pixel[2] = gray # Blue
    return number, width


def mulchProcess(useCPU: int):
    start = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=useCPU) as executer:
        fs = [ executer.submit(changeToGray, i, width) for width, i in zip( img, range(len(img)) ) ]
        for future in concurrent.futures.as_completed(fs):
            line_number = future.result()[0]
            gray_width  = future.result()[1]
            img[line_number] = gray_width
    print(str( time.time()-start ) + "秒かかりました！！")

if __name__ == '__main__':
    main()
