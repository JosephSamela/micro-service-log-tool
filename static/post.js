
function submit() {

    var url = location.href
    var data = {
        'source': $('#source').val(),
        'code': $('#code').val(),
        'type': $('#type').val(),
        'description': $('#description').val()
    }

    $.ajax({
        url:url,
        type:"POST",
        data:JSON.stringify(data),
        contentType:"application/json; charset=utf-8",
        dataType:"json",
    })

    $('#message').html('Log submitted! Visit <a href="/search">/search</a> to see the result.')

}

function search() {

    var url = location.href
    var data = $('#query').val()

    r = $.ajax({
            url:url,
            type:"POST",
            data:data,
            success: drawTable
        })

    console.log(r.responseJSON)

}

function drawTable(logs) {
    // Empty table of previous query results
    $('#logs').empty()
    // Append heading row to table
    $('#logs').append(
        `<tr>
            <td><b>ID</b></td>
            <td><b>Timestamp</b></td>
            <td><b>Source</b></td>
            <td><b>Code</b></td>
            <td><b>Type</b></td>
            <td><b>Description</b></td>
        </tr>`
    )
    // Re-generate log table with logs in query result
    $.each(logs, function( index, row ) {
        $.each(logs, function(rowIndex, r) {
            var row = $('<tr/>');
            $.each(r, function(colIndex, c) { 
                row.append($('<td/>').text(c));
            });
            $('#logs').append(row);
        });
       $('#logs').html(table)
    });
}
