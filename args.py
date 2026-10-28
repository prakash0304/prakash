def build_user_profile(username, **kwargs):
    # username is a standard required argument
    # kwargs receives all additional key=value pairs as a dictionary
     profile = {"username": username}
     profile.update(kwargs)
     return profile
    


# Pass required arguments along with optional named attributes:
user1 = build_user_profile("alex99", role="admin", status="active")
user2 = build_user_profile("dev_sam", email="sam@example.com", location="India", theme="dark")

print(user1)
# Output: {'username': 'alex99', 'role': 'admin', 'status': 'active'}

print(user2)
# Output: {'username': 'dev_sam', 'email': 'sam@example.com', 'location': 'India', 'theme': 'dark'}