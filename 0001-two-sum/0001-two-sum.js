/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    // define map/dictionary
    let myMap = new Map();
    let outputArray = []
    
    nums.forEach((item, index) => {
        // does target - item exist?
        if (myMap.has(target - item)){
            outputArray = [myMap.get(target - item), index]
        }else {
            myMap.set(item,index)
        }
    })
    
    return outputArray
    
};