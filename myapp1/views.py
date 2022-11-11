from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Waste_item_master_list
import pandas as pd
from .proj7_functions import save_waste_item_master_list
import json
from json import dumps


# Create your views here.
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

def project_1(request):
    return render(request,'Basic_HTML/PROJECT_1.html')

def project_2(request):
    return render(request,'Basic_HTML/PROJECT_2.html')

def project_3(request):
    return render(request,'Basic_HTML/PROJECT_3.html')

def project_4(request):
    return render(request,'Basic_HTML/PROJECT_4.html')

def project_5(request):
    return render(request,'Basic_HTML/PROJECT_5.html')

def project_6(request):
    return render(request,'Basic_HTML/PROJECT_6.html')

def project_7(request):
    return render(request,'Basic_HTML/PROJECT_7.html')

def project_8(request):
    return render(request,'Basic_HTML/PROJECT_8.html')

def project_modal(request):
    return render(request,'Basic_HTML/HTML_MODAl.html')

#Test Project P'Tukta

#Project Scrap Control

def go_html_record_weight(request):
    return  render(request,'proj7_scrap_control/proj7_page1_record_weight.html')

@csrf_exempt
def proj7_read_database_product(request):
    btn_name_sv = request.POST['btn_name']
    month_salary = int(request.POST['salary'])
    print("Test request server : " , btn_name_sv)

    #net_salary_years = 12 * month_salary
    #print(net_salary_years)

    #Read Excel
    df_excel = pd.read_excel(r"C:\django_Project\project_smartfactory\static\upload\waste item master list.xlsx")
    print(df_excel)

    # Read database from dBeaver and Print show
    db_item_master = pd.DataFrame(list(Waste_item_master_list.objects.all().values()))
    print(db_item_master)

    #Save data from excel to Database เรียนกใช้ Functions
    save_waste_item_master_list(df_excel)

    #convert to Json
    json_records = df_excel.reset_index().to_json(orient='records')
    data_loads = json.loads(json_records)

    
    ajax_proj7_read_database_waste_item = dumps(data_loads)
    return HttpResponse(ajax_proj7_read_database_waste_item)


