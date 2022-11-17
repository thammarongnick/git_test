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
    path('Clean_POS',views.Clean_POS),
    path('Product_Transfer_to_WH',views.Product_Transfer_to_WH),
    path('Product_standard_lead_time_Report',views.Product_standard_lead_time_Report),
    path('Item_inventory_data',views.Item_inventory_data),
    path('Clear_Query_Lot',views.Clear_Query_Lot),
    path('Cancel_Lot',views.Cancel_Lot),
    path('Check_Scan_Mat',views.Check_Scan_Mat),
    path('Test_Formula',views.Test_Formula),
    path('Main_menu_Test',views.Main_menu_Test),

    #Project smart scrap
    path('MAIN_MENU',views.MAIN_MENU),
    path('Waste_group_master_list',views.Waste_group_master_list),
    path('Waste_item_master_list',views.Waste_item_master_list),
    path('Waste_item_prices_list',views.Waste_item_prices_list),
    path('Upload_database',views.Upload_database),


    # Smart scrap control
        # Go to Page1
    path('go_html_record_weight',views.go_html_record_weight),

    # Function for page1
    path('proj7_read_database_product',views.proj7_read_database_product),
    path('proj_page1_delete_waste_item_master',views.proj_page1_delete_waste_item_master),
]

