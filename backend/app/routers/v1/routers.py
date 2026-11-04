from app.routers.v1.auth import password_reset, password_auth
from app.routers.v1 import user
from fastapi import APIRouter
from sqlalchemy import text
from app.routers.v1.auth import google_auth
from app.routers.dependencies import SessionDep

router = APIRouter()

# user api
router.include_router(user.router, prefix="/user", tags=["user"])


# sign-in and login api
router.include_router(google_auth.router, prefix="/auth/google", tags=["google_auth"])
router.include_router(password_auth.router, prefix="/auth", tags=["auth"])
router.include_router(
    password_reset.router, prefix="/auth/password-reset", tags=["password-reset"]
)
