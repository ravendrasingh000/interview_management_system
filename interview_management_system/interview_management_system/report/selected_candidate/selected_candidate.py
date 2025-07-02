# Copyright (c) 2025, Ravin and contributors
# For license information, please see license.txt



import frappe

def execute(filters=None):
    columns = [
        {
            "label": "Name",
            "fieldname": "name",
            "fieldtype": "Link",
            "options": "Interview",
            "width": 200
        },
        {
            "label": "Job Position",
            "fieldname": "job_position",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": "Current Status",
            "fieldname": "status",
            "fieldtype": "Data",
            "width": 150
        }
    ]

    data = frappe.get_all("Interview", fields=["name", "job_position", "status"])
    

	# ..................................Chart......................................

    status_count = {}

    for row in data:
        status = row.get("status")
        if status in status_count:
            status_count[status] += 1
        else:
            status_count[status] = 1

    chart = {
        "data": {
            "labels": list(status_count.keys()),
            "datasets": [
                {
                    "name": "Interview Status",
                    "values": list(status_count.values())
                }
            ]
        },
        "type": "pie",
        "colors": ["#FF6384", "#36A2EB", "#FFCE56", "#4BC0C0", "#9966FF"]
    }
    
	# ..............................................................................

    return columns, data, "This Is My Report", chart
