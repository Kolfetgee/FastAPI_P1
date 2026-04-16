from fastapi import Request
from fastapi.responses import JSONResponse

from src.apps.auth.connector import user_auth_connector
from src.apps.auth.utils import decode_token


PROTECTED_PATHS = {
    "/auth/me-middleware",
}


async def auth_middleware(request: Request, call_next):
    path = request.url.path

    if path not in PROTECTED_PATHS:
        return await call_next(request)

    auth_header = request.headers.get("Authorization")
    if auth_header is None:
        return JSONResponse(
            status_code=401,
            content={"detail": "Not authenticated"},
        )

    if not auth_header.startswith("Bearer "):
        return JSONResponse(
            status_code=401,
            content={"detail": "Invalid authorization header"},
        )

    token = auth_header.removeprefix("Bearer ").strip()
    payload = decode_token(token)

    if payload is None:
        return JSONResponse(
            status_code=401,
            content={"detail": "Invalid token"},
        )

    if payload.get("type") != "access":
        return JSONResponse(
            status_code=401,
            content={"detail": "Invalid token type"},
        )

    email = payload.get("sub")
    if email is None:
        return JSONResponse(
            status_code=401,
            content={"detail": "Invalid token payload"},
        )

    auth_user = user_auth_connector.get_auth_user_by_email(email)
    if auth_user is None:
        return JSONResponse(
            status_code=401,
            content={"detail": "User not found"},
        )

    request.state.auth_user = auth_user
    return await call_next(request)