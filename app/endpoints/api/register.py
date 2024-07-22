import random, string

from fastapi import APIRouter, HTTPException
import asyncpg, bcrypt

from ...services import EnvironService

router = APIRouter()


def randomToken(n):
    return "".join(random.choices(string.ascii_letters + string.digits, k=n))


@router.post("/api/register")
async def register(username: str, password: str):
    conn: asyncpg.Connection = asyncpg.connect(EnvironService.get("dsn"))
    check = await conn.fetchrow("SELECT * FROM users WHERE id = $1", username.lower())
    if check:
        raise HTTPException(400, "そのIDのユーザーはすでに存在しています")

    salt = bcrypt.gensalt(rounds=10, prefix=b"2a")
    await conn.execute(
        """
        INSERT INTO users (id, password, id_original)
        VALUES ($1, $2, $3)
        """,
        username.lower(),
        bcrypt.hashpw(password, salt).decode(),
        username,
    )

    token = randomToken(32)
    await conn.execute(
        """
        INSERT INTO tokens (token, id)
        VALUES ($1, $2)
        """,
        username.lower(),
        token,
    )
    return {"token": token, "username": username}
