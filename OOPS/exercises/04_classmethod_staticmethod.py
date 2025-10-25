"""
Exercise 04 — Instance vs Class vs Static Methods; Factory Methods

Goals:
- Practice when to use @classmethod and @staticmethod
- Create factory constructors
"""

# TODO: Implement class `User` with:
# - __init__(username, email)
# - from_email(cls, email): parse username before '@'
# - is_valid_email(email): very basic check: contains '@' and '.'
# - info(self): "User(username='x', email='y')"
#
# Use @classmethod for from_email and @staticmethod for validation.

def main():
    # u1 = User("alice", "alice@example.com")
    # u2 = User.from_email("bob@example.org")
    # print(User.is_valid_email("bademail"))  # False
    # print(u1.info())
    # print(u2.info())
    pass

if __name__ == "__main__":
    main()
