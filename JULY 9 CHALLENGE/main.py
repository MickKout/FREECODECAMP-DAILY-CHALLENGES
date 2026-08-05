"""""
Given an issue title and an array of current labels, return an updated array of labels based on the following rules:

If the issue doesn't have any labels, add:

"bug" and "needs triage" if the title contains "error" or "bug"
"enhancement" and "discussing" if the title contains "feature" or "add"
Otherwise, if the given labels contain:

"needs triage" and the title contains "simple" or "easy", remove "needs triage" and add "good first issue"
"discussing" and the title contains "planned" or "next", remove "discussing" and add "on the roadmap"
Otherwise, if "needs triage" or "discussing" is present, remove it and add "help wanted"
If the title contains:

"security", add a "critical" label
"""

def triage_issue(title, labels):
    updated_labels = labels.copy()

    # Check if there are no labels
    if len(updated_labels) == 0:
        if "error" in title or "bug" in title:
            updated_labels.extend(["bug", "needs triage"])
        elif "feature" in title or "add" in title:
            updated_labels.extend(["enhancement", "discussing"])
    else:
        # Apply rules based on existing labels and title
        if "needs triage" in updated_labels:
            if "simple" in title or "easy" in title:
                updated_labels.remove("needs triage")
                updated_labels.append("good first issue")
            else:
                updated_labels.remove("needs triage")
                updated_labels.append("help wanted")

        if "discussing" in updated_labels:
            if "planned" in title or "next" in title:
                updated_labels.remove("discussing")
                updated_labels.append("on the roadmap")
            else:
                updated_labels.remove("discussing")
                updated_labels.append("help wanted")

    # Check for security-related titles
    if "security" in title:
        updated_labels.append("critical")

    return updated_labels