class Emulator {
    constructor(canvas, romData) {
        this.canvas = canvas;
        this.romData = romData;
        this.ctx = this.canvas.getContext('2d');
        this.isRunning = false;
    }

    start() {
        if (!this.isRunning) {
            this.isRunning = true;
            console.log("Émulateur démarré avec ROM :", this.romData);
            this.updateScreen();
        }
    }

    updateScreen() {
        // Exemple de mise à jour de l'écran avec une couleur simple
        this.ctx.fillStyle = "#000000";
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
    }

    stop() {
        this.isRunning = false;
        console.log("Émulateur arrêté");
    }
}
