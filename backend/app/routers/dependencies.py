from app.db.session import SessionDep
from app.auth.current_user import get_current_user_or_raise_http_error
from fastapi import Depends, HTTPException, Query
from typing import Annotated
from dataclasses import dataclass
from datetime import date
from app.models.users import User

# Login user details, current user dependency
CurrentUser = Annotated[User, Depends(get_current_user_or_raise_http_error)]


__all__ = ["CurrentUser", "SessionDep"]
