# CHOPPEEEER-var2.0 
**体調管理 Webアプリケーション**  

---

## 概要  
CHOPPEEEERは、社員の体調管理をサポートするWebアプリケーションです。  
社員は自分の体温を記録・グラフ表示でき、管理者は社員情報や体調データを簡単に管理できます。

---

## 主な機能  
- **社員情報管理**: 社員番号、氏名、部署、電話番号などの登録・編集。  
- **体調記録と可視化**: 社員の体温を記録し、時系列でグラフ化。  
- **アクセス権限の区別**: 一般社員と管理者に異なる権限を付与。  
- **不調の視覚化**: 不調がある社員を背景色で強調表示。  
- **お知らせ機能**: 管理者が全社員向けのお知らせメッセージを作成・編集・削除可能。

---

## 基本操作  
- **社員登録**: 管理者が新規社員情報を登録。  
- **体調記録**: 社員は体温を登録し、過去データをグラフで確認可能。  
- **検索機能**: 社員番号または名前で情報を検索可能。  
- **社員情報の閲覧・管理**: 管理者が全社員の体調データを一括管理。  

---

## インストール方法  

### 必要なもの  
- **Python 3.10.0**  
- `requirements.txt` に記載されたライブラリ。  

#### 手順  
1. リポジトリをクローンします：  
   ```bash
   git clone https://github.com/koshiba-k/CHOPPEEEER-var2.0
   cd CHOPPEEEER-var2.0
   
2. 仮想環境を作成し、依存関係をインストールします：  
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   pip install -r requirements.txt
3. アプリケーションを起動します：
   ```bash
   python app.py


## テストデータの使用方法

**注意**: データベースを初期化すると既存のテストデータが削除されます。また、既存のテストデータが古い場合、データベースの初期化の指示に従って新しくテストデータを作成することをお勧めします。

### データベースの初期化
**注意**:instanceフォルダーがないことを課kにしてください。またある場合はinstanceフォルダーごと削除してください。

1. **データベースマイグレーション**:  
   以下のコマンドを実行してデータベースを再作成します：

   ```bash
   flask db init      # 初回のみ
   flask db migrate   # マイグレーションスクリプトの生成
   flask db upgrade   # マイグレーションを適用

2. **テストデータの生成:
    テストデータを挿入するスクリプトを実行します：
   ```bash
   python test_data.py

## テストデータの詳細  
- **テストデータファイル**: `employee_data.txt`
- **社員番号**: すべての社員アカウントはデフォルトで `"EMP{社員番号}"`。
- **パスワード**: すべての社員アカウントはデフォルトで `"password123"`。

## ライセンス  
このプロジェクトは、**GNU General Public License v3.0** のもとで公開されています。  