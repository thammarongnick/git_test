from django.shortcuts import render

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

