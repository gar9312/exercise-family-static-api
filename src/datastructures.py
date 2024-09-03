"""
Update this file to implement the following methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        # Example list of members
        self._members = [
            {
                "id": 1,
                "first_name": "John",
                "last_name": last_name,
                "age": 33, 
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": 2,
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35, 
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": 3,
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5, 
                "lucky_numbers": [1]
            },
        ]

    # Read-only: Use this method to generate random member IDs when adding members to the list
    def _generate_id(self):
        return randint(1, 99999999)

    def add_member(self, member):
        member["last_name"] = self.last_name     
        self._members.append(member)        
        return self._members 

    def delete_member(self, member_id):
        for member in self._members:
            if member["id"] == member_id:
                self._members.remove(member)
                return True
        return False

    def get_member(self, member_id):
        for member in self._members:
            if member["id"] == member_id:
                return member
        return None

    # This method is complete; it returns a list of all family members
    def get_all_members(self):
        return self._members

