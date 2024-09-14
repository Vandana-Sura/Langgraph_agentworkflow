class PlanAgent:
    def __init__(self, lang_graph):
        self.lang_graph = lang_graph

    def split_query(self, user_query):
        # Split query into sub-tasks, filtering out empty strings
        sub_tasks = [task.strip() for task in user_query.split('.') if task.strip()]
        for i, task in enumerate(sub_tasks):
            task_id = f'sub_task_{i + 1}'
            self.lang_graph.add_task(task_id, task)

        return sub_tasks
