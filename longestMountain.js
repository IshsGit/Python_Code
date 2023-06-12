function longestMountain(A: number[]): number {
    let maxLength = 0;
    let increasing = 0;
    let decreasing = 0;

    for (let i = 1; i < A.length; i++) {
        if ((decreasing > 0 && A[i - 1] < A[i]) || A[i - 1] === A[i]) {
            increasing = 0;
            decreasing = 0;
        }

        if (A[i - 1] < A[i]) {
            increasing++;
        } else if (A[i - 1] > A[i]) {
            decreasing++;
        }

        if (increasing > 0 && decreasing > 0) {
            maxLength = Math.max(maxLength, increasing + decreasing
