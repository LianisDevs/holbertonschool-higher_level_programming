#!/usr/bin/python3
import os


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        return {"error": "Template must be a string"}

    if not isinstance(attendees, list):
        return {"error": "Attendees must be a list"}

    if not all(isinstance(i, dict) for i in attendees):
        return {"error": "Attendees must be a list of dictionaries"}

    if not template:
        return {"error": "Template is empty, no output files generated."}

    if not attendees:
        return {"error": "No data provided, no output files generated."}

    counter = 1
    for person in attendees:
        # Grab a copy of the template
        copy_template = template

        # Start replacing each value and make sure it is updating as you go
        copy_template = copy_template.replace(
            "{name}", person["name"] or "N/A")
        copy_template = copy_template.replace(
            "{event_title}", person["event_title"] or "N/A")
        copy_template = copy_template.replace(
            "{event_date}", person["event_date"] or "N/A")
        copy_template = copy_template.replace(
            "{event_location}", person["event_location"] or "N/A")

        # Write to a file
        try:
            file_name = f"output_{counter}.txt"

            exists = os.path.exists(file_name)

            if exists is True:
                raise FileExistsError(
                    "This file already exists: {}".format(file_name))

            with open(file_name, 'w') as f:
                f.write(copy_template)

            counter += 1
        except FileExistsError as e:
            print("Error:", e)
            return {"error": "File already exists"}
