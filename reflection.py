class Reflection:
    def __init__(self, lang_graph):
        self.lang_graph = lang_graph

    def reflect_on_task(self, task_id):
        task = self.lang_graph.get_task(task_id)
        if task and task['status'] == 'completed':
            feedback = task.get('feedback', 'No feedback available')
            print(f"Feedback for {task_id}: {feedback}")
            # Check if additional refinement is needed
            if "error" in feedback:  # Hypothetical error checking
                self.lang_graph.update_task(task_id, 'refined', "Re-running task")
                return "Re-run required"
            return "Task successful"
        return "Task not completed"