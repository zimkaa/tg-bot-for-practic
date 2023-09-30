import asyncio

from bot.deps.main import MainContainer
from bot.main import main


if __name__ == "__main__":
    container = MainContainer()
    asyncio.run(main())
