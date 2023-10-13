import PySimpleGUI as sg
from pytube import YouTube

# Função para baixar o vídeo
def download_video(url, download_path):
    try:
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download(output_path=download_path)
        sg.popup("Download concluído!")
    except Exception as e:
        sg.popup_error(f"Erro: {str(e)}")

# Defina o layout da janela
layout = [
    [sg.Text("URL do vídeo do YouTube:")],
    [sg.InputText(key='url')],
    [sg.Text("Diretório de download:")],
    [sg.InputText(key='download_path'), sg.FolderBrowse()],
    [sg.Button("Baixar"), sg.Button("Sair")],
]

# Crie a janela
window = sg.Window("Downloader de Vídeo do YouTube", layout)

# Loop para capturar eventos da interface gráfica
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Sair":
        break
    elif event == "Baixar":
        url = values['url']
        download_path = values['download_path']
        if url and download_path:
            download_video(url, download_path)

# Feche a janela
window.close()
