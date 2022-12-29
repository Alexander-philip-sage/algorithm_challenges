from typing import List, Dict
challenge = """
input: List[List[str, str]]
    List of events. Event is a list of two strings. first string is the person's name, second is direction they pass through the door "in" or "out".

algorithm: 
    A buglary support system tracking customer's faces tracks which direction the customer walks through the door to ensure that everyone enters and 
    exits through the main door during business hours, not before, not after. 

return: bool
    whether or not the system detected an error."""



def track(people_tic: Dict[str, int], event: List[str]) -> bool:
    '''track if the action should set off an alarm. if not, log the action
    input: people_tic: a dictionary where key is the person's name/id and the value is the counter of how they have moved through the front door.
    event: is a list of inputs [person's name, in/out]'''
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
        raise ValueError("only accepted events are [in, out], did not recognize: "+str(event[1]))
    

def detect(events: List[List[str]]) -> bool:
    '''given list of events, detect if an alarm should fire based on incorrect use of the front door
    input: List of events where each event is a list of inputs [person's name, in/out]'''
    people_tic = {}
    for ev in events:
        if ev[0] in people_tic.keys():
            if not track(people_tic, ev):
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

def tests():
    cases = [
            ##[events, succeed]
            ##in
            [[["lenna", "in"], ["angela", "in"], ["penny", "in"], ["kelly", "in"], ["lenna", "out"], ["stella", "in"]], False],
            ##out 
            [[["lenna", "in"], ["angela", "in"], ["penny", "in"], ["kelly", "in"],  ["angela", "out"], ["penny", "out"], ["kelly", "out"], ["lenna", "out"], ["stella", "out"]], False],
            ##4x in out
            [[["lenna", "in"], ["angela", "in"], ["penny", "in"], ["kelly", "in"],  ["angela", "out"], ["penny", "out"], ["kelly", "out"], ["lenna", "out"]], True],
            ##2x in out
            [[["lenna", "in"], ["angela", "in"], ["angela", "out"], ["lenna", "out"]], True],
            ## in
            [[["lenna", "in"]], False],
            ## out
            [[["lenna", "out"]], False],
            ##in out in
            [[["lenna", "in"], ["angela", "in"], ["angela", "out"], ["lenna", "out"], ["lenna", "in"]], False],
            ##in out in out
            [[["lenna", "in"], ["angela", "in"], ["angela", "out"], ["lenna", "out"], ["lenna", "in"], ["lenna", "out"]], True],
            ## out in
            [[["angela", "in"], ["angela", "out"], ["lenna", "out"], ["lenna", "in"]], False],
            ## in in
            [[["angela", "in"],["lenna", "in"], ["angela", "out"],["lenna", "in"]], False],
            ## out out
            [[["lenna", "out"],["lenna", "out"]], False],
        ]
    passed = True
    for case in cases:
        res = case[1]
        events = case[0]
        if res != detect(events):
            passed = False
            print("\nfailed")
            print(events)
    if passed:
        print("All tests passed")
if __name__=="__main__":
    tests()