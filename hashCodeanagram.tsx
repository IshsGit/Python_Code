function findAnagrams(s: string, p: string): number[] {
    const pFreq = new Map<string, number>();
    const sFreq = new Map<string, number>();
    const result: number[] = [];

    for (const char of p) {
        pFreq.set(char, (pFreq.get(char) || 0) + 1);
    }

    let left = 0;
    for (let right = 0; right < s.length; right++) {
        const char = s[right];

        sFreq.set(char, (sFreq.get(char) || 0) + 1);

        while (sFreq.get(char) > pFreq.get(char
