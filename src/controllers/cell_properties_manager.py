class CellPropertiesManager:
    """
    A class to manage cell colors in Google Sheets.
    Stateless class.
    """   
    @staticmethod
    def update_cell_properties(red: int, green: int, blue: int):
        """
        Update the cell properties based on the cell color.
        Args:
            red (int): The red value.
            green (int): The green value.
            blue (int): The blue value.
        Returns:
            red (int): The updated red value.
            green (int): The updated green value.
            blue (int): The updated blue value.
            if_view_limit_near (bool): If the view limit is near.
            if_view_limit_reached (bool): If the view limit reached.
        """

        # if cell's color is white
        if (red, green, blue) == (1, 1, 1) or (red, green, blue) == (0, 0, 0):
            red, green, blue = 1, 1, 0
            if_view_limit_near = False
            if_view_limit_reached = False
        
        # if cell's color is yellow
        elif (red, green, blue) == (1, 1, 0):
            red, green, blue = 0, 1, 0
            if_view_limit_near = False
            if_view_limit_reached = False
        
        # if cell's color is green
        elif (red, green, blue) == (0, 1, 0):
            red, green, blue = 0, 1, 1
            if_view_limit_near = True
            if_view_limit_reached = False
        
        # if cell's color is blue
        else:
            if_view_limit_near = False
            if_view_limit_reached = True

        return red, green, blue, if_view_limit_near, if_view_limit_reached


    @staticmethod
    def update_gmail_user_state(column: int, if_view_limit_near: bool, if_view_limit_reached: bool, csv_data, file_ids_dict: dict, shareable_file_id_list: list, offset: int, view_limit_near_dates: str):
        """
        Update the Gmail user state based on the row of cells color.
        Args:
            column (int): The column index of the cell.
            if_view_limit_near (bool): If the view limit is near.
            if_view_limit_reached (bool): If the view limit is reached.
            csv_data (DataFrame): The CSV data.
            file_ids_dict (dict): The mapping of column indices to file IDs for sharing.
            shareable_file_id_list (list): The list of file IDs to share.
            offset (int): The offset for the expiration date.
            view_limit_near_dates (str): The date near view limit.
        Returns:
            shareable_file_id_list (list): The updated list of file IDs to share.
            offset (int): The updated offset for the expiration date.
            view_limit_near_dates (str): The updated date near view limit.
        """

        if not if_view_limit_reached:
            shareable_file_id_list.append(file_ids_dict.get(column))
            offset += 2
            if if_view_limit_near:
                view_limit_near_dates += csv_data.columns[column] + " "

        return shareable_file_id_list, offset, view_limit_near_dates