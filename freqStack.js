class FreqStack {
    freqMap: Map<number, number>;
    stack: Map<number, number[]>;
    maxFreq: number;

    constructor() {
        this.freqMap = new Map();
        this.stack = new Map();
        this.maxFreq = 0;
    }

    push(x
