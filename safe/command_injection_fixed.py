import subprocess

def execute_command():
    user_argument = input("Enter argument: ")

    subprocess.run(
        ["echo", user_argument],
        shell=False,
        check=True
    )

if __name__ == "__main__":
    execute_command()