from transitions import Machine

STATES = [
    "idle",
    "detecting",
    "reeling",
    "reel_complete",
    "generating_response",
    "output",
    "error",
]

# (trigger, source, dest) の組。詳細な意味は docs/architecture/state_machine.md を参照。
TRANSITIONS = [
    {"trigger": "vibration_detected", "source": "idle", "dest": "detecting"},
    {"trigger": "debounce_failed", "source": "detecting", "dest": "idle"},
    {"trigger": "vibration_confirmed", "source": "detecting", "dest": "reeling"},
    {"trigger": "reel_position_detected", "source": "reeling", "dest": "reel_complete"},
    {"trigger": "reel_timeout", "source": "reeling", "dest": "error"},
    {"trigger": "start_response_generation", "source": "reel_complete", "dest": "generating_response"},
    {"trigger": "response_ready", "source": "generating_response", "dest": "output"},
    {"trigger": "output_complete", "source": "output", "dest": "idle"},
    {"trigger": "reset", "source": "error", "dest": "idle"},
]


class ReelStateMachine:
    """竿の振動検知〜巻き上げ〜LLM応答出力までを管理する状態機械。

    センサー/モーター/Bedrockとの実際の結線は device/main.py 側で
    on_enter_<state> フックとして後付けする想定。ここでは遷移ルールのみを定義する。
    """

    def __init__(self):
        self.machine = Machine(
            model=self,
            states=STATES,
            transitions=TRANSITIONS,
            initial="idle",
        )
