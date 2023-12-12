import pytest
import asyncio

async def async_function():
    await asyncio.sleep(1)
    raise ValueError("Expected exception")

@pytest.mark.asyncio
async def test_async_function_exception():
    expected_exception = ValueError

    with pytest.raises(expected_exception):
        await async_function()