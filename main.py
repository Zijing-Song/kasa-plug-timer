import asyncio
from kasa import SmartPlug
import time


async def main():
    run = 1

    t1 = input("on timer:")

    t2 = input("off timer:")

    p = SmartPlug("192.168.1.117")
    while run == 1:
        await p.update()
        await p.turn_on()
        time.sleep(int(t1))
        await p.turn_off()
        time.sleep(int(t2))


if __name__ == "__main__":
    asyncio.run(main())


