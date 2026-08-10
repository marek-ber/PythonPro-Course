from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from background import analyze_sentiment, send_comment_email
from database import get_db
from models import CommentORM, PostORM, UserORM
from schemas import (
    CommentCreate,
    CommentResponse,
    PostCreate,
    PostResponse,
    PostUpdate,
    PostWithComments,
    UserCreate,
    UserResponse,
    UserUpdate,
)


router = APIRouter(tags=["Blog"])


@router.post("/users", response_model=UserResponse, status_code=201)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    new_user = UserORM(**user.model_dump())
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user


@router.get("/users", response_model=list[UserResponse])
async def get_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(UserORM))
    return result.scalars().all()


@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await db.get(UserORM, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@router.put("/users/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: int,
    data: UserUpdate,
    db: AsyncSession = Depends(get_db),
):
    user = await db.get(UserORM, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(user, field, value)

    await db.commit()
    await db.refresh(user)
    return user


@router.delete("/users/{user_id}", status_code=204)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await db.get(UserORM, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    await db.delete(user)
    await db.commit()
    return None


@router.post("/posts", response_model=PostResponse, status_code=201)
async def create_post(post: PostCreate, db: AsyncSession = Depends(get_db)):
    user = await db.get(UserORM, post.author_id)

    if not user:
        raise HTTPException(status_code=404, detail="Author not found")

    new_post = PostORM(**post.model_dump())
    db.add(new_post)
    await db.commit()
    await db.refresh(new_post)
    return new_post


@router.get("/posts", response_model=list[PostResponse])
async def get_posts(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(PostORM))
    return result.scalars().all()


@router.get("/posts/{post_id}", response_model=PostResponse)
async def get_post(post_id: int, db: AsyncSession = Depends(get_db)):
    post = await db.get(PostORM, post_id)

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    return post


@router.put("/posts/{post_id}", response_model=PostResponse)
async def update_post(
    post_id: int,
    user_id: int,
    data: PostUpdate,
    db: AsyncSession = Depends(get_db),
):
    post = await db.get(PostORM, post_id)

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    if post.author_id != user_id:
        raise HTTPException(status_code=403, detail="Only author can edit post")

    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(post, field, value)

    await db.commit()
    await db.refresh(post)
    return post


@router.delete("/posts/{post_id}", status_code=204)
async def delete_post(
    post_id: int,
    user_id: int,
    db: AsyncSession = Depends(get_db),
):
    post = await db.get(PostORM, post_id)

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    if post.author_id != user_id:
        raise HTTPException(status_code=403, detail="Only author can delete post")

    await db.delete(post)
    await db.commit()
    return None


@router.post("/posts/{post_id}/comments", response_model=CommentResponse, status_code=201)
async def create_comment(
    post_id: int,
    comment: CommentCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
):
    post = await db.get(PostORM, post_id)
    user = await db.get(UserORM, comment.author_id)

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    new_comment = CommentORM(
        content=comment.content,
        author_id=comment.author_id,
        post_id=post_id,
    )
    db.add(new_comment)
    await db.commit()
    await db.refresh(new_comment)

    background_tasks.add_task(send_comment_email, post_id)
    background_tasks.add_task(analyze_sentiment, new_comment.content)

    return new_comment


@router.get("/posts/{post_id}/with-comments", response_model=PostWithComments)
async def get_post_with_comments(post_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(PostORM)
        .options(selectinload(PostORM.comments))
        .where(PostORM.id == post_id)
    )
    post = result.scalar_one_or_none()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    return post


@router.post("/posts/{post_id}/summarize")
async def summarize_post(post_id: int, db: AsyncSession = Depends(get_db)):
    post = await db.get(PostORM, post_id)

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    summary = post.content[:120]

    if len(post.content) > 120:
        summary += "..."

    return {
        "post_id": post.id,
        "summary": summary,
        "info": "Symulacja AI",
    }
