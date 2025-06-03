from data import data
from tool import tool
import asyncio

data_local = data()

def Start():
    tool.clear_screen()

async def main():
    if not data_local.Debug: tool.verify_modules()
    await asyncio.create_task(tool.add_path_modules(data_local))
    Start()
    return

if __name__ == "__main__":
    asyncio.run(main())