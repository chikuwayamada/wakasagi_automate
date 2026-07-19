import json
from pathlib import Path

import boto3

PROMPT_PATH = Path(__file__).parent / "prompts" / "angler_character.md"


class BedrockCharacterClient:
    """AWS Bedrockを呼び出し、釣り人キャラクターの応答を生成する薄いラッパー。"""

    def __init__(self, region: str, model_id: str):
        self._client = boto3.client("bedrock-runtime", region_name=region)
        self._model_id = model_id
        self._character_prompt = PROMPT_PATH.read_text()

    def generate_response(self, vibration_strength: str, reel_duration_seconds: float) -> str:
        prompt = (
            f"{self._character_prompt}\n\n"
            f"振動の強さ: {vibration_strength}\n"
            f"巻き上げにかかった時間: {reel_duration_seconds:.1f}秒\n"
        )
        body = {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 200,
            "messages": [{"role": "user", "content": prompt}],
        }
        response = self._client.invoke_model(
            modelId=self._model_id,
            body=json.dumps(body),
        )
        payload = json.loads(response["body"].read())
        return payload["content"][0]["text"]
