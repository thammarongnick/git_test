$(document).ready(function() {
    $("#btn_read_database_product").click(function() {

            let get_btn_name = $('#btn_read_database_product').text();
            alert(get_btn_name)

            $.ajax({
                url: 'proj7_read_database_product', // เรียกใช้ URL
                type: 'post', // ประเภทของการส่งข้อมูล
                data: { // ข้อมูลที่จะถูกส่งไปกับ url
                    'btn_name': get_btn_name,
                    'btn_color': 'Blue',
                    'salary': 16500,
                },
                success: function(ajax_proj7_read_database_waste_item) {
                    console.log(ajax_proj7_read_database_waste_item);

                    let json_txt = JSON.parse(ajax_proj7_read_database_waste_item)
                    console.log(ajax_proj7_read_database_waste_item);
                    let row_no = 0
                    let row
                    $.each(json_txt, function(key, value_db) {
                        row_no += 1;
                        row += '<tr>' +
                            '<td>' + row_no + '</td>' +
                            '<td>' + value_db.waste_item_code + '</td>' +
                            '<td>' + value_db.description_EN + '</td>' +
                            '<td>' + value_db.description_TH + '</td>' +
                            '<td>' + value_db.waste_group_code + '</td>' +
                            '<td>' + value_db.update_date + '</td>' +
                            '<td>' + value_db.update_by + '</td>' +
                            '<td>' + value_db.waste_Unit + '</td>' +
                            '</tr>'
                    })
                    $('#tb_waste_item_master_list').html(row);
                }
            })
        })
        // delete waste item
    $('#btn_delete_item').click(function() {
        let input_item_delete = $('#item_delete').val();
        $.ajax({
            url: 'proj_page1_delete_waste_item_master', // เรียกใช้ URL
            type: 'post', // ประเภทของการส่งข้อมูล
            data: { // ข้อมูลที่จะถูกส่งไปกับ url
                'item_delete': input_item_delete
            },
            success: function(ajax_proj_page1_delete_waste_item_master) {
                console.log(ajax_proj_page1_delete_waste_item_master);
                alert("Delete item " + ajax_proj_page1_delete_waste_item_master + " Completed")
            }
        })
    })
})