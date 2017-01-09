from Objs.Events.Event import Event
import random

def func(Event, mainActor, state=None, participants=None, victims=None, sponsors=None):
    mainActor.addItem(state["items"]["Clean Water"])
    state["allRelationships"].IncreaseFriendLevel(mainActor.name, sponsors[0].name, random.randint(1,2))
    choice = random.randint(0,1)
    if choice:
        desc = sponsors[0].name+' gave clean water to '+mainActor.name+"."
    else:
        desc = 'An unknown sponsor gave clean water to '+mainActor.name+"."
    return (desc, [sponsors[0].name, mainActor.name], []) # Second entry is the contestants named in desc, in order. Third is anyone who died. This is in strings.

Event.doEventSponsorGiveWater = classmethod(func)

Event.registerEvent("SponsorGiveWater", Event.doEventSponsorGiveWater)