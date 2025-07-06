from fastapi import Request, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

AUTH_SECRET = "secret-token"
security = HTTPBearer()


def verify_auth(request: Request, credentials: HTTPAuthorizationCredentials = security) -> None:
    if credentials.credentials != AUTH_SECRET:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing token",
        )