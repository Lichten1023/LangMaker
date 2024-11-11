# How to use LangMaker? | LangMaker公式ドキュメント

## はじめに
LangMakerはREADME.mdにも記載がありますが、プログラミング言語の作成を支援するソフトウェアです。最終的な目標はもちろん高級言語を簡単に自作することができるシステムです。<br>
また、このHowToUse.mdはmainディレクトリにありますが、部分ごとのドキュメントや詳細な仕様はdocsフォルダに配置されていることには留意してください。

**困ったときはdocsフォルダ**、これだけは覚えておいてください。

## 基本的な操作方法
まずはmain.pyを実行してください(LangMaker.exeが同じ階層に存在している場合はそちらを起動しても大丈夫です)。その後は基本的にmain.pyを実行したテキストエディタまたはLangMaker.exeの起動時に立ち上がるCLIで続行することとなります。<br>
また、基本的にはドキュメントを読まなくても対話型で使用可能な設計です。不明なことがある場合はこのドキュメントに戻ってきてください。<br>

- [新規プロジェクトを作成する](#新規プロジェクトを作成する)
- [プロジェクトを開く](#プロジェクトを開く)

- [はじめての言語を作る](#はじめての言語を作る)
  + [四則演算ができる言語の作成](#四則演算ができる言語の作成)
  + [brainfuck互換言語の作成](#brainfuck互換言語の作成)

### 新規プロジェクトを作成する
ここでは以下の入力を求められます。<br>

* プロジェクト名<br>
* プロジェクトフォルダのパス<br>
* 初期バージョン<br>

ここで、すでに作成したプロジェクトの別バージョンを製作したい場合は[プロジェクトを開く](#プロジェクトを開く)でプロジェクトを開き、変更点を設定して保存してください(プロジェクト保存時に新規バージョンで保存する選択肢を選択できます)。

### プロジェクトを開く

### はじめての言語を作る
さて新規プロジェクトを作成し、それを開いた今やるべきことと言えば1つ。それは勿論、自分の理想的なプログラミング言語の作成に向けてプロジェクトを前に進めること。<br>
…といっても、まだソフトウェアの仕様的にも理想的なプログラミング言語を作る段階には到達していないので、まずは四則演算ができる言語(言語？)の作成と、brainfuck互換言語の作成をやってみましょう。

#### 四則演算ができる言語の作成
さて作業を始めていきましょう。LangMakerで言語を作るということは、ドキュメントを見ながらjsonを書くということです。ドキュメントはこのmdファイルがあるディレクトリにdocsフォルダがあり、そこに各種ドキュメントが置かれています。(同じファイル名を持つ.mdと.pdfと.txtの内容は共通です。好きな形式のファイルを開いてください。ここではmdファイルを開く仮定で進行します。現時点では日本語版のみを配置しています。)<br>
ここで開くドキュメントはFunctions/BasicCalculations.mdです。この中に四則演算の関数を定義するために必要な情報が記載されています。

まずはこのLangMakerでプログラミング言語を作成する手順について解説していきます。

#### brainfuck互換言語の作成
先の「[四則演算ができる言語の作成](#四則演算ができる言語の作成)」を終えた前提で話を進めます。先ほど「**LangMakerで言語を作るということは、ドキュメントを見ながらjsonを書くということ**」とお伝えしましたが、こちらでもその通りに進めていきます。さて今回開くドキュメントはOther/brainfuck.mdです。