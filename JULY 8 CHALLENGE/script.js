// Issue Triage

// Given a number of milliseconds since the last post on an issue, and the last message posted on the issue, determine what you should do with the issue according to these rules:

// If the last message is less than 7 days ago, return "leave it"
// If the last message is 7 or more days ago and its content contains "bump" (case-insensitive), return "close it"
// Otherwise, return "bump it"

function triageIssue(ms, message) {
    // Convert milliseconds to days
    const daysSinceLastPost = ms / (1000 * 60 * 60 * 24);

    // Check the conditions based on the rules provided
    if (daysSinceLastPost < 7) {
        return "leave it";
    } else if (daysSinceLastPost >= 7 && message.toLowerCase().includes("bump")) {
        return "close it";
    } else {
        return "bump it";
    }
}

console.log(triageIssue(86400000, "Lets fix it"));  // Expected: "leave it"
console.log(triageIssue(1209600000, "still waiting"));  // Expected: "bump it"
console.log(triageIssue(864000000, "bump"));  // Expected: "close it"
console.log(triageIssue(604800000, "Do we still want this?"));  // Expected: "bump it"
console.log(triageIssue(604800000, "Bumping this"));  // Expected: "close it"
console.log(triageIssue(345600000, "I'll make a PR"));  // Expected: "leave it"