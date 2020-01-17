from fastapi import FastAPI

app = FastAPI()

@app.get('/{file_path:path}')
async def root(file_path: str):
    return {"message": file_path}
