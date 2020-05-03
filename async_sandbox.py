#! python

import asyncio

async def test(a):
	await asyncio.sleep(4)
	print(a)

async def main():
	await asyncio.gather(test(5), test(6))

asyncio.run(main())
