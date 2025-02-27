# user_auth.py

# Dictionary to store usernames and passwords
users = {
    'user1': 'password1',
    'user2': 'password2',
    'user3': 'password3'
}

def authenticate(username, password):
    """Authenticate the user."""
    if username in users and users[username] == password:
        return True
    else:
        return False

def main():
    """Main function to handle user input and authentication."""
    username = input("Enter username: ")
    password = input("Enter password: ")

    if authenticate(username, password):
        print("Login successful!")
    else:
        print("Invalid username or password.")

if __name__ == "__main__":
    main()
