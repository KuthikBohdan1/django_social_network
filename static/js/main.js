
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

                    let html = ``;

                        if (message.soons && Object.keys(message.soons).length > 0) {
                            console.log("Soons:", message.soons);
                            html = `<div class="card">
                            пост:${message.id}
                            <b>${message.obj}</b>
                            `;
                            html += renderMessages(message.soons)
                        }
                        else {
                            console.log("синів нема:", message.soons);
                            html = `<div class="card">
                            пост id${message.id}
                            <b>${message.obj}
                            </b>
                            `;
                        }
                    html +=   `</div> <br>`
                    container.innerHTML += html;
                }
            })
            .catch(error => console.error("Помилка:", error));
    }

///////////  то шось наподобі parent_structurator(
function renderMessages(messages) {
    let html = "" //це локальна змінна
    for (const key in messages) {  ////цикл
        const message = messages[key];

        html += `<div class="card">
        <p><b>відповідь${message.id}</b>: ${message.obj}</p>
        </div>`;

        if (message.soons && Object.keys(message.soons).length > 0) { ///// умова чиє сини
            html += renderMessages(message.soons);
        }
        else{
            console.log(message.id , "немає синів");
        

        }
}
return html;
}