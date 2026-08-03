# Given a number of milliseconds since the last post on an issue, and the last message posted on the issue, determine what you should do with the issue according to these rules:

# If the last message is less than 7 days ago, return "leave it"
# If the last message is 7 or more days ago and its content contains "bump" (case-insensitive), return "close it"
# Otherwise, return "bump it"

def triage_issue(ms, message):
    # Convert milliseconds to days
    days_since_last_post = ms / (1000 * 60 * 60 * 24)

    # Check the conditions based on the rules provided
    if days_since_last_post < 7:
        return "leave it"
    elif days_since_last_post >= 7 and "bump" in message.lower():
        return "close it"
    else:
        return "bump it"

print(triage_issue(86400000, "Lets fix it"))  # Expected: "leave it"
print(triage_issue(1209600000, "still waiting"))  # Expected: "bump it"
print(triage_issue(864000000, "bump"))  # Expected: "close it"
print(triage_issue(604800000, "Do we still want this?"))  # Expected: "bump it"
print(triage_issue(604800000, "Bumping this"))  # Expected: "close it"
print(triage_issue(345600000, "I'll make a PR"))  # Expected: "leave it"