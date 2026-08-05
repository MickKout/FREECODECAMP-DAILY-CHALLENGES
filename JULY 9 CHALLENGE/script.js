// Issue Triage 2
// Given an issue title and an array of current labels, return an updated array of labels based on the following rules:

// If the issue doesn't have any labels, add:

// "bug" and "needs triage" if the title contains "error" or "bug"
// "enhancement" and "discussing" if the title contains "feature" or "add"
// Otherwise, if the given labels contain:

// "needs triage" and the title contains "simple" or "easy", remove "needs triage" and add "good first issue"
// "discussing" and the title contains "planned" or "next", remove "discussing" and add "on the roadmap"
// Otherwise, if "needs triage" or "discussing" is present, remove it and add "help wanted"
// If the title contains:

// "security", add a "critical" label
// Tests:
// Waiting:1. triageIssue("app crashes with error", []) should return ["bug", "needs triage"].
// Waiting:2. triageIssue("app crashes with error", ["bug", "needs triage"]) should return ["bug", "help wanted"].
// Waiting:3. triageIssue("add dark mode", []) should return ["enhancement", "discussing"].
// Waiting:4. triageIssue("add dark mode", ["enhancement", "discussing"]) should return ["enhancement", "help wanted"].
// Waiting:5. triageIssue("xss security bug", []) should return ["bug", "needs triage", "critical"].
// Waiting:6. triageIssue("security vulnerability in auth", []) should return ["critical"].
// Waiting:7. triageIssue("easy a11y fix", ["bug", "needs triage"]) should return ["bug", "good first issue"].
// Waiting:8. triageIssue("planned api migration", ["enhancement", "discussing"]) should return ["enhancement", "on the roadmap"].
// Waiting:9. triageIssue("improve security", ["enhancement", "discussing"]) should return ["enhancement", "help wanted", "critical"].

function triageIssue(title, labels) {

  const updatedLabels = [...labels];

  // Check if there are no labels
  if (updatedLabels.length === 0) {
    if (title.includes("error") || title.includes("bug")) {
      updatedLabels.push("bug", "needs triage");
    } else if (title.includes("feature") || title.includes("add")) {
      updatedLabels.push("enhancement", "discussing");
    }
  } else {
    // Apply rules based on existing labels and title
    if (updatedLabels.includes("needs triage")) {
      if (title.includes("simple") || title.includes("easy")) {
        updatedLabels.splice(updatedLabels.indexOf("needs triage"), 1);
        updatedLabels.push("good first issue");
      } else {
        updatedLabels.splice(updatedLabels.indexOf("needs triage"), 1);
        updatedLabels.push("help wanted");
      }
    }

    if (updatedLabels.includes("discussing")) {
      if (title.includes("planned") || title.includes("next")) {
        updatedLabels.splice(updatedLabels.indexOf("discussing"), 1);
        updatedLabels.push("on the roadmap");
      } else {
        updatedLabels.splice(updatedLabels.indexOf("discussing"), 1);
        updatedLabels.push("help wanted");
      }
    }
  }

  // Check for security-related titles
  if (title.includes("security")) {
    updatedLabels.push("critical");
  }

  return updatedLabels;
}