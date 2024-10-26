// main.js
document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.getElementById('file-input');
    const startButton = document.getElementById('startbutton');
    const canvas = document.getElementById('canvas');
    const loadingDiv = document.getElementById('loadingdiv');

    function startEmulator(romData) {
        if (typeof Emulator !== 'undefined') {
            const emulator = new Emulator(canvas, romData);
            emulator.start();
            loadingDiv.style.display = 'none';
        } else {
            console.error('Emulator is not defined');
        }
    }

    fileInput.addEventListener('change', function() {
        const file = fileInput.files[0];
        if (file) {
            loadingDiv.style.display = 'block';
            const reader = new FileReader();
            reader.onload = function(e) {
                const romData = e.target.result;
                startEmulator(romData);
            };
            reader.readAsArrayBuffer(file);
        }
    });

    startButton.addEventListener('click', function() {
        fileInput.click();
    });
});
