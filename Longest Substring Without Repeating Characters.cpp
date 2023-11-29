class Solution {
public:
    void print_arr(int length){
        for(int i = 0; i < length; i++){
            for(int j = 0;j < length; j++){
                cout << arr[i][j] << " ";
            }
            cout << endl;
        }
    }
    int DP(int x, int dis, string s, int max){
        if(s.length() == 0)
            return 0;
        else if(s.length() == 1)
            return 1;
        else{
            string substr = s.substr(x, dis);
            //cout << "substr : " << substr <<  " string elements : " << s[x+dis] << endl;
            if(substr.find(s[x+dis]) == substr.npos){
                //cout << "arr elements : " << arr[x+1][x+dis] << " " << arr[x][x+dis-1] << " " << arr[x+1][x+dis] << endl;
                arr[x][x+dis] = (arr[x][x+dis-1] <= arr[x+1][x+dis])?arr[x][x+dis-1]+1:arr[x+1][x+dis]+1;
                if(arr[x][x+dis] > max){
                    max = arr[x][x+dis];
                }
            }
            else
                arr[x][x+dis] = (arr[x][x+dis-1] <= arr[x+1][x+dis])?arr[x][x+dis-1]:arr[x+1][x+dis];

            if(x + dis + 1 == s.length()){
                //print_arr(arr, s.length());
                if(x != 0)
                    return DP(0, dis+1, s, max);
                else
                    return max;
            }
            else{
                return DP(x+1, dis, s, max);
            }
        }
    }
    int lengthOfLongestSubstring(string s) {
        int length = s.length();
        //int **arr;
        arr = new int* [length];
        
        // init table
        for(int i = 0; i < length; i++){
            arr[i] = new int [length];
            for(int j = 0;j < length; j++){
                if(i == j)
                    arr[i][j] = 1;
                else
                    arr[i][j] = 0;
            }
        }

        // Dynamic Programming
        int answer = DP(0, 1, s, 1);

        // release memory
        delete [] arr;
        return answer;
    }
private:
    int **arr;
};
