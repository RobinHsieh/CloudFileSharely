# Update cells
up_color.update_cells_color(
    0, 23, 0.8, 0.8, 0.8, 
    f_i.L4_SPREADSHEET_ID, 
    f_i.SHEET_NAME_list[0])
up_color.update_cells_color(
    0, 23, 0.8, 0.8, 0.8, 
    f_i.L5_SPREADSHEET_ID, 
    f_i.SHEET_NAME_list[1])
up_color.update_cells_color(
    0, 23, 0.8, 0.8, 0.8, 
    f_i.L10_SPREADSHEET_ID, 
    f_i.SHEET_NAME_list[2])
up_color.update_cells_color(
    0, 23, 0.8, 0.8, 0.8, 
    f_i.L11_SPREADSHEET_ID, 
    f_i.SHEET_NAME_list[3])
up_color.update_cells_color(
    0, 23, 0.8, 0.8, 0.8, 
    f_i.L13_SPREADSHEET_ID, 
    f_i.SHEET_NAME_list[4])
up_color.update_cells_color(
    0, 23, 0.8, 0.8, 0.8, 
    f_i.L14_SPREADSHEET_ID, 
    f_i.SHEET_NAME_list[5])

handle_csv.send_mail(data_L4, f_i.L4_video_id_dic, f_i.L4_SPREADSHEET_ID, f_i.SHEET_NAME_list[0])
print("@.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o<|")
handle_csv.send_mail(data_L5, f_i.L5_video_id_dic, f_i.L5_SPREADSHEET_ID, f_i.SHEET_NAME_list[1])
print("@.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o<|")
handle_csv.send_mail(data_L10, f_i.L10_video_id_dic, f_i.L10_SPREADSHEET_ID, f_i.SHEET_NAME_list[2])
print("@.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o<|")
handle_csv.send_mail(data_L11, f_i.L11_video_id_dic, f_i.L11_SPREADSHEET_ID, f_i.SHEET_NAME_list[3])
print("@.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o<|")
handle_csv.send_mail(data_L13, f_i.L13_video_id_dic, f_i.L13_SPREADSHEET_ID, f_i.SHEET_NAME_list[4])
print("@.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o<|")
handle_csv.send_mail(data_L14, f_i.L14_video_id_dic, f_i.L14_SPREADSHEET_ID, f_i.SHEET_NAME_list[5])
print("~End~====================================================================================================")