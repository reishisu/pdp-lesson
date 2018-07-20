"""
共通の処理を行うモジュール
"""

def progressBar(start, end):
    """
    進捗バーを表示する関数
        @param start 進捗の最初の値
        @param end   進捗の最後の値
    """
    print( "\r進捗率：[" + "#" * int(start/end*100) + " " * (100 - int(start/end*100)) + "] " + str(start) + "/" + str(end) + " 書き込み済", end="" )