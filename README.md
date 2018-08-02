並列分散処理 - H班 -
====

私たちはOpenCV、NumPy、concurrent.futureasなどと言ったライブラリやモジュールを利用することで画像をグレースケールにする処理を高速かつ並列に行いました。

## 説明

OpenCV：画像の読み書き、解析などを行うのに必要なライブラリ  
NumPy:行列など数値計算を効率的に行うのに必要なライブラリ  
concurrent.futures:マルチスレッドやマルチプロセスと言った並列処理を行うのに必要なモジュール

## 推奨環境

Python3.2以上で実行すること

## ディレクトリの構成
主に作業や画像、ソースコードは「nk」のディレクトリにある
```
TOP  
┃  
┣ .idea .. IntelliJ IDEAでgitを利用する際に作成される  
┃　┣ misc.xml  
┃　┣ modules.xml  
┃　┗ vcs.xml  
┃  
┣ Ikki .. e165713's workspace  
┃　┗ test.py  
┃  
┣ Taken .. e165735's workspace  
┃　┗ Test.txt  
┃  
┣ nk .. e165765's workspace  
┃　┣ __pycache__ .. VSCodeを利用した際に出来たディレクトリ  
┃　┃　┗ common.cpython-36.pyc  
┃　┃  
┃　┣ images .. 処理で利用した画像を格納するディレクトリ  
┃　┃　┗ big_sample.jpg  
┃　┃　┗ lovelive.jpg  
┃　┃　┗ mid_sample.jpg  
┃　┃  
┃　┣ メモ書き .. 調べてソースコードを作成している最中に得た知見をまとめたディレクトリ  
┃　┃　┗ Monochrome.py .. グレースケール処理で気が付いた事など  
┃　┃　┗ OpenCV.py .. OpenCVを利用して気が付いた事など  
┃　┃　┗ Parallel.py .. 並列処理で気が付いた事など  
┃　┃  
┃　┣ ParallelMono.py	.. 画像を１行ずつプロセス渡す事で動的負荷分散を行って画像を表示する  
┃　┣ ParallelMono2.py	.. 画像を行数ごとに区切ってプロセス渡す事で静的負荷分散を行って画像を表示する  
┃　┣ common.py	.. 進捗バーなど共通処理をまとめた自作モジュール  
┃　┣ concurrent.futures.pdf .. 公式のサイトからページをDLしたもの  
┃　┣ speedtest.py .. ParallelMono.pyの画像処理部分の実行速度を計測して表示する  
┃　┣ speedtest2.py .. ParallelMono2.pyの画像処理部分の実行速度を計測して表示する  
┃　┗ グレースケール処理時間計測結果.xlsx .. 実行速度などをExcelファイルにまとめたもの  
┃  
┣ README.md  
┗ pdp-lesson.iml  
```

## 実行する前に

あらかじめ以下のコマンドを入力してインストールしておくこと
```zsh
pip install opencv-python
pip install matplotlib
pip install futures
```

## 使い方  

主にParallelMono.pyとParallelMono2.pyを利用する。  
使用する際にはコマンドライン引数として画像のパスを指定する必要がある。  
```
python ParallelMono.py hoge/hogehoge.jpg  
python ParallelMono2.py hoge/hogehoge.png  
```
  
処理速度を計測するだけならspeedtest.pyとspeedtest2.pyを利用する。  
使用する際にはコマンドライン引数として画像のパスとコア数を指定する必要がある。  
```
python speedtest.py hoge/hogehoge.jpg 1  
python speedtest2.py hoge/hogehoge.png 8  
```
