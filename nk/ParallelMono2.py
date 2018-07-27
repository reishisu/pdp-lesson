"""
並列処理成功作
( モノクロ処理　＜ まとめる処理 )
まとめる処理 × コア数
まとめる処理を減らしてうまく高速化できた！！

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
useCPU = 1

# ステップ数を初期化
step = 1


def main():
    try:
        useCPU = int( input("使用するCPUのコアを入力してください[ 1 ~ {0} ] : ".format(os.cpu_count())) )
    except:
        useCPU = os.cpu_count()
    if useCPU > os.cpu_count():
        useCPU = os.cpu_count()
    if useCPU > len(img):
        useCPU = len(img)
    step = int( len(img) / useCPU ) if int( len(img) / useCPU ) > 0 else 1
    print("{0}コアで処理を開始します!!".format(useCPU))
    mulchProcess(useCPU=useCPU, step= step)
    plt.imshow(img)
    plt.show()


def changeToGray( number: int , length: int ):
    """
    並列化する処理
    @param  number      (int) : 画像の処理対象範囲の先頭の添字
    @param  length      (int) : 対象範囲の長さ
    @return number      (int) : 画像の処理対象範囲の先頭の添字
    @return part_height (int) : 処理後の画像の配列
    """
    start = time.time()
    endPoint = number + length if number + length < len(img)  else  len(img) - 1
    part_height = img[ number : endPoint ]
    count = 0
    for width in part_height:
        width[...] = np.tile((width * [0.3, 0.59, 0.11]).sum(axis=1), (3, 1)).T
        count += 1
        common.progressBar(count, len(part_height))
    return number, part_height


def mulchProcess(useCPU: int, step: int):
    """
    マルチコアでプロセスを生成して実行させる処理
    @param  useCPU (int)  : 使用するCPUのコア数
    @param  step   (int)  : 画像の高さをコア数で割った数
    """
    # 配列の区切りポイント
    index_list = [ i for i in range(0, len(img), step)  if i < len(img) ]
    start = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=useCPU) as executer:
        fs = [ executer.submit(changeToGray, i, step) for i in index_list ]
        for future in concurrent.futures.as_completed(fs):
            line_number = future.result()[0]
            part_height  = future.result()[1]
            img[line_number:line_number+len(part_height)] = part_height
    print("終了しました!!")
    print("かかった時間:{0}秒".format( time.time()-start ))



if __name__ == '__main__':
    main()