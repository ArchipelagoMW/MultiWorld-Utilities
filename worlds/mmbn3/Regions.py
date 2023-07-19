import typing
from .Names.LocationName import LocationName


class RegionName:
    Menu = "Menu"
    ACDC_Overworld = "ACDC Overworld"
    ACDC_Cyberworld = "ACDC Cyberworld"
    SciLab_Overworld = "SciLab Overworld"
    SciLab_Cyberworld = "SciLab Cyberworld"
    Yoka_Overworld = "Yoka Overworld"
    Yoka_Cyberworld = "Yoka Cyberworld"
    Beach_Overworld = "Beach Overworld"
    Beach_Cyberworld = "Beach Cyberworld"
    Undernet = "Undernet"
    Deep_Undernet = "Deep Undernet"
    Secret_Area = "Secret Area"
    WWW_Island = "WWW Island"


class RegionInfo:
    name: str
    connections: typing.List[str]
    locations: typing.List[str]

    def __init__(self, name, connections, locations):
        self.name = name
        self.connections = connections
        self.locations = locations


regions = [
    RegionInfo(RegionName.Menu, [RegionName.ACDC_Overworld], []),
    RegionInfo(RegionName.ACDC_Overworld,
               [RegionName.ACDC_Cyberworld, RegionName.SciLab_Overworld, RegionName.Yoka_Overworld, RegionName.Beach_Overworld],
               [
                    LocationName.ACDC_SonicWav_W_Trade,
                    LocationName.ACDC_Bubbler_C_Trade,
                    LocationName.ACDC_Recov120_S_Trade,
                    LocationName.ACDC_School_Desk,
                    LocationName.ACDC_Class_5B_Bookshelf,
                    LocationName.School_1_Entrance_BMD,
                    LocationName.School_1_North_Central_BMD,
                    LocationName.School_1_Far_West_BMD_2,
                    LocationName.School_1_KeyDataA_BMD,
                    LocationName.School_1_KeyDataB_BMD,
                    LocationName.School_1_KeyDataC_BMD,
                    LocationName.School_2_South_BMD,
                    LocationName.School_2_Entrance_BMD,
                    LocationName.School_2_Mainframe_BMD,
                    LocationName.School_2_CodeA_BMD,
                    LocationName.School_2_CodeB_BMD,
                    LocationName.School_2_CodeC_BMD,
                    LocationName.ACDC_Dog_House_BMD,
                    LocationName.ACDC_Lans_Security_Panel_BMD,
                    LocationName.ACDC_Yais_Phone_BMD,
                    LocationName.ACDC_NumberMan_Display_BMD,
                    LocationName.ACDC_Tank_BMD_1,
                    LocationName.ACDC_Tank_BMD_2,
                    LocationName.ACDC_School_Server_BMD_1,
                    LocationName.ACDC_School_Server_BMD_2,
                    LocationName.ACDC_School_Blackboard_BMD,
                    LocationName.Numberman_Code_01,
                    LocationName.Numberman_Code_02,
                    LocationName.Numberman_Code_03,
                    LocationName.Numberman_Code_04,
                    LocationName.Numberman_Code_05,
                    LocationName.Numberman_Code_06,
                    LocationName.Numberman_Code_07,
                    LocationName.Numberman_Code_08,
                    LocationName.Numberman_Code_09,
                    LocationName.Numberman_Code_10,
                    LocationName.Numberman_Code_11,
                    LocationName.Numberman_Code_12,
                    LocationName.Numberman_Code_13,
                    LocationName.Numberman_Code_14,
                    LocationName.Numberman_Code_15,
                    LocationName.Numberman_Code_16,
                    LocationName.Numberman_Code_17,
                    LocationName.Numberman_Code_18,
                    LocationName.Numberman_Code_19,
                    LocationName.Numberman_Code_20,
                    LocationName.Numberman_Code_21,
                    LocationName.Numberman_Code_22,
                    LocationName.Numberman_Code_23,
                    LocationName.Numberman_Code_24,
                    LocationName.Numberman_Code_25,
                    LocationName.Numberman_Code_26,
                    LocationName.Numberman_Code_27,
                    LocationName.Numberman_Code_28,
                    LocationName.Numberman_Code_29,
                    LocationName.Numberman_Code_30,
                    LocationName.Numberman_Code_31,
                    LocationName.Mayls_HP_BMD,
                    LocationName.Yais_HP_BMD_1,
                    LocationName.Yais_HP_BMD_2,
                    LocationName.Dexs_HP_BMD_1,
                    LocationName.Dexs_HP_BMD_2,
                    LocationName.Mayls_HP_PMD
                    ]),
    RegionInfo(RegionName.ACDC_Cyberworld,
               [RegionName.SciLab_Cyberworld, RegionName.Yoka_Cyberworld, RegionName.Beach_Cyberworld],
               [
                    LocationName.ACDC_1_Southwest_BMD,
                    LocationName.ACDC_1_Northeast_BMD,
                    LocationName.ACDC_1_PMD,
                    LocationName.ACDC_2_Center_BMD,
                    LocationName.ACDC_2_North_BMD,
                    LocationName.ACDC_3_Southwest_BMD,
                    LocationName.ACDC_3_Northeast_BMD,
                ]),
    RegionInfo(RegionName.SciLab_Overworld,
               [RegionName.SciLab_Cyberworld, RegionName.ACDC_Overworld, RegionName.Yoka_Overworld, RegionName.Beach_Overworld],
               [
                    LocationName.SciLab_Shake1_S_Trade,
                    LocationName.SciLab_Garbage_Can,
                    LocationName.SciLab_Vending_Machine_BMD,
                    LocationName.SciLab_Virus_Lab_Door_BMD_1,
                    LocationName.SciLab_Virus_Lab_Door_BMD_2,
                    LocationName.SciLab_Dads_Computer_BMD,
                    LocationName.SciLab_Dads_Computer_PMD,
                    LocationName.Please_deliver_this,
                    LocationName.My_Navi_is_sick,
                    LocationName.Help_me_with_my_son,
                    LocationName.Transmission_error,
                    LocationName.Chip_Prices,
                    LocationName.Im_broke,
                    LocationName.Rare_chips_for_cheap,
                    LocationName.Be_my_boyfriend,
                    LocationName.Will_you_deliver,
                    #LocationName.Look_for_friends,
                    #LocationName.Stuntmen_wanted,
                    #LocationName.Riot_stopped,
                    #LocationName.Gathering_Data,
                    LocationName.Somebody_please_help,
                    LocationName.Looking_for_condor,
                    LocationName.Help_with_rehab,
                    LocationName.Old_Master,
                    LocationName.Catching_gang_members,
                    LocationName.Please_adopt_a_virus,
                    LocationName.Legendary_Tomes,
                    LocationName.Legendary_Tomes_Treasure,
                    LocationName.Hide_and_seek_First_Child,
                    LocationName.Hide_and_seek_Second_Child,
                    LocationName.Hide_and_seek_Third_Child,
                    LocationName.Hide_and_seek_Fourth_Child,
                    LocationName.Hide_and_seek_Completion,
                    LocationName.Finding_the_blue_Navi,
                    LocationName.Give_your_support,
                    LocationName.Stamp_collecting,
                    LocationName.Help_with_a_will
                ]),
    RegionInfo(RegionName.SciLab_Cyberworld,
               [RegionName.ACDC_Cyberworld, RegionName.Yoka_Cyberworld, RegionName.Beach_Cyberworld,RegionName.Deep_Undernet],
               [
                    LocationName.SciLab_1_East_BMD,
                    LocationName.SciLab_1_WWW_BMD,
                    LocationName.SciLab_2_South_BMD,
                    LocationName.SciLab_2_West_BMD
                ]),
    RegionInfo(RegionName.Yoka_Overworld,
               [RegionName.Yoka_Cyberworld, RegionName.ACDC_Overworld, RegionName.SciLab_Overworld, RegionName.Beach_Overworld, RegionName.Secret_Area],
               [
                    LocationName.Yoka_Mr_Quiz,
                    LocationName.Yoka_Quiz_Master,
                    LocationName.Yoka_FireSwrd_P_Trade,
                    LocationName.Yoka_Inn_Jars,
                    LocationName.Yoka_Zoo_Garbage,
                    LocationName.Zoo_Panda_PMD,
                    LocationName.Zoo_1_East_BMD,
                    LocationName.Zoo_1_North_BMD,
                    LocationName.Zoo_1_Central_BMD,
                    LocationName.Zoo_2_East_BMD,
                    LocationName.Zoo_2_Central_BMD,
                    LocationName.Zoo_2_West_BMD,
                    LocationName.Zoo_3_North_BMD,
                    LocationName.Zoo_3_Central_BMD,
                    LocationName.Zoo_3_Path_BMD,
                    LocationName.Zoo_3_Northwest_BMD,
                    LocationName.Zoo_4_West_BMD,
                    LocationName.Zoo_4_Northwest_BMD,
                    LocationName.Zoo_4_Southeast_BMD,
                    LocationName.Yoka_TV_BMD,
                    LocationName.Yoka_Armor_BMD,
                    LocationName.Yoka_Hot_Spring_BMD,
                    LocationName.Yoka_Ticket_Machine_BMD,
                    LocationName.Yoka_Giraffe_BMD,
                    LocationName.Yoka_Panda_BMD,
                    LocationName.Tamakos_HP_BMD,
                    LocationName.Tamakos_HP_PMD,
                    LocationName.Comedian,
                    LocationName.Chocolate_Shop_01,
                    LocationName.Chocolate_Shop_02,
                    LocationName.Chocolate_Shop_03,
                    LocationName.Chocolate_Shop_04,
                    LocationName.Chocolate_Shop_05,
                    LocationName.Chocolate_Shop_06,
                    LocationName.Chocolate_Shop_07,
                    LocationName.Chocolate_Shop_08,
                    LocationName.Chocolate_Shop_09,
                    LocationName.Chocolate_Shop_10,
                    LocationName.Chocolate_Shop_11,
                    LocationName.Chocolate_Shop_12,
                    LocationName.Chocolate_Shop_13,
                    LocationName.Chocolate_Shop_14,
                    LocationName.Chocolate_Shop_15,
                    LocationName.Chocolate_Shop_16,
                    LocationName.Chocolate_Shop_17,
                    LocationName.Chocolate_Shop_18,
                    LocationName.Chocolate_Shop_19,
                    LocationName.Chocolate_Shop_20,
                    LocationName.Chocolate_Shop_21,
                    LocationName.Chocolate_Shop_22,
                    LocationName.Chocolate_Shop_23,
                    LocationName.Chocolate_Shop_24,
                    LocationName.Chocolate_Shop_25,
                    LocationName.Chocolate_Shop_26,
                    LocationName.Chocolate_Shop_27,
                    LocationName.Chocolate_Shop_28,
                    LocationName.Chocolate_Shop_29,
                    LocationName.Chocolate_Shop_30,
                    LocationName.Chocolate_Shop_31,
                    LocationName.Chocolate_Shop_32
                ]),
    RegionInfo(RegionName.Yoka_Cyberworld,
               [RegionName.ACDC_Cyberworld, RegionName.SciLab_Cyberworld, RegionName.Beach_Cyberworld],
               [
                    LocationName.Yoka_1_North_BMD,
                    LocationName.Yoka_1_WWW_BMD,
                    LocationName.Yoka_1_PMD,
                    LocationName.Yoka_2_Lower_BMD,
                    LocationName.Yoka_2_Upper_BMD,
                ]),
    RegionInfo(RegionName.Beach_Overworld,
               [RegionName.ACDC_Overworld, RegionName.SciLab_Overworld, RegionName.Yoka_Overworld, RegionName.WWW_Island],
               [
                    LocationName.Hospital_Quiz_Queen,
                    LocationName.Hades_Quiz_King,
                    LocationName.Hospital_DynaWav_V_Trade,
                    LocationName.Beach_DNN_WideSwrd_C_Trade,
                    LocationName.Beach_DNN_HoleMetr_H_Trade,
                    LocationName.Beach_DNN_Shadow_J_Trade,
                    LocationName.Hades_GrabBack_K_Trade,
                    #LocationName.Mod_Tools_Guy,
                    LocationName.Beach_Department_Store,
                    LocationName.Beach_Hospital_Plaque,
                    LocationName.Beach_Hospital_Pink_Door,
                    LocationName.Beach_Hospital_Tree,
                    LocationName.Beach_Hospital_Hidden_Conversation,
                    LocationName.Beach_Hospital_Girl,
                    LocationName.Beach_DNN_Kiosk,
                    LocationName.Beach_DNN_Boxes,
                    LocationName.Beach_DNN_Poster,
                    LocationName.Hades_Boat_Dock,
                    LocationName.Hades_South_BMD,
                    LocationName.Hades_Gargoyle_BMD,
                    LocationName.Hospital_1_North_BMD,
                    LocationName.Hospital_1_West_BMD,
                    LocationName.Hospital_1_Center_BMD,
                    LocationName.Hospital_2_Island_BMD,
                    LocationName.Hospital_2_Central_BMD,
                    LocationName.Hospital_2_Southwest_BMD,
                    LocationName.Hospital_3_West_BMD,
                    LocationName.Hospital_3_Central_BMD,
                    LocationName.Hospital_3_Northwest_BMD,
                    LocationName.Hospital_4_North_BMD,
                    LocationName.Hospital_4_Central_BMD,
                    LocationName.Hospital_4_Southeast_BMD,
                    LocationName.Hospital_5_Island_BMD,
                    LocationName.Hospital_5_Northeast_BMD,
                    LocationName.Hospital_5_Southwest_BMD,
                    LocationName.Beach_Hospital_Bed_BMD,
                    LocationName.Beach_TV_BMD,
                    LocationName.Beach_Vending_Machine_BMD,
                    LocationName.Beach_News_Van_BMD,
                    LocationName.Beach_Battle_Console_BMD,
                    LocationName.Beach_Security_System_BMD,
                    LocationName.Beach_Broadcast_Computer_BMD,
                    LocationName.Beach_DNN_Security_Panel_PMD,
                    LocationName.Beach_DNN_Main_Console_PMD,
                    LocationName.Undernet_6_TV_BMD
                ]),
    RegionInfo(RegionName.Beach_Cyberworld,
               [RegionName.ACDC_Cyberworld, RegionName.SciLab_Cyberworld, RegionName.Yoka_Cyberworld, RegionName.Undernet],
               [
                    LocationName.Beach_1_BMD,
                    LocationName.Beach_1_PMD,
                    LocationName.Beach_2_East_BMD,
                    LocationName.Beach_2_West_BMD,
                    LocationName.Villain
                ]),
    RegionInfo(RegionName.Undernet,
               [],
               [
                    LocationName.Undernet_1_South_BMD,
                    LocationName.Undernet_1_WWW_BMD,
                    LocationName.Undernet_2_Lower_BMD,
                    LocationName.Undernet_2_Upper_BMD,
                    LocationName.Undernet_3_South_BMD,
                    LocationName.Undernet_3_Central_BMD,
                    LocationName.Undernet_4_Pillar_Prog,
                    LocationName.Undernet_4_Top_North_BMD,
                    LocationName.Undernet_4_Bottom_West_BMD,
                    LocationName.Undernet_4_Top_Pillar_BMD,
                    LocationName.Undernet_5_Upper_BMD

                ]),
    RegionInfo(RegionName.Deep_Undernet,
               [],
               [
                    LocationName.Undernet_5_Lower_BMD,
                    LocationName.Undernet_6_East_BMD,
                    LocationName.Undernet_6_Central_BMD,
                    LocationName.Undernet_7_PMD,
                    LocationName.Undernet_7_West_BMD,
                    LocationName.Undernet_7_Northeast_BMD,
                    LocationName.Undernet_7_Northwest_BMD,
                    LocationName.Undernet_7_Upper_BMD,
                ]),
    RegionInfo(RegionName.WWW_Island,
               [],
               [
                    LocationName.WWW_Control_Room_1_Screen,
                    LocationName.WWW_Wilys_Desk,
                    LocationName.WWW_Wall_BMD,
                    LocationName.WWW_1_East_BMD,
                    LocationName.WWW_1_West_BMD,
                    LocationName.WWW_1_Central_BMD,
                    #LocationName.WWW_1_South_BMD,
                    LocationName.WWW_2_East_BMD,
                    LocationName.WWW_2_Northwest_BMD,
                    #LocationName.WWW_2_West_BMD,
                    LocationName.WWW_3_East_BMD,
                    LocationName.WWW_3_North_BMD,
                    #LocationName.WWW_3_South_BMD,
                    LocationName.WWW_4_Central_BMD,
                    LocationName.WWW_4_Northwest_BMD,
                    #LocationName.WWW_4_East_BMD
                    LocationName.Alpha_Defeated
                ]),
    RegionInfo(RegionName.Secret_Area,
               [],
               [
                    LocationName.Secret_1_South_BMD,
                    LocationName.Secret_1_Northeast_BMD,
                    LocationName.Secret_1_Northwest_BMD,
                    LocationName.Secret_2_Island_BMD,
                    LocationName.Secret_2_Lower_BMD,
                    LocationName.Secret_2_Upper_BMD,
                    LocationName.Secret_3_Island_BMD,
                    LocationName.Secret_3_South_BMD,
                    LocationName.Secret_3_BugFrag_BMD
                ])
]
