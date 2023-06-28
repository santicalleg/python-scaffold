from fastapi import APIRouter

router = APIRouter(prefix="/api")

@router.get("/case-one")
async def caseone(latency: int = 0):
    return f"Latency: {latency}"

@router.get("/case-two")
async def casetwo():
    return {"case": "two"}

@router.get("/case-three")
async def casetwo():
    return {"case": "three"}
