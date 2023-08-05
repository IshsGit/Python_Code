function subarraysWithKDistinct(A: number[], K: number): number {
    const atMostK = (k: number) => {
        let left = 0;
        let count = 0;
        const freq = new Map<number, number>();

        for (let right = 0; right < A.length; right++) {
            if (!freq.has(A[right])) {
                freq.set(A[right], 0);
            }

            if (freq.get(A[right]) === 0) {
                k--;
            }

            freq.set(A[right], freq.get(A[right]) + 1);

            while (k < 0) {
                freq.set(A[left], freq.get(A[left]) - 1);
                if (freq.get(A[left]) === 0) {
                    k++;
                }
                left++;
            }

            count += right - left + 1;
        }

        return count;
    };

    return atMostK(K) - atMostK(K - 1);
}
