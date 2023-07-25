function minSwaps(data: number[]): number {
    let onesCount = data.reduce((count, num) => count + num, 0);
    let left = 0;
    let minSwaps = Number.MAX_SAFE_INTEGER;
    let currentZeros = 0;

    for (let right = 0; right < data.length; right++) {
        if (data[right] === 0) {
            currentZeros++;
        }

        while (right - left + 1 > onesCount) {
            if (data[left]
