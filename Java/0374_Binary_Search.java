/* The guess API is defined in the parent class GuessGame.
   @param num, your guess
   @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
      int guess(int num); */

public class Solution extends GuessGame {
    public int guessNumber(int n) {
        if (n == 1) {
            return 1;
        }
        int i = 1, j = n, ans = 0;
        while (i <= j) {
            //System.out.println(i + ":" + j);
            int a = i % 2 == 1 && j % 2 == 1 ? 1 : 0;
            int m = a + i / 2 + j / 2;
            int g = guess(m);
            if (g == 0) {
                ans = m;
                break;
            } else if (g == 1) {
                i = m + 1;
            } else {
                j = m - 1;
            }
        }
        return ans;
    }
}
