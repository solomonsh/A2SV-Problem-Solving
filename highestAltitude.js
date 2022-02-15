/**
 * @param {number[]} gain
 * @return {number}
 */
 var largestAltitude = function(gain) {
    
    let prefixSum = Array(gain.length+1).fill(0);
    prefixSum[0] = gain[0];
    
    for (let i = 1;i<gain.length;i++){
        prefixSum[i] = prefixSum[i-1] + gain[i];
    }
    
   
    const result =  Math.max(...prefixSum);
    return result;
};