import os

def generate_invitations(template, attendees):
    # Validate template type
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return

    # Validate attendees type
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return

    # Check for empty template
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Check for empty attendee list
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Generate output files
    for index, attendee in enumerate(attendees, start=1):
        # Prepare a filled-in template copy
        invitation = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            invitation = invitation.replace(f"{{{key}}}", str(value))

        # Write to file
        filename = f"output_{index}.txt"
        with open(filename, 'w') as file:
            file.write(invitation)
