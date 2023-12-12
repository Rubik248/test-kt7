import pytest
import aiohttp
import asyncio

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

@pytest.mark.asyncio
async def test_fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    response = await fetch_data(url)


    assert response is not None
    assert isinstance(response, dict)
    assert "userId" in response