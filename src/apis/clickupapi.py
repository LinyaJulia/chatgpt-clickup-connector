# These should contain the clickup routes
# There shouldn't be that much of them

from configs import ClickUpConfig
from apis import app, root_api_url
import requests
import pandas as pd
from flask import jsonify


def parse_response(response):
    name = response['name']

    custom_field_val = "No value"
    custom_fields = response['custom_fields']

    for custom_field in custom_fields:
        if custom_field['name'] == "E-MAIL" and 'value' in custom_field:
            custom_field_val = custom_field['value']
            break

    return pd.Series([name, custom_field_val], index=['name', 'sample_custom_field_value'])


# GET KPIS
# This endpoint will return a string in csv format of the kpis and their corresponding values
@app.route(root_api_url + "clickup/getkpis/<list_id>")
def getKpis(list_id):
    url = f"https://api.clickup.com/api/v2/list/{list_id}/task"

    query = {
        "archived": "false",
        "include_markdown_description": "true",
        "page": "0",
        "order_by": "string",
        "reverse": "true",
        "subtasks": "true",
        "statuses": "string",
        "include_closed": "true",
        "assignees": "string",
        "tags": "string",
        "due_date_gt": "0",
        "due_date_lt": "0",
        "date_created_gt": "0",
        "date_created_lt": "0",
        "date_updated_gt": "0",
        "date_updated_lt": "0",
        "date_done_gt": "0",
        "date_done_lt": "0",
        "custom_fields": "string",
        "custom_items": "0"
    }

    headers = {"Authorization": ClickUpConfig.api_key}

    # Make sure to pass the query parameters to the requests.get() method
    response = requests.get(url, headers=headers, params=query)
    if response.status_code == 200:
        data = response.json()
        tasks = data.get('tasks', [])

        dataFrame = pd.DataFrame(tasks)
        dataFrame = dataFrame[['name', 'custom_fields']]
        
        parsed_data = dataFrame.apply(parse_response, axis=1)
        csv_string = parsed_data.to_csv(index=False)

        return csv_string, 200, {'Content-Type': 'text/csv'}
    else:
        # Handling errors: returning a JSON error message with the corresponding status code
        return jsonify({"error": "Failed to fetch data from ClickUp API", "status_code": response.status_code}), response.status_code