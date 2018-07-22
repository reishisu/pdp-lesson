"""
並列で画像をモノクロにする
画像をコマンドライン引数で渡しておく
例）python Monochrome.py 画像.pngとか
事前に
  pip install opencv-python
  pip install matplotlib
  pip install futures
をしておく
"""

# スレッドで並列化を利用する為に必要なモジュール
import concurrent.futures

# その他各ライブラリをインポート
import matplotlib.pyplot as plt
import numpy as np
import cv2
import common
import sys
import os
import time


# コンソールをクリア
os.system('clear')

# コマンドライン引数から画像を読み込む
img = common.getRGBImage( sys.argv[1] )

# 使用数を初期化
useThread = 1
useCPU = 1

def main():
    # スレッドかCPUか選ぶ
    msg = "マルチスレッドかマルチプロセスどちらにしますか？\n"\
          "[1:マルチスレッド 2:マルチプロセス] : "
    multchType = int( input(msg.format(os.cpu_count())) )
    # 使用する数を選択
    if multchType == 1:
        useThread = int( input("使用するスレッドの数を入力してください : ") )
        if useThread > 1:
            mulchThread(useThread= useThread)
            plt.imshow(img)
            plt.show()
        else:
            print("0以下なので終了")
    elif multchType == 2:
        useCPU = int( input("使用するCPUのコアを入力してください[ 1 ~ {0} ] : ".format(os.cpu_count())) )
        if useCPU >= 1 and useCPU <= os.cpu_count():
            mulchProcess(useCPU= useCPU)
            plt.imshow(img)
            plt.show()
        else:
            print("選択の範囲外なので終了")
    else:
        print("どちらでもないので終了")



def changeToGray( number: int, width: np.ndarray ):
    """
    並列化する処理
    @param  number (int)       : このスレッドの番号
    @param  width (np.ndarray) : 横１行の配列[ [R, G, B], ・・・・ ,[R, G, B] ]
    @return number (int)       : このスレッドの番号
    @return width (np.ndarray) : 引数で受け取った配列をグレースケールに変換した配列
    """
    for pixel in width:
        # グレースケールにするする処理
        # グレーの値 = Redの値*0.3 + Greenの値*0.59 + Blueの値*0.11
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
    print("")
    start = time.time()
    count = 0
    print("{0}コアで処理を開始します!!".format(useCPU))
    with concurrent.futures.ProcessPoolExecutor(max_workers=useCPU) as executer:
        fs = [ executer.submit(changeToGray, i, width) for width, i in zip( img, range(len(img)) ) ]
        for future in concurrent.futures.as_completed(fs):
            line_number = future.result()[0]
            gray_width  = future.result()[1]
            img[line_number] = gray_width
            count += 1
            common.progressBar(count, len(img))
    print("\n終了しました!!")
    print("かかった時間:{0}秒".format( time.time()-start ))



def mulchThread(useThread: int):
    """
    スレッドを生成して実行させる処理
    @param  useThread (int)  : 使用するスレッドの数
    """
    print("")
    start = time.time()
    count = 0
    print("{0}スレッドで処理を開始します!!".format(useThread))
    with concurrent.futures.ThreadPoolExecutor(max_workers=useThread) as executer:
        fs = [ executer.submit(changeToGray, i, width) for width, i in zip( img, range(len(img)) ) ]
        for future in concurrent.futures.as_completed(fs):
            line_number = future.result()[0]
            gray_width  = future.result()[1]
            img[line_number] = gray_width
            count += 1
            common.progressBar(count, len(img))
    print("\n終了しました!!")
    print("かかった時間:{0}秒".format( time.time()-start ))



if __name__ == '__main__':
    main()