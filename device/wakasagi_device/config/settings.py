from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass
class GpioSettings:
    vibration_sensor_pin: int
    photo_switch_pin: int
    motor_driver_in1_pin: int
    motor_driver_pwm_pin: int


@dataclass
class SensorSettings:
    vibration_threshold: float
    debounce_samples: int
    debounce_window_seconds: float


@dataclass
class ReelSettings:
    timeout_seconds: float
    motor_speed: float


@dataclass
class BedrockSettings:
    region: str
    model_id: str
    prompt_file: str


@dataclass
class OutputSettings:
    mode: str


@dataclass
class Settings:
    gpio: GpioSettings
    sensor: SensorSettings
    reel: ReelSettings
    bedrock: BedrockSettings
    output: OutputSettings

    @classmethod
    def from_yaml(cls, path: Path) -> "Settings":
        with open(path, "r") as f:
            raw = yaml.safe_load(f)
        return cls(
            gpio=GpioSettings(**raw["gpio"]),
            sensor=SensorSettings(**raw["sensor"]),
            reel=ReelSettings(**raw["reel"]),
            bedrock=BedrockSettings(**raw["bedrock"]),
            output=OutputSettings(**raw["output"]),
        )
