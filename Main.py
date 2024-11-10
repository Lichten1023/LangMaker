from Module.Settings import Setting
from Module.MakeNewProject import MakeNewProject
from Module.Boot import Boot

def main():
    Boot()
    while True:
        print("選択してください。")
        print("1: 新規プロジェクト | 2: プロジェクトを開く | 3:設定 | 4:終了")
        c = input(">> ")
        if c == '1':
            MakeNewProject()
#        elif c == '2':
#            OpenProject()
        elif c == '3':
            Setting.OpenSetting()
#        elif c == '4':
#            Shutdown()

main()