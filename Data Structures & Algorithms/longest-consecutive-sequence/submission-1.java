class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> hs = new HashSet<>();
        for(int i:nums){
            hs.add(i);
        }
        int longest = 0;
        for(int current:hs){
            if(hs.contains(current-1)){
                continue;
            }
            int curr = current , count=1;
            while (hs.contains(curr+1)){
                curr++;
                count++;
            }
            longest = Math.max(longest,count);
        }
        return longest;
    }
}
