const bal = document.getElementById('bal');
const karalabe = document.getElementById('karalabe');
const vissza = document.getElementById('vissza');

karalabe.addEventListener('click', () => {
    bal.classList.add('hidden');
    vissza.classList.add('hid');
});
vissza.addEventListener('click', () =>{
    bal.classList.remove('hidden');
    vissza.classList.remove('hid');
});
karalabe.addEventListener('click', () => {
    document.body.classList.add('sidebar');
});
vissza.addEventListener('click', () =>{
    document.body.classList.remove('sidebar');
});