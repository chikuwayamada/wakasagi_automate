from gpiozero import DigitalOutputDevice, PWMOutputDevice


class ReelMotor:
    """TB6612FNG等のモータードライバ経由でリール巻き上げモーターを制御する。

    初期スコープでは巻き上げ（正転）のみを扱い、逆転（仕掛けリリース）は
    docs/architecture/state_machine.md の方針により対象外とする。
    """

    def __init__(self, in1_pin: int, pwm_pin: int, speed: float):
        self._direction = DigitalOutputDevice(in1_pin)
        self._pwm = PWMOutputDevice(pwm_pin)
        self._speed = speed

    def start(self) -> None:
        self._direction.on()
        self._pwm.value = self._speed

    def stop(self) -> None:
        self._pwm.value = 0
        self._direction.off()

    def close(self) -> None:
        self._pwm.close()
        self._direction.close()
