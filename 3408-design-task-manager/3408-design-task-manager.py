class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.h = []
        self.tasks = {}
        self.removed = set()

        for user, task, p in tasks:
            self.tasks[task] = (user,p)
            self.h.append((-p,-task, user))

        heapq.heapify(self.h)
        

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heappush(self.h, (-priority, -taskId, userId))
        self.tasks[taskId] = (userId, priority)

    def edit(self, taskId: int, newPriority: int) -> None:
        u,p = self.tasks[taskId]
        if p == newPriority:
            return
        self.rmv(taskId)
        self.add(u,taskId,newPriority)

    def rmv(self, taskId: int) -> None:
        u,p = self.tasks[taskId]
        del self.tasks[taskId]
        self.removed.add((p,taskId,u))

    def execTop(self) -> int:
        if not self.h:
            return -1
        p,t,u = heappop(self.h)
        while self.h and (-p,-t,u) in self.removed:
            self.removed.remove((-p,-t,u))
            p,t,u = heappop(self.h)
        if (-p,-t,u) in self.removed:
            return -1
        return u
            


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()