import PySimpleGUI as sg
from extratorfun import extract_archive


label1 = sg.Text("Select file")
input1 = sg.Input()
choose_buttom1 = sg.FileBrowse("Choose" , key="archive")

label2 = sg.Text("Select fdest dir:")
input2 = sg.Input()
choose_buttom2 = sg.FolderBrowse("Choose" , key="folder")

extract_buttom = sg.Button("Extract")
ouput_label = sg.Text(key="output", text_color="green")

window = sg.Window("Archive Extractor",
                   layout=[[label1,input1,choose_buttom1],
                           [label2,input2,choose_buttom2],
                           [extract_buttom,ouput_label]])

while True:
    event, values = window.read()
    print(event,values)
    archivepath = values['archive']
    dest_dir = values['folder']
    extract_archive(archivepath, dest_dir)
    window["output"].update(value="Extraction Complete")

window.close()