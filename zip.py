import PySimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select file to compress:")
input1 = sg.Input()
choose_buttom1 = sg.FileBrowse("Choose" , key="files")

label2 = sg.Text("Select file to compress:")
input2 = sg.Input()
choose_buttom2 = sg.FolderBrowse("Choose" , key="folder")

compress_buttom = sg.Button("Compress")
ouput_label = sg.Text(key="output", text_color="green")

window = sg.Window("file compressor",
                   layout=[[label1,input1,choose_buttom1],
                           [label2,input2,choose_buttom2],
                           [compress_buttom,ouput_label]])

while True:
    event, values = window.read()
    print(event,values)
    filepath = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepath, folder)
    window["output"].update(value="Compession completed.!")
window.close()
##dddd


