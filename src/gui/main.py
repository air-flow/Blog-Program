import os
import glob
import PySimpleGUI as sg
import pprint
import inspect
import sys
sg.theme('DarkAmber')


def cd():
    # print(inspect.stack()[1].filename)
    # print(inspect.stack()[1].function)
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
    layout = [[sg.Text('Some text on Row 1')],
              #   [sg.Text('Enter something on Row 2'), sg.InputText()],
              [sg.Text('実行ファイル選択'), sg.Combo(
                  exec_file_list, default_value=exec_file_list[0])],
              [sg.Text('実行後ファイル移動先path選択'), sg.Combo(
                  AfterExecutionFilePath, default_value=AfterExecutionFilePath[0])],
              [sg.Checkbox('クリップボードにコピー', default=True)],
              [sg.Button('exec'), sg.Button('Cancel')]
              #   []
              ]
    return layout, exec_file_dict


def GetFileReadText():
    with open("../../mine/pathfile.txt", encoding="utf-8") as target:
        text = target.readline()
    return text


def GetFileBlogList(path=""):
    path = GetFileReadText()
    max_value = 2
    main_blog_files = glob.glob(path + "/*.md")
    book_blog_files = glob.glob(path + "/book/*")
    main_blog_files = sorted(
        main_blog_files, key=lambda f: os.stat(f).st_mtime, reverse=True)
    book_blog_files = sorted(
        book_blog_files, key=lambda f: os.stat(f).st_mtime, reverse=True)
    # for file in (main_blog_files[:2]+book_blog_files[:2]):
    #     print(file)
    return (main_blog_files[:max_value] + book_blog_files[:max_value])


def CreatedFileCdPathList(path=""):
    path = GetFileReadText()
    path = path + "\\created"
    created_path = [path]
    created_path += glob.glob(path + "/*")
    created_path = [i for i in created_path if "md" not in i]
    # files = os.listdir(path+"/created")
    # files_dir = [f for f in files if os.path.isdir(os.path.join(path, f))]
    # pprint.pprint(md)
    return created_path


def TagAdd(file_name):
    div.main(file_name)
    # print(exec_file_dict[file_name])


def main():
    layout, exec_file_dict = ElementSetUp()
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        if event == "exec":
            tag_file_name = values[0]
            TagAdd(exec_file_dict[tag_file_name])
        print('You entered ', values, event)

    window.close()


if __name__ == "__main__":
    main()
    # cd()
    pass
    # ElementSetUp()
    # CreatedFileCdPathList()
    # GetFileBlogList()
