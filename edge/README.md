# edge（将来構想メモ）

現状は未実装。`cloud/bedrock` でAWS Bedrockを直接呼び出す構成が安定してきたら、
以下の方向でエッジ化を検討する。

## 構想

- AWS IoT Greengrassを導入し、Raspberry Pi上にGreengrassコアデバイスを構成する
- Bedrock API呼び出しを、Greengrass上で動く小型ローカルLLM（例: 量子化されたオープンモデル）に置き換え、
  ネットワーク非依存でキャラクター応答を生成できるようにする
- `cloud/bedrock/client.py` と同じインターフェース（`generate_response(...)`）を持つ
  ローカル版クライアントを用意し、`device/`側からは呼び出し先を設定で切り替えられるようにする

## 未確定事項

- ローカルLLMのモデル選定・量子化方式
- Pi 4のリソース（CPU/メモリ）でどの程度の応答速度・品質が出せるか
- Greengrassコンポーネントとしてのパッケージング方法
