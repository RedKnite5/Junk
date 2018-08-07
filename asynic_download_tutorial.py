import asyncio

async def speak_async():  
    print('OMG asynchronicity!')

loop = asyncio.get_event_loop()  
loop.run_until_complete(speak_async())  
loop.close()  
	
