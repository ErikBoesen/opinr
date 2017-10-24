var disp = document.getElementById('display');
var articles = document.getElementsByClassName('article');

function display(source, lean, url) {
    disp.innerHTML = '';
    disp.innerHTML += '<h3>' + source + '</h3>';
    var assessment = '';
    if (Math.abs(lean) > 7) assessment += 'Extremely ';
    else if (Math.abs(lean) > 4) {}
    else assessment += 'Slightly ';
    if (lean > 0) assessment += 'Conservative';
    if (lean < 0) assessment += 'Liberal';
    disp.innerHTML += '<p>Lean: ' + lean + ' (' + assessment + ')';
    disp.innerHTML += '<a href="' + url + '">Open Article</a>';
}

onclick = function(e) {
    var node = e.target.parentNode;
    if (node.className.baseVal == 'article') {
        display(node.getAttribute('data-source'), node.getAttribute('data-lean'), node.getAttribute('data-url'));
    }
}
