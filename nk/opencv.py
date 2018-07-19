'''
OpenCVの使ってみるファイル
予め
　pip install opencv-pythonでOpenCV
　pip install tqdm
をしておく


OpenCVで読み込む画像の構造
# 画像を1つに対して１つの配列
[ 
    # 高さのピクセル
    [[R, G, B], [R, G, B], [R, G, B], ~ [R, G, B], [R, G, B]],   # 横1列のピクセル
    [[R, G, B], [R, G, B], [R, G, B], ~ [R, G, B], [R, G, B]],   # 横1列のピクセル
        :
        :
        :
    [[R, G, B], [R, G, B], [R, G, B], ~ [R, G, B], [R, G, B]]    # 横1列のピクセル
]
'''
# OpenCVをインポート
import cv2

# 各種ライブラリをインポート
import os, sys
from tqdm import tqdm

# コンソールをクリアする
os.system('clear')

# 画像を読み込み
fileName = sys.argv[1]
img = cv2.imread(fileName)

'''
メイン関数
'''
def main():
    WriteInFileAllPixel( anyFileNameExetention( fileName, "txt" ) )


'''
テキストファイルにRGBの値を全部保存
'''
def WriteInFileAllPixel(name):
    line_num = 1
    # ファイルを開く(無ければ新規作成)
    f = open(name, 'w')
    # 縦の行のループ
    for height in img:
        # 行数をファイルに書き込み
        f.write( str( line_num ).rjust(3) + "| " )
        # 横の行のループ
        for width in height:
            # 各ピクセルのRGB値を書き込み
            f.write( str( width ))
        print( "\r進捗率　：　[" + "#" * int(line_num/len(img)*100) + " " * (100 - int(line_num/len(img)*100)) + "] " + str(line_num) + "/" + str(len(img)) + "書き込み済", end="" )
        line_num += 1
    print("")


'''
画像のRGB値を全部表示
'''
def showAllPixel():
    print("全ピクセルのRGP値")
    line_num = 1
    # 縦の行のループ
    for height in img:
        print( str( line_num ).rjust(3) + "| ", end="" )
        # 横の行のループ
        for width in height:
            print( str( width ), end="" )
        line_num += 1
        print("")


'''
画像の真ん中の列のRGB値を全部表示
'''
def showAllCenterPixel():
    line_num = 1
    print("画像真ん中の列のRGB値")
    for px in img:
        # 真ん中の列のピクセルのRGBを上から下に表示
        print( str( line_num ).rjust(3) + "| " + str( px[ int( len(img)/2 ) ] ) )
        line_num += 1

'''
名前に任意の拡張子をつけて返す関数
'''
def anyFileNameExetention(oldName: str, extention: str):
    newFileName = ""
    tmp = oldName.split(".")
    for i in range( 0, len(tmp)-1 ):
        newFileName += tmp[i]
    # 最後の.以外を取り除いて新しい拡張子をつけて返す
    print("newFileName = " + newFileName + "." + extention)
    return newFileName + "." + extention


'''
実行される処理
'''
if __name__ == '__main__':
    main()
