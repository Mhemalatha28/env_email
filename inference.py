from email_env import EmailEnvironment, smart_agent

def run_inference():
    env = EmailEnvironment()

    for task in ["easy", "medium", "hard"]:
        print(f"\nRunning task: {task}")

        email = env.reset(task)
        actions = []
        done = False

        while not done:
            action = smart_agent(email)
            next_email, reward, done, info = env.step(action)

            actions.append(action)
            email = next_email

        score = env.grade(actions)
        print(f"{task} accuracy: {score}")


if __name__ == "__main__":
    run_inference()