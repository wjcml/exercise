function ajax_request(url, obj, method, contents_type) {
  usp = new URLSearchParams(obj)
  query_str = usp.toString()

  var xhr = new XMLHttpRequest();
  xhr.open(method, url, true);

  if(method == 'POST') {
    xhr.setRequestHeader('Content-Type', contents_type);
  }

  xhr.send(query_str);
}

function ajax_get(url, obj) {
  ajax_request(url, obj, 'GET', null)
}

function ajax_post(url, obj) {
  ajax_request(url, obj, 'POST', 'application/x-www-form-urlencoded')
}

function delete_film(event) {
  var id = event.target.getAttribute("data-id")
  ajax_post('/delete_film', {'id':id})
}

function addCell(film_div, value, is_id, is_title, is_last) {
  var cell_div = document.createElement('div');
  if (is_id)
    cell_div.className = "div_table_cell_id"
  else if (is_title)
    cell_div.className = "div_table_cell_title"
  else if (is_last)
    cell_div.className = "div_table_cell_last"
  else
    cell_div.className = "div_table_cell"

  cell_div.innerHTML = value;
  film_div.appendChild(cell_div)
}

function successListener() {
  var data = JSON.parse(this.responseText);

  for (var i = 0, len = data.length; i < len; ++i) {
    film = data[i]

    var film_div = document.createElement('div');
    film_div.className = "div_table_row"

    addCell(film_div, film.id, true, null, null)
    addCell(film_div, film.title, null, true, null)
    addCell(film_div, film.director, null, null, null)
    addCell(film_div, film.producer, null, null, null)
    addCell(film_div, film.release_date, null, null, null)
    addCell(film_div, film.rt_score, null, null, null)
    addCell(film_div, 
        "<button> \
          <a href='/get_film_info?id=" + film.id + "'>详情</a> \
        </button> \
        <button data-id='" + film.id + "' onclick='delete_film(event)'>删除</button>", null, null, true)

    document.getElementById('content').appendChild(film_div);
  }
}

function failureListener(err) {
  console.log('Request failed', err);
}

var request = new XMLHttpRequest();
request.onload = successListener;
request.onerror = failureListener;
request.open('get', '/get_film_list', true);
request.send();