from typing import Annotated

from fastapi import FastAPI, Request, HTTPException, status, Depends
from schemas.movies import Movie


app = FastAPI(
    title="Catalog Movie",
)

MOVIES = [
    Movie(
        id=1,
        title="Один дома",
        description="Парень остается один дома",
        genre="Комедия",
        year=1990,
    ),
    Movie(
        id=2,
        title="Маска",
        description="Парень находит маску",
        genre="Комедия",
        year=1994,
    ),
    Movie(
        id=3,
        title="Остров сокровищ",
        description="У них есть пушка, но зачем?",
        genre="Приключения",
        year=1988,
    ),
]


@app.get("/")
def read_root(request: Request, name: str = "World"):
    docs_url = request.url.replace(
        path="/docs",
        query="",
    )
    return {
        "message": f"Hello, {name}!",
        "docs": str(docs_url),
    }


@app.get("/movies/", response_model=list[Movie])
def get_all_movies():
    return MOVIES


def find_movie(movie_id: int) -> Movie | None:
    for movie in MOVIES:
        if movie.id == movie_id:
            return movie
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            f"Movie {movie_id!r} not found",
        )


@app.get("/movies/{movie_id}", response_model=Movie)
def get_movies_by_id(movie: Annotated[Movie, Depends(find_movie)]):
    return find_movie(movie.id)
