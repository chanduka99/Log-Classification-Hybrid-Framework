from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import pandas as pd
from classify import classify_csv, classify_log
import io

app = FastAPI(title="Log Classification API", version="1.0.0")


class LogEntry(BaseModel):
    source: str
    log_message: str


@app.post("/classify-csv")
async def classify_csv_endpoint(file: UploadFile = File(...)):
    """
    Classify logs from an uploaded CSV file.

    The CSV must contain columns: 'source' and 'log_message'.
    Returns the classified data as JSON.
    """
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="File must be a CSV")

    try:
        contents = await file.read()
        buffer = io.StringIO(contents.decode('utf-8'))
        df_classified = classify_csv(buffer)
        return JSONResponse(content=df_classified.to_dict(orient='records'))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/classify-log")
async def classify_log_endpoint(entry: LogEntry):
    """
    Classify a single log entry.

    Expects JSON with 'source' and 'log_message'.
    Returns the classification label.
    """
    try:
        label = classify_log(entry.source, entry.log_message)
        return {"label": label}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Log Classification API"}
