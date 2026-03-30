const bal = document.getElementById('bal');
const karalabe = document.getElementById('karalabe');
const vissza = document.getElementById('vissza');

karalabe.addEventListener('click', () => {
    bal.classList.add('hidden');
});
vissza.addEventListener('click', () =>{
    bal.classList.remove('hidden');
});
karalabe.addEventListener('click', () => {
    document.body.classList.add('sidebar');
});
vissza.addEventListener('click', () =>{
    document.body.classList.remove('sidebar');
});