
import random

username =[
    'captainSub','seaCaptain','admiralPants',
    'coffeeIT','techSupport00','tech_coffee',
    'earth_coder','terranCoder','code_xx',
    'web_user','redacted_text','purple_hair',
    'usr_sandwich','root_salad','root_usr_b33r',
    'organic_usr','buffr_ovrflow','rgb_team',
    'osint_tea','inbound_filter','dot_search',
    'bicycleHacker','xday_vuln','etc_usr',
    'importError','router_1701_D','hack_1701D',
    'ENT_isp','ENT_ssh','ghost_whaler','shapeshift_usr',
    'magic_spider','goddess_scorpion','vetala_ssh',
    'uid_strix','udi_varkolak','cactus_cat','arimanius',
    'Xiezhi','snow_lion','root_kurma','wolf359r','rgb_rain',
    'holosuite_hacker','r2d2_ssh','tech_coldbrew','andorian_blu',
    'romulan_shell','obisidian_x67','typescript_ship',
    'cosmetic_code','folder_blt','offchain_block','deathstar_tech',
    'tech_starbase_89','cheese_coder','klingon_logger',
    'dihydrogen_monoxr','plasma_exe','ice_meltr','thermos_os',
    'fridge_hackr','sandwich_stackr','dilithium_x','hydro_perox',
    'bajor_ssh','lakshmi_linux','saraswati_linux','kernel_durga',
    'usr_bragi','root_eris','usr_nike','ixchel_ssh','code_weaver',
    'code_assembler','python_puzzles','github_user','git_cloner',
    'mercury_osx','remote_access_sleep','remote_shell','seashore_shell',
    'jimjam_blam','d0t_c0m_','ice_cubepy','juicy_js','super_func',
    'requests_pbj','ctrl_saver','crystal_lite','pearl_perl','starz_x67',
    'pizza_osx','bic_pen_tester','epislon_off','zeta_etc','random_theta',
    'kappa_slappa','lambda_lamb','rho_berry_py','rohroh_raw','fee_phi_fae',
    'breached_bleach','rubix_fix','upsilon_down_ssh','silent_daemona',
    'volcano_linux','code_camper','kanaskis_code','code_mountain','codePusher',
    'self_tech_support','staff_piedpiper','dry_coder','coffee_coder','code_stasher',
    'code_starter','organic_root','root_veggies','coffee_neuralnet','grizzly_osx',
    'moose_ops','wildfire_tech','hash_nacl','NaCl_pepper','code_ketchup','mustard_code',
    'code_chutney','code_relish','onion_code','Sriracha_osx','Sriracha_linux',
    'code_noodles','vermicelli_code','top_secret_coder','jiffy_code','jpl_rocketer',
    'westjet_osx','code_witchery',
    'noctilucent_cloud','cirriform_nacreous',
    'cirrostratus_ops','cirrus_linux','altostratus_ops',
    'cirrocumulus_osx','nimbostratus_ops','nimbostratus_osx',
    'stratus_coder','stratus_shell','stratus_linux','code_mist',
    'foggy_code','deepdish_coder','centrum_osx','dunder_mifflin_tech',
    'code_park','paprika_linux','paprika_osx','campfire_coder',
    'code_ninja','white_hat_ninja','dove_osx','rpdr_coder',
    'project_lampshade','e2e_bots','ai_iou_','prompt_engnr',
    'prompt_coder','freshmint_code','freshmint_ssh','purplerain_linux',
    'jedi_osx','c3p0_tech','c3p0_os','mapleleafs_tech','maple_osx'
    'codestackoverflow','antiox_osx','cherrypop_kernel','banana_split',
    'strawberri_py','febreeze_os','pinetree_shell','trident_linux',
    'code_recycler','this_code','code_self','paperbag_ops',
    'bug_compiler','bug_raid','fruitloops_osx','legendary_code',
    'code_fantasy','saturn_linux','saturday_coder','mars_tech',
    'uranus_osx','venus_ssh','random_import','lipstick_ops',
    'mascara_linux','eyeshadow_linux','mascara_ops','code_ruvealr',
    'lipstick_challengee','coconut_osx','coconut_tech','coconut_ops',
    'code_memo','fax_the_code','dialup_lisp','c0de_eth0s',
    'vending_machine_code','code_sauce','mx_robot','robotx',
    'cabin_code_logs','code_party','michelin_star_coder',
    'hipster_code','friendly_codex','digita1_c1oud','backslash_dir',
    'oss_coder','code_fossil','pancake_stack','poptart_stack',
    'purplehoodie','bluehoodie','code_oracle','dolphin_code',
    'phasers_ops','sud0_code','sud0ps','code_decorator','code_decour',
    'xmas_shell','frosty_linux','cereal_tech_support','sundae_ops',
    'c0de_t4c0','code_6urr1t0','sushi_code','code_roll','friedrice_osx',
    'section31_ops','obisidian_0rd3r','lemons_osx','fruitpunch_ssh',
    'grep_grapes','cat_kitkat_dat',
    'grandbar_100x','mu5k3t33rs_x1',
    'avenue5_ops','aero_mlops','almond_shell',
    'baby_ruth_rb','black_thunder_ops','bounty_ops',
    'exploit_butterfinger','cadbury_py','chunky_osx',
    'cloud9_mlops','coffee_crisp_tech','dove_osx','dove_linux',
    'echo_echo_bar','code_bubbles','hershey_shell','jersey_jacki',
    'lion_osx','m&m_codes','code_mounds','code_moos','mx_good_code',
    'nestle_ops','skor_more_code','code_smarties','sky_terminal',
    'cloud_terminal','terran_terminal','timtam_pam','toblerone_ops',
    'toffee_crisp_tech','twix_linux','usr_whatchamacallit','wunder_code',
    'zero_osx','nato_ops','code_flipflops','code_treatyx33','code_neutral',
    'sudo_zelda','princess_peach','klingon_redteam','vulcan_linux',
    'oath_2_code','duty_2code','passionfruit_code','pomegranite_ops',
    'pomegranite_osx','wifi_r00tr','code_springs','tidepods_tech',
    'egg0_my_code0','code_saga','quaker_oats_code','got_code',
    'posh_os','microwave_shell','tvdinner_code','g0vt_ml0p5',
    'code_floppydisk','n4ch0s_os','blackhole_shell','romantic_code',
    'code_sonneter','poems_that_code','smokemirrors_code',
    'rand_forest_code','victorious_osx','silverline_cloud',
    'dentalfloss_ops','sailboat_coder','code_iron','carpet_code',
    'code_paramedic','code_council','code_launcher','cloaked_code'
    'octo_code','occupy_py','radiometer_code','bubblebath_tech',
    'sp4c3_invadr','nutella_ops','offthechain_proxy','touch_faith_txt',
    'tuxedo_tux','staples_ops','sourcream_potato','perrier_cto',
    'code_bbq_ssh','turtle_pwrshell','windows_windex','hotsprings_ops',
    'goat_code_hub','code_and_paste','dress_code','ctrlA_ops',
    'freshbaked_code','happyhr_coder','eula_hack','socialcode_ops',
    'hermit_code_ssh','plant_techsupport','happiness_boot_usb',
    'ethos_h2o_code','instantcofee_code','trenti_code','code_short_decaf',
    'trenta_exprs0','s0y_code_latte','reduce_reuse_recode',
    'c0de_3xp10r','wine_and_c0de','sourpatch_code','alleged_code',
    'git_pushups','code_stash_dash','c0d3_mut4ti0n5','jurassic_coder',
    'abdarainurus_code','triceratops_linux','pterodactlus_linux',
    'Peteinosaurus_ssh','Tanystropheus_code','vicksvapo_osx',
    'vitamin3_ops','b3t4_carotine_code','usr_Staurikosaurus',
    'Postosuchus_repo','Plateosaurus_osx','usr_Cynognathus',
    'Lystrosaurus_linux','cephalopod_ops','hunger_ftp','plinko_cto',
    'candy_ztables','hashes_and_dashes','codebreak_brachiopod',
    'c4ndy_appl3s_osx','theranos_Theropoda','milkshake_techops',
    'theCircle_cto','squarehub_usr','sayno2malware','locallysourcedcode',
    'home_code_depot','cloud_wifi','ssh_vendingmachine','skittles_cloud',
    'ducttape_cod3r','hibernating_c0d3','fastfoodcode','reboot_heels',
    'channel13_code','usr_asperagus','broccolli_files','hamcheese_ops',
    'countryclub_code','code_hallucinations','fishtank_repo',
    'finedining_codex','code_entrees','teatime_ops','coffee_ftp',
    'arcade_codes','del_fear','ssh_xfiles','agent_Scully',
    'aws_candycloud','parkbench_ops','codethelimo','textbookcoder',
    'alicewondr_codes','matriarch_c0d3','pulpc0d3fiction','codegump',
    'digitalc0d3club','recursv_elevetor','kleenex_tech_support',
    'numpy_m4tr1x','key_grepper78','wundrful_lifecode','lambda_silence',
    'saving_private_files','city_d3_code','localcodesupply','interstellar_c0d3',
    'rgb_code_mile','back2home_dir','whiplash_shell','codelights_rgb',
    'apocalypse_nope','code_momento','django_mango_usr','raideroflostdirectory',
    'sunset_blvd_code','path2c0d3glory','foss_code_avenger','code_be4tyx9',
    'dr_codel0v3','inglorius_imports','t0ycode_logs','br4v3coder','das_linux_boot',
    'codeprincess','good_bug_hunting','cod3indarain','dreamcode_requiem',
    'return_jedi_files','spacecode_odyss3y','eternal_bugfree','the_bug_hunt',
    'codecitiz3n','vertigo_code','amelia_codes','clockwork_ff6600'
    'fullmetal_code','ham1lt0n_codex','programa_mockingbird','sourcecode_metropolis',
    'cod3h4rd',


    'popcorn_techsupport','codechex0x0','diet_codex2',
    'codepops','tonytiger_code','herbs_spice_code',
    'captain_codecrunch','lasagna_codeA','cod3chanel_5',
    'localradio_code','baskinrobbins_code','usr_motorcycle',
    'neon_c0d3s','redherring_osx','scrabble_code','roboticshell',
    'codewithavue','occupymars_code','nhl_cup','nasdaq_dat',
    'famous_amos_cookies','durritos_bugos','code_mahal',
    'volkscoden','acute_code','pressStart_ops','holyc0d3cow',
    'discounted_code','windows_cleaner','solidstate_code',
    'elevator_codes','c0d3_x_chip5','cheese_cod3factory',
    'rce_toaster_exploit','rce_shower_exploit','caribbean_pirated',
    'medic0d3_hashes','c0d3_unions','freshfried_code','luxury_code',
    'farm2compiler','usb_designer','solidstate_ic3cr3am','code_confidential',
    'snatch_the_code','topgun_mlops','codedownfall','batman_codes',
    'csharp_sealops','casino_c0d3','truman_codeshow','code_labyrinth',
    'cod3rs_islands','fiddler_on_cpp','nickelc0d3back','guardians_of_code',
    'the_great_esc','grep_nemo','spiderman_codes_py','v4v3nd3tt4',
    'gonewith_rm_r','dialm4compile','kosher_code','trainscoding',
    'fargo_go','catchmycodesoutside','milliondollarcode','childrenofcode',
    'codeblade_runner','thegold_rust','deathlyhollowsdirectory','ben_hur_shell',
    'grand_bugapest_hotel','onthecodingfront','compilerinthewind',
    'lather_rinse_code','pwrshell_ridge','wagesofbash','bashofthetitans',
    'codetalesfiles','codemaxfury','trainmydragons','deadcod3society',
    'monsters_shell','java_jaws_film','toky0_drift_go','joanofassembly',
    'rockyroad_r','logan_credentials','c0d3_terminat0r','rush_rust',
    'fsharp_fiberoptics','anaconda_ponds','kettlewifi','code_kombucha',
    'codingstreams','plantwifi','oxygen_osx','tvremoteexecution',
    'latex_imports','westpalmdiet_code','https_grep','wizard0fwebasm',
    'bugsinthewild','bestline5ofc0d3','bug_exorci5t','codedumplings',
    'gr4p35ofwebsam','coolhandcod3r','danceswithwebassembly','aptget_code',
    'roastedredcoders','jellyfish_osx','sonic_mlops','holypyth0ntemple',
    'bekindrewindcode','blockbuster_tech','blackberry_cfo','codecalcculus',
    'phillych33secode','rce_tinder','royalbank0fpyth0n','p4lm7r33s_linux',
    'sears_code_catalogue','codematchmaker','readthedocs_docker',
    'code_hummus','chocolatecodepretzels','secularimportcode',
    'herpes_zip_file','hotchocolatecode','nestleqwikcode','codebraces',
    'awd_google_drive','jeep_java','code0fsi5terhood','spicegirls_ssh',
    'rce_hoverboard','csharp_wranglers','codeunderthest0rm',
    'lillipop_ops','rustontheranch','bashcodehere','julia_notebooks',
    'technicolorc0d3','basic_code','staysharp_c#','camila_caml',
    'cshell_byshore','carbonbasedcode','cduce_deux','rce_ceylon',
    'mariokartdart','dartmart','darwin_evo_ops','rx_ecmascript',
    'fsharp_bflat','refact0rtractor','ffp_or3','honeyglazed_gams',
    'gangsta_gcode','genie_in_file','j0rjigogo','code_harb0ur',
    'haggis_code','ibm_tech_ops','jsharpjcool','jaithechai',
    'kixtart_twix','sn4k3s_ladd3rs','lassosomecode','chocolavacode',
    'legoscript_scrolls','ponds_lillypond','zelda_linc_ssh',
    'm4rmulatanglang','m#_3flat','codemad_i','magma_osx','holymarycode',
    'matlab_secrets','maudesys_admin','netlegolago','lysol_code_wipes',
    'netdotdata','petsdotcom_tech','oaktreecode','ober0n_ops','objectcrisp',
    'obj_pascal_empty','workout0bliqs','pascal_script_poems','cascade_dishops',
    'perlygates','php_shrimp','rplusplus_0','cod3racket','raku4you','slang_tang',
    'scalaholla','scratchnsniff','codegelato','scriptdotnettypot','nfl_tacl',
    'tidytadspods','ubercode_eats','telcomp_compress','vala_lala','vim_cleaner_ops',
    'gijoe_cobra_code','visul_dataflexbox','webdna_admin','zebra_zpl','zeno_eno_io'
    'whata_haskell','wolframatmidnight','mojo_os',

    'verykissstartswithcode','rce_allergies','sleep_ops','oldtestament_code',
    'newtestament_code','sephora_tech_support','oldnavy_mlops','cinnamon_code',
    'frenchtoast_exploit','egghack_exploit','scrambled_hash','codechemistryset',
    'playdoh_code_io','sql_siliconinjection','oceanspray_tech','expox86_tech',
    'disneypark_py','codemeditations','nyc_subway_ops','loreal_tech','codetherapy',
    'rce_doorbell_exploit','mentalcodehealth','facelift_exploitcode',
    'mozilla_ftp','yahoo_coder','daycare4code','pepperoni_compiler',
    'seabornlandcoded','bloomingdotonion','karlmarx_osx','htmlfamilynodes',
    'hello_c0d3fresh','rustynails','cannescodefest','programmingoffplanet',
    'polkadots_io','cuddlycoder','riceandcsharp','joinmycobol','cobaltcobol',
    'madeintor_onion','sudokumatrix','nda_clojure','emacsbigmac',
    
    
    'nimslimjam','javalavacode','elixir_mixer','olay_tech','sillysilicon',
    'workstation_90','z3r0daybrownies','siliconchips_xl',
    'eggsbacon_exe','kidney_py','chickensoup_cpp','dontbe_awk',
    'crazy_BAT','ASPenNet','throw_dart','users_dmg','fantasy_img',
    'future_exs','flava_flv','stop_dot_go','users_gzip','bluesky_jpeg',
    'cookie_jar','jasons_json','pegs_jpegs','kivy_key_pie',
    'moola_lua','matlab_mfile','markdown_md','mini_mdi','moo_mov',
    'wolfram_tapioca','fuji_film','HP_printer_cmd','portable_pdf',
    'tmi_pdi','frozen_coffee','dills_pkl','platypus_pl','apache_tomcat',
    'apache_maven','slides_pptx','google_protocols','plasma_prp',
    'adobe_postscript','photoshop_psd','photocloud_psdc','archive_pst',
    'protools_ptf','quicktime_qt','radiance_rad','remote_access_lang',
    'ampl_run','safe_saif','spss_sav','scratch_sb3','scriptbasic_sbh',
    'aaa_batteries','shakeshack_shell','walrus_tusks','kgb_blt',
    'assassins_sandwich','froyo_ops','tactical_waterballoon',
    'buffalocodewings','buffermatrix','siri_alexa_ops',
    'spyonabudget','buttercups_hiccups','ironchef_codes',
    'showtime_code','feathers_tar','virtualuser','visualbasic_vbr',
    'floppy_bird',
    
    
    'arbys_beef','auntie_anne','burgerking_mlops','carlsjr_admin',
    'chipolte_bowl_ops','cinnabon_tech','dairyqueen_mlops',
    'dunkincodedonuts','fivegals_code','hardees_menu','jollibee_code',
    'lilcaesars_code','mcdonalds_arches','pizza_tech_hut',
    'popeyes_recipes','redlobster_shell','sbarro_slice',
    'starbucks_coder','codesubway','tacocodebell','timhortons_ops',
    'whitecastle_admin','wingstop_exe','shesburger_ops','frenchbread_code',
    'boosterjuice_code','coffeecodetime','code_freshii','harveys_code',
    'newyorkfries_ops','pitapit_py','yogenfruz_code','applebees_dot_c',
    'atlantabread_code','bajafresh_bash','benihanna_ops','blimpie_cpp',
    'bostonmarket_exe','cheesecakefactory_exe','davebusters_tech',
    'deltaco_dot_go','elpolloloco_go','panda3xp_exe','panerabread_ops',
    'orangejulius_mlops','spaghettifactory_new','nathansfamous_password',
    'mrsfields_password','manchuwok_tech','krispycode','justsaladcode',
    'jackinthebox_ops','ihop_flop','sonic_devops','tacobell_dev',
    'tgi_codes','wafflehouse_ssh','lightbulb_tech','crystalgems',

    'steak_potatoes','code_omelet','code_olives','pinkhair',
    'cabbager0lls','herb_garden','windycode','c0d3tiles',
    'rainbowblaster','gryffindoor_code','ravenclaw_club',
    'hufflepuff_smurf','undercover_code','silkycode',


    'jewelspider','spider_orbw3b','tasmanian_sp1d3r',
    'trapd00r_spider','netcasting_spider','sp1dercave',
    'p1ratespider','spitting_cobra','prodigycode',
    'centipede_rss','lizards_rds','tattoocoder',

    # star trek characters
    'lt_saavik','dr_crusher','deanna_tr0i','airiam_cyb0rg',
    'captain_archer','soji_asha',"B'Etor",'brunt_fca','gabrielle_burnham',
    'chakotay_voyager','majel_barrett','christine_chapel','kimara_cretak',
    'dr_culber','jal_culluh','ezri_dax','degra_xindi','keyla_detmer',
    'elnor','philippa_georgiou','sonya_gomez','gowron_klingon',
    'guinen_el_aurian','erika_hernandez','hugh_borg','iska_ferengi',
    'katheryn_janeway','agnes_hurati',"B'Ehleyr_klingon",'kes_ocampa',
    'kira_nerys','laan_noonien_singh','laris_romulan','leeta_bajoran',
    'gabriel_lorca','lore_android',"L'Reil_klingon",'lursa_klingon',
    'carol_marcus','beckett_mariner','martok_klingon','dr_mcCoy',
    'mezoti_norcadian','mila_cardassian','mara_pol','raffi_muskiker',
    'narek_romulan','alynna_nechayev','neelix_talaxian','nhan_barzan',
    'susan_nicoletti','nilsson_humanoid','keiko_obrien','molly_obrien',
    'alyssa_olgawa','opaka_sulan','joann_owosekun','phlox_denobulan',
    'renee_picard','chris_pike','tracy_pollard','katherine_pulaski',
    'janice_rand','rebi_wysanti','jet_reno','gen_rhys','chris_rios',
    'narissa_rizzo','ro_laren','saavik_vulcan','sarek_vulcan','saru_kelpien',
    'hoshi_sato','sela_romulan','seska_cardassian','7ofnine','m_scott',
    'shakaar_edon','thylek_shran','silik_sulliban','jennifer_sisko',
    'sarah_sisko','soval_vulcan','spock_vulcan','stamets_science','lon_sudar',
    'hikaru_sulu','enabran_tain','sylvia_tilly','tomalak_romulan','tora_ziyal',
    'bElanna_torres','tpol_vulcan','the_traveler','deanna_troi','lwaxana_troi',
    'tuvok_vulcan','ash_tyler','nyota_uhura','una_human','vash_human',
    'weyoun_vorta','naomi_wildman','winn_adami','tasha_yar','kasidy_yates','zhaban_romulan',



    # emojis
    'skeleton_1f480',':coffin_26b0','ghost_1f47b',
    'candy_1f36c','birthdaycake_1f382','chocolatebar_1f36b',
    'banana_1f34c','cherries_1f352','avocado_1f951',
    'burrito_1f32f','hotpepper_1f336','cactus_1f335',
    'herb_1f33f','broccoli_1f966','greenapple_1f34f',
    'greenheart_1f49a','recycle_267b','fire_1f525',
    'cannedfood_1f96b','battery_1f50b','magnet_1f9f2',
    'compass_1f9ed','sailboat_26f5','waterwave_1f30a',
    'penguin_1f427','eagle_1f985','beaver_1f9ab',
    'sparkles_2728','star_2b50','whiteheart_1f90d',
    ''



]






print("""




##  ##                                              
##  ##                                              
##  ##  ###   ###  # ## # ##   ###   # ## ##   ###  
##  ## ## ## ## ## ###  ## ## #  ##  ## ## ## ## ## 
##  ##  ###  ##### ##   ## ##  ####  ## ## ## ##### 
##  ##    ## ##    ##   ## ## ## ##  ## ## ## ##    
##  ## ## ## ## ## ##   ## ## ## ##  ## ## ## ## ## 
 ####   ###   ###  ##   ## ##  ## ## ## ## ##  ###  
""")

# print( len(username) ) # 1030

x = random.randint(1, len(username))

print("----------------------------------------------")
print(f"\t {username[x]} ")
print("----------------------------------------------\n")