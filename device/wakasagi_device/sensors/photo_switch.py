from collections.abc import Callable

from gpiozero import DigitalInputDevice


class PhotoSwitch:
    """フォトインタラプタで満巻き位置の遮光を検知するラッパー。

    リールが満巻き位置に達し遮光板を検知した瞬間に1回だけ on_detected を呼ぶ
    （回転数カウント方式ではなく位置検知方式。docs/architecture/state_machine.md 参照）。
    """

    def __init__(self, pin: int, on_detected: Callable[[], None]):
        self._device = DigitalInputDevice(pin)
        self._device.when_activated = on_detected

    def close(self) -> None:
        self._device.close()
