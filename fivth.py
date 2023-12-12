import pytest
import asyncio
import concurrent.futures

async def async_function():
    await asyncio.sleep(1)
    return "Async result"

def run_async_function():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(async_function())
    loop.close()
    return result

def test_async_function_in_thread():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(run_async_function)
        result = future.result()

        assert result == "Async result"