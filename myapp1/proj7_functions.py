from .models import Waste_item_master_list , Company_contact_name_list
from datetime import datetime

#Function save database > save_waste_item_master_list
def save_waste_item_master_list(df_excel):
    datetime_save = datetime.now()
    date_save = datetime_save.date()
    time_save = datetime_save.time()
    datesave = date_save.strftime("%d/%m/%y")
    timesave = time_save.strftime("%H:%M")
    datetimesave = str(datesave) + " " + str(timesave)

    print(df_excel.columns)
    for i in df_excel.itertuples(index=False):
        item_code = i.waste_item_code
        desc_en = i.description_EN
        desc_th = i.description_TH
        group_code = i.waste_group_code
        print(item_code, desc_en, desc_th, group_code)
        db_save = Waste_item_master_list()
        db_save.waste_item_code = item_code
        db_save.description_EN = desc_en
        db_save.description_TH = desc_th
        db_save.waste_group_code = group_code
        db_save.update_date = datetimesave
        db_save.update_by = "Anupab.K"
        db_save.save()
        print("Save completed" , item_code , desc_en , datetimesave)

#Function update database > update_waste_item_master_list
def update_waste_item_master_list(df_update):
    datetime_save = datetime.now()
    date_save = datetime_save.date()
    time_save = datetime_save.time()
    datesave = date_save.strftime("%d/%m/%y")
    timesave = time_save.strftime("%H:%M")
    datetimesave = str(datesave) + " " + str(timesave)

    for i in df_update.itertuples(index=False):
        item_code = i.waste_item_code
        desc_en = i.description_EN_x
        desc_th = i.description_TH_x
        group_code = i.waste_group_code_x
        # print("Test update")
        Waste_item_master_list.objects.filter(waste_item_code=item_code).update(
            description_EN = desc_en,
            description_TH = desc_th,
            waste_group_code = group_code,
            update_date = datetimesave,
            update_by = "Anupab.K"
        )
