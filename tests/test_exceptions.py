import pytest
from fastapi import HTTPException, Request

from app.core.exceptions import http_exception_handler


@pytest.mark.asyncio
async def test_http_exception_handler_401():

    request = Request(
        {
            "type": "http",
            "method": "GET",
            "path": "/"
        }
    )

    exc = HTTPException(
        status_code=401,
        detail="Invalid token"
    )

    response = await http_exception_handler(
        request,
        exc
    )

    assert response.status_code == 401
    assert response.body == b'{"code":401,"message":"Unauthorized"}'


@pytest.mark.asyncio
async def test_http_exception_handler_other_status():

    request = Request(
        {
            "type": "http",
            "method": "GET",
            "path": "/"
        }
    )

    exc = HTTPException(
        status_code=404,
        detail="Not found"
    )

    response = await http_exception_handler(
        request,
        exc
    )

    assert response.status_code == 404
    assert b"Not found" in response.body
