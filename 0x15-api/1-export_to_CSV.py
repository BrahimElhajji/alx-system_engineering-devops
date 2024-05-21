#!/usr/bin/python3
"""Returns task list information for a
given team member ID and exports to CSV."""
import requests
import sys
import csv


def get_team_member_task_list(team_member_id):
    api_url = "https://jsonplaceholder.typicode.com/"
    team_member_data = requests.get(api_url + "users/{}".format(
        team_member_id)).json()
    task_list = requests.get(
            api_url + "todos", params={"userId": team_member_id}).json()

    completed_tasks = ([task.get("title") for task in task_list if task.get(
        "completed") is True])
    print("Team Member {} has completed tasks({}/{}):".format(
        team_member_data.get("name"), len(completed_tasks), len(task_list)))
    for task in completed_tasks:
        print("\t{}".format(task))

    with open('{}.csv'.format(team_member_id), 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(
                ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in task_list:
            csv_writer.writerow(
                    [team_member_id, team_member_data.get("name"),
                        task.get("completed"), task.get("title")])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 1-export_to_CSV.py <team_member_id>")
        sys.exit(1)

    team_member_id = int(sys.argv[1])
    get_team_member_task_list(team_member_id)
