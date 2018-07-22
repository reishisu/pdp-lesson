"""
並列で画像をモノクロにする

画像をコマンドライン引数で渡しておく
例）python Monochrome.py 画像.pngとか

事前に
　pip install opencv-python
　pip install matplotlib
をしておく
"""

# スレッドで並列化を利用する為に必要なモジュール
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# その他各ライブラリをインポート
import matplotlib.pyplot as plt
import cv2
import common
import sys
import os


def main():
    """ 実行されるメイン関数 """
    # コンソールを綺麗にする
    os.system('clear')
    # コマンドライン引数から画像を読み込み
    fileName = sys.argv[1]
    img = cv2.imread(fileName)
    # 色の並びがデフォルトでは[B, G, R]となっているので[R, G, B]に変換する
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    print(len(img))         # 縦
    print(len(img[0]))      # 横
    print(len(img[0][0]))   # RGB
    cores = os.cpu_count()
    print(len(img)/os.cpu_count())


    # マルチプロセスを管理する配列
    futures = []
    #  CPUのコア数を取得している
    # cpu_core = os.cpu_count()
    pool = ThreadPoolExecutor(4)
    # 仕事の分割数
    task_num = cpu_core * 2
    # 使用するコア数を引数にとって並列処理を実行する
    with ProcessPoolExecutor( cpu_core ) as executer:
        # 配列の要素をタスク数で割って均等に分散させる
        avg = int( len( img ) / task_num )
        
        # タスクを実行する
        for index in range( task_num ):

            # 前の添字
            pre = avg * index

            # 今の添字
            now = avg * (index + 1)
            
            # マルチプロセスを管理する配列にプロセス追加する
            futures.append(executer.submit(paralleImageToMono, img[ pre, now], index))

    # 実行が終わったのから結果を表示
    for x in as_completed(futures):
        print( x.result() )


def paralleImageToMono(partImage):
    """
    並列化する処理
    @param  width (np.Array) : 元の画像の配列一部
    @return 
    """
    grayImage = partImage
    for height in grayImage:
        for width in height:
            # グレースケールにするする処理
            # グレーの値 = Redの値*0.3 + Greenの値*0.59 + Blueの値*0.11
            gray = int(width[0]*0.3) + int(width[1]*0.59) + int(width[2]*0.11)
            width[0] = gray # Red  
            width[1] = gray # Green
            width[2] = gray # Blue
    return grayImage

if __name__ == '__main__':
    main()