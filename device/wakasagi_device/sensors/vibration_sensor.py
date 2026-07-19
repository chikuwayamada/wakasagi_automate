from collections.abc import Callable

from gpiozero import DigitalInputDevice


class VibrationSensor:
    """SW-420等のデジタル振動センサーをラップする。

    デバウンス判定（ノイズによる誤検知の除去）は state_machine 側で行う。
    ここでは生のGPIO状態変化をコールバックに伝えるだけの薄いラッパーとする。
    """

    def __init__(self, pin: int, on_vibration: Callable[[], None]):
        self._device = DigitalInputDevice(pin)
        self._device.when_activated = on_vibration

    def close(self) -> None:
        self._device.close()
