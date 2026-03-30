const bal = document.getElementById('bal');
const karalabe = document.getElementById('karalabe');
const vissza = document.getElementById('vissza');

karalabe.addEventListener('click', () => {
    bal.classList.add('hidden');
});
vissza.addEventListener('click', () =>{
    bal.classList.add('visible');
});