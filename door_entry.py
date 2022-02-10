def track(people_tic, event):
    if event[1]=='in':
        if people_tic[event[0]] ==0: 
            people_tic[event[0]] +=1
            return True
        else:
            return False
    elif event[1]=='out':
        if people_tic[event[0]] ==1:
            people_tic[event[0]] -=1
            return True
        else:
            return False
    else:
        return False
    

def solution(events):
    people_tic = {}
    for ev in events:
        if ev[0] in people_tic.keys():
            bl = track(people_tic, event)
            if not bl:
                return False
        else:
            if ev[1]=='in':
                people_tic[ev[0]] = 1
            else:
                return False
    if sum(list(people_tic.values())) ==0:
        return True
    else:
        return False