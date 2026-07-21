""""
Given two database objects, return the second object with any missing properties from the first filled in.

Fields that already exist in the record should not be overwritten.

Tests:
Waiting:1. migrate_record({ "username": "", "posts": 0 }, { "verified": True }) should return { "username": "", "posts": 0, "verified": True }.
Waiting:2. migrate_record({ "username": "", "posts": 0 }, { "username": "camper", "posts": 5 }) should return { "username": "camper", "posts": 5 }.
Waiting:3. migrate_record({ "username": "", "posts": 0, "verified": False }, { "username": "camper" }) should return { "username": "camper", "posts": 0, "verified": False }.
Waiting:4. migrate_record({ "username": "", "posts": 0 }, { "username": "camper", "role": "admin" }) should return { "username": "camper", "role": "admin", "posts": 0 }.
Waiting:5. migrate_record({ "username": "", "email": "", "posts": 0, "verified": False, "role": "user", "banned": False }, { "username": "camper", "email": "camper@freecodecamp.org", "role": "admin" }) should return { "username": "camper", "email": "camper@freecodecamp.org", "role": "admin", "posts": 0, "verified": False, "banned": False }.
"""""

def migrate_record(schema, record):


 return {**schema, **record}

print(migrate_record({ "username": "", "email": "", "posts": 0, "verified": False, "role": "user", "banned": False }, { "username": "camper", "email": "camper@freecodecamp.org", "role": "admin" }))
print(migrate_record({ "username": "", "posts": 0 }, { "verified": True }))
print(migrate_record({ "username": "", "posts": 0 }, { "username": "camper", "posts": 5 }))
print(migrate_record({ "username": "", "posts": 0, "verified": False }, { "username": "camper" }))
print(migrate_record({ "username": "", "posts": 0 }, { "username": "camper", "role": "admin" }))