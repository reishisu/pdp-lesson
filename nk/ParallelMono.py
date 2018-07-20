"""
並列で画像をモノクロにする
"""

# スレッドで並列化を利用する為に必要なモジュール
from concurrent.futures import ThreadPoolExecutor

# その他各ライブラリをインポート
import matplotlib.pyplot as plt
import cv2
import common
import sys
import os


