import secrets
import string

class linode_secrets_file(object):

    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()

def write_password_to_linode_secrets_file():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(32))
    with linode_secrets_file("/home/jakuta/.secrets/linode_secrets.txt", "w") as secret:
        secret.write(f"PASSWORD = {password} \n")

if __name__ == "__main__":
    write_password_to_linode_secrets_file()
