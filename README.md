# Project Name 

Behaviour-Adaptive Task Scheduler

## Project Description 

This project is a command line interface task scheduler that. Implemented with the intention
to erradicate to the greatest extent the habit of procastination throughout the life of a student.
This is done by scheduling and prioritizing tasks based on deadlines, difficulty and task duration through 
user behaviour patterns. The systems also adapts over time, by tracking whether previous tasks have been 
completed, skipped or postponed, and adjusts the priority order for future tasks.

## Project Key Features

- Prioritizing tasks is based on the following parameters (Dealine, Difficulty & Duration)
- Adaptive behaviour modeling for difficult problems
- Long-term memory using a JSON file as a storage
- Final behavioral feedback loop
- Input validation for deadlines and difficulty levels

## How does it work?

The user is initially presented with the desired number of tasks to complete. As a next step, the user is given the option of entering all the necessary information to define a task. Specifically, the task consists of the following elements: the Task Name, the Task Duration (hours and minutes), the Task Difficulty, and the Deadline. Following the entry of all necessary information, the sorted tuple allows to arrange the tasks in ascending order, establishing their priority. It is important to note that the priority order is as follows:
1. Closest Deadline
2. Hardest Difficulty
3. Longest Duration
Ultimately, the program allows the user to provide an update on whether the task was completed, skipped, or postponed. The new status of the task will be saved in the JSON. A skipped or postponed task will be recorded as skipped. If a task has been completed, it will simply be recorded as completed. With the assistance of these records, the program will be able to penalize the student (by moving difficult tasks up the priority list without affecting the deadline) or reward the user (by moving difficult tasks down the priority list). The user's previous behavior with respect to each task determines how these adjustments will be made. It's worth pointing out that skipped, postponed, or completed activities will only have an effect if the activity is repeated twice or more. This enables us to find patterns in the user's activity and ignore any possible anomalies.

## Installation
1. Clone the repository
2. Make sure you have Python 3.10.12 or greater
3. Run: python main.py

## Future Improvements

- Convert to GUI



