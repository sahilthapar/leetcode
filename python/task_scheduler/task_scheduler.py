
from __future__ import annotations
from typing import List, Optional


class Task:
    """
    Represents a task that can be scheduled
    """
    def __init__(self, name: str, dependent_tasks: Optional[List[Task]] = None):
        self.name = name
        self.dependent_tasks = dependent_tasks
        self.is_completed = False

    def ready(self) -> bool:
        """check if no dependent tasks or all dependent_tasks are completed"""
        if not self.dependent_tasks:
            return True
        return not self.has_pending_dependent_tasks

    def has_pending_dependent_tasks(self):
        """check if any dependent tasks are incomplete"""
        for t in self.dependent_tasks:
            if not t.is_completed:
                return False
        return True

    def __str__(self):
        return self.name


class TaskScheduler:
    """Represents a task scheduler"""
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        """
        Add a task to the scheduler
        :param task:
        :return:
        """
        self.tasks.append(task)

    @staticmethod
    def complete_task(task: Task):
        """
        Complete the task
        :param task:
        :return:
        """
        task.completed = True

    def get_next_task(self) -> Task:
        """
        Find the next task to be scheduled
        - task is not completed AND
        - no incomplete dependent tasks
        :return:
        """
        for task in self.tasks:
            if not task.is_completed and task.ready():
                return task

    @staticmethod
    def get_plan(target_task) -> Optional[List[Task]]:
        """
        Generates an execution plan for a task
        :param target_task:
        :return:
        """
        visited = set()
        execution_plan = []

        def _plan_task(tsk: Task):
            if tsk in visited:
                return
            visited.add(tsk)

            if tsk.dependent_tasks:
                for dep_task in tsk.dependent_tasks:
                    _plan_task(dep_task)
            execution_plan.append(tsk)

        _plan_task(target_task)

        return execution_plan


if __name__ == "__main__":
    # Create some tasks with dependencies
    yoga_task = Task("Yoga")
    coffee_task = Task("Coffee")
    toast_task = Task("Toast", [yoga_task, coffee_task])
    brainstorm_task = Task("Brainstorm", [toast_task])
    loo_task = Task("Loo", [coffee_task])

    scheduler = TaskScheduler()
    scheduler.add_task(yoga_task)
    scheduler.add_task(coffee_task)
    scheduler.add_task(toast_task)
    scheduler.add_task(brainstorm_task)
    scheduler.add_task(loo_task)

    # Get execution plan for task D
    plan = scheduler.get_plan(brainstorm_task)
    print("Execution plan for task D:")
    for task in plan:
        print(task)

    # Output should be something like:
    # Execution plan for task D:
    # Yoga
    # Coffee
    # Toast
    # Brainstorm
