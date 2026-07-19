# device

Raspberry Pi上で動くデバイスドライバ層。振動センサー・フォトスイッチの監視、
モーター（リール）の制御、状態機械の実行を行う。

## セットアップ

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp wakasagi_device/config/config.example.yaml wakasagi_device/config/config.yaml
```

`config.yaml` はGPIOピン番号・タイムアウト秒数・Bedrock関連の設定値を持つ。
`.gitignore`で除外されているため、実機ごとに個別に用意する。

## 実行

```bash
python -m wakasagi_device.main
```

## テスト

実機（GPIO）に依存しない状態機械ロジックのみを対象にしている。

```bash
pytest
```

## モジュール構成

- `sensors/` — 振動センサー・フォトスイッチの読み取り
- `actuators/` — モーター（リール）制御
- `state_machine/` — `transitions`ライブラリによる状態遷移ロジック（[設計はこちら](../docs/architecture/state_machine.md)）
- `output/` — キャラクター応答の出力（テキスト/将来TTS）
- `config/` — 設定の読み込み
