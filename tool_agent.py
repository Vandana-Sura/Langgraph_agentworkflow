class ToolAgent:
    def __init__(self, lang_graph):
        self.lang_graph = lang_graph

    def solve_task(self, task_id):
        task_info = self.lang_graph.get_task(task_id)
        if task_info:
            # Simulate solving the task using a tool (e.g., language model, API)
            result = f"Solved: {task_info['info']}"
            self.lang_graph.update_task(task_id, 'completed', result)
            return result
        return None

