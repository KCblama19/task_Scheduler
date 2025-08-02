import time


class Task:
    def __init__(self, name: str, priority: int, duration: int):
        self.name = name
        self.priority = priority
        self.duration = duration

    def __str__(self):
        return f"{self.name} - Priority: {self.priority}, Duration: {self.duration}s"

class TaskNode:
    def __init__(self, task: Task):
        self.task = task
        self.next = None

# Handle various task methods, add, view, process, peek, size, etc.
class TaskQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    # enqueue task to the queue
    def add_task(self, task: Task):
        newTask = TaskNode(task)

        # Check if the queue is empty and add task to front of queue
        if self.rear is None:
            self.front = self.rear = newTask
        else:
            self.rear.next = newTask
            self.rear = newTask
        self.size += 1
        print("Task added Successfully.")

    # Print the task in the Queue
    def view_tasks(self):
        # Check if there are task in the queue
        if self.front is None:
            print("Sorry, no task in queue, please add task to view.")
            return
        
        # Print the task in the Queue
        print(f"\nTotal Tasks: {self.size}")
        currentTask = self.front
        while currentTask:
            print(currentTask.task)
            currentTask = currentTask.next
        print("...")
    
    # Process the highest priority task(lower = highest)
    def process_task(self):
        if self.front is None:
            print("No tasks to process.")
            return

        # Find the task with the highest priority
        min_priority = self.front.task.priority
        prev, current = None, self.front
        min_prev, min_node = None, self.front

        while current.next:
            if current.next.task.priority < min_priority:
                min_priority = current.next.task.priority
                min_prev = current
                min_node = current.next
            current = current.next

        # Remove from queue
        if min_node == self.front:
            self.front = self.front.next
            if self.front is None:
                self.rear = None
        else:
            min_prev.next = min_node.next
            if min_node == self.rear:
                self.rear = min_prev

        self.size -= 1
        print(f"Processing: {min_node.task} (Estimated Time: {min_node.task.duration}s)")
        time.sleep(min_node.task.duration)

        self.view_tasks()

    
    def peek_next_task(self):
        if self.front is None:
            print("No task to peek")
        else:
            print(self.front.task)

    def get_size(self):
        print(f"Current task in queue: {self.size}")
    
    
# Handle User input and testing for future scalability
class TaskSchedulerApp:
    def __init__(self):
        self.queue = TaskQueue()
    
    def run(self):
        while True:
            print("\nTask Scheduler Menu:")
            print("1. Add Task")
            print("2. Process Task")
            print("3. View Tasks")
            print("4. Peek the next task")
            print("5. Show number of task in queue")
            print("6. Exit")

            try:
                option = int(input("> ").strip())
            except ValueError:
                print("Invalid input. Please enter 1-4.")
                continue

            if option == 1:
                self.add_task()
            elif option == 2:
                self.queue.process_task()
            elif option == 3:
                self.queue.view_tasks()
            elif option == 4:
                self.queue.peek_next_task()
            elif option == 5:
                self.queue.get_size()
            elif option == 6:
                try:
                    confirm = int(input("Wanna leave(1(Yes), 2(No)): ").strip())
                except ValueError:
                    print("Please enter a valid value")

                if confirm == 1:
                    print("Thanks for scheduling.")
                    break
                elif confirm == 2:
                    continue
                else:
                    print("Choose a valid option")
            else:
                print("Choose a valid option.")

    def add_task(self):
        name = input("Enter task name: ").strip()
        try:
            priority = int(input("Enter priority (lower is higher): "))
            duration = int(input("Enter duration (in seconds): "))
        except ValueError:
            print("Invalid input. Priority and duration must be numbers.")
            return
        
        task = Task(name, priority, duration)
        self.queue.add_task(task)

if __name__ == "__main__":
    TaskSchedulerApp().run()