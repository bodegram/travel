// Function to add a new row to the flight table
function addRow() {
    var table = document.getElementById("flightTable").getElementsByTagName('tbody')[0];
    var newRow = table.insertRow(table.rows.length);
    var cells = [];

    for (var i = 0; i < 7; i++) {
        cells[i] = newRow.insertCell(i);
        cells[i].innerHTML = '<input type="text" name="flightRow' + (table.rows.length - 1) + '_' + i + '" required>';
    }

    cells[7] = newRow.insertCell(7);
    cells[7].innerHTML = '<button type="button" onclick="deleteRow(this)">Delete</button>';
}

// Function to delete a row from the flight table
function deleteRow(button) {
    var row = button.parentNode.parentNode;
    row.parentNode.removeChild(row);
}
