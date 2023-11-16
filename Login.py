from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('DarkAmber')

layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(20,1))],
    [sg.Text('Senha  '), sg.Input(key='senha',password_char='*', size=(20,1))],
    [sg.Checkbox('Salvar o Login?')],
    [sg.Button('Entrar')]    
]

# Janela
janela = sg.Window('Tela de Login', layout)

# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Rhenan Rose' and valores['senha'] == '123456':
            print('Bem Vindo!')
