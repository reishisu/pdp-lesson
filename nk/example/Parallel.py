"""
並列処理のサンプル
└─ ほとんどメモ書き

事前に
  pip install futures
をしておく
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
#### スレッドが実行終了してFutureが準備出来た順番にFutureを返す
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
# ・ max_worker はちゃんと最大本数で動いていた
# ・ fsは実行結果数だけ格納されていた
# ・ 個人的には終わりを待って実行できる方が確実に並列かできると感じた 
# ・ 戻り値についてはFuture.result()で取得できた
# ・ スレッドは演算処理に向いていないので使うべきでは無い
# 
# concurrent.futures.wait( fs )について
#     1. 全部のFutureが帰ってくるまで待機する
#     2. 実行結果を見るのが一番わかりやすかった
#     3. 画像を処理の際にはwait()は使わずにas_completed()を使ったほうが良さそう
#
#########################################################################
#########################################################################


sample_num = 0
range_num = 20


def executer_sum( number ):
    try:
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


    #### 全Futureの終わり待たない
    for future in concurrent.futures.as_completed(fs):
        print("f", end=" ", flush=True)
        sample_num += future.result()
    print("\n実行が終了しました")
    print("かかった時間:" + str(time.time() - start))
    print("")
    ########################
    ## [ 実行結果 ] 
    ## 理想 : 0 f 1 f 2 f 3 f 4 f 5 f 6 f 7 f 8 f 9 f 10 f 11 f 12 f 13 f 14 f 15 f 16 f 17 f 18 f 19 f
    ## 実際 : 1 0 3 5 7 2 4 8 6 9 f f f f f f f f f f 10 f 11 f 13 12 14 f 16 f 17 18 19 f 15 f f f f f


    #### 全Futureの終わり待つ
    # concurrent.futures.wait(fs)     # この行で終わり待ち(全Futureの実行待ち)
    # for future in fs:
    #     print("f", end=" ", flush=True)
    #     sample_num += future.result()
    # print("\n実行が終了しました")
    # print("かかった時間:" + str(time.time() - start))
    # print("")
    ########################
    ## [ 実行結果 ] 
    ## 理想 : 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 f f f f f f f f f f f f f f f f f f f f
    ## 実際 : 2 4 0 8 11 13 1 5 17 18 12 7 15 6 16 9 10 19 3 14 f f f f f f f f f f f f f f f f f f f f


#### 逐次
sample_num = 0
start = time.time()
for i in range(range_num):
    sample_num += executer_sum(i)
    print("f", end=" ", flush=True)
print("\n実行が終了しました")
print("かかった時間:" + str(time.time() - start))
########################
## [ 実行結果 ] 
## 理想 : f 0 f 1 f 2 f 3 f 4 f 5 f 6 f 7 f 8 f 9 f 10 f 11 f 12 f 13 f 14 f 15 f 16 f 17 f 18 f 19
## 実際 : f 0 f 1 f 2 f 3 f 4 f 5 f 6 f 7 f 8 f 9 f 10 f 11 f 12 f 13 f 14 f 15 f 16 f 17 f 18 f 19
