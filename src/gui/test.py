import os
import glob
from tkinter.constants import TRUE
import PySimpleGUI as sg
import pprint
sg.theme('DarkAmber')


def cd():
    os.chdir(os.path.dirname(__file__))


def ElementSetUp():
    temp = GetFileBlogList()
    exec_file_list = list(map(lambda l: l.split("\\")[-1], temp))
    # pprint.pprint(dict(zip(exec_file_list, temp)))
    exec_file_dict = dict(zip(exec_file_list, temp))
    AfterExecutionFilePath = CreatedFileCdPathList()
    layout = [[sg.Text('Some text on Row 1')],
              [sg.Text('Enter something on Row 2'), sg.InputText()],
              [sg.Text('実行ファイル選択'), sg.Combo(
                  exec_file_list, default_value=exec_file_list[0])],
              [sg.Text('実行後ファイル移動先path選択'), sg.Combo(
                  AfterExecutionFilePath, default_value=AfterExecutionFilePath[0])],
              [sg.Checkbox('クリップボードにコピー', default=TRUE)],
              [sg.Button('exec'), sg.Button('Cancel')]
              ]
    return layout


def GetFileReadText():
    cd()
    with open("../../mine/pathfile.txt", encoding="utf-8") as target:
        text = target.readline()
    return text


def GetFileBlogList(path=GetFileReadText()):
    max_value = 2
    main_blog_files = glob.glob(path+"/*.md")
    book_blog_files = glob.glob(path+"/book/*")
    main_blog_files = sorted(
        main_blog_files, key=lambda f: os.stat(f).st_mtime, reverse=True)
    book_blog_files = sorted(
        book_blog_files, key=lambda f: os.stat(f).st_mtime, reverse=True)
    # for file in (main_blog_files[:2]+book_blog_files[:2]):
    #     print(file)
    return (main_blog_files[:max_value]+book_blog_files[:max_value])


def CreatedFileCdPathList(path=GetFileReadText()):
    path = path + "\\created"
    created_path = [path]
    created_path += glob.glob(path+"/*")
    created_path = [i for i in created_path if "md" not in i]
    # files = os.listdir(path+"/created")
    # files_dir = [f for f in files if os.path.isdir(os.path.join(path, f))]
    # pprint.pprint(md)c
    return created_path

def funcname(parameter_list):
    """
    docstring
    """
    pass

def main():
    layout = ElementSetUp()
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        if event == "exec":
            print(event)
        print('You entered ', values, event)

    window.close()


if __name__ == "__main__":
    main()
    # ElementSetUp()
    # CreatedFileCdPathList()
    # GetFileBlogList()
