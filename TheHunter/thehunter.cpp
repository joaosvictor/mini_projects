#include <iostream>
#include <unordered_map>
#include <string>
#include <vector>
#include <queue>
#include <unordered_set>

using std::cout;
using std::endl;

bool is_hunter(const std::string& name) {
    return name.back() == 'l'; // a dumb way to find the hunter with the '-1' name 
}

template <typename T>
bool search(const T& name, const std::unordered_map<T, std::vector<T>>& graph) {
    std::queue<T> search_queue;
    std::unordered_set<T> searched;

    // add all friends to search queue
    for (auto&& friend_name : graph.find(name) -> second)
        search_queue.push(friend_name);

    while (!search_queue.empty()) {
        T& person = search_queue.front();
        search_queue.pop();

        // only search this person if you haven't already searched them.
        if (searched.find(person) == searched.end()) {
            if (is_hunter(person)) {
                cout << person << " is the hunter. Yeaaah" << endl;
                return true;
            }
            
            // add all friends of a person to search queue
            for (auto&& friend_name : graph.find(person) -> second)
                search_queue.push(friend_name);

            // mark this person as searched
            searched.insert(person);
        }
    }

    return false;
}

int main() {
    std::unordered_map<std::string, std::vector<std::string>> graph;
    graph.insert({"Carlos", {"Paul","Jhony", "Lucas"}});
    graph.insert({"Lucas", {"Michael", "Jeff"}});
    graph.insert({"Jhony", {"George","Jeff"}});
    graph.insert({"Paul", {}});
    graph.insert({"Michael", {"Cory"}});
    graph.insert({"Cory", {"Mike"}});
    graph.insert({"Mike", {}});
    graph.insert({"Jeff", {}});

    std::string name = "Carlos";
    bool result = search(name, graph);
    cout << "Found The hunter: " << result << endl;

    // create a sample to find the number of classes in the same both ways and say if it's correct. 
}

