function maxScore(cardPoints: number[], k: number): number {
    const totalPoints = cardPoints.reduce((sum, point) => sum + point, 0);
    const windowSize = cardPoints.length - k;
    let windowSum = 0;
    
    for (let i = 0; i < windowSize; i++) {
        windowSum += cardPoints[i];
    }
    
    let minWindowSum = windowSum;
    
    for (let i = windowSize; i < cardPoints.length; i++) {
        windowSum = windowSum - cardPoints[i - windowSize] + cardPoints[i];
        minWindowSum = Math.min(minWindowSum, windowSum);
    }
    
    return totalPoints - minWindowSum;
}
