# cloud

AWS Bedrockをプロンプトベースで直接呼び出し、釣り人キャラクターの応答を生成する層。

現状は `device/` と同じRaspberry Pi上から呼び出す最小構成（IoT Core/Lambda等は使わない）。
`device/` と分離しているのは、将来Lambda化する際にこのフォルダごと移植しやすくするため。

## セットアップ

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
aws configure  # IAMプロファイルを設定（アクセスキーをコードや.envに書かない）
```

## モジュール構成

- `bedrock/client.py` — `boto3.client("bedrock-runtime")` の薄いラッパー
- `bedrock/prompts/angler_character.md` — 釣り人キャラクターの人格プロンプト

## 将来構想

AWS IoT Greengrass + ローカルLLMによるエッジ化を検討している。詳細は [../edge/README.md](../edge/README.md) 参照。
