function characterReplacement(s: string, k: number): number {
    let left = 0;
    let maxRepeatCount = 0;
    const charCount = new Map<string, number>();
    let maxLength = 0;

    for (let right = 0; right < s.length; right++) {
        charCount.set(s[right], (charCount.get(s[right]) || 0) + 1);
        maxRepeatCount = Math.max(maxRepeatCount, charCount.get(s[right]) || 0);

        while (right - left + 1 - maxRepeatCount > k) {
            charCount.set(s[left], charCount.get(s[left]) - 1);
            left++;
        }

        maxLength = Math.max(maxLength, right - left + 1);
    }

    return maxLength;
}
