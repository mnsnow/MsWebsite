from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from .api import Msapi, Msapi_item_details




#Home
def home(request):
    """ Home page """
    return render(request, 'ms_pages/home.html')



#Forum
def forum(request):
    """forum page"""
    return render(request, 'ms_pages/forum.html')

def forum_general_discussion(request):
    """forum general discussion page"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'ms_pages/forum_general_discussion.html',context)

def forum_gms(request):
    """forum GMS page"""
    return render(request, 'ms_pages/forum_gms.html')

def forum_itcg(request):
    """forum itcg page"""
    return render(request, 'ms_pages/forum_itcg.html')

def forum_ms2(request):
    """forum Maplestory 2 page"""
    return render(request, 'ms_pages/forum_ms2.html')

@login_required
def topics(request):
    """ topics page"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'ms_pages/topics.html', context)

@login_required
def topic(request, topic_id):
    """ Individual topic page """
    topic = Topic.objects.get(id=topic_id)
    #make sure the topic belongs to the current user
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'ms_pages/topic.html', context)

@login_required
def new_topic(request):
    """ Page for user to create new topic """
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('ms_pages:forum_general_discussion'))

    context = {'form': form}
    return render(request, 'ms_pages/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """ Page for user to create new entry """
    topic = Topic.objects.get(id = topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('ms_pages:topic',
                                                args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'ms_pages/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """ Edit an existing entry """
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm(instance = entry)
    else:
        form = EntryForm(instance = entry, data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ms_pages:topic',
                                                args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form':form}
    return render(request, 'ms_pages/edit_entry.html', context)



#Music
def music(request):
    """music page"""
    return render(request, 'ms_pages/music.html')

def music_bgms(request):
    """bgms page"""
    return render(request, 'ms_pages/music_bgms.html')

def music_others(request):
    """music others bgm"""
    return render(request, 'ms_pages/music_others.html')

def music_others_budapestsymphony(request):
    """music others budapest symphony bgm"""
    return render(request, 'ms_pages/music_others_budapestsymphony.html')

def music_others_itcg(request):
    """music others itcg bgm"""
    return render(request, 'ms_pages/music_others_itcg.html')

def music_others_fanmade(request):
    """music others fan made bgm"""
    return render(request, 'ms_pages/music_others_fanmade.html')



#News
def news(request):
    """news page"""
    return render(request, 'ms_pages/news.html')



#Ingame database
def ingame_db(request):
    """Database of ingame items"""
    return render(request, 'ms_pages/ingame_db.html')


#ingame database classes and jobs
def ingame_db_classandjob(request):
    """ingame class and jobs"""
    return render(request, 'ms_pages/ingame_db_classandjob.html')


#Warrior
def ingame_db_classandjob_warrior(request):
    """ingame warrior page"""
    return render(request, 'ms_pages/ingame_db_classandjob_warrior.html')

def ingame_db_classandjob_warrior_explorer(request):
    """ingame warrior explorer page"""
    return render(request, 'ms_pages/ingame_db_classandjob_warrior_explorer.html')

def ingame_db_classandjob_warrior_aran(request):
    """ingame warrior aran page"""
    return render(request, 'ms_pages/ingame_db_classandjob_warrior_aran.html')

def ingame_db_classandjob_warrior_dawnwarrior(request):
    """ingame warrior dawnwarrior page"""
    return render(request, 'ms_pages/ingame_db_classandjob_warrior_dawnwarrior.html')

def ingame_db_classandjob_warrior_demonavenger(request):
    """ingame warrior demonavenger page"""
    return render(request, 'ms_pages/ingame_db_classandjob_warrior_demonavenger.html')

def ingame_db_classandjob_warrior_demonslayer(request):
    """ingame warrior demonslayer page"""
    return render(request, 'ms_pages/ingame_db_classandjob_warrior_demonslayer.html')

def ingame_db_classandjob_warrior_hayato(request):
    """ingame warrior hayato page"""
    return render(request, 'ms_pages/ingame_db_classandjob_warrior_hayato.html')

def ingame_db_classandjob_warrior_kaiser(request):
    """ingame warrior kaiser page"""
    return render(request, 'ms_pages/ingame_db_classandjob_warrior_kaiser.html')

def ingame_db_classandjob_warrior_mihile(request):
    """ingame warrior mihile page"""
    return render(request, 'ms_pages/ingame_db_classandjob_warrior_mihile.html')

def ingame_db_classandjob_warrior_zero(request):
    """ingame warrior zero page"""
    return render(request, 'ms_pages/ingame_db_classandjob_warrior_zero.html')

def ingame_db_classandjob_warrior_blaster(request):
    """ingame warrior blaster page"""
    return render(request, 'ms_pages/ingame_db_classandjob_warrior_blaster.html')


#Magician
def ingame_db_classandjob_magician(request):
    """ingame magician page"""
    return render(request, 'ms_pages/ingame_db_classandjob_magician.html')

def ingame_db_classandjob_magician_explorer(request):
    """ingame magician explorer page"""
    return render(request, 'ms_pages/ingame_db_classandjob_magician_explorer.html')

def ingame_db_classandjob_magician_battlemage(request):
    """ingame magician battlemage page"""
    return render(request, 'ms_pages/ingame_db_classandjob_magician_battlemage.html')

def ingame_db_classandjob_magician_beasttamer(request):
    """ingame magician beasttamer page"""
    return render(request, 'ms_pages/ingame_db_classandjob_magician_beasttamer.html')

def ingame_db_classandjob_magician_blazewizard(request):
    """ingame magician blazewizard page"""
    return render(request, 'ms_pages/ingame_db_classandjob_magician_blazewizard.html')

def ingame_db_classandjob_magician_evan(request):
    """ingame magician evan page"""
    return render(request, 'ms_pages/ingame_db_classandjob_magician_evan.html')

def ingame_db_classandjob_magician_kanna(request):
    """ingame magician kanna page"""
    return render(request, 'ms_pages/ingame_db_classandjob_magician_kanna.html')

def ingame_db_classandjob_magician_luminous(request):
    """ingame magician luminous page"""
    return render(request, 'ms_pages/ingame_db_classandjob_magician_luminous.html')

def ingame_db_classandjob_magician_kinesis(request):
    """ingame magician kinesis page"""
    return render(request, 'ms_pages/ingame_db_classandjob_magician_kinesis.html')


#Bowman
def ingame_db_classandjob_bowman(request):
    """ingame bowman page"""
    return render(request, 'ms_pages/ingame_db_classandjob_bowman.html')

def ingame_db_classandjob_bowman_explorer(request):
    """ingame bowman explorer page"""
    return render(request, 'ms_pages/ingame_db_classandjob_bowman_explorer.html')

def ingame_db_classandjob_bowman_wildhunter(request):
    """ingame bowman wildhunter page"""
    return render(request, 'ms_pages/ingame_db_classandjob_bowman_wildhunter.html')

def ingame_db_classandjob_bowman_windarcher(request):
    """ingame bowman windarcher page"""
    return render(request, 'ms_pages/ingame_db_classandjob_bowman_windarcher.html')

def ingame_db_classandjob_bowman_mercedes(request):
    """ingame bowman mercedes page"""
    return render(request, 'ms_pages/ingame_db_classandjob_bowman_mercedes.html')


#Thief
def ingame_db_classandjob_thief(request):
    """ingame thief page"""
    return render(request, 'ms_pages/ingame_db_classandjob_thief.html')

def ingame_db_classandjob_thief_explorer(request):
    """ingame thief explorer page"""
    return render(request, 'ms_pages/ingame_db_classandjob_thief_explorer.html')

def ingame_db_classandjob_thief_dualblade(request):
    """ingame thief dualblade page"""
    return render(request, 'ms_pages/ingame_db_classandjob_thief_dualblade.html')

def ingame_db_classandjob_thief_nightwalker(request):
    """ingame thief nightwalker page"""
    return render(request, 'ms_pages/ingame_db_classandjob_thief_nightwalker.html')

def ingame_db_classandjob_thief_phantom(request):
    """ingame thief phantom page"""
    return render(request, 'ms_pages/ingame_db_classandjob_thief_phantom.html')

def ingame_db_classandjob_thief_xenon(request):
    """ingame thief xenon page"""
    return render(request, 'ms_pages/ingame_db_classandjob_thief_xenon.html')



#Pirate
def ingame_db_classandjob_pirate(request):
    """ingame pirate page"""
    return render(request, 'ms_pages/ingame_db_classandjob_pirate.html')

def ingame_db_classandjob_pirate_explorer(request):
    """ingame pirate explorer page"""
    return render(request, 'ms_pages/ingame_db_classandjob_pirate_explorer.html')

def ingame_db_classandjob_pirate_angelicbuster(request):
    """ingame pirate angelicbuster page"""
    return render(request, 'ms_pages/ingame_db_classandjob_pirate_angelicbuster.html')

def ingame_db_classandjob_pirate_cannoneer(request):
    """ingame pirate cannoneer page"""
    return render(request, 'ms_pages/ingame_db_classandjob_pirate_cannoneer.html')

def ingame_db_classandjob_pirate_jett(request):
    """ingame pirate jett page"""
    return render(request, 'ms_pages/ingame_db_classandjob_pirate_jett.html')

def ingame_db_classandjob_pirate_mechanic(request):
    """ingame pirate mechanic page"""
    return render(request, 'ms_pages/ingame_db_classandjob_pirate_mechanic.html')

def ingame_db_classandjob_pirate_shade(request):
    """ingame pirate shade page"""
    return render(request, 'ms_pages/ingame_db_classandjob_pirate_shade.html')

def ingame_db_classandjob_pirate_thunderbreaker(request):
    """ingame pirate thunderbreaker page"""
    return render(request, 'ms_pages/ingame_db_classandjob_pirate_thunderbreaker.html')


#beginner
def ingame_db_classandjob_beginner(request):
    """ingame beginner page"""
    return render(request, 'ms_pages/ingame_db_classandjob_beginner.html')



#Items
def ingame_db_items(request):
    """ingame items"""
    item_ids = ''
    item_names = ''
    query = request.GET.get('q')
    if query:
        result = Msapi(query=query)
        item_ids = result.item_ids
        item_names = result.item_names

    context = {'item_ids':item_ids, 'item_zip':zip(item_ids,item_names), 'item_names':item_names,}
    return render(request, 'ms_pages/ingame_db_items.html',context)

def ingame_db_items_details(request, item_id):
    """ingame item details"""
    result = Msapi(item_id=item_id)
    item_overallcategory = result.item_overallcategory
    item_category = result.item_category
    item_subcategory = result.item_subcategory
    item_name = result.item_name
    item_description = result.item_description
    context = {'item_id': item_id, 'item_category':item_category,
        'item_name': item_name, 'item_description': item_description,
        'item_overallcategory': item_overallcategory, 'item_subcategory': item_subcategory}
    return render(request, 'ms_pages/ingame_db_items_details.html',context)



#Monster
def ingame_db_monster(request):
    """ingame monster"""
    return render(request, 'ms_pages/ingame_db_monster.html')



#ITCG
def itcg(request):
    """ingame itcg page"""
    return render(request, 'ms_pages/itcg.html')

def itcg_baseset(request):
    """ingame itcg base set page"""
    card_ids = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15",
    "16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32",
    "33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49",
    "50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66",
    "67","68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83",
    "84","85","86","87","88","89","90","91","92","93","94","95","96"]
    card_names = ["Arrow Blow","Battle Bow","Black Robin Hat","Blue Diros","Cerebes","Curse Eye",
    "Drake","Fairy","Focus","Golden Crow","Green Trixter","Hector","Horned Mushroom","Jr. Boogie",
    "Lunar Pixie","Nixie","Platoon Chronos","Power Knock-Back","Rain of Arrows","Risky Shot",
    "Skyhawk","Soul Arrow","Stirge","Tweeter","Bellflower Root","Chief Gray","Dark Axe Stump",
    "Energy Bolt","Evil Tale","Heal","Jr. Necki","Knowledge Is Power","Lioner","Lucida","Magic Claw",
    "Maple Staff","Maya","Meditation","MP Eater","Octopus","Peach Monkey","Red Apprentice Hat",
    "Side Quest","Stormwind","Teleport","Thunder Bolt","Zeta Gray","Zombie Lupin","Avenger",
    "Blood Stain","Blue Nightfox","Buffy","Cico","Coconut Knife","Croco","Dark Shadow","Double Strike"
    ,"Emerald Earrings","Ivan","Krappy","Krip","Kumbi Throwing-Star","Lorang","Mistmoon",
    "Orange Mushroom","Pink Teddy","Propelly","Red Night","Red Snail","Seacle","Soul Teddy",
    "Swipe","Battle Shield","Block Golem","Doombringer","Fire Boar","Green Mushroom","Grizzly",
    "Item Trade","Jr. Yeti","Officer Skeleton","Panda","Pepe","Pull","Resting","Ribbon Pig","Sentinel",
    "Serpent’s Tongue","Sherman","Slime","Starblade","Stone Golem","Tauromacis","The Nine Dragons",
    "Wild Boar","Yeti & Pepe"]
    card_zip = zip(card_ids,card_names)
    context = {'card_zip':card_zip}
    return render(request, 'ms_pages/itcg_baseset.html',context)

def itcg_baseset_details(request, card_id):
    """ingame itcg baseset details page"""
    context = {'card_id': card_id}
    return render(request, 'ms_pages/itcg_baseset_details.html', context)


def itcg_omgbosses(request):
    """ingame itcg omg bosses! page"""
    card_ids = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14",
    "15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31",
    "32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48",
    "49","50","51","52","53","54","55","56","57","58","59","60"]
    card_names = ["Angry Stirge","Blue Mushroom","Brave Fairy","Chronos","Dark Drake",
    "Final Attack: Bow","Indigo","Janitor’s Mop","Jr. Balrog","Luster Pixie","Maple Soul Searcher",
    "Masterful Knock-Back","Papa Pixie","Papa Pixie’s Time Warp","Phantom Watch","Alishar",
    "Alishar’s Death Magic","Beginner’s Bolt","Black Magic Shoes","Blue Dragon Turtle",
    "Boosted Heal","Epic Quest","Felix","Fire Arrow","Ghost Stump","MP Recovery","MT-",
    "Plateon","Surprised Octopus","Wizard Wand","Book Ghost","Dark Scorpio","Lazy Buffy",
    "Nova","Omok Table","Pianus","Poison Poopa","Poisonous Mushroom","Reef Claw","Savage Blow",
    "Sneaky Twink","Stun","Tortie","Ward of Awakening","Zombie Mushmom","Bruno","Bubbling",
    "Dark Yeti & Pepe","Devil Slime","Iron Boar","Iron Hog","Jr. Pepe","King Slime","Manon",
    "Power Guard","Rage","Raging Black Golem","Silver Legend Shield","Training","Yeti"]
    card_zip = zip(card_ids,card_names)
    context = {'card_zip':card_zip}
    return render(request, 'ms_pages/itcg_omgbosses.html', context)

def itcg_omgbosses_details(request, card_id):
    """ingame itcg omg bosses details page"""
    context = {'card_id': card_id}
    return render(request, 'ms_pages/itcg_omgbosses_details.html', context)


def itcg_p3ts(request):
    """ingame itcg p3ts page"""
    card_ids = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14",
    "15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31",
    "32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48",
    "49","50","51","52","53","54","55","56","57","58","59","60"]
    card_names = ["Black Bunny","Blessing of the Amazon","Chirrpy","Cold Eye","Crow","Flyeye",
    "Flying Freezer","Ghost Pixie","Ginseng Jar","Maple Shield","Moby","Mortal Blow",
    "Nependeath","Rookie Knock-Back","Ryden","Bahamut","Brown Teddy","Cold Beam","Emerald Staff",
    "Ergoth","Invincible","Penelope","Porcupine","Robot","Rookie Energy Bolt","Rookie Magic Claw",
    "Seal","Spell Booster","Sr. Bellflower Root","White Fang","Black Dragon","Blood Larceny",
    "Brown Kitty","Call of the Wild","Captain","Destroy All Monsters","Disorder","Halfmoon Zamadar",
    "Keaton","Kru","Lord Pirate","Mini Yeti","Pinboom","Squid","Zombie Mushroom","Bain",
    "Battle Fury","Beetle","Bloctopus","Fire Tusk","Green Cornian","Jr. Cerebes","Kiri Viva",
    "Pet Jr. Balrog","Pet Panda","Pig","Puppy","Red Slime","Ruin","Watch Hog"]
    card_zip = zip(card_ids,card_names)
    context = {'card_zip':card_zip}
    return render(request, 'ms_pages/itcg_p3ts.html',context)

def itcg_p3ts_details(request, card_id):
    """ingame itcg p3tsdetails page"""
    context = {'card_id': card_id}
    return render(request, 'ms_pages/itcg_p3ts_details.html', context)


def itcg_npcheroes(request):
    """ingame itcg npc heroes page"""
    card_ids = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14",
    "15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31",
    "32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48",
    "49","50","51","52","53","54","55","56","57","58","59","60"]
    card_names = ["Arrow Crafting","Athena Pierce","Athena’s Death Arrow","Heroic Pentagon",
    "Jr. Reaper","Killa Bee","Master Chronos","Mia","Nightghost","Spider Venom Earrings","Squabble",
    "War Bow","Wonky","Wooden Target Dummy","Zozo","Braddock","Buy And Sell","Carta",
    "Chain Lightning","Cloto","Grendel The Really Old","Grendel’s Absorb","Holy Arrow",
    "Lakelis","Mateon","Metal Wand","Nella","Party Quest","Sand Dwarf","Sera’s Mirror",
    "Bone Fish","Boomer","Chipmunk","Cody","Dark Lord","Dark Lord’s Strike","Death Teddy",
    "Diamond Dagger","Eurek The Alchemist","Michi","Mithril Wristband","Moon Bunny","Power Elixir",
    "Triple-Tipped Zamadar","Vogen’s Forge","Balrog’s Dance","Crystal Boar","Dances With Balrog",
    "Ericsson","Ice Golem","Relaxer","Rexton","Shammos","Shawn’s Descent","Street Slime",
    "Taurospear","The Shinning","Tucker","Wild Kargo","Wooden Mask"]
    card_zip = zip(card_ids,card_names)
    context = {'card_zip':card_zip}
    return render(request, 'ms_pages/itcg_npcheroes.html', context)

def itcg_npcheroes_details(request, card_id):
    """ingame itcg npcheroes details page"""
    context = {'card_id': card_id}
    return render(request, 'ms_pages/itcg_npcheroes_details.html', context)


def itcg_beholdzakum(request):
    """ingame itcg behold zakum page"""
    card_ids = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15",
    "16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32",
    "33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49",
    "50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66",
    "67","68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83",
    "84","85","86","87","88","89","90"]
    card_names = ["Angry Hector","Brown Woodsman Boots","Cerebes","Combo Shot","Diamond Arrows",
    "Flynn","Giant Centipede","Green Avelin","Grim Phantom Watch","Jr. Boogie","Kiyo","Magik Fierry",
    "Mass Respawn","Metus","Pet Elephant","Power Knock-Back","Spook School","Tweeter","Alien Armada",
    "Barnard Gray","Beginner’s Bolt","Blue Apprentice Hat","Dark Axe Stump","Dark Noel",
    "Devouring Flowers","Elliza","Greater Spell Booster","Kage","Magic Armor","Mahibang",
    "Malady","Peach Monkey","Respawn","Tactical Strike","The Glimmer Man","Red Apprentice Hat",
    "Birthday Present","Black Mamba","Blin","Clang","Crop Of Mushrooms","Exploding Meso Bag",
    "Flower Fish","Gold Titans","Ivan","King Clang","Left Behind","Master Death Teddy","Morphed Blin",
    "Paper Fighter Plane","Psycho Jack","Shy Orange Mushroom","Orange Mushroom","Pink Teddy","Aggro",
    "Blue Kentaurus","Cube Slime","Dark Master Sergeant","Devil’s Sunrise","Dragon Blood","Fangblade",
    "Final Attack: Sword","Goo Zoo","Griffey","Ice Sentinel","Improving HP Recovery","Iron Hog",
    "Jr. Cellion","Mad Grizzly","Mithril Mutae","Pack Of Boars","Studded Pole"," Arms Of Zakum",
    "Adobis","Aura","Black Boogie","Blue Snail","Boogie","Eye Of Fire","Frozen Tuna",
    "Left Arms Of Zakum","Mighty Zakum","Mimic","Nimble Feet","Opachu","Punco","Right Arms Of Zakum",
    "Three Snails: Blue","Zakum Helmet","Zavier"]
    card_zip = zip(card_ids,card_names)
    context = {'card_zip':card_zip}
    return render(request, 'ms_pages/itcg_beholdzakum.html', context)

def itcg_beholdzakum_details(request, card_id):
    """ingame itcg behold zakum details page"""
    context = {'card_id': card_id}
    return render(request, 'ms_pages/itcg_beholdzakum_details.html', context)


def itcg_dangersofthedeepsea(request):
    """ingame itcg pirate: dangers of the deep sea page"""
    return render(request, 'ms_pages/itcg_dangersofthedeepsea.html')

def itcg_dangersofthedeepsea_details(request, card_id):
    """ingame itcg dangers of the deep sea details page"""
    context = {'card_id': card_id}
    return render(request, 'ms_pages/itcg_dangersofthedeepsea_details.html', context)



def ms2(request):
    """Maplestory 2 page"""
    return render(request, 'ms_pages/ms2.html')
