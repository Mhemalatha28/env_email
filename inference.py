import os
from openai import OpenAI
from email_env import EmailEnvironment

# -------- ENV VARIABLES --------
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

if HF_TOKEN is None:
    raise ValueError("HF_TOKEN environment variable is required")

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)

# -------- AGENT USING LLM --------
def llm_agent(email):
    prompt = f"""
Classify this email into one of these categories:
spam, important, normal

Email: {email}

Answer only one word: spam or important or normal
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip().lower()


# -------- RUN TASK --------
def run_task(task_name):
    env = EmailEnvironment()
    email = env.reset(task_name)

    step = 0
    rewards = []
    done = False
    success = False

    print(f"[START] task={task_name} env=email_env model={MODEL_NAME}")

    while not done:
        step += 1
        error = None

        try:
            action = llm_agent(email)
        except Exception as e:
            action = "normal"
            error = str(e)

        next_email, reward, done, info = env.step(action)

        rewards.append(f"{reward:.2f}")

        print(f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error={error if error else 'null'}")

        email = next_email

    success = True
    print(f"[END] success={str(success).lower()} steps={step} rewards={','.join(rewards)}")


# -------- MAIN --------
if __name__ == "__main__":
    for task in ["easy", "medium", "hard"]:
        run_task(task)
