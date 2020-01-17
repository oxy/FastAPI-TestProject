from fastapi import FastAPI
#import database stuff
#import any other stuff

app = FastAPI()

#@app.on_event("startup")
#    await database.connect()

#@app.on_event("shutdown")
#    await database.shutdown()

@app.get('/{file_path:path}')
async def root(file_path: str):
    return {"message": file_path}
