import gitlab
import random
import string
import time

"""
We are using a gitlab instance for the course.   
This script will create a list of new users 
and push a pre-defined project to each user.
"""

def random_string(l):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(l))

def random_email():
    return "{}.{}@{}.{}".format(
        random_string(5),
        random_string(5),
        random_string(5),
        random_string(5),
    )

# Using delete removes the user before creating a new one.
def create_user(gl, user_dict):
    user_dict["skip_confirmation"] = True
    lst = gl.users.list(search=user_dict["username"])
    user = None 
    if len(lst) != 0:
        user = lst[0]
        print("User {} already exists, deleting...".format(user.name))
        user.delete()
        time.sleep(5)
    
    user = gl.users.create(user_dict)
    print("User {} created.".format(user.name))

    # Create a project.
    gl.projects.import_project(
        open("./exported.tar.gz", 'rb'),
        "hello_php",
        sudo=user.id
    )


if __name__ == "__main__":
    print("Preparing GitLab for the workshop.")

    # You need to log in as a root user to get this token.   
    # When creating the tocken, pick ALL scopes.   
    # This token can burn this gitlab to the groud so be careful.   
    SUDO_TOKEN = "E8ya2wnTnvGgGDomPKpx"
    DEFAULT_PASS = "stegozaver"

    gl = gitlab.Gitlab("http://repo-server-eins.docker.iskratel.mak", SUDO_TOKEN)

    user = {
        "username": "kristjanvoje",
        "password": DEFAULT_PASS,
        "name": "Kristjan Voje",
        "email": random_email(),
    }
    create_user(gl, user)

    with open("users.txt") as f:
        for line in f.read().splitlines():
            spl = line.split(" ")
            username = "{}{}".format(spl[0], spl[1]).lower()
            name = "{} {}".format(spl[0], spl[1])
            email = spl[2]

            user = {
                "username": username,
                "password": DEFAULT_PASS,
                "name": name,
                "email": random_email(),
            }
            create_user(gl, user)
