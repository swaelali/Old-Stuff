def convert(network):
    net = [[x.split('-')[0],x.split('-')[1]] for x in network]
    mnet ={}
    for l in net:
        if l[0] in mnet.keys():
            mnet[l[0]].append(l[1])
        else:
            mnet[l[0]]=[]
            mnet[l[0]].append(l[1])
        if l[1] in mnet.keys():
            mnet[l[1]].append(l[0])
        else:
            mnet[l[1]]=[]
            mnet[l[1]].append(l[0])
    return mnet

def recsearch(net,keys,connections =[],searched =[]):
    for key in keys:
        if key in net.keys() and key not in searched:
            for elem in net[key]:
                connections.append(elem)
                searched.append(key)
            recsearch(net,net[key],connections,searched)
    return set(connections)

def check_connection(network, first, second):
    mnet = convert(network)
    connections = recsearch(mnet, [first],connections=[],searched=[])
    if second in connections:
        return True
    else:
        return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
        