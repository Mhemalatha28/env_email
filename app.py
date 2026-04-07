from fastapi import FastAPI
from email_env import EmailEnvironment

app = FastAPI()

env = EmailEnvironment()

@app.post("/reset")
def reset(task: str = "easy"):
    email = env.reset(task)
    return {"observation": email}

@app.post("/step")
def step(action: str):
    next_email, reward, done, info = env.step(action)
    return {
        "observation": next_email,
        "reward": reward,
        "done": done,
        "info": info
    }

@app.get("/state")
def state():
    return {"state": env.state()}
