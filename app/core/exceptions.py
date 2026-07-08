from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException


async def http_exception_handler(
        request: Request,
        exc: HTTPException
):
    if exc.status_code == 401:
        return JSONResponse(
            status_code=401,
            content={
                "code": 401,
                "message": "Unauthorized"
            }
        )

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "detail": exc.detail
        }
    )
