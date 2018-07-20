"""
共通の処理を行うモジュール
"""

def progressBar(start, end):
    """
    進捗バーを表示する関数

    Parameters
    ----------
    start : str
        進捗の最初の値
    end : str
        進捗の最後の値
    """
    print( "\r進捗率：[" + "#" * int(start/end*100) + 
           " " * (100 - int(start/end*100)) + "] " + str(start) + 
           "/" + str(end) + " 書き込み済", end="" )



def anyFileNameExetention(oldFileName: str, extention: str):
    """
    名前に任意の拡張子をつけて返す関数

    Parameters
    ----------
    oldFileName : str
        ファイルの名前
    extention : str
        拡張子の名前

    Returns
    -------
    newFileName : str
        oldNameの拡張子をextentionに変えた文字列
    """
    newFileName = ""
    tmp = oldName.split(".")
    for i in range( 0, len(tmp)-1 ):
        newFileName += tmp[i]
    # 最後の.以外を取り除いて新しい拡張子をつけて返す
    print("newFileName = " + newFileName + "." + extention)
    return newFileName + "." + extention



def anyFileNameGrayExetention(oldFileName: str):
    """
    拡張子の前に_grayをつける関数

    Parameters
    ----------
    oldFileName : str
        ファイルの名前

    Returns
    -------
    newFileName : str
        oldFileNameの拡張子の前に_grayを付けた文字列
    """
    newFileName = ""
    tmp = oldFileName.split(".")
    for i in range( 0, len(tmp)-1 ):
        newFileName += tmp[i]
    # 拡張子の前に_grayをつけて返す
    return newFileName + "_gray." + tmp[len(tmp)-1]