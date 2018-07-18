'''
画像の白黒に変換する
予めpip install opencv-pythonでOpenCVをインストールしておく
'''
# OpenCVをインポート
import cv2

# 画像を読み込み
img = cv2.imread('sample.jpg')

'''
imgの構造
# 画像を1つに対して１つの配列
[
    # 高さのピクセル
    [[R, G, B], [R, G, B], [R, G, B], ~ [R, G, B], [R, G, B]],   # 横1列のピクセル
    [[R, G, B], [R, G, B], [R, G, B], ~ [R, G, B], [R, G, B]],   # 横1列のピクセル
        :
        :
        :
    [[R, G, B], [R, G, B], [R, G, B], ~ [R, G, B], [R, G, B]],   # 横1列のピクセル
]
'''
print("画像の大きさ： " + str( len( img ) ) + "×" + str( len( img[0] ) ) + "\n" )
print("画像の中身")
for px in img:
    # 真ん中の列のピクセルのRGBを上から下に表示
    print( px[ int( len(img)/2 ) ] )

def showAllPixel():
    for width in 