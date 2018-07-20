"""
画像をモノクロにする

画像をコマンドライン引数で渡しておく
例）python Monochrome.py 画像.pngとか

事前に
　pip install opencv-python
　pip install matplotlib
をしておく
"""

# 各種ライブラリをインポート
import matplotlib.pyplot as plt
import common
import cv2
import sys
import os
import time

def main():
    # コンソールを綺麗にする
    os.system('clear')

    # コマンドライン引数から画像を読み込み
    fileName = sys.argv[1]
    img = cv2.imread(fileName)

    # 色の並びがデフォルトでは[B, G, R]となっているので[R, G, B]に変換する
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # グレースケールにする処理
    img = changeToGray(img)

    # グレースケールに変換された画像を保存する
    cv2.imwrite(common.anyFileNameGrayExetention(fileName), img)

    # 画像を表示
    plt.imshow(img)
    plt.show()


def changeToGray(img):
    """
    画像をモノクロに変更する関数

    Parameters
    ----------
    img : np.Array
        画像の配列

    Returns
    -------
    gray_img : np.Array
        グレースケールに変換された画像の配列
    """
    line_num = 1
    gray_img = img
    start = time.time()
    print("計測を始めます")

    # 縦の行のループ
    for height in gray_img:

        # 横の行のループ
        for width in height:
            # グレースケールにするする処理
            # グレーの値 = Redの値*0.3 + Greenの値*0.59 + Blueの値*0.11
            gray = int(width[0]*0.3) + int(width[1]*0.59) + int(width[2]*0.11)
            width[0] = gray # Red  
            width[1] = gray # Green
            width[2] = gray # Blue

        # 進捗バーを表示する関数
        common.progressBar(line_num, len(gray_img))
        line_num += 1
    print ("\nかかった時間 : " + str(time.time()-start) + "[秒]")
    return gray_img

if __name__ == '__main__':
    main()