class Car {
    constructor(model, speedLimit = 100) {
        this.model = model;
        this.engine = TURN.OFF;
        this.speed = 0;
        this.speedlimit = speedLimit;
    }

    async drive(speed = 10) {
        this.engine = TURN.ON;
        await this.setSpeed(speed);
        console.log(`Ridding with speed: ${this.speed}`);
        return this.speed;
    }

    async stop() {
        await this.setSpeed(0);
        this.engine = TURN.OFF;
        return this.speed;
    }

    async setSpeed(speed) {
        return new Promise((resolve, reject) => {
            if (this.engine === TURN.OFF) {
                reject('Turn on engine!');
            } else if (this.speedlimit < speed) {
                reject(`Can't reach speed: ${this.speed}. Max speed limit is ${this.speedLimit}`);
            } else {
                const interval = setInterval(async () => {
                    console.log('current speed:', this.speed);
                    if (this.speed < speed) {
                        this.speed++;
                    } else if (this.speed > speed) {
                        this.speed--;
                    } else {
                        resolve(this.speed);
                        clearInterval(interval);
                    }
                }, 100);
            }
        });
    }

    toString() {
        return `Car: ${this.model}; Engine turned on: ${this.engine}; ` + (this.engine ? `Current speed: ${this.speed}` : '');
    }
}

const TURN = {
    OFF: false,
    ON: true
}

const tesla = new Car('TESLA');

async function testDrive() {
    console.log(1, tesla + '');
    try {
        await tesla.drive(120);
    } catch(e) {
        console.log(e);
    }
    
    console.log(2, tesla + '');
    await tesla.stop();
    console.log(3, tesla + '');
}

testDrive();