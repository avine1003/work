from collections import deque

def search(name):    # 广度优先搜索 --> 最短路径
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_satisfied(person):
                print('find the %s' % person)
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


def person_is_satisfied(name):  # 是否有满足条件的人
    return name == 'sb'


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []
    
search('you')


