import unittest

from src.task_summary import summarize_tasks


class TaskSummaryTests(unittest.TestCase):
    def test_counts_and_order(self):
        tasks = [
            {"title": "Inspect pump", "completed": True},
            {"title": "Call supplier", "completed": False},
            {"title": "Update notes", "completed": False},
        ]

        result = summarize_tasks(tasks)

        self.assertEqual(result["total"], 3)
        self.assertEqual(result["completed"], 1)
        self.assertEqual(result["open"], 2)
        self.assertEqual(
            result["titles"],
            ["Inspect pump", "Call supplier", "Update notes"],
        )

    def test_rejects_missing_title(self):
        with self.assertRaises(ValueError):
            summarize_tasks([{"completed": False}])

    def test_rejects_missing_completed(self):
        with self.assertRaises(ValueError):
            summarize_tasks([{"title": "Inspect pump"}])


if __name__ == "__main__":
    unittest.main()
