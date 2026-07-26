#!/usr/bin/python3
"""Module for generating invitation files from a template."""


def generate_invitations(template, attendees):
    """Generate invitation files for each attendee using a template."""
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(
            isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    if template == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for i, attendee in enumerate(attendees, start=1):
        content = template
        for key in ("name", "event_title", "event_date", "event_location"):
            value = attendee.get(key, "N/A")
            if value is None:
                value = "N/A"
            content = content.replace("{" + key + "}", str(value))

        filename = f"output_{i}.txt"
        with open(filename, "w") as f:
            f.write(content)
