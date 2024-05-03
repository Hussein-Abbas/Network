document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.like-btn').forEach(function(button) {
        button.addEventListener('click', () => {
            const post_id = button.dataset.id;

            // Change status that user can see it
            let likesCount = button.parentElement.firstElementChild;
            if (button.innerHTML == '❤️') {
                button.innerHTML = '🤍';
                if (parseInt(likesCount.innerHTML) > 0) {
                    likesCount.innerHTML = parseInt(likesCount.innerHTML) - 1;
                }
            }
            else {
                button.innerHTML = '❤️'
                likesCount.innerHTML = parseInt(likesCount.innerHTML) + 1;
            }

            let csrfTokenElement = document.querySelector('#csrf_token').firstElementChild.value;
            // Make a PUT request to serevre to save the change
            fetch('/like', {
                method: 'PUT',
                body: JSON.stringify({
                    post_id: post_id
                }),
                headers: {
                    "X-CSRFToken": csrfTokenElement,
                }
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
            })
            .catch(error => {
                console.log(error);
            })
        });
    });
});
