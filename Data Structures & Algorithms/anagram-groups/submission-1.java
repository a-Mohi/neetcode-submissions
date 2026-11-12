class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> hm = new HashMap<>();
        for(int i=0; i<strs.length; i++){
            char[] toSort = strs[i].toCharArray();
            Arrays.sort(toSort);
            String sorted = new String(toSort);
            hm.putIfAbsent(sorted, new ArrayList<>());
            hm.get(sorted).add(strs[i]);
        }
        return new ArrayList<>(hm.values());
    }
}
