# Email Classification OpenEnv Environment

## 📌 Description
This project simulates a real-world email classification system where an AI agent classifies emails into:
- Spam
- Important
- Normal

## 🎯 Tasks
The environment has 3 difficulty levels:

- Easy
- Medium
- Hard

Each task contains multiple emails with correct labels.

## ⚙️ Actions
The agent can take 3 actions:
- spam
- important
- normal

## 🧠 Environment Functions

- `reset()` → Starts the environment and returns first email  
- `step(action)` → Takes action and returns:
  - next email
  - reward
  - done
  - info  
- `state()` → Returns current email  

## 🏆 Reward System

- Correct classification → +1.0  
- Wrong but valid → +0.5  
- Invalid action → -1.0  

## 📊 Results (Baseline Agent)

- Easy Accuracy: 1.0  
- Medium Accuracy: ~0.88  
- Hard Accuracy: ~0.91  

## ▶️ How to Run

```bash
python email_env.py