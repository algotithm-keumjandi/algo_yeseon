// BOJ-10845
#include <string>
#include <iostream>
#include <queue>
using namespace std;

int main(){
    queue<int> q;
    int N;
    string command;
    int num;
    
    cin >> N;
    
    for(int i = 0; i < N ; i++){
        cin >> command;
        
        if (command == "push") {
            cin >> num;
            q.push(num);
            
        } else if (command == "pop") {
            if (q.size() == 0) cout << -1 << endl;
            else{
               cout << q.front() << endl;
               q.pop(); 
            }
        } else if (command == "front") {
            if (q.size() == 0) cout << -1 << endl;
            else cout << q.front() << endl;
            
        } else if (command == "back") {
            if (q.size() == 0) cout << -1 << endl;
            else cout << q.back() << endl;
            
        } else if (command == "size") {
            if (q.size() == 0) cout << 0 << endl;
            else cout << q.size() << endl;
            
        } else if (command == "empty") {
            if (q.size() == 0) cout << 1 << endl;
            else cout << 0 << endl;
        }
    }
}