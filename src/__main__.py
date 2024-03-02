import asyncio

from src.deps.main import MainContainer
from .main import main


if __name__ == "__main__":
    container = MainContainer()
    asyncio.run(main())
