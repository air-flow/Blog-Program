import os
import PySimpleGUI as sg
sg.theme('DarkAmber')


def cd():
    os.chdir(os.path.dirname(__file__))


def ElementSetUp():
    layout = [[sg.Text('Some text on Row 1')],
              [sg.Text('Enter something on Row 2'), sg.InputText()],
              [sg.Text('実行ファイル選択'), sg.Combo(
                  ['test', 'test2'], default_value="test")],
              [sg.Button('Ok'), sg.Button('Cancel')]
              #   []
              ]
    return layout


def GetFileList():
    cd()
    with open("../../mine/pathfile.txt", encoding="utf-8") as target:
        text = target.readline()
    print(text)


def main():
    layout = ElementSetUp()
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        print('You entered ', values, event)

    window.close()


if __name__ == "__main__":
    # main()
    # ElementSetUp()
    pass
    GetFileList()
