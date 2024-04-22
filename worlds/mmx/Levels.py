
from worlds.AutoWorld import World
from .Names import LocationName

location_id_to_level_id = {
    LocationName.intro_completed:                   [0x00, 0x007, 0x00],
    LocationName.intro_mini_boss_1:                 [0x03, 0x000, 0x1C],
    LocationName.intro_mini_boss_2:                 [0x03, 0x000, 0x1D],

    LocationName.armored_armadillo_boss:            [0x03, 0x000, 0x00],
    LocationName.armored_armadillo_clear:           [0x03, 0x001, 0x04],
    LocationName.armored_armadillo_sub_tank:        [0x03, 0x004, 0x20],
    LocationName.armored_armadillo_heart_tank:      [0x03, 0x002, 0x02],
    LocationName.armored_armadillo_hadouken:        [0x03, 0x005, 0x00],
    LocationName.armored_armadillo_mini_boss_1:     [0x03, 0x000, 0x15],
    LocationName.armored_armadillo_mini_boss_2:     [0x03, 0x000, 0x16],

    LocationName.chill_penguin_boss:                [0x08, 0x000, 0x01],
    LocationName.chill_penguin_clear:               [0x08, 0x001, 0x0E],
    LocationName.chill_penguin_legs:                [0x08, 0x003, 0x08],
    LocationName.chill_penguin_heart_tank:          [0x08, 0x002, 0x01],

    LocationName.spark_mandrill_boss:               [0x06, 0x000, 0x02],
    LocationName.spark_mandrill_clear:              [0x06, 0x001, 0x0A],
    LocationName.spark_mandrill_sub_tank:           [0x06, 0x004, 0x40],
    LocationName.spark_mandrill_heart_tank:         [0x06, 0x002, 0x40],
    LocationName.spark_mandrill_mini_boss:          [0x06, 0x000, 0x17],

    LocationName.launch_octopus_boss:               [0x01, 0x000, 0x03],
    LocationName.launch_octopus_clear:              [0x01, 0x001, 0x00],
    LocationName.launch_octopus_heart_tank:         [0x01, 0x002, 0x80],
    LocationName.launch_octopus_mini_boss_1:        [0x01, 0x000, 0x18],
    LocationName.launch_octopus_mini_boss_2:        [0x01, 0x000, 0x19],
    LocationName.launch_octopus_mini_boss_3:        [0x01, 0x000, 0x1A],
    LocationName.launch_octopus_mini_boss_4:        [0x01, 0x000, 0x1B],

    LocationName.boomer_kuwanger_boss:              [0x07, 0x000, 0x04],
    LocationName.boomer_kuwanger_clear:             [0x07, 0x001, 0x0C],
    LocationName.boomer_kuwanger_heart_tank:        [0x07, 0x002, 0x20],
    
    LocationName.sting_chameleon_boss:              [0x02, 0x000, 0x05],
    LocationName.sting_chameleon_clear:             [0x02, 0x001, 0x02],
    LocationName.sting_chameleon_body:              [0x02, 0x003, 0x04],
    LocationName.sting_chameleon_heart_tank:        [0x02, 0x002, 0x08],

    LocationName.storm_eagle_boss:                  [0x05, 0x000, 0x06],
    LocationName.storm_eagle_clear:                 [0x05, 0x001, 0x08],
    LocationName.storm_eagle_sub_tank:              [0x05, 0x004, 0x10],
    LocationName.storm_eagle_heart_tank:            [0x05, 0x002, 0x04],
    LocationName.storm_eagle_helmet:                [0x05, 0x003, 0x01],

    LocationName.flame_mammoth_boss:                [0x04, 0x000, 0x07],
    LocationName.flame_mammoth_clear:               [0x04, 0x001, 0x06],
    LocationName.flame_mammoth_sub_tank:            [0x04, 0x004, 0x80],
    LocationName.flame_mammoth_heart_tank:          [0x04, 0x002, 0x10],
    LocationName.flame_mammoth_arms:                [0x04, 0x003, 0x02],

    LocationName.sigma_fortress_1_bospider:         [0x09, 0x000, 0x08],
    LocationName.sigma_fortress_1_vile:             [0x09, 0x000, 0x09],
    LocationName.sigma_fortress_1_boomer_kuwanger:  [0x09, 0x000, 0x0A],

    LocationName.sigma_fortress_2_chill_penguin:    [0x0A, 0x000, 0x0B],
    LocationName.sigma_fortress_2_storm_eagle:      [0x0A, 0x000, 0x0C],
    LocationName.sigma_fortress_2_rangda_bangda:    [0x0A, 0x000, 0x0D],

    LocationName.sigma_fortress_3_armored_armadillo:[0x0B, 0x000, 0x0E],
    LocationName.sigma_fortress_3_sting_chameleon:  [0x0B, 0x000, 0x0F],
    LocationName.sigma_fortress_3_spark_mandrill:   [0x0B, 0x000, 0x10],
    LocationName.sigma_fortress_3_launch_octopus:   [0x0B, 0x000, 0x11],
    LocationName.sigma_fortress_3_flame_mammoth:    [0x0B, 0x000, 0x12],
    LocationName.sigma_fortress_3_d_rex:            [0x0B, 0x000, 0x1E],

    LocationName.sigma_fortress_4_velguarder:       [0x0C, 0x000, 0x13],
    LocationName.sigma_fortress_4_sigma:            [0x0C, 0x006, 0x14],
}
