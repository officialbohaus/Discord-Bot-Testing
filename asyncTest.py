import pytest

@pytest.mark.asyncio
async def test_my_async_code():
    result = await fetch_data()
    assert result == "success"
