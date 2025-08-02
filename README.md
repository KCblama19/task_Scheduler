# Console-Based Task Scheduler

A simple console-based task scheduler that allows users to create, manage, and process tasks based on **priority**. This project uses a **manually implemented linked list–based priority queue** to process the highest-priority task first (lower number = higher priority).

## Features

- Add tasks with name, priority, and estimated duration
- View all scheduled tasks
- Process the next highest-priority task
- Peek at the front task
- Track the number of tasks in the queue
- Console menu navigation

## How It Works

This scheduler uses a **custom singly linked list** to manage tasks and searches for the task with the **lowest priority number** during processing. It simulates task execution using `time.sleep()` based on the task’s duration.

> This project does **not use built-in heaps or libraries** for priority queues — the algorithm is implemented manually to demonstrate my understanding of data structures.

## Key Concepts

- Object-Oriented Programming (OOP)
- Custom Linked List Implementation
- Priority Queue Behavior
- Console-Based Menus
- Time-Based Task Simulation

## Requirements

- Python 3.7+

No external libraries are required.

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/task-scheduler.git
   cd task-scheduler

2. Run the app:
```bash
python task_scheduler.py
```
3. Follow the menu prompts to add, view or process tasks.
```bash
Task Scheduler Menu:
1. Add Task
2. Process Task
3. View Tasks
4. Peek the next task
5. Show number of task in queue
6. Exit

> 1
Enter task name: Backup
Enter priority (lower is higher): 2
Enter duration (in seconds): 5
Task added Successfully.

> 2
Processing: Backup - Priority: 2, Duration: 5s (Estimated Time: 5s)...
```
## Folder Structure
```bash
task-scheduler/
│
├── task_scheduler.py    # Main program file
├── README.md            # Project documentation
```

## Future Enhancements
- I planned to use a heapq or a binary heap for more efficient priority queue operations

- Add file-based persistence (save/load tasks)

- Unit tests with unittest or pytest(Not good at testing right now but will be good in the future, still learning)

- GUI or web-based version( After I learn a web framework, lol)

- Add task categories or labels

## Contributing
This project was built for personal learning, but contributions and feedback are welcome! Fork the repo, improve features, or refactor the logic.

## License
MIT License

Developed by Me(haha): [Abraham K. Blama](https://github.com/KCblama19) – Learning DSA and applying it to real-world simulations.