""" url patterns for ms pages """
from django.conf.urls import url
from . import views

urlpatterns = [
    #Home page
    url(r'^$', views.home, name='home'),
    url(r'^home_alter$', views.home_alter, name='home_alter'),

    #Forum
    url(r'^forum$', views.forum, name='forum'),
    url(r'^forum/general_discussion$', views.forum_general_discussion, name='forum_general_discussion'),

    url(r'^forum/gms$', views.forum_gms, name='forum_gms'),
    url(r'^forum/itcg$', views.forum_itcg, name='forum_itcg'),
    url(r'^forum/ms2$', views.forum_ms2, name='forum_ms2'),
    url(r'^topics$', views.topics, name='topics'),
    url(r'^topics/(?P<topic_id>\d+)$', views.topic, name='topic'),
    url(r'^new_topic/$', views.new_topic, name = 'new_topic'),
    url(r'^new_entry/(?P<topic_id>\d+)$', views.new_entry, name = 'new_entry'),
    url(r'^edit_entry/(?P<entry_id>\d+)$', views.edit_entry, name = 'edit_entry'),

    #News
    url(r'^news$', views.news, name='news'),

    #Music
    url(r'^music$', views.music, name='music'),
    url(r'^music/bgms$', views.music_bgms, name='music_bgms'),
    url(r'^music/others$', views.music_others, name='music_others'),
    url(r'^music/others/budapestsymphony$', views.music_others_budapestsymphony, name='music_others_budapestsymphony'),
    url(r'^music/others/itcg$', views.music_others_itcg, name='music_others_itcg'),
    url(r'^music/others/fanmade$', views.music_others_fanmade, name='music_others_fanmade'),


    #Ingame Databases
    url(r'^ingame_db$', views.ingame_db, name='ingame_db'),

    #Classes and Jobs
    url(r'^ingame_db/class&job$', views.ingame_db_classandjob, name='ingame_db_classandjob'),
    #Warrior
    url(r'^ingame_db/class&job/warrior$', views.ingame_db_classandjob_warrior, name='ingame_db_classandjob_warrior'),
    url(r'^ingame_db/class&job/warrior/explorer$', views.ingame_db_classandjob_warrior_explorer, name='ingame_db_classandjob_warrior_explorer'),
    url(r'^ingame_db/class&job/warrior/aran$', views.ingame_db_classandjob_warrior_aran, name='ingame_db_classandjob_warrior_aran'),
    url(r'^ingame_db/class&job/warrior/dawnwarrior$', views.ingame_db_classandjob_warrior_dawnwarrior, name='ingame_db_classandjob_warrior_dawnwarrior'),
    url(r'^ingame_db/class&job/warrior/demonavenger$', views.ingame_db_classandjob_warrior_demonavenger, name='ingame_db_classandjob_warrior_demonavenger'),
    url(r'^ingame_db/class&job/warrior/demonslayer$', views.ingame_db_classandjob_warrior_demonslayer, name='ingame_db_classandjob_warrior_demonslayer'),
    url(r'^ingame_db/class&job/warrior/hayato$', views.ingame_db_classandjob_warrior_hayato, name='ingame_db_classandjob_warrior_hayato'),
    url(r'^ingame_db/class&job/warrior/kaiser$', views.ingame_db_classandjob_warrior_kaiser, name='ingame_db_classandjob_warrior_kaiser'),
    url(r'^ingame_db/class&job/warrior/mihile$', views.ingame_db_classandjob_warrior_mihile, name='ingame_db_classandjob_warrior_mihile'),
    url(r'^ingame_db/class&job/warrior/zero$', views.ingame_db_classandjob_warrior_zero, name='ingame_db_classandjob_warrior_zero'),
    url(r'^ingame_db/class&job/warrior/blaster$', views.ingame_db_classandjob_warrior_blaster, name='ingame_db_classandjob_warrior_blaster'),
    #Magician
    url(r'^ingame_db/class&job/magician$', views.ingame_db_classandjob_magician, name='ingame_db_classandjob_magician'),
    url(r'^ingame_db/class&job/magician/explorer$', views.ingame_db_classandjob_magician_explorer, name='ingame_db_classandjob_magician_explorer'),
    url(r'^ingame_db/class&job/magician/battlemage$', views.ingame_db_classandjob_magician_battlemage, name='ingame_db_classandjob_magician_battlemage'),
    url(r'^ingame_db/class&job/magician/beasttamer$', views.ingame_db_classandjob_magician_beasttamer, name='ingame_db_classandjob_magician_beasttamer'),
    url(r'^ingame_db/class&job/magician/blazewizard$', views.ingame_db_classandjob_magician_blazewizard, name='ingame_db_classandjob_magician_blazewizard'),
    url(r'^ingame_db/class&job/magician/evan$', views.ingame_db_classandjob_magician_evan, name='ingame_db_classandjob_magician_evan'),
    url(r'^ingame_db/class&job/magician/kanna$', views.ingame_db_classandjob_magician_kanna, name='ingame_db_classandjob_magician_kanna'),
    url(r'^ingame_db/class&job/magician/luminous$', views.ingame_db_classandjob_magician_luminous, name='ingame_db_classandjob_magician_luminous'),
    url(r'^ingame_db/class&job/magician/kinesis$', views.ingame_db_classandjob_magician_kinesis, name='ingame_db_classandjob_magician_kinesis'),
    #Bowman
    url(r'^ingame_db/class&job/bowman$', views.ingame_db_classandjob_bowman, name='ingame_db_classandjob_bowman'),
    url(r'^ingame_db/class&job/bowman/explorer$', views.ingame_db_classandjob_bowman_explorer, name='ingame_db_classandjob_bowman_explorer'),
    url(r'^ingame_db/class&job/bowman/wildhunter$', views.ingame_db_classandjob_bowman_wildhunter, name='ingame_db_classandjob_bowman_wildhunter'),
    url(r'^ingame_db/class&job/bowman/windarcher$', views.ingame_db_classandjob_bowman_windarcher, name='ingame_db_classandjob_bowman_windarcher'),
    url(r'^ingame_db/class&job/bowman/mercedes$', views.ingame_db_classandjob_bowman_mercedes, name='ingame_db_classandjob_bowman_mercedes'),
    #Thief
    url(r'^ingame_db/class&job/thief$', views.ingame_db_classandjob_thief, name='ingame_db_classandjob_thief'),
    url(r'^ingame_db/class&job/thief/explorer$', views.ingame_db_classandjob_thief_explorer, name='ingame_db_classandjob_thief_explorer'),
    url(r'^ingame_db/class&job/thief/dualblade$', views.ingame_db_classandjob_thief_dualblade, name='ingame_db_classandjob_thief_dualblade'),
    url(r'^ingame_db/class&job/thief/nightwalker$', views.ingame_db_classandjob_thief_nightwalker, name='ingame_db_classandjob_thief_nightwalker'),
    url(r'^ingame_db/class&job/thief/phantom$', views.ingame_db_classandjob_thief_phantom, name='ingame_db_classandjob_thief_phantom'),
    url(r'^ingame_db/class&job/thief/xenon$', views.ingame_db_classandjob_thief_xenon, name='ingame_db_classandjob_thief_xenon'),
    #Pirate
    url(r'^ingame_db/class&job/pirate$', views.ingame_db_classandjob_pirate, name='ingame_db_classandjob_pirate'),
    url(r'^ingame_db/class&job/pirate/explorer$', views.ingame_db_classandjob_pirate_explorer, name='ingame_db_classandjob_pirate_explorer'),
    url(r'^ingame_db/class&job/pirate/angelicbuster$', views.ingame_db_classandjob_pirate_angelicbuster, name='ingame_db_classandjob_pirate_angelicbuster'),
    url(r'^ingame_db/class&job/pirate/cannoneer$', views.ingame_db_classandjob_pirate_cannoneer, name='ingame_db_classandjob_pirate_cannoneer'),
    url(r'^ingame_db/class&job/pirate/jett$', views.ingame_db_classandjob_pirate_jett, name='ingame_db_classandjob_pirate_jett'),
    url(r'^ingame_db/class&job/pirate/mechanic$', views.ingame_db_classandjob_pirate_mechanic, name='ingame_db_classandjob_pirate_mechanic'),
    url(r'^ingame_db/class&job/pirate/shade$', views.ingame_db_classandjob_pirate_shade, name='ingame_db_classandjob_pirate_shade'),
    url(r'^ingame_db/class&job/pirate/thunderbreaker$', views.ingame_db_classandjob_pirate_thunderbreaker, name='ingame_db_classandjob_pirate_thunderbreaker'),
    #Beginner
    url(r'^ingame_db/class&job/beginner$', views.ingame_db_classandjob_beginner, name='ingame_db_classandjob_beginner'),

    #Items
    url(r'^ingame_db/items$', views.ingame_db_items, name='ingame_db_items'),
    url(r'^ingame_db_items/(?P<item_id>\d+)/$', views.ingame_db_items_details, name='ingame_db_items_details'),

    #Monster
    url(r'^ingame_db/monster$', views.ingame_db_monster, name='ingame_db_monster'),


    #ITCG
    url(r'^itcg$', views.itcg, name='itcg'),
    url(r'^itcg/baseset$', views.itcg_baseset, name='itcg_baseset'),
    url(r'^itcg/baseset/(?P<card_id>\d+)$', views.itcg_baseset_details, name='itcg_baseset_details'),
    url(r'^itcg/omgbosses$', views.itcg_omgbosses, name='itcg_omgbosses'),
    url(r'^itcg/omgbosses/(?P<card_id>\d+)$', views.itcg_omgbosses_details, name='itcg_omgbosses_details'),
    url(r'^itcg/p3ts$', views.itcg_p3ts, name='itcg_p3ts'),
    url(r'^itcg/p3ts/(?P<card_id>\d+)$', views.itcg_p3ts_details, name='itcg_p3ts_details'),
    url(r'^itcg/npcheroes$', views.itcg_npcheroes, name='itcg_npcheroes'),
    url(r'^itcg/npcheroes/(?P<card_id>\d+)$', views.itcg_npcheroes_details, name='itcg_npcheroes_details'),
    url(r'^itcg/beholdzakum$', views.itcg_beholdzakum, name='itcg_beholdzakum'),
    url(r'^itcg/beholdzakum/(?P<card_id>\d+)$', views.itcg_beholdzakum_details, name='itcg_beholdzakum_details'),
    url(r'^itcg/dangersofthedeepsea$', views.itcg_dangersofthedeepsea, name='itcg_dangersofthedeepsea'),
    url(r'^itcg/dangersofthedeepsea/(?P<card_id>\d+)$', views.itcg_dangersofthedeepsea_details, name='itcg_dangersofthedeepsea_details'),


    #Maplestory 2
    url(r'^ms2$', views.ms2, name='ms2'),

    ]
