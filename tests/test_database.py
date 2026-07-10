import pytest

from app.db.database import get_db


@pytest.mark.asyncio
async def test_get_db():

    generator = get_db()

    session = await generator.__anext__()

    assert session is not None

    await generator.aclose()
