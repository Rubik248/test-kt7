import pytest
import asyncio

async def async_function():
    await asyncio.sleep(1)
    return 42

@pytest.mark.asyncio
async def test_async_function():
    expected_value = 42


    result = await async_function()


    assert result == expected_value
