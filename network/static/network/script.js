document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("editPostForm").addEventListener("submit", function(event) {
        const content = document.querySelector('#content').value;
        const csrfTokenElement = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const post_id = document.querySelector('#post_id').value;

        fetch(`/edit/${post_id}`, {
            method: "POST",
            body: JSON.stringify({
                content: content
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

        // Stop form from submitting
        return false;
    });
});
