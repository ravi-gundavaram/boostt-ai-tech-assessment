from dataclasses import dataclass

@dataclass
class Reward:
    experiment_id: str
    reward_value: float

    def SerializeToString(self):
        return f"{self.experiment_id}:{self.reward_value}".encode()

import json

def json_to_reward(json_str: str) -> Reward:
    data = json.loads(json_str)
    return Reward(
        experiment_id=data["experiment_id"],
        reward_value=data["lift"]
    )
