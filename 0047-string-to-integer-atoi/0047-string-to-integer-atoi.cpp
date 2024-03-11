class Solution {
public:
    int atoi(const char *str) {
        int result=0;
        bool nega=false;
        bool start=false;
        while (str && *str!='\0') {
            if (*str>='0' && *str<='9') {
                if ((result*10+*str-'0')<result)
                    return nega? INT_MIN:INT_MAX;
                result =result*10+(*str-'0');
                start=true;
            } else if (*str=='-' && start==false) {
                nega=true;
                start=true;
            } else if (start) break;
            str++;
        }
        return nega? -result:result;
    }
};