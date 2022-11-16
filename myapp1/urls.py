from django.urls import path , include
from . import views

urlpatterns = [
    #เรียน Html
    path('index',views.go_index),
    path('go_form1',views.go_form1),
    path('go_class',views.go_class),
    path('go_symbol',views.go_symbol),
    path('go_Absolute',views.go_Absolute),
    path('go_border',views.go_border),
    path('go_box_inline',views.go_box_inline),
    path('go_font_color',views.go_font_color),
    path('go_universal',views.go_universal),
    path('go_Width_Height',views.go_Width_Height),
    path('BLOCK_INLINE',views.BLOCK_INLINE),
    path('POSITION',views.POSITION),
    path('project_modal',views.project_modal),
    path('Over_flow',views.Over_flow),
    path('Box_window',views.Box_window),
    path('Flex_block',views.Flex_block),
    path('over_flow',views.over_flow),
    path('responsive_web',views.responsive_web),

    #Projec P'Tukta
    path('project_1',views.project_1),
    path('project_2',views.project_2),
    path('project_3',views.project_3),
    path('project_4',views.project_4),
    path('project_5',views.project_5),
    path('project_6',views.project_6),
    path('project_7',views.project_7),
    path('project_8',views.project_8),
    path('Men_menu',views.Men_menu),

    #Project smart scrap
    path('project_scrap',views.project_scrap),
    path('project_scrap2',views.project_scrap2),
    path('project_scrap3',views.project_scrap3),
    path('Upload_database',views.Upload_database),


    # Smart scrap control
        # Go to Page1
    path('go_html_record_weight',views.go_html_record_weight),

    # Function for page1
    path('proj7_read_database_product',views.proj7_read_database_product),
    path('proj_page1_delete_waste_item_master',views.proj_page1_delete_waste_item_master),
]

