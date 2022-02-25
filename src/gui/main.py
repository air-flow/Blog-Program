import os
import glob
import PySimpleGUI as sg
import pprint
import inspect
import sys
import shutil
import pyperclip
sg.theme('DarkAmber')


def cd():
    os.chdir(os.path.dirname(__file__))


cd()
sys.path.append(os.path.abspath(".."))
from tag import div
# div.test()


def ElementSetUp():
    temp = GetFileBlogList()
    exec_file_list = list(map(lambda l: l.split("\\")[-1], temp))
    # pprint.pprint(dict(zip(exec_file_list, temp)))
    exec_file_dict = dict(zip(exec_file_list, temp))
    AfterExecutionFilePath = CreatedFileCdPathList()
    layout = [[sg.Text('タグ追加プログラム')],
              #   [sg.Text('Enter something on Row 2'), sg.InputText()],
              [sg.Text('実行ファイル選択'), sg.Combo(
                  exec_file_list, default_value=exec_file_list[0])],
              [sg.Text('実行後ファイル移動先path選択'), sg.Combo(
                  AfterExecutionFilePath, default_value=AfterExecutionFilePath[0])],
              [sg.Checkbox('クリップボードにコピー', default=True)],
              [sg.Button('Exec'), sg.Button('Cancel')],
              ]
    return layout, exec_file_dict


def GetFileReadText():
    with open("../../mine/pathfile.txt", encoding="utf-8") as target:
        text = target.readline()
    return text


def GetFileBlogList(path=""):
    path = GetFileReadText()
    max_value = 10
    blog_files = []
    blog_files += glob.glob(path + "/*.md")
    blog_files += glob.glob(path + "/9_Doing/*/*")
    blog_files = sorted(
        blog_files, key=lambda f: os.stat(f).st_mtime, reverse=True)
    return blog_files[:max_value]


def CreatedFileCdPathList(path=""):
    path = GetFileReadText()
    path = path + "\\0_created"
    created_path = [path]
    created_path += glob.glob(path + "/*")
    created_path = [i for i in created_path if "md" not in i]
    created_path.append(False)
    return created_path


def TagAdd(file_name):
    result = div.main(file_name)
    if result == "end":
        return True
    return False


def FileChangeDirectory(file_name, cd_path):
    new_path = shutil.move(file_name, cd_path)
    return new_path


def ClipCopyBlogText(file_path):
    try:
        with open(file_path, encoding="utf-8") as target:
            text = target.read()
        pyperclip.copy(text)
    except Exception as Expe:
        return False
    return True


def main():
    layout, exec_file_dict = ElementSetUp()
    window = sg.Window('タグ追加プログラム', layout)
    while True:
        event, values = window.read()
        result_flag = False
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        if event == "Exec":
            tag_file_name = values[0]
            result_flag = TagAdd(exec_file_dict[tag_file_name])
        if result_flag and values[1] != 0:
            result_flag = FileChangeDirectory(
                exec_file_dict[tag_file_name], values[1])
        if result_flag and values[2] != 0:
            ClipCopyBlogText(result_flag)
            break

    window.close()


if __name__ == "__main__":
    main()
    # cd()
    # ElementSetUp()
    # CreatedFileCdPathList()
    # GetFileBlogList()
    # print(GetFileBlogList(path=GetFileReadText()))
