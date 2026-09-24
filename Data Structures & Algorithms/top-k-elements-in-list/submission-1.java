class Solution {
public int[] topKFrequent(int[] nums, int k) {
        TreeMap<Integer, Integer> tracker= new TreeMap<>();
        for (int num : nums) {
            if (tracker.containsKey(num)) {
                tracker.compute(num, (key, oldvalue) -> oldvalue + 1);
                continue;
            }
            tracker.put(num, 1);
        }
        List<Map.Entry<Integer,Integer>> l = new ArrayList<>(tracker.entrySet());
        l.sort((a,b)-> b.getValue() - a.getValue());

        int[] arr = new int[k];
        for(int i = 0; i < k; i++){
            arr[i] = l.get(i).getKey();
        }
        return arr;
    }
}
