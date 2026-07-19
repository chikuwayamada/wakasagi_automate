"""エントリポイント（骨格）。

センサー/モーターの実結線とBedrock呼び出しの実装は次フェーズで行う。
現状は状態機械を初期化して待機状態にするところまで。
"""

from pathlib import Path

from wakasagi_device.config.settings import Settings
from wakasagi_device.state_machine.machine import ReelStateMachine

CONFIG_PATH = Path(__file__).parent / "config" / "config.yaml"


def main() -> None:
    settings = Settings.from_yaml(CONFIG_PATH)
    state_machine = ReelStateMachine()
    print(f"起動しました。現在の状態: {state_machine.state}")
    print(f"振動センサーピン: {settings.gpio.vibration_sensor_pin}")
    # TODO: センサー/モーターのイベントを state_machine のトリガーに接続する


if __name__ == "__main__":
    main()
