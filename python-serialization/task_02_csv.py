#!/usr/bin/python3

"""
This is task_02_csv module
Contains convert_csv_to_json function
"""

import csv
import json


def convert_csv_to_json(filename):
    """
    convert_csv_to_json function
    Parameters: filename is csv file to read from
    Return: True if sucessful, False if unsuccessful
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = list(csv.DictReader(file))
    except FileNotFoundError:
        return False
    except PermissionError:
        return False
    except Exception:
        return False

    try:
        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)
            return True
    except FileNotFoundError:
        return False
    except PermissionError:
        return False
    except Exception:
        return False
