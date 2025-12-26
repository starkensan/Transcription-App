# Whisper 音声文字起こしGUI（Python / Tkinter）

OpenAI Whisper を使って、音声ファイル（mp3 / wav / m4a / mp4）を **GUIで簡単に文字起こし**できるPythonアプリです。  
ファイル選択から文字起こし、結果のコピーまでを直感的に操作できます。

---

## 特徴

- TkinterベースのシンプルなGUI
- 対応音声形式  
  - `.mp3`
  - `.wav`
  - `.m4a`
  - `.mp4`
- 文字起こし結果を画面に表示
- 結果をクリップボードへコピー可能
- 文字起こし処理は別スレッドで実行（UIが固まりにくい）

---

## 動作環境

- Python 3.9 以上（推奨）
- OS  
  - Windows  
  - macOS  
  - Linux  

---

## セットアップ

### 1. Pythonパッケージのインストール

```bash
pip install -U openai-whisper
````

※ `tkinter` は多くの環境で標準搭載されています。

---

### 2. FFmpeg のインストール（必須）

Whisper は音声処理に **FFmpeg** を使用します。
未インストールの場合、音声ファイル読み込み時にエラーが発生します。

#### Windows

```bash
winget install Gyan.FFmpeg
```

#### macOS

```bash
brew install ffmpeg
```

#### Ubuntu / Debian

```bash
sudo apt-get install ffmpeg
```

---

## 使い方

```bash
python whisper_gui.py
```

1. アプリを起動
2. 「ファイルを選択して文字起こし」をクリック
3. 音声ファイルを選択
4. 文字起こし結果が画面に表示されます
5. 必要に応じて「コピーする」でクリップボードへコピー

---

## 使用モデルについて

デフォルトでは `base` モデルを使用しています。

モデル変更はコード内の以下の部分を編集してください。

```python
whisper_init("base")
```

### モデル一覧（参考）

| モデル            | 特徴                |
| -------------- | ----------------- |
| tiny           | 最速・精度低め           |
| base           | 速度と精度のバランス（デフォルト） |
| small          | 精度高め              |
| medium / large | 高精度（処理が重い）        |

---

## ディレクトリ構成

```
.
├── whisper_gui.py
└── README.md
```

---

## よくあるトラブル

### 音声ファイルが読み込めない

* FFmpeg がインストールされているか確認してください
* FFmpeg の PATH が通っているか確認してください

### 処理が遅い

* モデルを `tiny` や `base` に変更してください
* 長時間の音声は分割すると安定します

---

## 今後の改善案（アイデア）

* GUIでモデルサイズを選択
* 進捗バーの追加
* 出力を `.txt` / `.srt` ファイルとして保存
* 言語指定（日本語固定など）


---

## 謝辞

* OpenAI Whisper
* FFmpeg
