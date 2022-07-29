#!/usr/bin/python3
"""
    Python script that adds all args to a Python List.
    List is then saved to a file.
"""
import sys
import json

if __name__ == "__main__":

    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


    try:
        loadFile = load_from_json_file("add_item.json")
    except FileNotFoundError:
        loadFile = []

    for i in range(1, len(sys.argv)):
        loadfile.append(sys.argv[i])

    save_to_json_file(loadFile, "add_item.json")

