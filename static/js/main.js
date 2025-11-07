
function ajaxInversed(){
    fetch("/ajax-inversed/")
    .then(response => {
        console.log(response)
    if (!response.ok){
        throw new Error('Network response was not ok'+ response.statusText);
        }
        document.body.style.backgroundColor = "#A9A9A9";
    })
    .catch(error => console.log('Error:', error))
}



