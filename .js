document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.getElementById('file-input');
    const startButton = document.getElementById('startbutton');
    const stopButton = document.getElementById('stopbutton');
    const canvas = document.getElementById('canvas');
    const loadingDiv = document.getElementById('loadingdiv');
    let emulator;

    function startEmulator(romData) {
        if (typeof Emulator !== 'undefined') {
            emulator = new Emulator(canvas, romData);
            emulator.start();
            loadingDiv.style.display = 'none';
            startButton.style.display = 'none';
            stopButton.style.display = 'block';
        } else {
            console.error('Emulator is not defined');
        }
    }

    function stopEmulator() {
        if (emulator) {
            emulator.stop();
            startButton.style.display = 'block';
            stopButton.style.display = 'none';
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

    stopButton.addEventListener('click', stopEmulator);
});
