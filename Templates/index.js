function getBathValue(){
    var uiBath = document.getElementsByName("uiBath");
    for(var i in uiBath)
    {
        if(uiBath[i].checked)
            return parseInt(i)+1;
    }
    return -1;
}

function getBHKValue(){
    var uiBHK = document.getElementsByName('uiBHK');
    for(var i in uiBHK)
    {
        if(uiBHK[i].checked)
        return parseInt(i)+1;
    }
    return -1;
}

function onClickEstimatePrice(){
    console.log("Estimate price button clicked")
    var sqft = document.getElementById('validationCustom01');
    var bhk = getBHKValue();
    var bathrooms = getBathValue();
    var location = document.getElementById('validationCustom04');
    var estprice = document.getElementById('uiEstimatedPrice');

    var url='http://127.0.0.1:5000/predict_home_price';

    $.post(url, {
        total_sqft: parseFloat(sqft.value),
        bhk: bhk,
        bath: bathrooms,
        location: location.value
    }, function(data,status){
        console.log(data.estimated_price);
        if(data.estimated_price<0){
            estprice.innerHTML = "Try higher values";
            console.log("Error");
    }
        else{
            estprice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
        }
    }
    );
}


function onPageload(){
    console.log(" document loaded ")

    var url = `http://127.0.0.1:5000/get_location`;
    $.get(url, function(data, status){
        console.log("got response for get_location request");
        if(data){
            var locations = data.locations;
            var validationCustom04 = document.getElementById('validationCustom04');
            //$('#validationCustom04').empty();
            for (var i in locations){
                var opt = new Option(locations[i]);
                //console.log(opt)
                $('#validationCustom04').append(opt);
            }
        }
    });
}
window.onload = onPageload;