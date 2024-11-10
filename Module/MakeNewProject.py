import os
import re

def MakeNewProject():
    print("プロジェクト名を入力してください")
    Pname = input("> ")
    print("プロジェクトフォルダへのパスを入力してください。プロジェクトのルートとなるフォルダが指定したフォルダの中に作られます。")
    Ppath = input(r"> ")
    print("初期のバージョンを入力してください。テキストと数字をサポートします。(ピリオドで区切った数字も使用できます。その場合はx.x.x.xの4つのセグメントまでが使用可能です。各桁の数字に桁数の制限はありません。)")
    print("(例: Alpha 使用可能, Alpha v1 使用可能, Alpha 0 使用可能(Alpha v0には変換されない) 0 使用可能(v0に変換) 1.2 使用可能(v1.2に変換), 1.2.3 使用可能(v1.2.3に変換), 1.2.3.4 使用可能(v1.2.3.4に変換), 1.2.3.4.5 使用可能(v1.2.3.4.5には変換されない)")
    Pversion = input("> ")
    MakeNewProjectFolder(Ppath, Pname, Pversion)

def MakeNewProjectFolder(Ppath, Pname, Pversion):

    if re.fullmatch(r'^\d+(\.\d+){0,3}$', Pversion):  # 整数または小数
        Pversion = 'v' + Pversion
    else:
        Pversion = Pversion

    try:
        MNPF_Project = os.path.join(Ppath, Pname)  # ルートディレクトリ生成
        os.mkdir(MNPF_Project)
    except FileExistsError:
        print("プロジェクト名が重複しているため新規プロジェクトの作成は不可能です。\n既存のプロジェクトの新規バージョンを製作したい場合は、プロジェクトを開く→新規バージョンで保存を選択してください。\n新規バージョンのフォルダが製作され、プロジェクトが保存されます。")
        print("処理をリセットします。\n")
        MakeNewProject()

    MNPF_root = os.path.join(MNPF_Project, Pversion)  # ルートディレクトリ生成
    os.mkdir(MNPF_root)
    MNPF_rootMAIN = os.path.join(MNPF_root, "main.py")   # main.py生成
    with open(MNPF_rootMAIN, 'w') as file:
        file.write(f'# {Pname}, {Pversion}')

    MNPF_rootREADME = os.path.join(MNPF_root, "README.md")   # README.md生成
    with open(MNPF_rootREADME, 'w') as file:
        file.write(f'# {Pname} {Pversion} | Readme')

    MNPF_rootJSON = os.path.join(MNPF_root, "project.json")   # project.json生成
    with open(MNPF_rootJSON, 'w') as file:
        file.write(f'''
{{
    "name": "{Pname}",
    "filename": "project.json",
    "version": "{Pversion}"
}}
                   ''')

    MNPF_source = os.path.join(MNPF_root, "src")     # srcフォルダ生成
    os.mkdir(MNPF_source)

    MNPF_sourceLexer = os.path.join(MNPF_source, "lexer")     # src/lexerフォルダ生成
    os.mkdir(MNPF_sourceLexer)
    MNPF_sourceParser = os.path.join(MNPF_source, "parser")     # src/parserフォルダ生成
    os.mkdir(MNPF_sourceParser)
    MNPF_sourceAST = os.path.join(MNPF_source, "ast")     # src/astフォルダ生成
    os.mkdir(MNPF_sourceAST)
    MNPF_sourceInterpreter = os.path.join(MNPF_source, "interpreter")     # src/interpreterフォルダ生成
    os.mkdir(MNPF_sourceInterpreter)
    MNPF_sourceCompiler = os.path.join(MNPF_source, "compiler")     # src/compilerフォルダ生成
    os.mkdir(MNPF_sourceCompiler)

    MNPF_sourceJSON = os.path.join(MNPF_source, "src.json")
    with open(MNPF_sourceJSON, 'w') as file:
        file.write(f'''
{{
    "name": "{Pname}",
    "filename": "src.json",
    "version": "{Pversion}"
}}
                   ''')


    MNPF_library = os.path.join(MNPF_root, "lib")   # libraryフォルダ生成
    os.mkdir(MNPF_library)
    MNPF_libraryJSON = os.path.join(MNPF_library, "lib.json")
    with open(MNPF_libraryJSON, 'w') as file:
        file.write(f'''
{{
    "name": "{Pname}",
    "filename": "lib.json",
    "version": "{Pversion}"
}}
                   ''')

    MNPF_object = os.path.join(MNPF_root, "obj")    # objフォルダ生成
    os.mkdir(MNPF_object)

    MNPF_docs = os.path.join(MNPF_root, "docs")    # docsフォルダ生成
    os.mkdir(MNPF_docs)

    MNPF_docsDOCS = os.path.join(MNPF_docs, "docs.md")   # README.md生成
    with open(MNPF_docsDOCS, 'w') as file:
        file.write(f'# {Pname} {Pversion} | Readme')

    MNPF_include = os.path.join(MNPF_root, "include")    # docsフォルダ生成
    os.mkdir(MNPF_include)

# MakeNewProject()