// get form input

let searchInput = document.getElementById('search');
let searchResults = document.querySelector('.result');


// add event listener
searchInput.addEventListener('input', (e) => {
    let searchValue = e.target.value;
    // console.log(searchValue)
    // http://localhost:5000/hacker-news/search?q=apple
    res = fetch('/hacker-news/search?q=' + searchValue)

    res.then((response) => {
        return response.json();
    }).then((data) => {
        searchResults.innerHTML = "";
        data.data.forEach((item) => {
            searchResults.innerHTML += `<p>${item.title}</p>`;
        });
    })
});