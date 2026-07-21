def on_travelled_fly():
    mobs.kill(mobs.target(LOCAL_PLAYER))
player.on_travelled(FLY, on_travelled_fly)

def on_on_chat():
    mobs.spawn(PIG, pos(100, 30, 3))
player.on_chat("run", on_on_chat)

def on_mob_killed_chicken():
    mobs.spawn(mobs.monster(WARDEN), pos(120, 40, 5))
mobs.on_mob_killed(CHICKEN, on_mob_killed_chicken)

def on_travelled_walk():
    pass
player.on_travelled(WALK, on_travelled_walk)

mobs.spawn(mobs.monster(CREEPER), pos(0, 0, 0))