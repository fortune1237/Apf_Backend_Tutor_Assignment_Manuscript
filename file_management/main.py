from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/files/")
async def upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename} 


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File):
    return {"message": f" This is a {file.filename.split(".")[-1]} file."}