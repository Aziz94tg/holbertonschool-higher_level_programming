import os

def generate_invitations(template, attendees):
    
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return

    
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return

    e
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    
    if not attendees:
        print("No data provided, no output files generated.")
        return

    
    for index, attendee in enumerate(attendees, start=1):
        
        invitation = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            invitation = invitation.replace(f"{{{key}}}", str(value))

        
        filename = f"output_{index}.txt"
        with open(filename, 'w') as file:
            file.write(invitation)
