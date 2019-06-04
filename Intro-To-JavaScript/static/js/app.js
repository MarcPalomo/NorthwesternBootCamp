// from data.js
var tableData = data;

// YOUR CODE HERE!
var tbody = d3.select("tbody");

// On load include all table data
tableData.forEach((UFOSighting) => {
     var row = tbody.append("tr");
     Object.entries(UFOSighting).forEach(([key, value]) => {
         var cell = row.append("td");
         cell.text(value);
     });
});

// Select the submit button
var submit = d3.select("#filter-btn");

submit.on("click", function() {

    // Prevent the page from refreshing
    d3.event.preventDefault();

    // Select the input element and get the raw HTML node
    var inputElement = d3.select("#datetime");
    var inputState = d3.select("#state");

    // Get the value property of the input element
    var inputValue = inputElement.property("value");
    var inputVState = inputState.property("value");

    console.log(inputValue);
    console.log(inputVState);

    // Remove all the previous table data
    var currentRow = d3.select("tbody").selectAll("tr");
    currentRow.remove();

    // Populate all the new table data
    if (inputValue === "" && inputVState ===""){
        console.log("no data entered");
    }
    
    if (inputValue != ''){
    
        var filteredData = tableData.filter(Sighting => Sighting.datetime === inputValue);

        if (inputVState != '') {
            var filteredData = filteredData.filter(state => state.state === inputVState);
        };
        console.log(filteredData);
        filteredData.forEach((UFOSighting) => {
            row = tbody.append("tr");
            Object.entries(UFOSighting).forEach(([key, value]) => {
                cell = row.append("td");
                cell.text(value);
            });
        });
    }
        else if (inputVState !=''){
            filteredData = tableData.filter(state => state.state === inputVState);
            console.log(filteredData);
            filteredData.forEach((UFOSighting) => {
                row = tbody.append("tr");
                Object.entries(UFOSighting).forEach(([key, value]) => {
                    cell = row.append("td");
                    cell.text(value);
                });
            });
        }

    // Clear the input value
    document.getElementById("datetime").value = "";
    document.getElementById("state").value = "";
    
});