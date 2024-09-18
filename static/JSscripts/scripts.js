function getform () {
        $('#Form').load('/getform.html?action=subAddr', function(responseTxt, statusTxt, jqXHR)
            {
                if(statusTxt == 'success'){
                        $('#addForm').modal();
                    }
                    if(statusTxt == 'error'){
                        alert('Error: ' + jqXHR.status + ' ' + jqXHR.statusText);
                    }
                }
        );
    };

function delete( e, dt, node, config )  {
    if (confirm('Are you sure you want to delete this item?')) {
        var id = table.$('tr.selected')[0].id;
        console.log('Delete user id ='+id);
        $("#Form").load("/getform.html?action=delAddr&id="+id, function(responseTxt, statusTxt, jqXHR)
        {
            if(statusTxt == 'success'){
                    $('#addFormdel').submit();
                }
                if(statusTxt == 'error'){
                    alert('Error: ' + jqXHR.status + ' ' + jqXHR.statusText);
                }
        });
    }
}

function tableinit () {
    var table = $('#myTable').DataTable({
    dom: 'Bfrtip',
    buttons: [
        {
            text:      '<i class="fa fa-plus"></i>',
            attr:  {
                title: 'Add item',
                id: 'BtAdd'
                },
            titleAttr: 'Add item',
            action: function ( e, dt, node, config ) {
                alert( 'Button activated' );
                }
        },
        {
            text:      '<i class="fa fa-pen"></i>',
            attr:  {
                title: 'Edit item',
                id: 'BtEdit'
                },
            init: function ( dt, node, config ) {
                this.disable();
            },
            action: function ( e, dt, node, config ) {
                alert( 'Button activated' );
            }
        },
        {
            text:      '<i class="fas fa-trash  aria-hidden="true"></i>',
            attr:  {
                title: 'Delete item',
                id: 'BtDelete'
            },

            init: function ( dt, node, config ) {
                this.disable();
            },
            action:    delete

        }
    ],
    pageLength: 25,
    select: true,
    rowId: 'id',
    language: {
        url:"/static/datatables/ru.json"
        },
});
    table.on( 'select deselect', function () {
        var selectedRows = table.rows( { selected: true } ).count();
        table.buttons(['#BtEdit']).enable( selectedRows === 1 );
        table.buttons(['#BtDelete']).enable( selectedRows > 0 );
    });
}

$(tableinit);


