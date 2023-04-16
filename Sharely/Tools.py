from Sharely import download_file, handle_csv, Tools
import pandas
import Sharely.update_cell_color as up_color
import Sharely.files_information as f_i

def sendMailAction(data, video_id_dic, SPREADSHEET_ID, SHEET_NAME_list,) -> None:

    handle_csv.send_mail(data, video_id_dic, SPREADSHEET_ID, SHEET_NAME_list)

def updateCellsColorAction(SPREADSHEET_ID, SHEET_NAME_list,) -> None:

    up_color.update_cells_color(
        0, 23, 0.8, 0.8, 0.8, 
        SPREADSHEET_ID, 
        SHEET_NAME_list,
    )