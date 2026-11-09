
## Step 4: Create `test_task_manager.py`

"""Basic tests for task_manager.py using unittest."""
import os
import unittest
import json
import task_manager


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        """Use a temporary test file so real tasks.json is untouched."""
        task_manager.TASKS_FILE = "test_tasks.json"
        if os.path.exists(task_manager.TASKS_FILE):
            os.remove(task_manager.TASKS_FILE)

    def tearDown(self):
        if os.path.exists(task_manager.TASKS_FILE):
            os.remove(task_manager.TASKS_FILE)

    def test_load_tasks_empty(self):
        self.assertEqual(task_manager.load_tasks(), [])

    def test_add_task(self):
        task_manager.add_task("Test task")
        tasks = task_manager.load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["description"], "Test task")
        self.assertFalse(tasks[0]["done"])

    def test_complete_task(self):
        task_manager.add_task("Task to complete")
        task_manager.complete_task(1)
        tasks = task_manager.load_tasks()
        self.assertTrue(tasks[0]["done"])

    def test_delete_task(self):
        task_manager.add_task("Task to delete")
        task_manager.delete_task(1)
        self.assertEqual(task_manager.load_tasks(), [])


if __name__ == "__main__":
    unittest.main()