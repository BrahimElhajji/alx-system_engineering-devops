#!/usr/bin/python3
"""Exporting an information for a given employee ID to JSON format."""
import json
import requests
import sys


def get_team_member_task_list(team_member_id):
    api_url = "https://jsonplaceholder.typicode.com/"
    team_member_data = requests.get(api_url + "users/{}".format(
        team_member_id)).json()
    task_list = requests.get(
            api_url + "todos", params={"userId": team_member_id}).json()

    with open('{}.json'.format(team_member_id), 'w') as jsonfile:
        json_data = {str(team_member_id): []}
        for task in task_list:
            json_data[str(team_member_id)].append({
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": team_member_data.get("username")
            })
        json.dump(json_data, jsonfile)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 2-export_to_JSON.py <team_member_id>")
        sys.exit(1)

    team_member_id = int(sys.argv[1])
    get_team_member_task_list(team_member_id)
