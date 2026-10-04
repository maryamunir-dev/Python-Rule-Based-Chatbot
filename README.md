# Python Rule-Based Chatbot

A beginner-friendly Python mini-project that demonstrates fundamental programming concepts through a simple rule-based personal chat assistant.

## Features

* Provides time-based greetings using Python's `datetime` module
* Responds to predefined conversational messages
* Takes and processes user input
* Uses a function to generate chatbot responses
* Runs continuously using a `while` loop
* Ends the conversation when the user types `bye`
* Provides a default response for unrecognized messages

## Technologies Used

* Python
* `datetime` module
* VS Code

## How It Works

The chatbot first checks the current time and displays an appropriate greeting. It then takes user input and converts it to lowercase for easier matching.

A predefined dictionary stores common questions and responses. The `getResponseofbot()` function checks the user's input against these predefined messages and returns the corresponding response.

The chatbot continues running until the user types `bye`.

## How to Run

1. Make sure Python is installed on your computer.
2. Download or clone this repository.
3. Open the project in VS Code or another Python editor.
4. Run `main.py`.
5. Enter a message and interact with the chatbot.

## Project Purpose

This project was created to practice Python fundamentals, including user input, conditional statements, functions, dictionaries, loops, string handling, and the `datetime` module.
