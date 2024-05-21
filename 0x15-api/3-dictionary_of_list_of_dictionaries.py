#!/usr/bin/python3
"""Exporting an information for all employees to JSON format."""
import json
import requests


def get_all_employees_task_list():
    api_url = "https://jsonplaceholder.typicode.com/"
    all_employees_data = requests.get(api_url + "users").json()
    all_tasks_data = requests.get(api_url + "todos").json()

    with open('todo_all_employees.json', 'w') as jsonfile:
        json_data = {}
        for employee in all_employees_data:
            employee_id = employee.get("id")
            employee_username = employee.get("username")
            employee_tasks = [task for task in all_tasks_data if task.get(
                "userId") == employee_id]
            json_data[str(employee_id)] = [
                    {"username": employee_username, "task": task.get(
                        "title"), "completed": task.get(
                            "completed")} for task in employee_tasks]
        json.dump(json_data, jsonfile)


if __name__ == "__main__":
    get_all_employees_task_list()
