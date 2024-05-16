# -*- coding: utf-8 -*-
from src.audio_input import AudioInput
from src.spectrogram import Spectrogram
from src.gui import MainWindow

# PyAudioストリーム入力取得クラス
input = AudioInput(chunk=1024) #, input_device_keyword="Real")
# スペクトログラム用クラス
# spectrogram = Spectrogram( input.RATE, (input.CHANNELS, input.CHUNK) )
# GUI用クラス
Main = MainWindow()

# 別スレッドで入力取得開始
import threading
thread = threading.Thread(target=input.run, args=(Main.indicater,))
thread.daemon=True
thread.start()

# スペクトログラム描画開始
Main.run()