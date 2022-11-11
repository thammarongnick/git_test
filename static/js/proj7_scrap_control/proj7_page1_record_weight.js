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
                        '</tr>'
                })
                $('#tb_waste_item_master_list').html(row);
            }
        })
    })
})