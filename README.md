

# 🤖 MY BUDDY

Welcome to **MY BUDDY** – your friendly neighborhood chatbot! Ever wanted a buddy who’s always available, won’t judge, and loves to chat? Meet MY BUDDY! 💬

![MY BUDDY Demo](images/chatbot_demo.png)

## Table of Contents

- [Overview](#overview)
- [Why MY BUDDY?](#why-my-buddy)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Example Request and Response](#example-request-and-response)
- [Acknowledgments](#acknowledgments)

## Overview

MY BUDDY is a simple chatbot created with **Python, Flask**, and **Hugging Face Transformers**. Using Facebook's BlenderBot, MY BUDDY loves chatting and keeping short-term memory, so your interactions feel natural (sort of).

## Why MY BUDDY?

1. **Never Ghosts You**: MY BUDDY is here 24/7!
2. **No Judgments**: Vent away – MY BUDDY is a patient listener.
3. **Loves Chit-Chat**: If you’ve got words, MY BUDDY’s got replies.
4. **Perfect Friend for the Socially Awkward**: No need for small talk skills here.

## Features 🚀

- **Conversational AI**: Uses BlenderBot-400M for some real (well, kinda) personality.
- **Flask Backend**: Runs smoothly on Flask, so you can set it up with minimal hassle.
- **CORS Support**: Perfect for frontend integration.
- **Remembers Recent Chats**: MY BUDDY’s got short-term memory, but don’t expect it to recall details forever!

## Technologies Used 🛠️

- **Python**: The language of love (well, for developers).
- **Flask**: Keeps everything running smoothly.
- **Flask-CORS**: Because MY BUDDY wants to be accessible to everyone.
- **Hugging Face Transformers**: For that delightful AI intelligence.
- **BlenderBot by Facebook**: So MY BUDDY can pretend to be human.

## Installation ⚙️

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mourvijoshi/Simple-Chatbot-Application.git
   cd Simple-Chatbot-Application/LLM_application_chatbot
   ```

2. **Install dependencies:**  
   Make sure Python is ready, then install:
   ```bash
   pip install flask flask-cors transformers
   ```

3. **Download the Model**  
   Just run it, and MY BUDDY will grab BlenderBot automatically. Sit back and relax. 😎

## Usage 🤔

1. **Run the App:**
   ```bash
   python app.py
   ```

2. **Meet MY BUDDY**  
   Head to [http://localhost:5000/](http://localhost:5000/). Type anything, hit enter, and see what your new buddy has to say!

3. **Start Chatting**  
   Type away, and MY BUDDY will keep responding. It’s the most loyal conversational partner you’ll ever have!

## Project Structure 📂

Your project directory looks like this:

```
LLM_application_chatbot/
├── app.py               # The Flask app - where MY BUDDY lives
├── templates/
│   └── index.html       # The friendly frontend
├── static/
│   └── script.js        # JavaScript for frontend awesomeness
├── images/
│   └── chatbot_demo.png # Image(s) for the README
```

## Example Request and Response 🗣️

Here’s a taste of what MY BUDDY can do:

- **Request (POST to `/chatbot`):**
  ```json
  {
    "prompt": "Hey, MY BUDDY!"
  }
  ```

- **Response:**
  ```json
  {
    "response": "Hey there! What's up?"
  }
  ```

It’s like texting a friend... who also happens to be code! 🥳

## Acknowledgments 🙌

- **BlenderBot**: Shoutout to Facebook for giving MY BUDDY some AI personality.
- **Hugging Face**: For the amazing Transformers library. Without it, MY BUDDY would be... less chatty.
- **You**: Thanks for hanging out with MY BUDDY – it’s thrilled to chat!

![image](https://github.com/user-attachments/assets/f9bfe79a-f046-4476-9d31-12c3ff906f46)
![image](https://github.com/user-attachments/assets/2356fd17-636e-4183-997f-5823f988a99e)

