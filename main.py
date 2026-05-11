import asyncio
import logging

import yaml
from llm.config import Config
from llm.service import LLMService

logging.basicConfig(level=logging.INFO)


async def load_and_validate_config() -> Config:
    with open("config.yaml") as f:
        data = yaml.safe_load(f)

    return Config.model_validate(data)


async def main():

    config = await load_and_validate_config()

    llm = LLMService(config)

    text = "Explain async/await in Python in one sentence."

    result = await llm.generate(text)
    print(f"Result : {result}")


if __name__ == "__main__":
    asyncio.run(main())
