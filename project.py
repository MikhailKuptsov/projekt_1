import PySimpleGUI as sg
layout = [
    [sg.Text('ФАЙЛ :'), sg.InputText(), sg.FileBrowse(),
     ],
    [sg.Text('дорога:'),
     sg.Checkbox('ВСБ'),sg.Checkbox('ГОР'),sg.Checkbox('ДВС'),sg.Checkbox('ЗАБ'),sg.Checkbox('ЗСБ'),
     sg.Checkbox('КБШ'),sg.Checkbox('КЛГ'),sg.Checkbox('КРС'),sg.Checkbox('МСК'),sg.Checkbox('ОКТ'),
     sg.Checkbox('ПРВ'),sg.Checkbox('СРВ'),sg.Checkbox('СЕВ'),sg.Checkbox('СКВ'),sg.Checkbox('ЮВС'),
     sg.Checkbox('ЮУР'),
     ],
    [sg.Text('станция задержки вагонов:'),
     sg.Checkbox('SHA255'),
     ],
    [sg.Text('Группа вопросов:')], 
    [sg.Checkbox('Задержка вагонов в пути следования')],
    [sg.Checkbox('Качество подаваемых под погрузку вагонов')],
    [sg.Checkbox('Качество и своевременность погрузочно-разгрузочных работ на путях общего пользования')],
    [sg.Checkbox('Качество обслуживания в подразделении ОАО РЖД')],
    [sg.Checkbox('Несвоевременная подача / уборка вагонов')],
    [sg.Checkbox("Работоспособность программного обеспечения")],
    [sg.Checkbox("Своевременность приема/выдачи груза оформление перевозочных документов")],
    #[sg.Output(size=(88, 20))],
    [sg.Text('сравнить'), sg.Checkbox("")],
    [sg.Submit(), sg.Cancel()]
]
window = sg.Window('File Compare', layout)   # сохранение всего написанного в layout
while True:                             # The Event Loop
    event, values = window.read()            #чтение запуск граф интерфейса
    # print(event, values) #debug
    if event in (None, 'cd', 'Cancel'):
        break



