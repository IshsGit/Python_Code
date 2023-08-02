function minSubArrayLen(s: number, nums: number[]): number {
  let left = 0;
  let minLength = Infinity;
  let sum = 0;

  for (let right = 0; right < nums.length; right++) {
    sum += nums[right];

    while (sum >= s) {
      minLength = Math.min(minLength, right - left + 1);
      sum -= nums[left];
      left++;
    }
  }

  return minLength !== Infinity ? minLength : 0;
}
