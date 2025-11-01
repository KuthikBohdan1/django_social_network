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
            // .then(response => response.json())
            // .then(data => {
            //     const html = data.message.map(msg => `
            //         <div class="alert alert-light" role="alert">
            //         <strong>${msg.user_email}</strong>
            //         <p>${msg.message}
            //         </p>
            //         </div>
            //         `).join("");
            //     console.log(html)
            //     console.log(data)
            //     document.getElementsByClassName("message-pools")[0].innerHTML = html
            // })

            .then(response => response.json())
            .then(data => {
                console.log(data.result);
                // const html = data.result
                // const html = data.result.map(msg => `
                //             <h2>Чат — група ${ result.group_id }</h2>
                //             `).join("");
                // console.log(html)
                const result = JSON.parse(data.result);
                const messages = result.messages;

                const container = document.getElementById("message")

                container.innerHTML = "";

                console.log(messages)
                for (key in messages){
                    const message = messages[key];
                    console.log(message.id);

                    let html = `<div>
                    <p><b>Батько ${message.id}</b>: ${message.obj}</p>
                </div>`;

                        if (message.soons && Object.keys(message.soons).length > 0) {
                            console.log("Soons:", message.soons);
                            const html = `
                            пост    ${message.id}
                            `;
                            html += renderMessages(message.soons)
                        }
                        else {
                            console.log("синів нема:", message.soons);
                            const html = `
                            пост ${message.id}
                            `;
                        }  
                    container.innerHTML += html;
                }
            })
            .catch(error => console.error("Помилка:", error));
    }

///////////  то шось наподобі parent_structurator(
function renderMessages(messages) {
    let html = "" //це локальна змінна
    for (const key in messages) {
        const message = messages[key];

        html += `<div class="reply">
        <p><b>Син ${message.id}</b>: ${message.obj}</p>
        </div>`;

        if (message.soons && Object.keys(message.soons).length > 0) {
            html += renderMessages(message.soons);
        }
        else{
            console.log(message.id , "немає синів");
        
        }

    return html;

}}