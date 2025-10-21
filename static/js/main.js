function showMore() {
fetch('?page=2', {
           headers: {
        'X-Requested-With': 'XMLHttpRequest'
    }}
)

    .then(response => {
        console.log(response)
        if (!response.ok) {
            throw new Error('Network response ok ' + response.statusText);

        }
        return response.text()
    })
    .then(data => {
        document.getElementsByClassName("poll-container")[0].innerHTML += data
    })
    .catch(error => console.log('Error:', error));


}