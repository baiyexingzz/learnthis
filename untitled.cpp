class Solution {
public:
    bool isPowerOfFour(int num) {
        if(num<4)
			return 0;
		double re;
		re = log(num)/log(4)
		if(re == (int)re)
			return 1;
		return 0;
    }
};
