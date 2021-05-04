import os

path = "../MySQL監視.md"


def FileRead():
    with open(path, mode="r", encoding="utf-8") as f:
        l = f.readlines()
    return l


def Divappend(l):
    check_flag = 0
    tag_list = ['<div class="code-title" data-title="{0}">\n', "</div>\n"]
    i = 0
    while i < (len(l) - 2):
        if CodeBlock(l[i]) and check_flag == 0:
            add_text = SearchName(l[i])
            l.insert(i, tag_list[check_flag].format(add_text))
            check_flag = 1
            i += 2
        elif CodeBlock(l[i]) and check_flag >= 1:
            l.insert(i + 1, tag_list[check_flag])
            i += 2
            check_flag = 0
        else:
            i += 1
    return l


def CodeBlock(text):
    if text[0:3] == "```":
        return True
    else:
        return False


def SearchName(text):
    if len(text) > 5:
        return text[3:].strip()
    else:
        return "text"


def FileWrite(l):
    with open(path, mode="w", encoding="utf-8") as f:
        f.writelines(l)
    print("END")


def insertTest():
    with open("./python/index.md", mode="r", encoding="utf-8") as f:
        l = f.readlines()
        # l.insert(0, 'TEST\n')
        print(l)


def cd():
    os.chdir(os.path.dirname(__file__))


def main():
    cd()
    l = FileRead()
    l = Divappend(l)
    FileWrite(l)


def test():
    print("test div function")


if __name__ == "__main__":
    main()
    # temp = ["1","2"]
    # l = list(map(str,list(range(0,10))))
    # l.insert(3,"test")
    # print(l)
    # with open("./python/index.md",mode="w",encoding="utf-8") as f:
    #     f.writelines(l)
    # print(SearchName("```"))
