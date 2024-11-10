from SoftwareName import SoftwareInfo

class Setting():
    def OpenSetting():
        while True:  # 無限ループで選択を繰り返す
            print("選択してください。")
            print("1: ドキュメントを開く | 9: ソフトウェア情報を表示 | 0: 終了")
            q = input("> ")
#            if q == '1':
#                OpenDocs()
            if q == '9':
                print(SoftwareInfo())
            elif q == '0':
                print("終了します。")
                break  # ループを終了
            else:
                print("無効な選択です。もう一度お試しください。")

Setting.OpenSetting()