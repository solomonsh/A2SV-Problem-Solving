/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
 var minSubArrayLen = function(target, nums) {
    
    let minLength = nums.length;
    let minFound = false;
    
    let left = 0
    let right = 0;
    
    let currentSum = 0;
    
    while (right < nums.length){
        
            currentSum += nums[right];
        
            while(currentSum>=target && left<=right){
                minFound = true;
                minLength = Math.min(minLength,right-left+1);
                currentSum -= nums[left];
                left += 1;
                
            }
            
            right += 1;
        
    }
    
    return minFound ? minLength : 0;
    
};


console.log(minSubArrayLen(7,[2,3,1,2,4,3]))