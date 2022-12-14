from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Waste_item_master_list
import pandas as pd
from .proj7_functions import save_waste_item_master_list , update_waste_item_master_list
import json
from json import dumps


# Create your views here.
# เรียน Html
def go_index(request):
    return render(request,'index.html')

def go_form1(request):
    return render(request,'Basic_HTML/HTML_0_from_1.html')

def go_class(request):
    return render(request,'Basic_HTML/HTML_CLASS.html')

def go_symbol(request):
    return render(request,'Basic_HTML/HTML_Symbol.html')

def go_Absolute(request):
    return render(request,'Basic_HTML/HTML_Absolute.html')

def go_border(request):
    return render(request,'Basic_HTML/HTML_ฺBorder_.html')

def go_box_inline(request):
    return render(request,'Basic_HTML/HTML_ฺฺBox_inline.html')

def go_font_color(request):
    return render(request,'Basic_HTML/HTML_ฺฺFont&Color_.html')

def go_universal(request):
    return render(request,'Basic_HTML/HTML_ฺUniversal.html')

def go_Width_Height(request):
    return render(request,'Basic_HTML/HTML_ฺWidth_Height.html')

def project_modal(request):
    return render(request,'Basic_HTML/HTML_MODAl.html')

def BLOCK_INLINE(request):
    return render(request,'Basic_HTML/HTML_BLOCK_INLINE.html')

def POSITION(request):
    return render(request,'Basic_HTML/HTML_POSITION.html')

def Over_flow(request):
    return render(request,'Basic_HTML/HTML_Overflow.html')

def Box_window(request):
    return render(request,'Basic_HTML/HTML_box_windows.html')

def Flex_block(request):
    return render(request,'Basic_HTML/HTML_Flex_block.html')

def over_flow(request):
    return render(request,'Basic_HTML/HTML_Overflow.html')

def responsive_web(request):
    return render(request,'Basic_HTML/HTML_Responsiveweb.html')


#Project P'Tukta
def Clean_POS(request):
    return render(request,'Basic_HTML/PROJECT_Clean_POS.html')

def Product_Transfer_to_WH(request):
    return render(request,'Basic_HTML/Product_Transfer_to_WH.html')

def Product_standard_lead_time_Report(request):
    return render(request,'Basic_HTML/Product_standard_lead_time_Report.html')

def Item_inventory_data(request):
    return render(request,'Basic_HTML/Item_inventory_data.html')

def Clear_Query_Lot(request):
    return render(request,'Basic_HTML/Clear_Query_Lot.html')

def Cancel_Lot(request):
    return render(request,'Basic_HTML/Cancel_Lot.html')

def Check_Scan_Mat(request):
    return render(request,'Basic_HTML/Check_Scan_Mat.html')

def Test_Formula(request):
    return render(request,'Basic_HTML/Test_Formula.html')

def Main_menu_Test(request):
    return render(request,'Basic_HTML/Main_menu_Test.html')
#Test Project P'Tukta

#Project Scrap Control font N
def MAIN_MENU(request):
    return render(request,'PROJECT_SMART_SCRAP/MAIN_MENU.HTML')

def Waste_group_master_list(request):
    return render(request,'PROJECT_SMART_SCRAP/Waste_group_master_list.html')

def Waste_item_master_list(request):
    return render(request,'PROJECT_SMART_SCRAP/Waste_item_master_list.html')

def Waste_item_prices_list(request):
    return render(request,'PROJECT_SMART_SCRAP/Waste_item_prices_list.html')

def Upload_database(request):
    return render(request,'PROJECT_SMART_SCRAP/Upload_database_smart_scrap.html')

def Smart_scrap_management(request):
    return render(request,'PROJECT_SMART_SCRAP/Smart_scrap_management.html')

#Project Scrap Control
def go_html_record_weight(request):
    return  render(request,'proj7_scrap_control/proj7_page1_record_weight.html')

@csrf_exempt
def proj7_read_database_product(request):
    # btn_name_sv = request.POST['btn_name']
    # month_salary = int(request.POST['salary'])
    # print("Test request server : " , btn_name_sv)
    

    df_excel = pd.read_excel(r"C:\django_Project\project_smartfactory\static\upload\waste item master list.xlsx")
    db_item_master = pd.DataFrame(list(Waste_item_master_list.objects.all().values()))

    check_db = Waste_item_master_list.objects.all().exists() #จะได้ค่า true/false เท่านั้น
    print("Check database" , check_db)
    if check_db == False:
        save_waste_item_master_list(df_excel)
        
        db_item_master = pd.DataFrame(list(Waste_item_master_list.objects.all().values()))
        json_records = db_item_master.reset_index().to_json(orient='records')
        data_loads = json.loads(json_records)
        ajax_proj7_read_database_waste_item = dumps(data_loads)
        return HttpResponse(ajax_proj7_read_database_waste_item)

    else:
        db_item_master = pd.DataFrame(list(Waste_item_master_list.objects.all().values()))
        db_item_master["exists_data"] = "YES"
        print(db_item_master.columns)
        
        df_merge_data = pd.merge(df_excel,db_item_master,how="left",on=["waste_item_code"])
        print(df_merge_data.columns)
        df_merge_data.fillna("NO",inplace=True) #แทนค่าจาก Nan > NO
        print(df_merge_data[["waste_item_code" , "exists_data"]])
        df_merge_data_save = df_merge_data[df_merge_data['exists_data']=="NO"] #Data ที่มีการเพิ่มเข้ามาใหม่
        df_merge_data_update = df_merge_data[df_merge_data['exists_data']=="YES"] #Data ที่มีอยู่แล้ว และมีการ Update
        print(df_merge_data_save)
        if len(df_merge_data_save) > 0 :
            #เปลี่ยนชื่อ Field ที่ทำการ Merge ไว้ ให้กลับมาเป็นชื่อเดิม
            df_merge_data_save.rename({"description_EN_x":"description_EN" , "description_TH_x":"description_TH" , "waste_group_code_x":"waste_group_code" , "waste_unit_x":"waste_unit" },axis=1 , inplace=True)
            save_waste_item_master_list(df_merge_data_save)
            
            db_item_master = pd.DataFrame(list(Waste_item_master_list.objects.all().values()))
            json_records = db_item_master.reset_index().to_json(orient='records')
            data_loads = json.loads(json_records)
            ajax_proj7_read_database_waste_item = dumps(data_loads)
            return HttpResponse(ajax_proj7_read_database_waste_item)
            # print("df_merge_data_save")
        if len(df_merge_data_update) > 0 :
            print(df_merge_data_update.columns)
            update_waste_item_master_list(df_merge_data_update)
            #convert to Json
            db_item_master = pd.DataFrame(list(Waste_item_master_list.objects.all().values()))
            json_records = db_item_master.reset_index().to_json(orient='records')
            data_loads = json.loads(json_records)
            ajax_proj7_read_database_waste_item = dumps(data_loads)
            return HttpResponse(ajax_proj7_read_database_waste_item)


@csrf_exempt
def proj_page1_delete_waste_item_master(request):
    waste_item_delete = request.POST['item_delete']
    print("Item delete :" , waste_item_delete)
    Waste_item_master_list.objects.filter(waste_item_code=waste_item_delete).delete()

    db_item_master = pd.DataFrame(list(Waste_item_master_list.objects.all().values()))
    json_records = db_item_master.reset_index().to_json(orient='records')
    data_loads = json.loads(json_records)
    ajax_proj_page1_delete_waste_item_master = dumps(data_loads)
    return HttpResponse(ajax_proj_page1_delete_waste_item_master)


