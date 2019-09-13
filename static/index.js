function create_image(src, div){
    const img = document.createElement('img');
    img.src = src;
    div.appendChild(img);
}

function create_header(id, div, s){
    const title = s['title'];

    const header = document.createElement('div');
    header.setAttribute("class", 'card__header');
    const theader = document.createElement('div');
    theader.setAttribute("class", 'card__header-title');
    theader.textContent = title;
    header.appendChild(theader);

    div.appendChild(header);
}

function create_left_side(id, div, s){
    const left = document.createElement('div');
    left.setAttribute("class", 'card__left');
    left.setAttribute("id", 'card__left' + id);

    
    create_image(s['image'], left);

    div.appendChild(left);
}

function create_ratings(div, s){
    const ratings = s['ratings'];
    for(rating in ratings){
        console.log(ratings[rating]);
    }
}

function create_description(div, s){
    const description = s['description'];
    const desc = document.createElement('p');
    desc.innerHTML = description;
    desc.setAttribute("class", 'card__description');
    div.appendChild(desc);

}

function create_right_side(id, div, s){ 
    const right = document.createElement('div');
    right.setAttribute("class", 'card__right');
    right.setAttribute("id", 'card__right' + id);

    create_ratings(right, s);
    create_description(right, s);
    div.appendChild(right);
}


function create_card(s) {
    const id = s['id'];

    const div = document.createElement('div');
    div.setAttribute("class", 'card');
    div.setAttribute("id", 'card' + id);

    create_header(id, div, s);
    create_left_side(id, div, s);
    create_right_side(id, div, s);

    document.body.appendChild(div);
}

window.onload = function () {
    fetch("/data/data.json")
        .then(res => res.json())
        .then(data => {
            let id = 0;
            for (let s of data) {
                create_card(s);
            }
        });
};
