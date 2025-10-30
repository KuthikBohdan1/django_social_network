function showMore() {
    var pageCur = Number(document.getElementById("page-cur").value);
    var pageNum = Number(document.getElementById("page-num").value);
    // alert(pageCur)
    pageCur += 1
fetch('?page=' + pageCur, {
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
        document.getElementById("page-cur").value = pageCur;
        if (pageCur == pageNum){
            document.getElementById("show-more").classList.add("disable");
        }
        
        var numPages = document.getElementsByClassName("pagination")[0];
        let ind = 1
        for (let nP of numPages.children){
           if (nP.classList.contains("active")){
            nP.classList.toggle("active");
           }
           if(pageCur == ind){
            nP.classList.add("disabled");
           }
           ind ++;
        }
    })
    .catch(error => console.log('Error:', error));


}

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



    function showGroup(groupId) {
        fetch(`/load-data/?id=${groupId}`)
            .then(response => response.json())
            .then(data => {
                const html = data.message.map(msg => `
                    <div class="alert alert-light" role="alert">
                    <strong>${msg.user_email}</strong>
                    <p>${msg.message}
                    </p>
                    </div>
                    `).join("");
                console.log(html)
                console.log(data)
                document.getElementsByClassName("message-pools")[0].innerHTML = html

            })
            .catch(error => console.error("Помилка:", error));
    }

