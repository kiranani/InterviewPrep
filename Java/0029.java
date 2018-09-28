class Solution {
    public int divide(int dividend, int divisor) {
        boolean positive = (dividend >= 0 && divisor > 0) || (dividend < 0 && divisor < 0);
        dividend = dividend < 0 ? dividend : -dividend;
        divisor = divisor < 0 ? divisor : -divisor;
        if (divisor == -1) {
            return positive ? (dividend == Integer.MIN_VALUE ? Integer.MAX_VALUE : -dividend) : dividend;
        } else if (divisor == dividend) {
            return positive ? 1 : -1;
        }
        int d = 0;
        while (dividend - divisor <= 0) {
            dividend -= divisor;
            if (d == Integer.MAX_VALUE) {
                break;
            }
            d++;
        }
        return positive ? d : -d;
    }
}
