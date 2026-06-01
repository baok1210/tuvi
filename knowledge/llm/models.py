MODEL_REGISTRY = {
    "gpt-4o": {"provider": "openai", "context": 128000, "cost_input": 2.50, "cost_output": 10.00},
    "gpt-4o-mini": {"provider": "openai", "context": 128000, "cost_input": 0.15, "cost_output": 0.60},
    "o1-mini": {"provider": "openai", "context": 128000, "cost_input": 1.10, "cost_output": 4.40},
    "claude-3-5-sonnet-latest": {"provider": "anthropic", "context": 200000, "cost_input": 3.00, "cost_output": 15.00},
    "claude-3-5-haiku-latest": {"provider": "anthropic", "context": 200000, "cost_input": 0.80, "cost_output": 4.00},
    "deepseek-chat": {"provider": "deepseek", "context": 64000, "cost_input": 0.27, "cost_output": 1.10},
    "deepseek-reasoner": {"provider": "deepseek", "context": 64000, "cost_input": 0.55, "cost_output": 2.19},
}


def get_model_info(model_name: str) -> dict:
    return MODEL_REGISTRY.get(model_name, {"provider": "unknown", "context": 4096})
