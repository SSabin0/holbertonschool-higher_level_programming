document.addEventListener('DOMContentLoaded', () => {
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => response.json())
    .then(data => {
      const hello = document.getElementById('hello');
      hello.innerText = data.hello;
    })
    .catch(error => console.error('Error:', error));
});
