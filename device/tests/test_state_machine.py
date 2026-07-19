import pytest

from wakasagi_device.state_machine.machine import ReelStateMachine


def test_initial_state_is_idle():
    sm = ReelStateMachine()
    assert sm.state == "idle"


def test_full_cycle_returns_to_idle():
    sm = ReelStateMachine()
    sm.vibration_detected()
    assert sm.state == "detecting"

    sm.vibration_confirmed()
    assert sm.state == "reeling"

    sm.reel_position_detected()
    assert sm.state == "reel_complete"

    sm.start_response_generation()
    assert sm.state == "generating_response"

    sm.response_ready()
    assert sm.state == "output"

    sm.output_complete()
    assert sm.state == "idle"


def test_debounce_failure_returns_to_idle():
    sm = ReelStateMachine()
    sm.vibration_detected()
    assert sm.state == "detecting"

    sm.debounce_failed()
    assert sm.state == "idle"


def test_reel_timeout_goes_to_error_then_resets():
    sm = ReelStateMachine()
    sm.vibration_detected()
    sm.vibration_confirmed()
    assert sm.state == "reeling"

    sm.reel_timeout()
    assert sm.state == "error"

    sm.reset()
    assert sm.state == "idle"


def test_invalid_transition_raises():
    sm = ReelStateMachine()
    with pytest.raises(Exception):
        # idle状態からreel_position_detectedへは直接遷移できない
        sm.reel_position_detected()
