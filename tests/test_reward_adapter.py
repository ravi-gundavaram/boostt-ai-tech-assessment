import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from reward_adapter import json_to_reward

def test_json_to_reward():
    input_json = '{"experiment_id": "exp_123", "lift": 0.15}'
    reward = json_to_reward(input_json)
    assert reward.experiment_id == "exp_123"
    assert reward.reward_value == 0.15
    assert isinstance(reward.SerializeToString(), bytes)
