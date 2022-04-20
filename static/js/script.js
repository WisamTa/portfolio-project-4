/**
 * codesnippet from django I think therefore i blog
 * Fade the messages away automatic.
 * */
 setTimeout(function () {
    let messages = document.getElementById('msg-box');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2500);

/**
 * jquery using ajax to search form in search view
 */
let url = window.location.href;
let searchInput = document.getElementById('search-input');
let resultBox = document.getElementById('result-box');
let csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;

const getsearchData =(username) => {
    $.ajax({
        type: 'POST',
        url: '/search/result/',
        data: {
            'csrfmiddlewaretoken': csrfToken,
            'username': username
        },
        success: (result)=>{
            const data = result.data;
            
            if (Array.isArray(data)) {
                resultBox.innerHTML = "";
                data.forEach(username=> {
                resultBox.innerHTML += `
                <a href="${url}${username.pk}" class="search-item">
                    <div class="row mt-2 mb-2">
                        <div class="col-12">
                            <h3>@${username.user}</h3>
                        </div>
                    </div>
                </a>
                `;
                });
            } else {
                if (searchInput.value.length > 0) {
                    resultBox.innerHTML = `<b>${data}</b>`;
                } else {
                    resultBox.classList.add('not-visible');
                }
            }
        },
        error: (err)=> {
        }
    });
};

searchInput.addEventListener('keyup', e=>{

    if (resultBox.classList.contains('not-visible')){
        resultBox.classList.remove('not-visible');
    }

    getsearchData(e.target.value);
});