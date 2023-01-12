from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.infrastructure.database import get_db

router = APIRouter()


@router.get("", summary="Health Check")
async def health_check(db: Session = Depends(get_db)) -> dict:
    return {"status": "ok"}
