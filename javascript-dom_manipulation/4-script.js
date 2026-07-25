const list = document.querySelector('.my_list');
const addItem = document.querySelector('#add_item');

addItem.addEventListener('click', function () {
  const newList = document.createElement('li');
  newList.innerText = 'Item';
  list.appendChild(newList);
});
