import os


def BeforeDivProgram(parameter_list):
    print("before")


def TextReadPath():
    result_path = ""
    with open("../mine/path.txt") as target:
        result_path = target.readline()

    return result_path


def cd():
    os.chdir(os.path.dirname(__file__))


if __name__ == "__main__":
    # TODO tag add function
    cd()
    print(TextReadPath())
