
class PSGSScheduler:
    def __init__(self, max_resources):
        self.max_resources = max_resources
        self.running_tasks = []
        self.waiting_tasks = []

    def can_run(self, task):
        return sum(task.resources) <= self.max_resources

    def schedule_tasks(self):
        while self.waiting_tasks or self.running_tasks:
            while self.waiting_tasks and self.can_run(self.waiting_tasks[0]):
                task = self.waiting_tasks[0]
                heapq.heappush(self.running_tasks, task)
                heapq.heappop(self.waiting_tasks)

            for task in self.running_tasks:
                task.remaining_time -= 1
                task.execute()

            while self.running_tasks and self.running_tasks[0].remaining_time == 0:
                heapq.heappop(self.running_tasks)

    def add_task(self, task):
        heapq.heappush(self.waiting_tasks, task)

    def run(self, tasks):
        for task in tasks:
            self.add_task(task)

        self.schedule_tasks()


if __name__ == '__main__':
    max_resources = 2

    tasks = [
        Task('Task1', 5, [1, 1]),
        Task('Task2', 2, [1, 1]),
        Task('Task3', 1, [1, 2]),
        Task('Task4', 3, [2, 1]),
        Task('Task5', 4, [1, 3]),
        Task('Task6', 2, [2, 2]),
    ]

    scheduler = PSGSScheduler(max_resources)
    scheduler.run(tasks)
if __name__ == '__main__':
    max_resources = 2

    tasks = [
        Task('Task1', 5, [1, 1]),
        Task('Task2', 2, [1, 1]),
        Task('Task3', 1, [1, 2]),
        Task('Task4', 3, [2, 1]),
        Task('Task5', 4, [1, 3]),
        Task('Task6', 2, [2, 2]),
    ]

    scheduler = Scheduler(max_resources)
    scheduler.run(tasks)