import os
import re


def BeforeDivProgram(parameter_list):
    print("before")


def TextReadPath():
    result_path = ""
    with open("../mine/path.txt") as target:
        result_path = target.readline()

    return result_path


def cd():
    os.chdir(os.path.dirname(__file__))


class Tag():
    tag_list = [
        {"```": '<div class="code-title" data-title="{0}">\n'},
        {"```": '"</div>\n"'}
    ]

    def __init__(self, test):
        self.test = test


def test():
    s = '"""sql'
    m = re.search(r'^("){3}', s)
    print(m)


if __name__ == "__main__":
    # TODO tag add function
    cd()
    # print(TextReadPath())
    test()
