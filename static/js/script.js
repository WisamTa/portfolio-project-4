/**codesnippet from django I think therefore i blog
 * Fade the messages away automatic.
 * */
 setTimeout(function () {
    let messages = document.getElementById('msg-box');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2500);

//search form 

let url = window.location.href
let searchForm = document.getElementById('search-form')
let searchInput = document.getElementById('search-input')
let resultBox = document.getElementById('result-box')
let csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value
console.log(csrfToken)

const getsearchData =(username) => {
    $.ajax({
        type: 'POST',
        url: 'search/',
        data: {
            
            'username': username
        },
        success: (result)=>{
            console.log(result)
        },
        error: (err)=> {
            console.log(err)
        }
    })
}

searchInput.addEventListener('keyup', e=>{
    console.log(e.target.value)

    if (resultBox.classList.contains('not-visible')){
        resultBox.classList.remove('not-visible')
    }

    getsearchData(e.target.value)
})