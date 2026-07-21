player.onTravelled(FLY, function () {
    mobs.kill(
    mobs.target(LOCAL_PLAYER)
    )
})
player.onChat("run", function () {
    mobs.spawn(PIG, pos(100, 30, 3))
})
mobs.onMobKilled(CHICKEN, function () {
    mobs.spawn(mobs.monster(WARDEN), pos(120, 40, 5))
})
player.onTravelled(WALK, function () {
	
})
mobs.spawn(mobs.monster(CREEPER), pos(0, 0, 0))
