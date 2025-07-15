from fastapi import FastAPI, Request, status, HTTPException, Depends


app = FastAPI(
    title="Catalog Movie",
)


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
