import asyncio
from webserver import app

async def main():
    while True:
        await asyncio.sleep(1)

if __name__ == '__main__':
    asyncio.run(main())
