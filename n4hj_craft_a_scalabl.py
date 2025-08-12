# n4hj_craft_a_scalabl.py

import random
import time
from abc import ABC, abstractmethod

class AutomationScriptSimulator(ABC):
    def __init__(self, name, task_list):
        self.name = name
        self.task_list = task_list
        self.task_queue = []

    @abstractmethod
    def simulate(self):
        pass

    def add_task(self, task):
        self.task_queue.append(task)

    def execute_tasks(self):
        while self.task_queue:
            task = self.task_queue.pop(0)
            print(f"Executing task: {task}")
            time.sleep(random.uniform(0.1, 0.5))  # simulate task execution time
            print(f"Task {task} completed")

class SimpleAutomationScriptSimulator(AutomationScriptSimulator):
    def simulate(self):
        print(f"Simulating automation script: {self.name}")
        self.execute_tasks()
        print(f"Automation script {self.name} completed")

class ScalableAutomationScriptSimulator(AutomationScriptSimulator):
    def __init__(self, name, task_list, num_threads):
        super().__init__(name, task_list)
        self.num_threads = num_threads

    def simulate(self):
        print(f"Simulating scalable automation script: {self.name} with {self.num_threads} threads")
        for _ in range(self.num_threads):
            self.execute_tasks_in_parallel()
        print(f"Scalable automation script {self.name} completed")

    def execute_tasks_in_parallel(self):
        while self.task_queue:
            task = self.task_queue.pop(0)
            print(f"Executing task: {task} in parallel")
            time.sleep(random.uniform(0.1, 0.5))  # simulate task execution time
            print(f"Task {task} completed in parallel")

# Example usage
script1 = SimpleAutomationScriptSimulator("Script 1", ["Task 1", "Task 2", "Task 3"])
script1.add_task("Task 4")
script1.simulate()

script2 = ScalableAutomationScriptSimulator("Script 2", ["Task A", "Task B", "Task C"], 3)
script2.add_task("Task D")
script2.simulate()