const csrftoken = Cookies.get('csrftoken');
const data = document.currentScript.dataset;
num = data.num;
console.log(num);
const buttonEx = document.getElementById('buttonEx');
$('#buttonEx').on('click', function(e){
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: 'update-num',
        headers: {'X-CSRFToken': csrftoken},
        data: {'num': num},
        success: function(response) {
            num = response.num;
            $('#numValue').text(num);
            console.log(response);
        },
        error: function(error) {
            console.log(error)
            // Handle errors here
        }
    
    });
    });

   