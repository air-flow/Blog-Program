import PySimpleGUI as sg

sg.theme('DarkAmber')


def ElementSetUp():
    layout = [[sg.Text('Some text on Row 1')],
              [sg.Text('Enter something on Row 2'), sg.InputText()],
              [sg.Combo(['test', 'test2'])],
              [sg.Button('Ok'), sg.Button('Cancel')]
              #   []
              ]
    return layout


def main():
    layout = ElementSetUp()
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        print('You entered ', values[0])

    window.close()


if __name__ == "__main__":
    main()
    ElementSetUp()
