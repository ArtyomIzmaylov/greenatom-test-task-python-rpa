import asyncio
import sys

async def robot():
    counter = 0
    while True:
        print(counter)
        counter += 1
        await asyncio.sleep(1)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "run":
        asyncio.run(robot())
