
class LangGraph:
    def __init__(self):
        self.graph = {}

    def add_task(self, task_id, task_info):
        self.graph[task_id] = {'info': task_info, 'status': 'pending'}

    def update_task(self, task_id, status, feedback=None):
        if task_id in self.graph:
            self.graph[task_id]['status'] = status
            if feedback:
                self.graph[task_id]['feedback'] = feedback

    def get_task(self, task_id):
        return self.graph.get(task_id, None)

    def list_tasks(self):
        return self.graph


