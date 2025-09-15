# mcp-trial-02

AWSアップデート情報を取得するMCPサーバープロジェクト

## 開発について

このプロジェクトは、2025年09月のSoftware Design特集記事「AI開発が加速 MCPでどう変わる？」をtrialしたものです。

## 概要

このプロジェクトはAWSのアップデート情報を探索・取得するためのMCP（Model Context Protocol）サーバーです。

## 必要な環境

- Python 3.7以上
- pip

## セットアップ

1. 仮想環境の作成と有効化:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# または
venv\Scripts\activate     # Windows
```

2. 依存関係のインストール:
```bash
pip install -r requirements.txt
```

## 使用方法

```bash
python src/aws_updates.py
```

## mcp登録

```zsh
claude mcp add aws-updates {phthonのフルパス} {src/aws_updates.pyへのフルパス}
```

## プロジェクト構成

```
mcp-trial-02/
├── README.md
├── requirements.txt
├── src/
│   └── aws_updates.py
└── venv/
```

## 依存関係

- fastmcp: MCP（Model Context Protocol）サーバーフレームワーク