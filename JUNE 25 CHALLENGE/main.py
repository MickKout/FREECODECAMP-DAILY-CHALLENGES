# Frontmatter Parser

# Given a string representing a frontmatter block, parse it and return an object (JavaScript) or dictionary (Python) with the keys and values.

# Frontmatter is wrapped in --- delimiters and contains key: value pairs within them, one per line. For example:

# ---
# title: My Post
# draft: false
# views: 100
# ---
# Should return:

# {
#   title: "My Post",
#   draft: false,
#   views: 100
# }

# Numbers, Booleans, and Strings should all be returned as their respective type.
# The given string will have new lines separated with the newline character ("\n"). The above example would be given as: "---\ntitle: My Post\ndraft: false\nviews: 100\n---".

# Tests:
# Waiting:1. parse_frontmatter("---\ntitle: My Post\ndraft: false\nviews: 100\n---") should return { title: "My Post", draft: False, views: 100 }.
# Waiting:2. parse_frontmatter("---\nid: 6a174db57256a112f932195c\ntitle: My Book\nlocale: en\nwordCount: 10000\npublished: false\n---") should return { id: "6a174db57256a112f932195c", title: "My Book", locale: "en", wordCount: 10000, published: False }.
# Waiting:3. parse_frontmatter("---\nversion: 1.0.0\nurl: https://example.com\nprivate: true\n---") should return { version: "1.0.0", url: "https://example.com", private: True }.
# Waiting:4. parse_frontmatter("---\nrating: 4.5\nprice: 9.99\n---") should return { rating: 4.5, price: 9.99 }.

def parse_frontmatter(s):
    result = {}
    lines = s.split('\n')

    for line in lines:
        if line.startswith('---'):
            continue          # skip both the opening and closing dashes

        colon_index = line.find(':')

        if colon_index == -1:
            continue

        key = line[:colon_index].strip()
        raw = line[colon_index + 1:].strip()

        # Type conversion
        if raw == 'true':
            result[key] = True
        elif raw == 'false':
            result[key] = False
        elif raw == '':
            continue
        else:
            try:
                result[key] = int(raw)
            except ValueError:
                try:
                    result[key] = float(raw)
                except ValueError:
                    result[key] = raw

    return result
    
print(parse_frontmatter("---\ntitle: My Post\ndraft: false\nviews: 100\n---"))
print(parse_frontmatter("---\nid: 6a174db57256a112f932195c\ntitle: My Book\nlocale: en\nwordCount: 10000\npublished: false\n---"))
print(parse_frontmatter("---\nversion: 1.0.0\nurl: https://example.com\nprivate: true\n---"))
print(parse_frontmatter("---\nrating: 4.5\nprice: 9.99\n---"))