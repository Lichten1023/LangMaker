# Basic Calculations | LangMaker Document

## はじめに
Basic Calculation = 基礎演算<br>
基本的な四則演算の命令トークンセット。

## 使用方法
language.jsonのもっとも初めのオブジェクトの「Library」キーの配列に「"bsca"」を追加してください。自動的に対応する命令を定義するファイルが読み込まれて言語に組み込まれます。

## 使用可能な命令トークン一覧

### + : 2つの値を加算する
* オブジェクト名 : lm.bsca.add

### - : 前の値から後ろの値を減算する
* オブジェクト名 : lm.bsca.sub

### * : 2つの値を乗算する
* オブジェクト名 : lm.bsca.mul

### / : 前の値を後ろの値で除算する
* オブジェクト名 : lm.bsca.div
