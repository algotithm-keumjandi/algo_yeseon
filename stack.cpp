// Programmers - 12909

#include <string>
#include <iostream>
#include <stack>

using namespace std;

bool solution(string s)
{
	bool answer = true;
	stack<char> st;
    
	for (int i = 0; i < s.length(); ++i) {
		char currentChar = s[i];
		if (currentChar == '(')
			st.push(currentChar);
		else if (currentChar == ')' && !st.empty())
            st.pop();
		else{
			answer = false;
            break;
        }
	}
    
	if (!st.empty())
        answer = false;
	return answer;
}

int main()
{
    string st;
    cin >> st;
    bool result = solution(st);
    cout << boolalpha << result;
    return 0;
}
