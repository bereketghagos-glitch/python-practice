contacts = [
   { "name": "John", "phone": "123456789", "email" : "john@example.com"},
   {"name" : "Jane", "phone": "723647273", "email" : "janeiscute@example.com"},
   {"name" : "Bob", "phone": "987654321", "email" :"bobby@example.com"}
]
for contact in contacts:
    print(contact["name"], contact["phone"])
contacts.append({"name": "alice", "phone": "777777777", "email": "gerbyherby@example.com"})
contacts.remove(contacts[0])
print(len(contacts))

