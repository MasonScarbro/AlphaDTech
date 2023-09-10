    // SCRIPT INSIDE THE HTML BACKUP 
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const messageForm = document.querySelector('.message-form');
    const messageInput = document.querySelector('.message-input');
    messageForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const message = messageInput.value.trim()
        console.log('Message:', message)
        if (message.length === 0) {
            return;
        }
    fetch('', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded',
        'X-CSRFToken': csrftoken
        },
        body: new URLSearchParams({
            'csrfmiddlewaretoken': csrftoken,
            'message': message
        })
    })
    .then(response => response.json())
    .then(data => {
        const response = data.response;
        console.log(response);
        const pdbUrl_response = data.pdbUrl_response;
        let success = false
        for (var i = 0; i < pdbUrl_response.length && !success; i++){
            const pdbUrlResponse = data.pdbUrl_response[i];
            const apiUrl = `https://alphafold.com/api/prediction/${pdbUrlResponse}?key=AIzaSyCeurAJz7ZGjPQUtEaerUkBZ3TaBkXrY94`
            fetchD(apiUrl)
                .then(result => {
                    if (result.status >= 200 && result.status <= 299) {
                    success = true; // Set the success flag to true
                    // Handle the successful response here
                    }
                })
                .catch(error => {
                console.error(`Error fetching data for ${pdbUrlResponse}: ${error}`);
                // Handle the error as needed
                });
        }
         // Assuming it's the first element
        

        
    });
});

    async function fetchD(url) {
        const data = await fetch(url);
        const result = await data.json();
        console.log(result[0].pdbUrl);
        return result[0].pdbUrl;
    }
    fetchD('https://alphafold.com/api/prediction/Q9BUP3?key=AIzaSyCeurAJz7ZGjPQUtEaerUkBZ3TaBkXrY94');


   