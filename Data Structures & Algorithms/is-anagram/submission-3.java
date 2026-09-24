class Solution {
    public boolean isAnagram(String s, String t) {
        List<Character> l1 = new ArrayList<>();
        List<Character> l2 = new ArrayList<>();

        for (char i : s.toCharArray()){
             l1.add(i);
        }
        for (char i : t.toCharArray()){
            l2.add(i);
        }
        Collections.sort(l1);
        Collections.sort(l2);
        
        return l1.equals(l2);
    }
}
