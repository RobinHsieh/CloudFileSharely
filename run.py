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


def main() -> None:

    print("Start----------------------------------------------------------------------------------------------------")
    # Update csv files
    for index, sheet_name in enumerate(f_i.spreadsheet_id_dic):

        download_file.update_file(
            sheet_name, 
            f_i.spreadsheet_id_dic.get(sheet_name), 
            f_i.SHEET_NAME_list[index]
        )

    # Access csv files
    pandas.set_option(
        "display.max_rows", 
        100, 
        "display.max_columns", 
        20, 
    )

    data_L4 = pandas.read_csv(
        filepath_or_buffer=f_i.project_path + "/data/L4.csv", sep=",")
    data_L5 = pandas.read_csv(
        filepath_or_buffer=f_i.project_path + "/data/L5.csv", sep=",")
    data_L10 = pandas.read_csv(
        filepath_or_buffer=f_i.project_path + "/data/L10.csv", sep=",")
    data_L11 = pandas.read_csv(
        filepath_or_buffer=f_i.project_path + "/data/L11.csv", sep=",")
    data_L13 = pandas.read_csv(
        filepath_or_buffer=f_i.project_path + "/data/L13.csv", sep=",")
    data_L14 = pandas.read_csv(
        filepath_or_buffer=f_i.project_path + "/data/L14.csv", sep=",")

    updateCellsColorAction(f_i.L4_SPREADSHEET_ID, f_i.SHEET_NAME_list[0])
    updateCellsColorAction(f_i.L5_SPREADSHEET_ID, f_i.SHEET_NAME_list[1])
    updateCellsColorAction(f_i.L10_SPREADSHEET_ID, f_i.SHEET_NAME_list[2])
    updateCellsColorAction(f_i.L11_SPREADSHEET_ID, f_i.SHEET_NAME_list[3])
    updateCellsColorAction(f_i.L13_SPREADSHEET_ID, f_i.SHEET_NAME_list[4])
    updateCellsColorAction(f_i.L14_SPREADSHEET_ID, f_i.SHEET_NAME_list[5])


    sendMailAction(
        data_L4,
        f_i.L4_video_id_dic,
        f_i.L4_SPREADSHEET_ID,
        f_i.SHEET_NAME_list[0],
    )
    print("@.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o<|")
    sendMailAction(
        data_L5,
        f_i.L5_video_id_dic,
        f_i.L5_SPREADSHEET_ID,
        f_i.SHEET_NAME_list[1],
    )
    print("@.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o<|")
    sendMailAction(
        data_L10,
        f_i.L10_video_id_dic,
        f_i.L10_SPREADSHEET_ID,
        f_i.SHEET_NAME_list[2],
    )
    print("@.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o<|")
    sendMailAction(
        data_L11,
        f_i.L11_video_id_dic,
        f_i.L11_SPREADSHEET_ID,
        f_i.SHEET_NAME_list[3],
    )
    print("@.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o<|")
    sendMailAction(
        data_L13,
        f_i.L13_video_id_dic,
        f_i.L13_SPREADSHEET_ID,
        f_i.SHEET_NAME_list[4],
    )
    print("@.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o<|")
    sendMailAction(
        data_L14,
        f_i.L14_video_id_dic,
        f_i.L14_SPREADSHEET_ID,
        f_i.SHEET_NAME_list[5],
    )
    print("~End~====================================================================================================")


if __name__ == '__main__':

    main()

