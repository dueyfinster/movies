function create_card(id, title, img_src) {
    const div = document.createElement('div');
    div.setAttribute("class", 'card');
    div.setAttribute("id", 'card' + id);

    const header = document.createElement('div');
    header.setAttribute("class", 'card__header');
    const theader = document.createElement('div');
    theader.setAttribute("class", 'card__header-title');
    theader.textContent = title;
    header.appendChild(theader);

    const main = document.createElement('div');
    main.setAttribute("class", 'card__main');
    main.setAttribute("id", 'card__main' + id);

    const img = document.createElement('img');
    img.src = img_src;
    main.appendChild(img);

    div.appendChild(header);
    div.appendChild(main);

    document.body.appendChild(div);

    return main;
}

window.onload = function () {
    fetch("/data/data.json")
        .then(res => res.json())
        .then(data => {
            let id = 0;
            for (let s of data) {
                create_card(s['id'], s['title'], s['image']);
            }
        });
};
