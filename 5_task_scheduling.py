import random

def task_scheduling(tasks):
  """
  Task scheduling algorithm.

  Args:
    tasks: A list of tasks, where each task is a tuple of (start_time, end_time).

  Returns:
    A list of tasks in the order they should be scheduled.
  """

  scheduled_tasks = []
  while tasks:
    current_task = tasks[0]
    for task in tasks:
      if task[0] <= current_task[1]:
        current_task = task
    scheduled_tasks.append(current_task)
    tasks.remove(current_task)
  return scheduled_tasks

if __name__ == "__main__":
  tasks = [(0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]
  scheduled_tasks = task_scheduling(tasks)
  print(scheduled_tasks)