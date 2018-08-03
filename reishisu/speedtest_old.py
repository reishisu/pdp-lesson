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
    """
        並列化する処理
        @param  number (int)       : このプロセスの番号
        @param  width (np.ndarray) : 横１行の配列[ [R, G, B], ・・・・ ,[R, G, B] ]
        @return number (int)       : このプロセスの番号
        @return width (np.ndarray) : 引数で受け取った配列をグレースケールに変換した配列
        """
    for pixel in width:
        # グレースケールにするする処理
        gray = int(pixel[0]*0.3) + int(pixel[1]*0.59) + int(pixel[2]*0.11)
        pixel[0] = gray # Red
        pixel[1] = gray # Green
        pixel[2] = gray # Blue
    return number, width


def mulchProcess(useCPU: int):
    """
        マルチコアでプロセスを生成して実行させる処理
        @param  useCPU (int)  : 使用するCPUのコア数
        """
    start = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=useCPU) as executer:
        fs = [ executer.submit(changeToGray, i, width) for width, i in zip( img, range(len(img)) ) ]
        for future in concurrent.futures.as_completed(fs):
            line_number = future.result()[0]
            gray_width  = future.result()[1]
            img[line_number] = gray_width
    print(str( time.time()-start ))

if __name__ == '__main__':
    main()
