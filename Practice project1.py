player_name="Alex"
player_lvl=5
player_inventory=["sword","shield","potion"]
player_position=(10,20)
player_achievments={"first_blood","dragon_slayer"}
player_info=dict(zip(["name","level","inventory","position","achievements"],[player_name,player_lvl,player_inventory,player_position,player_achievments]))
player_scores=[100,200,150,300,250]
def show_profile():
    return player_info
def score_stats():
    totalscore=sum(player_scores)
    avgscore=totalscore/len(player_scores)
    return totalscore, avgscore
def counter(x):
    return player_inventory.count(x)
print("Your profile:", show_profile())
print("Score statistics:", score_stats())
print("Potion count:", counter("potion"))
#GGS Well Done! 
