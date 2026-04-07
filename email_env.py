class EmailEnvironment:
    VALID_ACTIONS = ["spam", "important", "normal"]

    def __init__(self):
        # 3 tasks: easy → medium → hard
        self.tasks = {
            "easy": [
                ("Win a free lottery prize now", "spam"),
                ("Meeting at 5pm", "important"),
                ("Hello friend, long time", "normal"),
                ("Claim your free gift", "spam"),
                ("Project deadline tomorrow", "important"),
                ("Check our new blog post", "normal"),
            ],
            "medium": [
                ("Limited time offer, buy now", "spam"),
                ("Client feedback needs review", "important"),
                ("Weekly newsletter update", "normal"),
                ("Verify your account immediately", "spam"),
                ("Team meeting rescheduled", "important"),
                ("Explore trending articles", "normal"),
                ("Security alert: suspicious login", "spam"),
                ("Submit assignment by tonight", "important"),
                ("New features released this week", "normal"),
            ],
            "hard": [
                ("Urgent: update your bank details", "spam"),
                ("Interview scheduled for Monday", "important"),
                ("Discover new travel destinations", "normal"),
                ("Congratulations! You won ₹10,00,000", "spam"),
                ("Client meeting moved to Friday", "important"),
                ("Enjoy weekend sale offers", "normal"),
                ("Unauthorized login attempt detected", "spam"),
                ("Reminder: pay electricity bill", "important"),
                ("Latest updates from platform", "normal"),
                ("Reset password to avoid lockout", "spam"),
                ("Company-wide meeting announcement", "important"),
                ("Weekly newsletter subscription", "normal"),
            ],
        }

        self.current_task = "easy"
        self.index = 0
        self.current_email = None

    def reset(self, task="easy"):
        self.current_task = task
        self.index = 0
        self.current_email = self.tasks[task][0][0]
        return self.current_email

    def state(self):
        return self.current_email

    def step(self, action):
        correct = self.tasks[self.current_task][self.index][1]

        # reward logic
        if action == correct:
            reward = 1.0
        elif action in self.VALID_ACTIONS:
            reward = 0.5
        else:
            reward = -1.0

        info = {
            "correct_answer": correct,
            "your_action": action
        }

        self.index += 1

        if self.index >= len(self.tasks[self.current_task]):
            return None, reward, True, info
        else:
            self.current_email = self.tasks[self.current_task][self.index][0]
            return self.current_email, reward, False, info

    def grade(self, actions):
        correct = 0
        total = len(self.tasks[self.current_task])

        for i, action in enumerate(actions):
            if action == self.tasks[self.current_task][i][1]:
                correct += 1

        return correct / total


# ---------------- BASELINE AGENT ----------------
def smart_agent(email):
    email = email.lower()

    if any(w in email for w in [
        "lottery", "won", "prize", "free", "claim",
        "bank", "verify", "unauthorized", "suspicious"
    ]):
        return "spam"

    if any(w in email for w in [
        "meeting", "deadline", "interview", "client",
        "assignment", "reminder", "announcement"
    ]):
        return "important"

    if "urgent" in email:
        return "important"

    if any(w in email for w in ["offer", "sale", "deal"]):
        return "normal"

    return "normal"


# ---------------- RUN ----------------
def run(task="hard"):
    env = EmailEnvironment()
    email = env.reset(task)

    actions = []
    done = False

    while not done:
        print("\n Email :",email)

        action = smart_agent(email)
        print("Action:",action)

        next_email, reward , done , info = env.step(action)

        print("Reward:",reward)
        print("Info:",info)

        actions.append(action)
        email = next_email
    score = env.grade(actions)
    print("\nFinal Accuracy :", score)


if __name__ == "__main__":
    run("easy")
    run("medium")
    run("hard")