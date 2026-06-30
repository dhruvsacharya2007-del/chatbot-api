from fastapi import APIRouter

router = APIRouter()

@router.get("/chat/{session_id}")
def get_chat(session_id: str):
    return {
        "session_id": session_id
    }

@router.get("/messages")
def get_messages(limit: int = 10, skip: int = 0):
    return {
        "limit": limit,
        "skip": skip
    }

@router.get("/search")
def search(q: str = ""):
    return {
        "query": q
    }


@router.post("/echo")
def echo(payload: dict):
    return {
        "you_sent": payload
    }