import asyncio
import sys

async def robot(start_number=0):
    counter = start_number
    while True:
        print(counter)
        counter += 1
        await asyncio.sleep(1)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "run":
        start_number = int(sys.argv[2]) if len(sys.argv) > 2 else 0
        asyncio.run(robot(start_number))