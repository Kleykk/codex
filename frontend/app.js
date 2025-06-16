const list = document.getElementById('aircraft-list');
const form = document.getElementById('aircraft-form');

async function loadAircraft() {
    const resp = await fetch('/aircraft/');
    const data = await resp.json();
    list.innerHTML = '';
    data.forEach(ac => {
        const div = document.createElement('div');
        div.className = 'aircraft-item';
        div.textContent = `${ac.registration} - ${ac.type}`;
        list.appendChild(div);
    });
}

form.addEventListener('submit', async e => {
    e.preventDefault();
    const reg = document.getElementById('registration').value;
    const type = document.getElementById('type').value;
    await fetch('/aircraft/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ registration: reg, type })
    });
    form.reset();
    loadAircraft();
});

loadAircraft();
