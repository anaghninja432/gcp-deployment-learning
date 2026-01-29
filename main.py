from fastapi import FastAPI
import uvicorn

app=FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.get('/health')
async def health_check():
    return {"status":"ok"}

@app.get('/items/{item_id}')
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)         