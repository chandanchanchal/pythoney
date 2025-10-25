class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    @classmethod
    def from_email(cls, email):
        if not cls.is_valid_email(email):
            raise ValueError("invalid email")
        username = email.split("@", 1)[0]
        return cls(username, email)

    @staticmethod
    def is_valid_email(email):
        return isinstance(email, str) and "@" in email and "." in email.split("@")[-1]

    def info(self):
        return f"User(username='{self.username}', email='{self.email}')"

def main():
    u1 = User("alice", "alice@example.com")
    u2 = User.from_email("bob@example.org")
    print(User.is_valid_email("bademail"))  # False
    print(u1.info())
    print(u2.info())

if __name__ == "__main__":
    main()
