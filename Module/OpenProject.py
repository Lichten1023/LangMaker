def OpenProject():
    print("プロジェクトを開きます。プロジェクトのディレクトリ(バージョンごとのフォルダが存在しているディレクトリ)を選択してください。")
    OpenPpath = input("> ")
    with open('data.json', 'r') as file:
    ProjectData = json.load(file)