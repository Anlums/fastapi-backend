from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_posts():
    return {"message": "Posts endpoint"}
