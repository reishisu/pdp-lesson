"""
並列処理のサンプル
-- ほとんどメモ書き
"""

import concurrent.futures
import random
import time

####  分かった事
# Future は オブジェクト で その中でいろんな関数を持ってる
# ThreadPoolExecutor または ProcessPoolExecutor が submit() した時に　インスタンス化される
# つまり実行がsubmit()なので、実行した瞬間に管理するFutureが作られる！！
# よって、実際に使うのは Future だが 並列で複数あるので 配列でまとめた Futures を使う！！
#
#### Future の リンク
# https://docs.python.jp/3/library/concurrent.futures.html#concurrent.futures.Future
#
#### また、with を使うことで最後にshutdown()を呼ばなくても良い！
#
#### 終わった順番からFutureを返す
# concurrent.futures.as_completed( Futures[] )
#
#### 並列プログラムの実行方法
# executor.submit(関数名, 引数, ・・・)
#
#### submitが終わったら自動的に関数名を実行する
# Future.add_done_callback(関数名)
#
##### １行でかくリスト処理
# data配列の中身を2倍にする
# newData = [d * 2 for d in data]
#
# ifの条件をつけたリスト処理
# newData = [d * 2 for d in data if d % 2 == 0]
#
#### 確認できたこと
# max_worker はちゃんと最大本数で動いていた
# fsは実行結果数だけ格納されていた
# 個人的には終わりを待って実行できる方が確実に並列かできると感じた 
# 
# concurrent.futures.wait( fs )について
#     1. スレッドの最大本数分だけ待ってくれる
#     2. もしスレッドの最大本数が5本なら5本が確実に終わるまで次のスレッドは実行されない
#     3. しかし、実行中のスレッドの中での実行は終わったもの順で実行される
#     4. ほぼ同時で、高速に終わるなら次のFutureと混じることもあった
#
#########################################################################
#########################################################################


sample_num = 0
range_num = 20


def executer_sum( number ):
    try:
        time.sleep(range_num-number)
        print(str(number) + " ", end="", flush=True)
        return number
    except:
        print("Error")


# 並列処理
start = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executer:
    fs = [ executer.submit(executer_sum, i) for i in range(range_num) ]
    #### ↑の略さない書き方
    # fs = []   # スレッドを格納する配列
    # for i in range(range_num):
    #     fs.append( executer.submit(executer_sum, i) )

    #### みんなの終わり待たない
    # for future in concurrent.futures.as_completed(fs):
    #     sample_num += future.result()
    # print("\n実行が終了しました")
    # print("かかった時間:" + str(time.time() - start))
    # print("")

    #### みんなの終わり待つ
    concurrent.futures.wait(fs)     # この行で終わり待ち(感覚的にMax_workers単位の待ち)
    for future in fs:
        sample_num += future.result()
    print("\n実行が終了しました")
    print("かかった時間:" + str(time.time() - start))
    print("")

#### 逐次
# sample_num = 0
# start = time.time()
# for i in range(range_num):
#     sample_num += executer_sum(i)
# print("\n実行が終了しました")
# print("かかった時間:" + str(time.time() - start))

