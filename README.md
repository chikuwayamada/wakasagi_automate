# 全自動ワカサギ釣りマシーン (wakasagi_automate)

IoTとAIの学習を目的とした個人プロジェクト。ワカサギ釣り用の竿に振動センサーを取り付け、
アタリ（竿の振動）を検知したら自動でリールを巻き上げ、巻き上げ完了時に釣り人に扮した
LLMキャラクターが応答するマシーンを作る。

## 構成概要

```
wakasagi_automate/
├── docs/       設計ドキュメント（アーキテクチャ、ハードウェア）
├── device/     Raspberry Pi上で動くデバイスドライバ層（Python）
├── cloud/      LLM（AWS Bedrock）連携層
└── edge/       将来のGreengrass/ローカルLLM化の構想置き場（未実装）
```

詳細は以下を参照:

- [システム概要](docs/architecture/system_overview.md)
- [状態遷移設計](docs/architecture/state_machine.md)
- [部品表 (BOM)](docs/hardware/bom.md)
- [GPIOピン配置](docs/hardware/gpio_pinout.yaml)
- [結線表](docs/hardware/wiring.md)

## ハードウェア構成（概要）

- 竿: 市販のワカサギ釣り用竿
- センサー: 振動センサー（ピエゾ/SW-420等）でアタリを検知
- リール: ミニ四駆モーターを流用した自作巻き上げ機構
- 巻き上げ完了検知: フォトスイッチで満巻き位置を1回検知した時点で完了と判定
- 制御部: Raspberry Pi 4（モーター駆動系は電池＋モータードライバで別電源系統）

## ソフトウェア構成（概要）

- `device/`: センサー監視・モーター制御・状態機械（`transitions`ライブラリ）をPythonで実装
- `cloud/`: AWS Bedrockをプロンプトベースで直接呼び出し、釣り人キャラクターの応答を生成
- 出力はまずテキスト（ログ）、将来的にTTSで音声発話に拡張予定
- 将来的にAWS IoT Greengrassを使ったエッジ化・ローカルLLM化を検討（`edge/`参照）

## セットアップ

### Raspberry Pi側（device/）

```bash
cd device
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp wakasagi_device/config/config.example.yaml wakasagi_device/config/config.yaml
# config.yaml をGPIOピン番号や環境に合わせて編集
```

テスト実行（状態機械ロジックのみ、実機GPIO不要）:

```bash
cd device
pytest
```

### AWS連携側（cloud/）

```bash
cd cloud
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
aws configure  # IAMプロファイルを設定し、Bedrock呼び出し用の認証情報をPiに登録
```

AWS認証情報はコード上に埋め込まず、`aws configure`で設定したプロファイルを
boto3のデフォルト認証チェーン経由で利用する。

## 開発フェーズ

1. **現在**: リポジトリのひな形・設計ドキュメント・状態機械の骨格を用意
2. センサー/モーターの実配線と実装、Bedrock呼び出しの実装
3. TTSによる音声発話への拡張
4. AWS IoT Greengrass + ローカルLLMによるエッジ化（将来構想）
