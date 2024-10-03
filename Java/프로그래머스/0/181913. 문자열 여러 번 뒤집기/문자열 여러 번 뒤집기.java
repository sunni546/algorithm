class Solution {
    public String solution(String my_string, int[][] queries) {
        String answer = "";
        
        char[] arr = my_string.toCharArray();
        
        for (int i = 0; i < queries.length; i++) {
            int s = queries[i][0];
            int e = queries[i][1];
            for(int j = 0; j < (e - s + 1) / 2; j++) {
                char temp = arr[s + j];
                arr[s + j] = arr[e - j];
                arr[e - j] = temp;
            }
        }
        
        answer = String.valueOf(arr);
            
        return answer;
    }
}