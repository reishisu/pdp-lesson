'''
OpenCVの使ってみるファイル
予めpip install opencv-pythonでOpenCVをインストールしておく

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
import os

# 画像のフォルダパス
imagePath = "./images/"

# テキストファイルの出力先のパス
textExportPath = "./rgbtext/"

# コンソールをクリアする
os.system('clear')

# 画像を読み込み(無ければsampel.jpg)
fileName = input()
img = cv2.imread(imagePath + fileName)
if img is None:
    print("そのファイル名の画像は見つけられませんでした...")
    fileName = "sample.jpg"
    img = cv2.imread(imagePath + fileName)

'''
メイン関数
'''
def main():
    inFileAllPixel( anyFileNameExetention( textExportPath, fileName, "txt" ) )
    
'''
テキストファイルにRGBの値を全部保存
'''
def inFileAllPixel(name):
    # ファイルを開く(無ければ新規作成)
    f = open(name, 'w')
    # 縦の行のループ
    for height, line_num in zip( img, range( 1, len( img ) ) ):
        print( str( line_num ) + "行目を書き込み中" )
        # 行数をファイルに書き込み
        f.write( str( line_num ).ljust(3," ") + "| " )
        # 横の行のループ
        for width in height:
            # 各ピクセルのRGB値を書き込み
            # f.write( str( width ) + " " )
            f.write( str( width ))
        # 行の終わりに改行させる
        f.write("\n")

'''
画像のRGB値を全部表示
'''
def showAllPixel():
    print("全ピクセルのRGP値")
    line_num = 1
    # 縦の行のループ
    for height in img:
        print( str( line_num ).ljust(3," ") + "| ", end="" )
        # 横の行のループ
        for width in height:
            print( str( width ), end="" )
        count += 1
        print("")


'''
画像の真ん中の列のRGB値を全部表示
'''
def showAllCenterPixel():
    print("画像真ん中の列のRGB値")
    for px in img:
        # 真ん中の列のピクセルのRGBを上から下に表示
        print( px[ int( len(img)/2 ) ] )

'''
最後の.以外-に変換する関数
'''
def changeDotToBar( String: str ):
    # 分割
    sliceString = String.split(".")
    newString = ""

    # ドットの数が１つの時
    if len( sliceString ) == 2:
        print("正しいフォーマットです！")
        print("入力文字列： " + String)
        print("出力文字列： " + String)
        return String

    # 変換処理
    print(len( sliceString ))
    print(sliceString)
    for s, i in zip( sliceString, range( 0, len( sliceString ) ) ):
        if i == len( sliceString )-1:
            newString += s
            break
        newString += s + "-"
        print(newString)
    print("入力文字列： " + String)
    print("出力文字列： " + newString)
    return newString


'''
任意でパスも指定できる
名前に任意の拡張子をつけて返す関数
'''
def anyFileNameExetention(path: str, oldName: str, extention: str):
    # 最後の.以外を取り除いて新しい拡張子をつけて返す
    return path + changeDotToBar(oldName).split(".")[0] + "." + extention


'''
実行される処理
'''
if __name__ == '__main__':
    main()
