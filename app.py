from fastapi import FastAPI
from pydantic import BaseModel
from email_env import EmailEnvironment

app = FastAPI()
env = EmailEnvironment()

# -------- REQUEST MODELS --------
class ResetRequest(BaseModel):
    task: str = "easy"

class StepRequest(BaseModel):
    action: str

# -------- ROUTES --------
@app.post("/reset")
def reset(req: ResetRequest):
    email = env.reset(req.task)
    return {
        "observation": email,
        "info": {},
        "done": False
    }

@app.post("/step")
def step(req: StepRequest):
    next_email, reward, done, info = env.step(req.action)
    return {
        "observation": next_email,
        "reward": reward,
        "done": done,
        "info": info
    }

@app.get("/state")
def state():
    return {"state": env.state()}
