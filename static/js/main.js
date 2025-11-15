
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



async function toggleLike(postId) {
    console.log(postId)
    try {
        const csrftoken = document.querySelector('meta[name="csrf-token"]').content;

        const response = await fetch(`/api/posts/${postId}/toggle-like/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            }
        });
        
        const data = await response.json();
        
        // Оновлюємо кількість лайків на сторінці
        const likeBtn = document.querySelector(`[data-post-id="${postId}"]`);
        const likesCount = likeBtn.querySelector('.likes-count');
        likesCount.textContent = data.likes_count;
        
    } catch (error) {
        console.error('Помилка при обробці лайку:', error);
    }
}


//  Завантажуємо перші пости при завантаженні сторінки
document.addEventListener('DOMContentLoaded', function() {

    // Додаємо обробник кліку для кнопок лайків 
    document.addEventListener('click', function(e) {
        if (e.target.closest('.like-btn')) {
            const postId = e.target.closest('.like-btn').dataset.postId;
            toggleLike(postId);
        }
    });
});
