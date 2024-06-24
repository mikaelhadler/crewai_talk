from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from main import run_crew

app = FastAPI()

class TopicRequest(BaseModel):
    topic: str

@app.post("/run_crew")
def run_crew_endpoint(request: TopicRequest):
    try:
        result = run_crew(request.topic)
        return {"status": "success", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
