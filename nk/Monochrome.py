"""
画像をモノクロにする
事前に
pip install opencv-pythonでOpenCV
pip install matplotlib
をしておく
"""

# 各種ライブラリをインポート
import matplotlib.pyplot as plt
import common
import cv2
import sys

# 画像を読み込み
fileName = sys.argv[1]
img = cv2.imread(fileName)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def main():
    changeToGray()
    plt.imshow(img)
    plt.show()


def changeToGray():
    """
    画像をモノクロに変更する関数
    """
    line_num = 1
    # 縦の行のループ
    for height in img:
        # 横の行のループ
        for width in height:
            # グレースケールにするする処理
            gray = int(width[0]*0.3) + int(width[1]*0.59) + int(width[2]*0.11)
            width[0] = gray # Redの値*0.3
            width[1] = gray # Greenの値*0.59
            width[2] = gray # Blueの値*0.11
        common.progressBar(line_num, len(img))
        line_num += 1

if __name__ == '__main__':
    main()