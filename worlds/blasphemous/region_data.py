# This file is programmatically generated, do not modify by hand


regions = [
    {
        "name": "Menu",
        "exits": [],
        "locations": [
            "QI106",
            "QI107",
            "QI108",
            "QI109",
            "QI110",
            "PR101",
            "QI32",
            "QI33",
            "QI34",
            "QI35",
            "QI79",
            "QI80",
            "QI81",
            "Arena_NailManager[1000]",
            "HE10",
            "Arena_NailManager[3000]",
            "RB34",
            "Arena_NailManager[5000]",
            "RB35",
            "RB36",
            "COMBO_1",
            "COMBO_2",
            "COMBO_3",
            "CHARGED_1",
            "CHARGED_2",
            "CHARGED_3",
            "RANGED_1",
            "RANGED_2",
            "RANGED_3",
            "VERTICAL_1",
            "VERTICAL_2",
            "VERTICAL_3",
            "LUNGE_1",
            "LUNGE_2",
            "LUNGE_3"
        ],
        "transitions": []
    },
    {
        "name": "D01Z01S07",
        "exits": [
            {
                "target": "D01Z01S07[W]",
                "logic": []
            },
            {
                "target": "D01Z01S07[E]",
                "logic": []
            }
        ],
        "locations": [
            "QI31"
        ],
        "transitions": []
    },
    {
        "name": "D01Z01S01[W]",
        "exits": [
            {
                "target": "D01Z01S07",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z01S01[W]"
        ]
    },
    {
        "name": "D17Z01S03[E]",
        "exits": [
            {
                "target": "D01Z01S07",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D17Z01S03[E]"
        ]
    },
    {
        "name": "D01Z01S02",
        "exits": [
            {
                "target": "D01Z01S02[W]",
                "logic": []
            },
            {
                "target": "D01Z01S02[E]",
                "logic": []
            }
        ],
        "locations": [
            "PR14",
            "RB07"
        ],
        "transitions": []
    },
    {
        "name": "D01Z01S01[E]",
        "exits": [
            {
                "target": "D01Z01S02",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z01S01[E]"
        ]
    },
    {
        "name": "D01Z01S03[W]",
        "exits": [
            {
                "target": "D01Z01S02",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z01S03[W]"
        ]
    },
    {
        "name": "D01Z06S01",
        "exits": [
            {
                "target": "D01Z06S01[N]",
                "logic": []
            },
            {
                "target": "D01Z06S01[Santos]",
                "logic": [
                    {
                        "item_requirements": [
                            "bell"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "QI101"
        ],
        "transitions": []
    },
    {
        "name": "D01Z01S01[S]",
        "exits": [
            {
                "target": "D01Z06S01",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z01S01[S]"
        ]
    },
    {
        "name": "D01BZ07S01[Santos]",
        "exits": [
            {
                "target": "D01Z06S01",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01BZ07S01[Santos]"
        ]
    },
    {
        "name": "D01Z01S02[W]",
        "exits": [
            {
                "target": "D01Z01S01[W]",
                "logic": []
            },
            {
                "target": "D01Z01S01[E]",
                "logic": []
            },
            {
                "target": "D01Z01S01[S]",
                "logic": [
                    {
                        "item_requirements": [
                            "canBreakHoles"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z01S02[W]"
        ]
    },
    {
        "name": "D01Z01S07[E]",
        "exits": [
            {
                "target": "D01Z01S01[W]",
                "logic": []
            },
            {
                "target": "D01Z01S01[E]",
                "logic": []
            },
            {
                "target": "D01Z01S01[S]",
                "logic": [
                    {
                        "item_requirements": [
                            "canBreakHoles"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z01S07[E]"
        ]
    },
    {
        "name": "D01Z06S01[N]",
        "exits": [
            {
                "target": "D01Z01S01[S]",
                "logic": []
            },
            {
                "target": "D01Z01S01[W]",
                "logic": []
            },
            {
                "target": "D01Z01S01[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z06S01[N]"
        ]
    },
    {
        "name": "D01Z01S03",
        "exits": [
            {
                "target": "D01Z01S03[W]",
                "logic": []
            },
            {
                "target": "D01Z01S03[E]",
                "logic": []
            }
        ],
        "locations": [
            "CO04",
            "QI55",
            "RESCUED_CHERUB_07"
        ],
        "transitions": []
    },
    {
        "name": "D01Z01S02[E]",
        "exits": [
            {
                "target": "D01Z01S03",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z01S02[E]"
        ]
    },
    {
        "name": "D01Z02S01[W]",
        "exits": [
            {
                "target": "D01Z01S03",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z02S01[W]"
        ]
    },
    {
        "name": "D01Z02S01",
        "exits": [
            {
                "target": "D01Z02S01[W]",
                "logic": []
            },
            {
                "target": "D01Z02S01[E]",
                "logic": []
            }
        ],
        "locations": [
            "RE02",
            "RE04",
            "RE10"
        ],
        "transitions": []
    },
    {
        "name": "D01Z01S03[E]",
        "exits": [
            {
                "target": "D01Z02S01",
                "logic": []
            },
            {
                "target": "RB06",
                "logic": [
                    {
                        "item_requirements": [
                            "ceremonyItems3",
                            "hatchedEgg"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z01S03[E]"
        ]
    },
    {
        "name": "D01Z02S02[W]",
        "exits": [
            {
                "target": "D01Z02S01",
                "logic": []
            },
            {
                "target": "RB06",
                "logic": [
                    {
                        "item_requirements": [
                            "ceremonyItems3",
                            "hatchedEgg"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z02S02[W]"
        ]
    },
    {
        "name": "D01Z01S07[W]",
        "exits": [
            {
                "target": "D17Z01S03[E]",
                "logic": []
            },
            {
                "target": "D17Z01S03[relic]",
                "logic": [
                    {
                        "item_requirements": [
                            "elderKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D17Z01S11[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z01S07[W]"
        ]
    },
    {
        "name": "D17Z01S11[E]",
        "exits": [
            {
                "target": "D17Z01S03[E]",
                "logic": []
            },
            {
                "target": "D17Z01S03[relic]",
                "logic": [
                    {
                        "item_requirements": [
                            "elderKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D17Z01S11",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D17Z01S11[E]",
            "D17Z01S03[W]"
        ]
    },
    {
        "name": "D17BZ01S01[relic]",
        "exits": [
            {
                "target": "D17Z01S03[E]",
                "logic": []
            },
            {
                "target": "D17Z01S03[relic]",
                "logic": [
                    {
                        "item_requirements": [
                            "elderKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D17Z01S11[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D17BZ01S01[relic]"
        ]
    },
    {
        "name": "D01Z02S02",
        "exits": [
            {
                "target": "D01Z02S02[SW]",
                "logic": []
            },
            {
                "target": "D01Z02S02[SE]",
                "logic": []
            },
            {
                "target": "D01Z02S02[W]",
                "logic": []
            },
            {
                "target": "D01Z02S02[E]",
                "logic": []
            },
            {
                "target": "D01Z02S02[NE]",
                "logic": []
            }
        ],
        "locations": [
            "RB01",
            "QI66",
            "Tirso[500]",
            "Tirso[1000]",
            "Tirso[2000]",
            "Tirso[5000]",
            "Tirso[10000]",
            "QI56"
        ],
        "transitions": []
    },
    {
        "name": "D01Z02S01[E]",
        "exits": [
            {
                "target": "D01Z02S02",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z02S01[E]"
        ]
    },
    {
        "name": "D01Z02S03[W]",
        "exits": [
            {
                "target": "D01Z02S02",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z02S03[W]"
        ]
    },
    {
        "name": "D01Z02S03[NW]",
        "exits": [
            {
                "target": "D01Z02S02",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z02S03[NW]"
        ]
    },
    {
        "name": "D01Z02S04[W]",
        "exits": [
            {
                "target": "D01Z02S02",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z02S04[W]"
        ]
    },
    {
        "name": "D01Z02S06[E]",
        "exits": [
            {
                "target": "D01Z02S02",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z02S06[E]"
        ]
    },
    {
        "name": "D01Z02S06",
        "exits": [
            {
                "target": "D01Z02S06[W]",
                "logic": []
            },
            {
                "target": "D01Z02S06[E]",
                "logic": []
            }
        ],
        "locations": [
            "Sword[D01Z02S06]"
        ],
        "transitions": []
    },
    {
        "name": "D01Z02S02[SW]",
        "exits": [
            {
                "target": "D01Z02S06",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z02S02[SW]"
        ]
    },
    {
        "name": "D01Z02S07[E]",
        "exits": [
            {
                "target": "D01Z02S06",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z02S07[E]"
        ]
    },
    {
        "name": "D01Z02S04",
        "exits": [
            {
                "target": "D01Z02S04[W]",
                "logic": []
            },
            {
                "target": "D01Z02S04[E]",
                "logic": []
            },
            {
                "target": "D01Z02S04[Ossary]",
                "logic": []
            }
        ],
        "locations": [
            "CO43"
        ],
        "transitions": []
    },
    {
        "name": "D01Z02S02[SE]",
        "exits": [
            {
                "target": "D01Z02S04",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z02S02[SE]"
        ]
    },
    {
        "name": "D01BZ06S01[Ossary]",
        "exits": [
            {
                "target": "D01Z02S04",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01BZ06S01[Ossary]"
        ]
    },
    {
        "name": "D01Z05S01[N]",
        "exits": [
            {
                "target": "D01Z02S04",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S01[N]"
        ]
    },
    {
        "name": "D01Z02S03",
        "exits": [
            {
                "target": "D01Z02S03[W]",
                "logic": []
            },
            {
                "target": "D01Z02S03[E]",
                "logic": []
            },
            {
                "target": "D01Z02S03[church]",
                "logic": [
                    {
                        "item_requirements": [
                            "canBeatMercyBoss"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canBeatConventBoss"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canBeatGrievanceBoss"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RESCUED_CHERUB_08",
                "logic": [
                    {
                        "item_requirements": [
                            "rodeGotPElevator"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "pillar"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "cante"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "Lvdovico[500]",
            "Lvdovico[1000]",
            "PR03"
        ],
        "transitions": []
    },
    {
        "name": "D01Z02S02[E]",
        "exits": [
            {
                "target": "D01Z02S03",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z02S02[E]"
        ]
    },
    {
        "name": "D01Z02S02[NE]",
        "exits": [
            {
                "target": "D01Z02S03",
                "logic": []
            },
            {
                "target": "D01Z02S03[NW]",
                "logic": []
            },
            {
                "target": "RESCUED_CHERUB_08",
                "logic": [
                    {
                        "item_requirements": [
                            "canCrossGap2"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "lorquiana"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "aubade"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "cantina"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "chargeBeam"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "rangedAttack"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z02S02[NE]"
        ]
    },
    {
        "name": "D01Z02S05[W]",
        "exits": [
            {
                "target": "D01Z02S03",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z02S05[W]"
        ]
    },
    {
        "name": "D01BZ04S01[church]",
        "exits": [
            {
                "target": "D01Z02S03",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01BZ04S01[church]"
        ]
    },
    {
        "name": "D02Z02S11[-Cherubs]",
        "exits": [
            {
                "target": "D01Z02S03",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z02S11[-Cherubs]"
        ]
    },
    {
        "name": "D01Z02S05",
        "exits": [
            {
                "target": "D01Z02S05[W]",
                "logic": []
            },
            {
                "target": "D01Z02S05[E]",
                "logic": []
            }
        ],
        "locations": [
            "CO16"
        ],
        "transitions": []
    },
    {
        "name": "D01Z02S03[E]",
        "exits": [
            {
                "target": "D01Z02S05",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z02S03[E]"
        ]
    },
    {
        "name": "D01Z03S01[W]",
        "exits": [
            {
                "target": "D01Z02S05",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z03S01[W]"
        ]
    },
    {
        "name": "D01BZ04S01",
        "exits": [
            {
                "target": "D01BZ04S01[church]",
                "logic": []
            }
        ],
        "locations": [
            "RB104",
            "RB105"
        ],
        "transitions": []
    },
    {
        "name": "D01Z02S03[church]",
        "exits": [
            {
                "target": "D01BZ04S01",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z02S03[church]"
        ]
    },
    {
        "name": "D01Z02S04[E]",
        "exits": [
            {
                "target": "D01Z05S01[N]",
                "logic": []
            },
            {
                "target": "D01Z05S02[N]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z02S04[E]"
        ]
    },
    {
        "name": "D01Z05S02[N]",
        "exits": [
            {
                "target": "D01Z05S01[N]",
                "logic": []
            },
            {
                "target": "D01Z05S02[W]",
                "logic": []
            },
            {
                "target": "D01Z05S02[S]",
                "logic": [
                    {
                        "item_requirements": [
                            "openedDCLadder"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S02[N]",
            "D01Z05S01[S]",
            "D01Z05S27[E]",
            "D01Z05S01[W]"
        ]
    },
    {
        "name": "D01BZ06S01",
        "exits": [
            {
                "target": "D01BZ06S01[Ossary]",
                "logic": []
            },
            {
                "target": "D01BZ06S01[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "bones30"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "Undertaker[250]",
            "Undertaker[500]",
            "Undertaker[750]",
            "Undertaker[1000]",
            "Undertaker[1250]",
            "Undertaker[1500]",
            "Undertaker[1750]",
            "Undertaker[2000]",
            "Undertaker[2500]",
            "Undertaker[3000]",
            "Undertaker[5000]"
        ],
        "transitions": []
    },
    {
        "name": "D01Z02S04[Ossary]",
        "exits": [
            {
                "target": "D01BZ06S01",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z02S04[Ossary]"
        ]
    },
    {
        "name": "D01BZ08S01[W]",
        "exits": [
            {
                "target": "D01BZ06S01",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01BZ08S01[W]"
        ]
    },
    {
        "name": "D01Z02S05[E]",
        "exits": [
            {
                "target": "D01Z03S01[W]",
                "logic": []
            },
            {
                "target": "D01Z03S01[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z02S05[E]"
        ]
    },
    {
        "name": "D01Z03S02[W]",
        "exits": [
            {
                "target": "D01Z03S01[W]",
                "logic": []
            },
            {
                "target": "D01Z03S01[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z03S02[W]"
        ]
    },
    {
        "name": "D01Z03S02[SW]",
        "exits": [
            {
                "target": "D01Z03S01[SE]",
                "logic": []
            },
            {
                "target": "D01Z03S01[W]",
                "logic": []
            },
            {
                "target": "D01Z03S01[E]",
                "logic": []
            }
        ],
        "locations": [
            "RB04"
        ],
        "transitions": [
            "D01Z03S02[SW]"
        ]
    },
    {
        "name": "D01Z02S07",
        "exits": [
            {
                "target": "D01Z02S07[E]",
                "logic": []
            }
        ],
        "locations": [
            "QI65"
        ],
        "transitions": []
    },
    {
        "name": "D01Z02S06[W]",
        "exits": [
            {
                "target": "D01Z02S07",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z02S06[W]"
        ]
    },
    {
        "name": "D01BZ08S01",
        "exits": [
            {
                "target": "D01BZ08S01[W]",
                "logic": []
            }
        ],
        "locations": [
            "QI201"
        ],
        "transitions": []
    },
    {
        "name": "D01BZ06S01[E]",
        "exits": [
            {
                "target": "D01BZ08S01",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01BZ06S01[E]"
        ]
    },
    {
        "name": "D01Z03S02",
        "exits": [
            {
                "target": "D01Z03S02[W]",
                "logic": []
            },
            {
                "target": "D01Z03S02[SW]",
                "logic": []
            },
            {
                "target": "D01Z03S02[E]",
                "logic": []
            }
        ],
        "locations": [
            "CO14"
        ],
        "transitions": []
    },
    {
        "name": "D01Z03S01[E]",
        "exits": [
            {
                "target": "D01Z03S02",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z03S01[E]"
        ]
    },
    {
        "name": "D01Z03S01[SE]",
        "exits": [
            {
                "target": "D01Z03S02",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z03S01[SE]"
        ]
    },
    {
        "name": "D01Z03S03[W]",
        "exits": [
            {
                "target": "D01Z03S02",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z03S03[W]"
        ]
    },
    {
        "name": "D01Z05S05[N]",
        "exits": [
            {
                "target": "D01Z03S02",
                "logic": []
            },
            {
                "target": "D01Z03S02[S]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S05[N]"
        ]
    },
    {
        "name": "D01Z03S03",
        "exits": [
            {
                "target": "D01Z03S03[W]",
                "logic": []
            },
            {
                "target": "D01Z03S03[E]",
                "logic": []
            },
            {
                "target": "D01Z03S03[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "CO36",
            "RESCUED_CHERUB_10"
        ],
        "transitions": []
    },
    {
        "name": "D01Z03S02[E]",
        "exits": [
            {
                "target": "D01Z03S03",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z03S02[E]"
        ]
    },
    {
        "name": "D01Z03S04[SW]",
        "exits": [
            {
                "target": "D01Z03S03",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z03S04[SW]"
        ]
    },
    {
        "name": "D01Z03S07[-Cherubs]",
        "exits": [
            {
                "target": "D01Z03S03",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z03S07[-Cherubs]"
        ]
    },
    {
        "name": "D01Z05S05",
        "exits": [
            {
                "target": "D01Z05S05[N]",
                "logic": []
            },
            {
                "target": "D01Z05S05[NW]",
                "logic": []
            },
            {
                "target": "D01Z05S05[NE]",
                "logic": []
            },
            {
                "target": "D01Z05S05[SW]",
                "logic": []
            },
            {
                "target": "D01Z05S05[E]",
                "logic": []
            }
        ],
        "locations": [
            "CO09",
            "QI67"
        ],
        "transitions": []
    },
    {
        "name": "D01Z03S02[S]",
        "exits": [
            {
                "target": "D01Z05S05",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z03S02[S]"
        ]
    },
    {
        "name": "D01Z05S04[E]",
        "exits": [
            {
                "target": "D01Z05S05",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S04[E]"
        ]
    },
    {
        "name": "D01Z05S06[W]",
        "exits": [
            {
                "target": "D01Z05S05",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S06[W]"
        ]
    },
    {
        "name": "D01Z05S09[NW]",
        "exits": [
            {
                "target": "D01Z05S05",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S09[NW]"
        ]
    },
    {
        "name": "D01Z05S18[E]",
        "exits": [
            {
                "target": "D01Z05S05",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S18[E]"
        ]
    },
    {
        "name": "D01Z03S03[E]",
        "exits": [
            {
                "target": "D01Z03S04[SW]",
                "logic": []
            },
            {
                "target": "D01Z03S04[W]",
                "logic": []
            },
            {
                "target": "D01Z03S04[SE]",
                "logic": []
            },
            {
                "target": "D01Z03S04[E]",
                "logic": []
            },
            {
                "target": "D02Z01S01[SE]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z03S03[E]"
        ]
    },
    {
        "name": "D01Z03S05[W]",
        "exits": [
            {
                "target": "D01Z03S04[SW]",
                "logic": []
            },
            {
                "target": "D01Z03S04[W]",
                "logic": []
            },
            {
                "target": "D01Z03S04[SE]",
                "logic": []
            },
            {
                "target": "D01Z03S04[E]",
                "logic": []
            },
            {
                "target": "D02Z01S01[SE]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z03S05[W]"
        ]
    },
    {
        "name": "D01Z03S06[W]",
        "exits": [
            {
                "target": "D01Z03S04[SW]",
                "logic": []
            },
            {
                "target": "D01Z03S04[W]",
                "logic": []
            },
            {
                "target": "D01Z03S04[SE]",
                "logic": []
            },
            {
                "target": "D01Z03S04[E]",
                "logic": []
            },
            {
                "target": "D02Z01S01[SE]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z03S06[W]"
        ]
    },
    {
        "name": "D01Z03S07[E]",
        "exits": [
            {
                "target": "D01Z03S04[SW]",
                "logic": []
            },
            {
                "target": "D01Z03S04[W]",
                "logic": []
            },
            {
                "target": "D01Z03S04[SE]",
                "logic": []
            },
            {
                "target": "D01Z03S04[E]",
                "logic": []
            },
            {
                "target": "D02Z01S01[SE]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z03S07[E]"
        ]
    },
    {
        "name": "D02Z01S01[SE]",
        "exits": [
            {
                "target": "D01Z03S04[SW]",
                "logic": []
            },
            {
                "target": "D01Z03S04[W]",
                "logic": []
            },
            {
                "target": "D01Z03S04[SE]",
                "logic": []
            },
            {
                "target": "D01Z03S04[E]",
                "logic": []
            },
            {
                "target": "D02Z01S01[SW]",
                "logic": [
                    {
                        "item_requirements": [
                            "openedWOTWCave",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "openedWOTWCave",
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "CO11",
                "logic": [
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "QI59",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RB10",
                "logic": [
                    {
                        "item_requirements": [
                            "fullThimble",
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "fullThimble",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z01S02[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z01S01[SE]",
            "D01Z03S04[NW]"
        ]
    },
    {
        "name": "D01Z03S03[-Cherubs]",
        "exits": [
            {
                "target": "PR16",
                "logic": []
            },
            {
                "target": "RESCUED_CHERUB_13",
                "logic": []
            },
            {
                "target": "D01Z05S06[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z03S03[-Cherubs]"
        ]
    },
    {
        "name": "D01Z05S05[NE]",
        "exits": [
            {
                "target": "D01Z05S06[W]",
                "logic": []
            },
            {
                "target": "PR16",
                "logic": [
                    {
                        "item_requirements": [
                            "canWaterJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RESCUED_CHERUB_13",
                "logic": [
                    {
                        "item_requirements": [
                            "canWaterJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "pillar"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "cante"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "aubade"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "tirana"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canAirStall"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S05[NE]"
        ]
    },
    {
        "name": "D01Z03S07",
        "exits": [
            {
                "target": "D01Z03S07[E]",
                "logic": []
            },
            {
                "target": "D01Z03S07[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "HE02",
            "RESCUED_CHERUB_38"
        ],
        "transitions": []
    },
    {
        "name": "D01Z03S04[W]",
        "exits": [
            {
                "target": "D01Z03S07",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z03S04[W]"
        ]
    },
    {
        "name": "D02Z01S02[E]",
        "exits": [
            {
                "target": "D02Z01S01[SW]",
                "logic": [
                    {
                        "item_requirements": [
                            "openedWOTWCave"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z01S04[-N]",
                "logic": [
                    {
                        "item_requirements": [
                            "fullThimble"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "CO11",
                "logic": []
            },
            {
                "target": "QI59",
                "logic": []
            },
            {
                "target": "RB10",
                "logic": [
                    {
                        "item_requirements": [
                            "fullThimble"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "QI68",
                "logic": [
                    {
                        "item_requirements": [
                            "fullThimble"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z01S01[SE]",
                "logic": []
            },
            {
                "target": "D02Z01S02[W]",
                "logic": []
            },
            {
                "target": "D02Z01S02[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canEnemyBounce"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "canWalkOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "canCrossGap10"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canWalkOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canCrossGap10"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z01S02[]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RESCUED_CHERUB_23",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb",
                            "canWalkOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "canCrossGap4"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "pillar"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canWalkOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canCrossGap4"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "pillar"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z01S03[SE]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z01S02[E]",
            "D02Z01S01[W]"
        ]
    },
    {
        "name": "D02Z01S06[E]",
        "exits": [
            {
                "target": "D02Z01S01[SW]",
                "logic": [
                    {
                        "item_requirements": [
                            "openedWOTWCave"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z01S04[-N]",
                "logic": [
                    {
                        "item_requirements": [
                            "fullThimble",
                            "canDawnJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "CO11",
                "logic": []
            },
            {
                "target": "QI59",
                "logic": [
                    {
                        "item_requirements": [
                            "canDawnJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RB10",
                "logic": [
                    {
                        "item_requirements": [
                            "fullThimble",
                            "canDawnJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "fullThimble",
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "fullThimble",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "QI68",
                "logic": [
                    {
                        "item_requirements": [
                            "fullThimble",
                            "canDawnJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z01S01[SE]",
                "logic": []
            },
            {
                "target": "D02Z01S02[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "canDawnJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z01S06[E]"
        ]
    },
    {
        "name": "D02Z01S09[-CherubsL]",
        "exits": [
            {
                "target": "D02Z01S01[SW]",
                "logic": [
                    {
                        "item_requirements": [
                            "openedWOTWCave"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z01S04[-N]",
                "logic": [
                    {
                        "item_requirements": [
                            "fullThimble"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "CO11",
                "logic": []
            },
            {
                "target": "QI59",
                "logic": []
            },
            {
                "target": "RB10",
                "logic": [
                    {
                        "item_requirements": [
                            "fullThimble"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "QI68",
                "logic": [
                    {
                        "item_requirements": [
                            "fullThimble"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z01S01[SE]",
                "logic": []
            },
            {
                "target": "D02Z01S02[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z01S09[-CherubsL]"
        ]
    },
    {
        "name": "D02Z01S09[-CherubsR]",
        "exits": [
            {
                "target": "D02Z01S01[SW]",
                "logic": [
                    {
                        "item_requirements": [
                            "openedWOTWCave"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z01S04[-N]",
                "logic": [
                    {
                        "item_requirements": [
                            "fullThimble",
                            "canDawnJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "CO11",
                "logic": []
            },
            {
                "target": "QI59",
                "logic": [
                    {
                        "item_requirements": [
                            "canDawnJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RB10",
                "logic": [
                    {
                        "item_requirements": [
                            "fullThimble",
                            "canDawnJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "fullThimble",
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "fullThimble",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "QI68",
                "logic": [
                    {
                        "item_requirements": [
                            "fullThimble",
                            "canDawnJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z01S01[SE]",
                "logic": []
            },
            {
                "target": "D02Z01S02[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "canDawnJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z01S09[-CherubsR]"
        ]
    },
    {
        "name": "D01Z03S05",
        "exits": [
            {
                "target": "D01Z03S05[W]",
                "logic": []
            },
            {
                "target": "D01Z03S05[E]",
                "logic": []
            },
            {
                "target": "D01Z03S05[Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "QI06"
        ],
        "transitions": []
    },
    {
        "name": "D01Z03S04[SE]",
        "exits": [
            {
                "target": "D01Z03S05",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z03S04[SE]"
        ]
    },
    {
        "name": "D01Z04S01[NW]",
        "exits": [
            {
                "target": "D01Z03S05",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z04S01[NW]"
        ]
    },
    {
        "name": "D01Z03S06",
        "exits": [
            {
                "target": "D01Z03S06[W]",
                "logic": []
            },
            {
                "target": "D01Z03S06[E]",
                "logic": []
            }
        ],
        "locations": [
            "RB20"
        ],
        "transitions": []
    },
    {
        "name": "D01Z03S04[E]",
        "exits": [
            {
                "target": "D01Z03S06",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z03S04[E]"
        ]
    },
    {
        "name": "D08Z01S01[W]",
        "exits": [
            {
                "target": "D01Z03S06",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D08Z01S01[W]"
        ]
    },
    {
        "name": "D01Z03S05[E]",
        "exits": [
            {
                "target": "D01Z04S01[NW]",
                "logic": []
            },
            {
                "target": "D01Z04S01[E]",
                "logic": []
            },
            {
                "target": "D01Z04S03[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z03S05[E]"
        ]
    },
    {
        "name": "D01Z04S03[E]",
        "exits": [
            {
                "target": "D01Z04S01[NW]",
                "logic": []
            },
            {
                "target": "D01Z04S01[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z04S03[E]",
            "D01Z04S01[W]",
            "D01Z04S17[W]",
            "D01Z04S01[NE]"
        ]
    },
    {
        "name": "D01Z04S05[NW]",
        "exits": [
            {
                "target": "D01Z04S01[NW]",
                "logic": []
            },
            {
                "target": "D01Z04S01[E]",
                "logic": []
            },
            {
                "target": "D01Z04S03[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z04S05[NW]"
        ]
    },
    {
        "name": "D01Z04S05[SW]",
        "exits": [
            {
                "target": "D01Z04S01[SE]",
                "logic": []
            },
            {
                "target": "D01Z04S01[NW]",
                "logic": []
            },
            {
                "target": "D01Z04S01[E]",
                "logic": []
            },
            {
                "target": "D01Z04S03[E]",
                "logic": []
            },
            {
                "target": "D01Z04S15[N]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z04S05[SW]"
        ]
    },
    {
        "name": "D01Z04S15[N]",
        "exits": [
            {
                "target": "D01Z04S01[SE]",
                "logic": []
            },
            {
                "target": "D01Z04S01[NW]",
                "logic": []
            },
            {
                "target": "D01Z04S01[E]",
                "logic": []
            },
            {
                "target": "D01Z04S03[E]",
                "logic": []
            },
            {
                "target": "D01Z04S15[NE]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z04S15[N]",
            "D01Z04S01[S]"
        ]
    },
    {
        "name": "D01Z05S11",
        "exits": [
            {
                "target": "D01Z05S11[W]",
                "logic": []
            }
        ],
        "locations": [
            "QI45"
        ],
        "transitions": []
    },
    {
        "name": "D01Z03S05[Cherubs]",
        "exits": [
            {
                "target": "D01Z05S11",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z03S05[Cherubs]"
        ]
    },
    {
        "name": "D01Z05S10[NE]",
        "exits": [
            {
                "target": "D01Z05S11",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S10[NE]"
        ]
    },
    {
        "name": "D08Z01S01",
        "exits": [
            {
                "target": "D08Z01S01[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "canBeatBridgeBoss"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D08Z01S01[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "holyWounds3",
                            "canBeatBridgeBoss"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "BS12",
            "PR09"
        ],
        "transitions": []
    },
    {
        "name": "D01Z03S06[E]",
        "exits": [
            {
                "target": "D08Z01S01",
                "logic": []
            },
            {
                "target": "D08Z01S01[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z03S06[E]"
        ]
    },
    {
        "name": "D08Z01S02[-Cherubs]",
        "exits": [
            {
                "target": "D08Z01S01",
                "logic": []
            },
            {
                "target": "D08Z01S01[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "holyWounds3"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D08Z01S02[-Cherubs]"
        ]
    },
    {
        "name": "D08Z02S01[W]",
        "exits": [
            {
                "target": "D08Z01S01",
                "logic": []
            },
            {
                "target": "D08Z01S01[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "holyWounds3"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D08Z02S01[W]"
        ]
    },
    {
        "name": "D01Z04S05",
        "exits": [
            {
                "target": "D01Z04S05[NW]",
                "logic": []
            },
            {
                "target": "D01Z04S05[SW]",
                "logic": []
            }
        ],
        "locations": [
            "CO30"
        ],
        "transitions": []
    },
    {
        "name": "D01Z04S01[E]",
        "exits": [
            {
                "target": "D01Z04S05",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z04S01[E]"
        ]
    },
    {
        "name": "D01Z04S01[SE]",
        "exits": [
            {
                "target": "D01Z04S05",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z04S01[SE]"
        ]
    },
    {
        "name": "D01Z04S06[NW]",
        "exits": [
            {
                "target": "D01Z04S15[N]",
                "logic": []
            },
            {
                "target": "D01Z04S15[NE]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z04S06[NW]"
        ]
    },
    {
        "name": "D01Z04S06[SW]",
        "exits": [
            {
                "target": "D01Z04S15[W]",
                "logic": []
            },
            {
                "target": "D01Z04S15[E]",
                "logic": []
            },
            {
                "target": "D01Z04S15[N]",
                "logic": []
            },
            {
                "target": "D01Z04S15[NE]",
                "logic": []
            },
            {
                "target": "D01Z04S09[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z04S06[SW]"
        ]
    },
    {
        "name": "D01Z04S08[E]",
        "exits": [
            {
                "target": "D01Z04S15[W]",
                "logic": []
            },
            {
                "target": "D01Z04S15[E]",
                "logic": []
            },
            {
                "target": "D01Z04S15[N]",
                "logic": []
            },
            {
                "target": "D01Z04S15[NE]",
                "logic": []
            },
            {
                "target": "D01Z04S09[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z04S08[E]"
        ]
    },
    {
        "name": "D01Z04S09[E]",
        "exits": [
            {
                "target": "D01Z04S15[W]",
                "logic": []
            },
            {
                "target": "D01Z04S15[E]",
                "logic": []
            },
            {
                "target": "D01Z04S15[N]",
                "logic": []
            },
            {
                "target": "D01Z04S15[NE]",
                "logic": []
            },
            {
                "target": "D01Z04S09[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "openedDCGateE"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D01Z04S09[C]",
                "logic": []
            },
            {
                "target": "D01Z04S10[SW]",
                "logic": []
            },
            {
                "target": "D01Z04S13[SW]",
                "logic": []
            },
            {
                "target": "D01Z04S13[SE]",
                "logic": [
                    {
                        "item_requirements": [
                            "HardLogic",
                            "canDiveLaser",
                            "canAirStall"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "HardLogic",
                            "canDiveLaser",
                            "wheel"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "HardLogic",
                            "canDiveLaser",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "HardLogic",
                            "canDiveLaser",
                            "canEnemyBounce"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "CO21",
                "logic": [
                    {
                        "item_requirements": [
                            "canDiveLaser",
                            "canAirStall"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canDiveLaser",
                            "wheel"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canDiveLaser",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canDiveLaser",
                            "canEnemyBounce"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D01Z04S18",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z04S09[E]",
            "D01Z04S15[SW]",
            "D01Z04S10[NW]",
            "D01Z04S15[SE]",
            "D01Z04S10[SE]",
            "D01Z04S12[NW]",
            "D01Z04S12[SE]",
            "D01Z04S13[NW]",
            "D01Z04S18[E]",
            "D01Z04S12[W]",
            "D01Z04S02[W]",
            "D01Z04S13[NE]"
        ]
    },
    {
        "name": "D01Z04S14[E]",
        "exits": [
            {
                "target": "D01Z04S13[SW]",
                "logic": []
            },
            {
                "target": "D01Z04S13[SE]",
                "logic": [
                    {
                        "item_requirements": [
                            "HardLogic",
                            "canDiveLaser",
                            "canAirStall"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "HardLogic",
                            "canDiveLaser",
                            "wheel"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "HardLogic",
                            "canDiveLaser",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "HardLogic",
                            "canDiveLaser",
                            "canEnemyBounce"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "CO21",
                "logic": [
                    {
                        "item_requirements": [
                            "canDiveLaser",
                            "canAirStall"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canDiveLaser",
                            "wheel"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canDiveLaser",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canDiveLaser",
                            "canEnemyBounce"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D01Z04S09[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z04S14[E]"
        ]
    },
    {
        "name": "D01Z04S16[W]",
        "exits": [
            {
                "target": "D01Z04S13[SE]",
                "logic": []
            },
            {
                "target": "CO21",
                "logic": []
            },
            {
                "target": "D01Z04S13[SW]",
                "logic": []
            },
            {
                "target": "D01Z04S09[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z04S16[W]"
        ]
    },
    {
        "name": "D01Z04S07",
        "exits": [
            {
                "target": "D01Z04S07[W]",
                "logic": []
            }
        ],
        "locations": [
            "PR01"
        ],
        "transitions": []
    },
    {
        "name": "D01Z04S06[E]",
        "exits": [
            {
                "target": "D01Z04S07",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z04S06[E]"
        ]
    },
    {
        "name": "D01Z04S06",
        "exits": [
            {
                "target": "D01Z04S06[E]",
                "logic": []
            },
            {
                "target": "D01Z04S06[NW]",
                "logic": []
            },
            {
                "target": "D01Z04S06[SW]",
                "logic": []
            }
        ],
        "locations": [
            "CO03",
            "RESCUED_CHERUB_09"
        ],
        "transitions": []
    },
    {
        "name": "D01Z04S07[W]",
        "exits": [
            {
                "target": "D01Z04S06",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z04S07[W]"
        ]
    },
    {
        "name": "D01Z04S15[NE]",
        "exits": [
            {
                "target": "D01Z04S06",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z04S15[NE]"
        ]
    },
    {
        "name": "D01Z04S15[E]",
        "exits": [
            {
                "target": "D01Z04S06",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z04S15[E]"
        ]
    },
    {
        "name": "D01Z04S09[W]",
        "exits": [
            {
                "target": "D01Z05S12[E]",
                "logic": []
            },
            {
                "target": "D01Z05S10[SE]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z04S09[W]"
        ]
    },
    {
        "name": "D01Z05S10[SE]",
        "exits": [
            {
                "target": "D01Z05S12[E]",
                "logic": []
            },
            {
                "target": "D01Z05S10[NE]",
                "logic": []
            },
            {
                "target": "D01Z05S10[S]",
                "logic": []
            },
            {
                "target": "D01Z05S09[NW]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S10[SE]",
            "D01Z05S12[W]",
            "D01Z05S10[W]",
            "D01Z05S09[SE]"
        ]
    },
    {
        "name": "D01BZ02S01",
        "exits": [
            {
                "target": "D01BZ02S01[C]",
                "logic": []
            }
        ],
        "locations": [
            "QI58",
            "RB05",
            "RB09"
        ],
        "transitions": []
    },
    {
        "name": "D01Z04S09[C]",
        "exits": [
            {
                "target": "D01BZ02S01",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z04S09[C]"
        ]
    },
    {
        "name": "D01Z04S11",
        "exits": [
            {
                "target": "D01Z04S11[NE]",
                "logic": []
            }
        ],
        "locations": [
            "QI48"
        ],
        "transitions": []
    },
    {
        "name": "D01Z04S10[SW]",
        "exits": [
            {
                "target": "D01Z04S11",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z04S10[SW]"
        ]
    },
    {
        "name": "D01Z04S11[NE]",
        "exits": [
            {
                "target": "D01Z04S10[SW]",
                "logic": []
            },
            {
                "target": "D01Z04S09[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z04S11[NE]"
        ]
    },
    {
        "name": "D01Z04S18",
        "exits": [
            {
                "target": "D01Z04S18[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "canBeatMercyBoss"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D01Z04S09[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "canBeatMercyBoss"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "BS01"
        ],
        "transitions": []
    },
    {
        "name": "D01Z04S19[E]",
        "exits": [
            {
                "target": "D01Z04S18",
                "logic": []
            },
            {
                "target": "D01Z04S18[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z04S19[E]"
        ]
    },
    {
        "name": "D01Z04S14",
        "exits": [
            {
                "target": "D01Z04S14[E]",
                "logic": []
            }
        ],
        "locations": [
            "CO38"
        ],
        "transitions": []
    },
    {
        "name": "D01Z04S13[SW]",
        "exits": [
            {
                "target": "D01Z04S14",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z04S13[SW]"
        ]
    },
    {
        "name": "D01Z04S16",
        "exits": [
            {
                "target": "D01Z04S16[W]",
                "logic": []
            },
            {
                "target": "D01Z04S16[E]",
                "logic": []
            }
        ],
        "locations": [
            "RESCUED_CHERUB_33"
        ],
        "transitions": []
    },
    {
        "name": "D01Z04S13[SE]",
        "exits": [
            {
                "target": "D01Z04S16",
                "logic": []
            },
            {
                "target": "RB25",
                "logic": [
                    {
                        "item_requirements": [
                            "blueWax1"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z04S13[SE]"
        ]
    },
    {
        "name": "D05Z02S12[W]",
        "exits": [
            {
                "target": "D01Z04S16",
                "logic": []
            },
            {
                "target": "RB25",
                "logic": [
                    {
                        "item_requirements": [
                            "blueWax1"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z02S12[W]"
        ]
    },
    {
        "name": "D01Z04S08",
        "exits": [
            {
                "target": "D01Z04S08[E]",
                "logic": []
            }
        ],
        "locations": [
            "RB17"
        ],
        "transitions": []
    },
    {
        "name": "D01Z04S15[W]",
        "exits": [
            {
                "target": "D01Z04S08",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z04S15[W]"
        ]
    },
    {
        "name": "D01BZ02S01[C]",
        "exits": [
            {
                "target": "D01Z04S09[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "openedDCGateE"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D01Z04S09[E]",
                "logic": []
            },
            {
                "target": "D01Z04S09[C]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01BZ02S01[C]"
        ]
    },
    {
        "name": "D01Z05S12[E]",
        "exits": [
            {
                "target": "D01Z04S09[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "openedDCGateE"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D01Z04S09[E]",
                "logic": []
            },
            {
                "target": "D01Z04S09[C]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S12[E]"
        ]
    },
    {
        "name": "D01Z04S16[E]",
        "exits": [
            {
                "target": "D05Z02S12[W]",
                "logic": []
            },
            {
                "target": "D05Z02S12[N]",
                "logic": []
            },
            {
                "target": "D05Z02S04[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z04S16[E]"
        ]
    },
    {
        "name": "D05Z02S04[W]",
        "exits": [
            {
                "target": "D05Z02S12[W]",
                "logic": []
            },
            {
                "target": "D05Z02S12[N]",
                "logic": []
            },
            {
                "target": "D05Z02S04[C]",
                "logic": []
            },
            {
                "target": "D05Z02S03[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z02S04[W]",
            "D05Z02S12[E]",
            "D05Z02S04[E]",
            "D05Z02S03[W]"
        ]
    },
    {
        "name": "D05Z02S15[S]",
        "exits": [
            {
                "target": "D05Z02S12[W]",
                "logic": []
            },
            {
                "target": "D05Z02S12[N]",
                "logic": []
            },
            {
                "target": "D05Z02S04[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z02S15[S]"
        ]
    },
    {
        "name": "D01Z04S19",
        "exits": [
            {
                "target": "D01Z04S19[W]",
                "logic": []
            },
            {
                "target": "D01Z04S19[E]",
                "logic": []
            }
        ],
        "locations": [
            "QI38"
        ],
        "transitions": []
    },
    {
        "name": "D01Z04S18[W]",
        "exits": [
            {
                "target": "D01Z04S19",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z04S18[W]"
        ]
    },
    {
        "name": "D01Z05S19[E]",
        "exits": [
            {
                "target": "D01Z04S19",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S19[E]"
        ]
    },
    {
        "name": "D01Z04S19[W]",
        "exits": [
            {
                "target": "D01Z05S19[W]",
                "logic": []
            },
            {
                "target": "D01Z05S19[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z04S19[W]"
        ]
    },
    {
        "name": "D01Z05S15[SE]",
        "exits": [
            {
                "target": "D01Z05S19[W]",
                "logic": []
            },
            {
                "target": "D01Z05S19[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S15[SE]"
        ]
    },
    {
        "name": "D01Z05S03[NW]",
        "exits": [
            {
                "target": "D01Z05S02[N]",
                "logic": []
            },
            {
                "target": "D01Z05S02[W]",
                "logic": []
            },
            {
                "target": "D01Z05S02[S]",
                "logic": [
                    {
                        "item_requirements": [
                            "openedDCLadder"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D01Z05S03[W]",
                "logic": []
            },
            {
                "target": "D01Z05S03[E]",
                "logic": []
            },
            {
                "target": "D01Z05S04[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S03[NW]",
            "D01Z05S02[E]",
            "D01Z05S13[N]",
            "D01Z05S03[S]",
            "D01Z05S04[W]",
            "D01Z05S03[NE]"
        ]
    },
    {
        "name": "D01Z05S20[N]",
        "exits": [
            {
                "target": "D01Z05S02[N]",
                "logic": []
            },
            {
                "target": "D01Z05S02[W]",
                "logic": []
            },
            {
                "target": "D01Z05S02[S]",
                "logic": [
                    {
                        "item_requirements": [
                            "openedDCLadder"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S20[N]"
        ]
    },
    {
        "name": "D03Z01S01[NE]",
        "exits": [
            {
                "target": "D01Z05S02[N]",
                "logic": []
            },
            {
                "target": "D01Z05S02[W]",
                "logic": []
            },
            {
                "target": "D01Z05S02[S]",
                "logic": [
                    {
                        "item_requirements": [
                            "openedDCLadder"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z01S01[NE]"
        ]
    },
    {
        "name": "D03Z01S01",
        "exits": [
            {
                "target": "D03Z01S01[W]",
                "logic": []
            },
            {
                "target": "D03Z01S01[NE]",
                "logic": []
            },
            {
                "target": "D03Z01S01[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "CO13"
        ],
        "transitions": []
    },
    {
        "name": "D01Z05S02[W]",
        "exits": [
            {
                "target": "D03Z01S01",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S02[W]"
        ]
    },
    {
        "name": "D03Z01S02[E]",
        "exits": [
            {
                "target": "D03Z01S01",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z01S02[E]"
        ]
    },
    {
        "name": "D20Z01S03[N]",
        "exits": [
            {
                "target": "D03Z01S01",
                "logic": []
            },
            {
                "target": "D20Z01S03[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D20Z01S03[N]",
            "D03Z01S01[S]"
        ]
    },
    {
        "name": "D01Z05S07[E]",
        "exits": [
            {
                "target": "D01Z05S03[NW]",
                "logic": []
            },
            {
                "target": "D01Z05S03[W]",
                "logic": []
            },
            {
                "target": "D01Z05S03[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S07[E]"
        ]
    },
    {
        "name": "D01Z05S08[W]",
        "exits": [
            {
                "target": "D01Z05S03[NW]",
                "logic": []
            },
            {
                "target": "D01Z05S03[W]",
                "logic": []
            },
            {
                "target": "D01Z05S03[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S08[W]"
        ]
    },
    {
        "name": "D01Z05S20",
        "exits": [
            {
                "target": "D01Z05S20[W]",
                "logic": []
            },
            {
                "target": "D01Z05S20[N]",
                "logic": []
            }
        ],
        "locations": [
            "RESCUED_CHERUB_15"
        ],
        "transitions": []
    },
    {
        "name": "D01Z05S02[S]",
        "exits": [
            {
                "target": "D01Z05S20",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S02[S]"
        ]
    },
    {
        "name": "D01Z05S25[NE]",
        "exits": [
            {
                "target": "D01Z05S20",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S25[NE]"
        ]
    },
    {
        "name": "D01Z05S05[NW]",
        "exits": [
            {
                "target": "D01Z05S04[E]",
                "logic": []
            },
            {
                "target": "D01Z05S03[NW]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S05[NW]"
        ]
    },
    {
        "name": "D01Z05S07",
        "exits": [
            {
                "target": "D01Z05S07[E]",
                "logic": []
            }
        ],
        "locations": [
            "Oil[D01Z05S07]"
        ],
        "transitions": []
    },
    {
        "name": "D01Z05S03[W]",
        "exits": [
            {
                "target": "D01Z05S07",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S03[W]"
        ]
    },
    {
        "name": "D01Z05S08",
        "exits": [
            {
                "target": "D01Z05S08[W]",
                "logic": []
            }
        ],
        "locations": [
            "QI12",
            "RESCUED_CHERUB_14"
        ],
        "transitions": []
    },
    {
        "name": "D01Z05S03[E]",
        "exits": [
            {
                "target": "D01Z05S08",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S03[E]"
        ]
    },
    {
        "name": "D01Z05S14[W]",
        "exits": [
            {
                "target": "D01Z05S13[E]",
                "logic": []
            },
            {
                "target": "RESCUED_CHERUB_12",
                "logic": [
                    {
                        "item_requirements": [
                            "canSurvivePoison3",
                            "canWaterJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D01Z05S03[NW]",
                "logic": [
                    {
                        "item_requirements": [
                            "D01Z05S03[S]"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canSurvivePoison3",
                            "canWaterJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D01Z05S16[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "D01Z05S16[N]"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canSurvivePoison3",
                            "canWaterJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S14[W]"
        ]
    },
    {
        "name": "D01Z05S16[N]",
        "exits": [
            {
                "target": "RESCUED_CHERUB_12",
                "logic": []
            },
            {
                "target": "D01Z05S21[Reward]",
                "logic": [
                    {
                        "item_requirements": [
                            "shroud"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D01Z05S25[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "canWalkOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canCrossGap3"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "linen",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "linen",
                            "canAirStall"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RESCUED_CHERUB_22",
                "logic": [
                    {
                        "item_requirements": [
                            "pillar"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D01Z05S17[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "dash",
                            "canWaterJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "dash",
                            "canCrossGap5"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "CO32",
                "logic": [
                    {
                        "item_requirements": [
                            "canWaterJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canCrossGap5"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D01Z05S25[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D01Z05S25[SE]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "CO44",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z03S17[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S16[N]",
            "D01Z05S13[SW]",
            "D01Z05S21[E]",
            "D01Z05S16[SW]",
            "D01Z05S25[E]",
            "D01Z05S21[W]",
            "D01Z05S17[W]",
            "D01Z05S16[SE]"
        ]
    },
    {
        "name": "D01Z05S05[SW]",
        "exits": [
            {
                "target": "D01Z05S18[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S05[SW]"
        ]
    },
    {
        "name": "D01Z05S05[E]",
        "exits": [
            {
                "target": "D01Z05S09[NW]",
                "logic": []
            },
            {
                "target": "D01Z05S10[SE]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S05[E]"
        ]
    },
    {
        "name": "D01Z05S11[W]",
        "exits": [
            {
                "target": "D01Z05S10[NE]",
                "logic": []
            },
            {
                "target": "D01Z05S10[SE]",
                "logic": []
            },
            {
                "target": "D01Z05S10[S]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S11[W]"
        ]
    },
    {
        "name": "D01Z05S14[N]",
        "exits": [
            {
                "target": "D01Z05S10[NE]",
                "logic": []
            },
            {
                "target": "D01Z05S10[SE]",
                "logic": []
            },
            {
                "target": "D01Z05S10[S]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S14[N]"
        ]
    },
    {
        "name": "D01Z05S14",
        "exits": [
            {
                "target": "D01Z05S14[W]",
                "logic": []
            },
            {
                "target": "D01Z05S14[N]",
                "logic": []
            },
            {
                "target": "D01Z05S14[SE]",
                "logic": []
            }
        ],
        "locations": [
            "RESCUED_CHERUB_11"
        ],
        "transitions": []
    },
    {
        "name": "D01Z05S10[S]",
        "exits": [
            {
                "target": "D01Z05S14",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S10[S]"
        ]
    },
    {
        "name": "D01Z05S13[E]",
        "exits": [
            {
                "target": "D01Z05S14",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S13[E]"
        ]
    },
    {
        "name": "D01Z05S15[W]",
        "exits": [
            {
                "target": "D01Z05S14",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S15[W]"
        ]
    },
    {
        "name": "D01Z05S15",
        "exits": [
            {
                "target": "D01Z05S15[W]",
                "logic": []
            },
            {
                "target": "D01Z05S15[SW]",
                "logic": []
            },
            {
                "target": "D01Z05S15[SE]",
                "logic": []
            }
        ],
        "locations": [
            "CO41"
        ],
        "transitions": []
    },
    {
        "name": "D01Z05S14[SE]",
        "exits": [
            {
                "target": "D01Z05S15",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S14[SE]"
        ]
    },
    {
        "name": "D01Z05S19[W]",
        "exits": [
            {
                "target": "D01Z05S15",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S19[W]"
        ]
    },
    {
        "name": "D01Z05S22[E]",
        "exits": [
            {
                "target": "D01Z05S15",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S22[E]"
        ]
    },
    {
        "name": "D01Z05S22",
        "exits": [
            {
                "target": "D01Z05S22[E]",
                "logic": []
            }
        ],
        "locations": [
            "Lady[D01Z05S22]"
        ],
        "transitions": []
    },
    {
        "name": "D01Z05S15[SW]",
        "exits": [
            {
                "target": "D01Z05S22",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S15[SW]"
        ]
    },
    {
        "name": "D01BZ05S01[Reward]",
        "exits": [
            {
                "target": "D01Z05S21[Reward]",
                "logic": [
                    {
                        "item_requirements": [
                            "shroud"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D01Z05S16[N]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01BZ05S01[Reward]"
        ]
    },
    {
        "name": "D01BZ09S01[W]",
        "exits": [
            {
                "target": "D01Z05S17[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "CO32",
                "logic": []
            },
            {
                "target": "D01Z05S16[N]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01BZ09S01[W]"
        ]
    },
    {
        "name": "D01Z05S17[E]",
        "exits": [
            {
                "target": "D01BZ09S01[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S17[E]"
        ]
    },
    {
        "name": "D01Z05S20[W]",
        "exits": [
            {
                "target": "D01Z05S25[NE]",
                "logic": []
            },
            {
                "target": "D01Z05S25[SE]",
                "logic": []
            },
            {
                "target": "CO44",
                "logic": [
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RESCUED_CHERUB_22",
                "logic": [
                    {
                        "item_requirements": [
                            "obscureSkipsAllowed",
                            "aubade"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "obscureSkipsAllowed",
                            "cantina"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D01Z05S25[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen",
                            "canWalkOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "linen",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "linen",
                            "canAirStall"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D01Z05S16[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "HardLogic",
                            "tirana",
                            "obscureSkipsAllowed",
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z03S17[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S20[W]"
        ]
    },
    {
        "name": "D01Z05S23[E]",
        "exits": [
            {
                "target": "D01Z05S25[W]",
                "logic": []
            },
            {
                "target": "RESCUED_CHERUB_22",
                "logic": [
                    {
                        "item_requirements": [
                            "pillar",
                            "canWalkOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "pillar",
                            "canCrossGap3"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D01Z05S16[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "HardLogic",
                            "tirana",
                            "obscureSkipsAllowed",
                            "canWalkOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "HardLogic",
                            "tirana",
                            "obscureSkipsAllowed",
                            "canCrossGap3"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "HardLogic",
                            "tirana",
                            "obscureSkipsAllowed",
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D01Z05S25[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D01Z05S25[SE]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "CO44",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z03S17[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S23[E]"
        ]
    },
    {
        "name": "D01Z05S26[W]",
        "exits": [
            {
                "target": "D01Z05S25[NE]",
                "logic": []
            },
            {
                "target": "D01Z05S25[SE]",
                "logic": []
            },
            {
                "target": "CO44",
                "logic": [
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RESCUED_CHERUB_22",
                "logic": [
                    {
                        "item_requirements": [
                            "obscureSkipsAllowed",
                            "aubade"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "obscureSkipsAllowed",
                            "cantina"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D01Z05S25[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen",
                            "canWalkOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "linen",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "linen",
                            "canAirStall"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D01Z05S16[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "HardLogic",
                            "tirana",
                            "obscureSkipsAllowed",
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z03S17[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S26[W]"
        ]
    },
    {
        "name": "D03Z03S17[E]",
        "exits": [
            {
                "target": "D01Z05S25[NE]",
                "logic": []
            },
            {
                "target": "D01Z05S25[SE]",
                "logic": []
            },
            {
                "target": "CO44",
                "logic": [
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RESCUED_CHERUB_22",
                "logic": [
                    {
                        "item_requirements": [
                            "obscureSkipsAllowed",
                            "aubade"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "obscureSkipsAllowed",
                            "cantina"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D01Z05S25[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen",
                            "canWalkOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "linen",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "linen",
                            "canAirStall"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D01Z05S16[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "HardLogic",
                            "tirana",
                            "obscureSkipsAllowed",
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z03S17[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z03S17[E]",
            "D01Z05S25[SW]"
        ]
    },
    {
        "name": "D20Z01S09[E]",
        "exits": [
            {
                "target": "D01Z05S25[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D01Z05S25[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen",
                            "canWalkOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "linen",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "linen",
                            "canAirStall"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D01Z05S25[SE]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "CO44",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RESCUED_CHERUB_22",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D01Z05S16[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "HardLogic",
                            "tirana",
                            "obscureSkipsAllowed",
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z03S17[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D20Z01S09[E]"
        ]
    },
    {
        "name": "D20Z01S10[W]",
        "exits": [
            {
                "target": "D01Z05S25[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D01Z05S25[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen",
                            "canWalkOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "linen",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "linen",
                            "canAirStall"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D01Z05S25[SE]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "CO44",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RESCUED_CHERUB_22",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D01Z05S16[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "HardLogic",
                            "tirana",
                            "obscureSkipsAllowed",
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z03S17[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D20Z01S10[W]"
        ]
    },
    {
        "name": "D01BZ05S01",
        "exits": [
            {
                "target": "D01BZ05S01[Reward]",
                "logic": []
            }
        ],
        "locations": [
            "RB03"
        ],
        "transitions": []
    },
    {
        "name": "D01Z05S21[Reward]",
        "exits": [
            {
                "target": "D01BZ05S01",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S21[Reward]"
        ]
    },
    {
        "name": "D01Z05S24",
        "exits": [
            {
                "target": "D01Z05S24[W]",
                "logic": []
            },
            {
                "target": "D01Z05S24[E]",
                "logic": []
            }
        ],
        "locations": [
            "Sword[D01Z05S24]"
        ],
        "transitions": []
    },
    {
        "name": "D01Z05S23[W]",
        "exits": [
            {
                "target": "D01Z05S24",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S23[W]"
        ]
    },
    {
        "name": "D20Z01S04[E]",
        "exits": [
            {
                "target": "D01Z05S24",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D20Z01S04[E]"
        ]
    },
    {
        "name": "D01Z05S24[W]",
        "exits": [
            {
                "target": "D20Z01S04[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "openedDCGateW"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D20Z01S01[S]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S24[W]"
        ]
    },
    {
        "name": "D20Z01S01[S]",
        "exits": [
            {
                "target": "D20Z01S04[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "openedDCGateW"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D20Z01S01[W]",
                "logic": []
            },
            {
                "target": "D20Z01S01[E]",
                "logic": []
            },
            {
                "target": "RB202",
                "logic": []
            },
            {
                "target": "D20Z01S09[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "blood",
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D20Z01S01[S]",
            "D20Z01S04[N]",
            "D20Z01S05[E]",
            "D20Z01S04[W]",
            "D20Z01S06[NE]",
            "D20Z01S05[W]",
            "D20Z01S07[NW]",
            "D20Z01S06[SE]",
            "D20Z01S07[SE]",
            "D20Z01S09[W]",
            "D20Z01S08[W]",
            "D20Z01S07[NE]"
        ]
    },
    {
        "name": "D01Z05S23",
        "exits": [
            {
                "target": "D01Z05S23[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "chalice",
                            "chaliceRooms3"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D01Z05S23[E]",
                "logic": []
            }
        ],
        "locations": [
            "QI75"
        ],
        "transitions": []
    },
    {
        "name": "D01Z05S24[E]",
        "exits": [
            {
                "target": "D01Z05S23",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S24[E]"
        ]
    },
    {
        "name": "D01Z05S25[W]",
        "exits": [
            {
                "target": "D01Z05S23",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S25[W]"
        ]
    },
    {
        "name": "D03Z03S16[E]",
        "exits": [
            {
                "target": "D03Z03S17[W]",
                "logic": []
            },
            {
                "target": "D03Z03S17[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z03S16[E]"
        ]
    },
    {
        "name": "D01Z05S26",
        "exits": [
            {
                "target": "D01Z05S26[W]",
                "logic": []
            }
        ],
        "locations": [
            "Lady[D01Z05S26]"
        ],
        "transitions": []
    },
    {
        "name": "D01Z05S25[SE]",
        "exits": [
            {
                "target": "D01Z05S26",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S25[SE]"
        ]
    },
    {
        "name": "D01Z05S25[EchoesW]",
        "exits": [
            {
                "target": "D20Z01S09[E]",
                "logic": []
            },
            {
                "target": "RB202",
                "logic": [
                    {
                        "item_requirements": [
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D20Z01S01[S]",
                "logic": [
                    {
                        "item_requirements": [
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S25[EchoesW]"
        ]
    },
    {
        "name": "D01Z05S25[EchoesE]",
        "exits": [
            {
                "target": "D20Z01S10[W]",
                "logic": []
            },
            {
                "target": "D20Z01S11[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "blood",
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z05S25[EchoesE]"
        ]
    },
    {
        "name": "D20Z01S11[W]",
        "exits": [
            {
                "target": "D20Z01S10[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "blood",
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D20Z02S11",
                "logic": []
            },
            {
                "target": "D20Z02S12[E]",
                "logic": []
            },
            {
                "target": "D20Z01S14[E]",
                "logic": []
            },
            {
                "target": "D20Z02S10[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "HardLogic",
                            "mourningSkipAllowed",
                            "canCrossGap5"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D20Z01S11[W]",
            "D20Z01S10[E]",
            "D20Z01S12[E]",
            "D20Z01S11[NW]",
            "D20Z01S13[W]",
            "D20Z01S11[NE]",
            "D20Z02S11[NW]",
            "D20Z01S13[E]",
            "D20Z02S12[W]",
            "D20Z01S11[SE]",
            "D20Z01S14[S]",
            "D20Z01S13[N]"
        ]
    },
    {
        "name": "D01Z06S01[Santos]",
        "exits": [
            {
                "target": "D01BZ07S01[Santos]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D01Z06S01[Santos]"
        ]
    },
    {
        "name": "D02Z01S01[SW]",
        "exits": [
            {
                "target": "D02Z01S06[E]",
                "logic": []
            },
            {
                "target": "D02Z01S06[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "CO19",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "blood",
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RESCUED_CHERUB_27",
                "logic": [
                    {
                        "item_requirements": [
                            "dash",
                            "pillar"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "dash",
                            "cante"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "dash",
                            "canDiveLaser"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "wallClimb",
                            "pillar"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "wallClimb",
                            "cante"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "wallClimb",
                            "canDiveLaser"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "doubleJump",
                            "lorquiana"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "doubleJump",
                            "aubade"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "doubleJump",
                            "cantina"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "doubleJump",
                            "canAirStall"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "dash",
                            "lorquiana"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "dash",
                            "aubade"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "dash",
                            "cantina"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "dash",
                            "canAirStall"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z01S01[SW]"
        ]
    },
    {
        "name": "D02Z01S02[]",
        "exits": [
            {
                "target": "CO19",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb",
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z01S06[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z01S06[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RESCUED_CHERUB_27",
                "logic": [
                    {
                        "item_requirements": [
                            "dash",
                            "pillar"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "dash",
                            "cante"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "dash",
                            "canDiveLaser"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "wallClimb",
                            "pillar"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "wallClimb",
                            "cante"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "wallClimb",
                            "canDiveLaser"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "doubleJump",
                            "lorquiana"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "doubleJump",
                            "aubade"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "doubleJump",
                            "cantina"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "doubleJump",
                            "canAirStall"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "dash",
                            "lorquiana"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "dash",
                            "aubade"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "dash",
                            "cantina"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "dash",
                            "canAirStall"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z01S02[]"
        ]
    },
    {
        "name": "D02Z01S08[E]",
        "exits": [
            {
                "target": "D02Z01S06[W]",
                "logic": []
            },
            {
                "target": "RESCUED_CHERUB_27",
                "logic": [
                    {
                        "item_requirements": [
                            "pillar"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "cante"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canDiveLaser"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "lorquiana"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "aubade"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "cantina"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "canAirStall"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z01S06[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "CO19",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "blood",
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z01S08[E]"
        ]
    },
    {
        "name": "D02Z01S03[SE]",
        "exits": [
            {
                "target": "D02Z01S02[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "canWalkOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canCrossGap10"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canEnemyBounce"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RESCUED_CHERUB_23",
                "logic": [
                    {
                        "item_requirements": [
                            "canWalkOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canCrossGap4"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "pillar"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z01S02[W]",
                "logic": []
            },
            {
                "target": "D02Z01S02[E]",
                "logic": []
            },
            {
                "target": "D02Z01S02[]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z01S03[SW]",
                "logic": []
            },
            {
                "target": "D02Z02S08[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S02[SE]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb",
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z01S03[SE]",
            "D02Z01S02[NW]",
            "D02Z02S01[E]",
            "D02Z01S03[W]"
        ]
    },
    {
        "name": "D02Z01S04[E]",
        "exits": [
            {
                "target": "D02Z01S02[W]",
                "logic": []
            },
            {
                "target": "D02Z01S02[E]",
                "logic": []
            },
            {
                "target": "D02Z01S02[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canEnemyBounce"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "canWalkOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "canCrossGap10"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canWalkOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canCrossGap10"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z01S02[]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RESCUED_CHERUB_23",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb",
                            "canWalkOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "canCrossGap4"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "pillar"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canWalkOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canCrossGap4"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "pillar"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z01S03[SE]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z01S04[E]"
        ]
    },
    {
        "name": "D02Z01S09[W]",
        "exits": [
            {
                "target": "D02Z01S02[NE]",
                "logic": []
            },
            {
                "target": "RESCUED_CHERUB_23",
                "logic": []
            },
            {
                "target": "D02Z01S03[SE]",
                "logic": [
                    {
                        "item_requirements": [
                            "canWalkOnRoot",
                            "canCrossGap5"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z01S02[W]",
                "logic": []
            },
            {
                "target": "D02Z01S02[E]",
                "logic": []
            },
            {
                "target": "D02Z01S02[]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z01S09[W]"
        ]
    },
    {
        "name": "D02Z01S04",
        "exits": [
            {
                "target": "D02Z01S04[E]",
                "logic": []
            },
            {
                "target": "D02Z01S04[-N]",
                "logic": [
                    {
                        "item_requirements": [
                            "fullThimble",
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "fullThimble",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "QI68",
                "logic": [
                    {
                        "item_requirements": [
                            "fullThimble",
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "fullThimble",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "QI20"
        ],
        "transitions": []
    },
    {
        "name": "D02Z01S02[W]",
        "exits": [
            {
                "target": "D02Z01S04",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z01S02[W]"
        ]
    },
    {
        "name": "D02Z01S05[E]",
        "exits": [
            {
                "target": "D02Z01S03[SW]",
                "logic": []
            },
            {
                "target": "D02Z01S03[SE]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z01S05[E]"
        ]
    },
    {
        "name": "D02Z02S14[-Cherubs]",
        "exits": [
            {
                "target": "D02Z01S03[SE]",
                "logic": []
            },
            {
                "target": "D02Z01S03[SW]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z02S14[-Cherubs]"
        ]
    },
    {
        "name": "D02Z01S09",
        "exits": [
            {
                "target": "D02Z01S09[W]",
                "logic": []
            },
            {
                "target": "D02Z01S09[-CherubsL]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z01S09[-CherubsR]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen",
                            "canWalkOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "linen",
                            "canCrossGap2"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "linen",
                            "canEnemyBounce",
                            "canAirStall"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "HE05"
        ],
        "transitions": []
    },
    {
        "name": "D02Z01S02[NE]",
        "exits": [
            {
                "target": "D02Z01S09",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z01S02[NE]"
        ]
    },
    {
        "name": "D02Z01S05",
        "exits": [
            {
                "target": "D02Z01S05[E]",
                "logic": []
            }
        ],
        "locations": [
            "QI07"
        ],
        "transitions": []
    },
    {
        "name": "D02Z01S03[SW]",
        "exits": [
            {
                "target": "D02Z01S05",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z01S03[SW]"
        ]
    },
    {
        "name": "D02Z02S02[SE]",
        "exits": [
            {
                "target": "D02Z01S03[SE]",
                "logic": []
            },
            {
                "target": "D02Z02S08[E]",
                "logic": []
            },
            {
                "target": "D02Z02S02[-CherubsR]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RESCUED_CHERUB_24",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "pillar"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "cante"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "tirana"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "canDiveLaser"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S03[SW]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z02S02[SE]",
            "D02Z02S01[NW]"
        ]
    },
    {
        "name": "D02Z02S03[-Cherubs]",
        "exits": [
            {
                "target": "D02Z01S03[SE]",
                "logic": []
            },
            {
                "target": "D02Z02S08[E]",
                "logic": []
            },
            {
                "target": "D02Z02S02[SE]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z02S03[-Cherubs]"
        ]
    },
    {
        "name": "D02Z02S08[E]",
        "exits": [
            {
                "target": "D02Z01S03[SE]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S08[W]",
                "logic": []
            },
            {
                "target": "D02Z02S08[C]",
                "logic": []
            },
            {
                "target": "CO42",
                "logic": [
                    {
                        "item_requirements": [
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canBreakHoles"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canCrossGap8"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RESCUED_CHERUB_31",
                "logic": [
                    {
                        "item_requirements": [
                            "canDiveLaser"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "pillar"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canCrossGap8"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S02[SE]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z02S08[E]",
            "D02Z02S01[W]"
        ]
    },
    {
        "name": "D02Z01S08",
        "exits": [
            {
                "target": "D02Z01S08[E]",
                "logic": []
            }
        ],
        "locations": [
            "PR04"
        ],
        "transitions": []
    },
    {
        "name": "D02Z01S04[-N]",
        "exits": [
            {
                "target": "D02Z01S08",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z01S04[-N]"
        ]
    },
    {
        "name": "D02Z01S06[W]",
        "exits": [
            {
                "target": "D02Z01S08",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z01S06[W]"
        ]
    },
    {
        "name": "D02Z02S02[-CherubsR]",
        "exits": [
            {
                "target": "CO42",
                "logic": []
            },
            {
                "target": "RESCUED_CHERUB_31",
                "logic": []
            },
            {
                "target": "D02Z02S08[W]",
                "logic": []
            },
            {
                "target": "D02Z02S08[E]",
                "logic": []
            },
            {
                "target": "D02Z02S08[C]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z02S02[-CherubsR]"
        ]
    },
    {
        "name": "D02Z02S04[-CherubsL]",
        "exits": [
            {
                "target": "D02Z02S08[W]",
                "logic": []
            },
            {
                "target": "D02Z02S08[E]",
                "logic": []
            },
            {
                "target": "D02Z02S08[C]",
                "logic": []
            },
            {
                "target": "CO42",
                "logic": [
                    {
                        "item_requirements": [
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canBreakHoles"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canCrossGap8"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RESCUED_CHERUB_31",
                "logic": [
                    {
                        "item_requirements": [
                            "canDiveLaser"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "pillar"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canCrossGap8"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z02S04[-CherubsL]"
        ]
    },
    {
        "name": "D02Z02S11[SE]",
        "exits": [
            {
                "target": "D02Z02S08[W]",
                "logic": []
            },
            {
                "target": "D02Z02S08[E]",
                "logic": []
            },
            {
                "target": "D02Z02S08[C]",
                "logic": []
            },
            {
                "target": "CO42",
                "logic": [
                    {
                        "item_requirements": [
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canBreakHoles"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canCrossGap8"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RESCUED_CHERUB_31",
                "logic": [
                    {
                        "item_requirements": [
                            "canDiveLaser"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "pillar"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canCrossGap8"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z02S11[SE]"
        ]
    },
    {
        "name": "D02BZ02S01[C]",
        "exits": [
            {
                "target": "D02Z02S08[W]",
                "logic": []
            },
            {
                "target": "D02Z02S08[E]",
                "logic": []
            },
            {
                "target": "D02Z02S08[C]",
                "logic": []
            },
            {
                "target": "CO42",
                "logic": [
                    {
                        "item_requirements": [
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canBreakHoles"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canCrossGap8"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RESCUED_CHERUB_31",
                "logic": [
                    {
                        "item_requirements": [
                            "canDiveLaser"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "pillar"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canCrossGap8"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D02BZ02S01[C]"
        ]
    },
    {
        "name": "D02Z02S03[SW]",
        "exits": [
            {
                "target": "RESCUED_CHERUB_24",
                "logic": [
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "pillar"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "cante"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "tirana"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canDiveLaser"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S02[SE]",
                "logic": []
            },
            {
                "target": "D02Z02S02[-CherubsR]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S03[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb",
                            "canCrossGap11"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "blood",
                            "canWalkOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "blood",
                            "canCrossGap7"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "canWalkOnRoot",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "canWalkOnRoot",
                            "canAirStall"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S03[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "QI46",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canCrossGap2"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "CO29",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "QI08",
                "logic": [
                    {
                        "item_requirements": [
                            "canClimbOnRoot",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canClimbOnRoot",
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "blood",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S04[-CherubsL]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "CO01",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canEnemyUpslash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RESCUED_CHERUB_25",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb",
                            "blood",
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "doubleJump",
                            "canEnemyBounce"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "lorquiana"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "cante"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "verdiales"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "aubade"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "cantina"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canEnemyUpslash",
                            "blood",
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canEnemyUpslash",
                            "canEnemyBounce"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canEnemyUpslash",
                            "lorquiana"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canEnemyUpslash",
                            "cante"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canEnemyUpslash",
                            "verdiales"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canEnemyUpslash",
                            "aubade"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canEnemyUpslash",
                            "cantina"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "pillar"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S05[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canEnemyUpslash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S05[SW]",
                "logic": [
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S09[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canEnemyUpslash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z02S03[SW]",
            "D02Z02S02[NE]",
            "D02Z02S04[SE]",
            "D02Z02S02[NW]"
        ]
    },
    {
        "name": "D02Z02S05[-CherubsL]",
        "exits": [
            {
                "target": "RESCUED_CHERUB_24",
                "logic": []
            },
            {
                "target": "D02Z02S02[SE]",
                "logic": []
            },
            {
                "target": "D02Z02S02[-CherubsR]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S03[SW]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z02S05[-CherubsL]"
        ]
    },
    {
        "name": "D02Z02S05[-CherubsR]",
        "exits": [
            {
                "target": "RESCUED_CHERUB_24",
                "logic": []
            },
            {
                "target": "D02Z02S02[SE]",
                "logic": []
            },
            {
                "target": "D02Z02S02[-CherubsR]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S03[SW]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z02S05[-CherubsR]"
        ]
    },
    {
        "name": "D02Z02S05[SW]",
        "exits": [
            {
                "target": "CO01",
                "logic": [
                    {
                        "item_requirements": [
                            "dash",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "dash",
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RESCUED_CHERUB_25",
                "logic": [
                    {
                        "item_requirements": [
                            "dash",
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "dash",
                            "doubleJump",
                            "canEnemyBounce"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "dash",
                            "lorquiana"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "dash",
                            "cante"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "dash",
                            "verdiales"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "dash",
                            "aubade"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "dash",
                            "cantina"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "dash",
                            "pillar"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S05[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "dash",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "dash",
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "EnemySkips",
                            "doubleJump",
                            "canEnemyBounce"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S04[-CherubsL]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen",
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S03[SW]",
                "logic": []
            },
            {
                "target": "D02Z02S05[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S05[-CherubsL]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S05[-CherubsR]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RB15",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "QI46",
                "logic": []
            },
            {
                "target": "CO29",
                "logic": []
            },
            {
                "target": "D02Z02S03[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb",
                            "canCrossGap11"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "blood",
                            "canWalkOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "blood",
                            "canCrossGap7"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "canWalkOnRoot",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "canWalkOnRoot",
                            "canAirStall"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S03[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "QI08",
                "logic": [
                    {
                        "item_requirements": [
                            "canClimbOnRoot",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canClimbOnRoot",
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "blood",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S09[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S07[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "RB32"
        ],
        "transitions": [
            "D02Z02S05[SW]",
            "D02Z02S04[E]",
            "D02Z02S05[SE]",
            "D02Z02S03[NW]"
        ]
    },
    {
        "name": "D02Z02S05[W]",
        "exits": [
            {
                "target": "D02Z02S04[-CherubsL]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "CO01",
                "logic": []
            },
            {
                "target": "RESCUED_CHERUB_25",
                "logic": [
                    {
                        "item_requirements": [
                            "blood",
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canEnemyBounce"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "lorquiana"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "cante"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "verdiales"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "aubade"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "cantina"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "pillar"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S03[SW]",
                "logic": []
            },
            {
                "target": "D02Z02S05[SW]",
                "logic": []
            },
            {
                "target": "D02Z02S05[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S05[-CherubsL]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S05[-CherubsR]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RB15",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S09[E]",
                "logic": []
            },
            {
                "target": "D02Z02S07[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z02S05[W]",
            "D02Z02S04[NE]"
        ]
    },
    {
        "name": "D02Z02S09[E]",
        "exits": [
            {
                "target": "D02Z02S04[-CherubsL]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "CO01",
                "logic": [
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RESCUED_CHERUB_25",
                "logic": [
                    {
                        "item_requirements": [
                            "blood",
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canEnemyBounce"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "lorquiana"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "cante"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "verdiales"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "aubade"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "cantina"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "pillar"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S05[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S03[SW]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z02S09[E]",
            "D02Z02S04[W]"
        ]
    },
    {
        "name": "D02Z02S14[W]",
        "exits": [
            {
                "target": "D02Z02S03[NE]",
                "logic": []
            },
            {
                "target": "QI46",
                "logic": []
            },
            {
                "target": "CO29",
                "logic": []
            },
            {
                "target": "QI08",
                "logic": [
                    {
                        "item_requirements": [
                            "canClimbOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "blood",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S03[SW]",
                "logic": []
            },
            {
                "target": "D02Z02S03[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S05[SW]",
                "logic": [
                    {
                        "item_requirements": [
                            "canWalkOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z02S14[W]"
        ]
    },
    {
        "name": "D02Z02S07[E]",
        "exits": [
            {
                "target": "D02Z02S05[E]",
                "logic": []
            },
            {
                "target": "RB15",
                "logic": []
            },
            {
                "target": "D02Z02S05[SW]",
                "logic": []
            },
            {
                "target": "D02Z02S05[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "EnemySkips",
                            "doubleJump",
                            "canEnemyBounce"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S05[-CherubsL]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S05[-CherubsR]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z03S08[SW]",
                "logic": []
            },
            {
                "target": "D02Z02S11",
                "logic": []
            },
            {
                "target": "D01Z02S03[NW]",
                "logic": []
            },
            {
                "target": "D02Z02S11[E]",
                "logic": []
            },
            {
                "target": "D02Z02S11[NE]",
                "logic": []
            },
            {
                "target": "D02Z03S02[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z02S07[E]",
            "D02Z02S05[NW]",
            "D02Z03S01[E]",
            "D02Z02S07[W]",
            "D02Z03S08[E]",
            "D02Z03S01[W]",
            "D02Z03S08[SE]",
            "D02Z03S14[W]",
            "D02Z03S14[E]",
            "D02Z02S11[NW]",
            "D02Z03S16[W]",
            "D02Z03S08[NE]",
            "D02Z03S02[S]",
            "D02Z03S16[N]"
        ]
    },
    {
        "name": "D02Z02S10[W]",
        "exits": [
            {
                "target": "D02Z02S05[E]",
                "logic": []
            },
            {
                "target": "D02Z02S05[SW]",
                "logic": []
            },
            {
                "target": "D02Z02S05[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "EnemySkips",
                            "doubleJump",
                            "canEnemyBounce"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S05[-CherubsL]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S05[-CherubsR]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RB15",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S07[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z02S10[W]"
        ]
    },
    {
        "name": "D02Z02S14",
        "exits": [
            {
                "target": "D02Z02S14[W]",
                "logic": []
            },
            {
                "target": "D02Z02S14[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "RB106",
            "Amanecida[D02Z02S14]"
        ],
        "transitions": []
    },
    {
        "name": "D02Z02S03[NE]",
        "exits": [
            {
                "target": "D02Z02S14",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z02S03[NE]"
        ]
    },
    {
        "name": "D02Z02S10",
        "exits": [
            {
                "target": "D02Z02S10[W]",
                "logic": []
            }
        ],
        "locations": [
            "Oil[D02Z02S10]"
        ],
        "transitions": []
    },
    {
        "name": "D02Z02S05[E]",
        "exits": [
            {
                "target": "D02Z02S10",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z02S05[E]"
        ]
    },
    {
        "name": "D02Z03S10[-Cherubs]",
        "exits": [
            {
                "target": "D02Z02S07[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z03S10[-Cherubs]"
        ]
    },
    {
        "name": "D02Z02S11",
        "exits": [
            {
                "target": "D02Z02S11[W]",
                "logic": []
            },
            {
                "target": "D02Z02S11[SE]",
                "logic": []
            },
            {
                "target": "D02Z02S11[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "canCrossGap6"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S11[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "QI53",
            "RESCUED_CHERUB_26"
        ],
        "transitions": []
    },
    {
        "name": "D02Z02S06[E]",
        "exits": [
            {
                "target": "D02Z02S11",
                "logic": []
            },
            {
                "target": "D01Z02S03[NW]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z02S06[E]"
        ]
    },
    {
        "name": "D02Z02S08[W]",
        "exits": [
            {
                "target": "D02Z02S11",
                "logic": []
            },
            {
                "target": "D01Z02S03[NW]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z02S08[W]"
        ]
    },
    {
        "name": "D02Z02S12[W]",
        "exits": [
            {
                "target": "D02Z02S11",
                "logic": []
            },
            {
                "target": "D01Z02S03[NW]",
                "logic": []
            },
            {
                "target": "D02Z02S11[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z02S12[W]"
        ]
    },
    {
        "name": "D02Z02S13[W]",
        "exits": [
            {
                "target": "D02Z02S11",
                "logic": []
            },
            {
                "target": "D01Z02S03[NW]",
                "logic": []
            },
            {
                "target": "D02Z02S11[E]",
                "logic": []
            },
            {
                "target": "D02Z02S11[NE]",
                "logic": []
            },
            {
                "target": "D02Z02S07[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z02S13[W]"
        ]
    },
    {
        "name": "D02BZ02S01",
        "exits": [
            {
                "target": "D02BZ02S01[C]",
                "logic": []
            }
        ],
        "locations": [
            "QI11",
            "RB37",
            "RB02"
        ],
        "transitions": []
    },
    {
        "name": "D02Z02S08[C]",
        "exits": [
            {
                "target": "D02BZ02S01",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z02S08[C]"
        ]
    },
    {
        "name": "D02Z02S06",
        "exits": [
            {
                "target": "D02Z02S06[E]",
                "logic": []
            }
        ],
        "locations": [
            "RB38"
        ],
        "transitions": []
    },
    {
        "name": "D02Z02S11[W]",
        "exits": [
            {
                "target": "D02Z02S06",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z02S11[W]"
        ]
    },
    {
        "name": "D02Z02S12",
        "exits": [
            {
                "target": "D02Z02S12[W]",
                "logic": []
            }
        ],
        "locations": [
            "Lady[D02Z02S12]"
        ],
        "transitions": []
    },
    {
        "name": "D02Z02S11[E]",
        "exits": [
            {
                "target": "D02Z02S12",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z02S11[E]"
        ]
    },
    {
        "name": "D02Z02S13",
        "exits": [
            {
                "target": "D02Z02S13[W]",
                "logic": []
            }
        ],
        "locations": [
            "HE11"
        ],
        "transitions": []
    },
    {
        "name": "D02Z02S11[NE]",
        "exits": [
            {
                "target": "D02Z02S13",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z02S11[NE]"
        ]
    },
    {
        "name": "D02Z03S07[E]",
        "exits": [
            {
                "target": "D02Z03S08[W]",
                "logic": []
            },
            {
                "target": "D02Z03S08[SW]",
                "logic": []
            },
            {
                "target": "D02Z02S07[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z03S07[E]"
        ]
    },
    {
        "name": "D02Z03S12[E]",
        "exits": [
            {
                "target": "D02Z03S08[SW]",
                "logic": []
            },
            {
                "target": "D02Z02S07[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z03S12[E]"
        ]
    },
    {
        "name": "D02Z03S02[W]",
        "exits": [
            {
                "target": "CO05",
                "logic": [
                    {
                        "item_requirements": [
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canCrossGap3"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z03S05[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canCrossGap3"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z03S05[S]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RB08",
                "logic": [
                    {
                        "item_requirements": [
                            "dash",
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "dash",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S07[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z03S02[W]",
            "D02Z03S03[E]",
            "D02Z03S05[E]",
            "D02Z03S03[W]"
        ]
    },
    {
        "name": "D02Z03S05[NE]",
        "exits": [
            {
                "target": "CO05",
                "logic": []
            },
            {
                "target": "D02Z03S05[S]",
                "logic": []
            },
            {
                "target": "RB08",
                "logic": [
                    {
                        "item_requirements": [
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z03S02[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z03S05[NE]",
            "D02Z03S03[NW]"
        ]
    },
    {
        "name": "D02Z03S21",
        "exits": [
            {
                "target": "D02Z03S21[W]",
                "logic": []
            },
            {
                "target": "D02Z03S21[E]",
                "logic": []
            }
        ],
        "locations": [
            "QI40",
            "QI57"
        ],
        "transitions": []
    },
    {
        "name": "D02Z03S02[NW]",
        "exits": [
            {
                "target": "D02Z03S21",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z03S02[NW]"
        ]
    },
    {
        "name": "D02Z03S20[E]",
        "exits": [
            {
                "target": "D02Z03S21",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z03S20[E]"
        ]
    },
    {
        "name": "D02Z03S13",
        "exits": [
            {
                "target": "D02Z03S13[W]",
                "logic": []
            }
        ],
        "locations": [
            "Sword[D02Z03S13]"
        ],
        "transitions": []
    },
    {
        "name": "D02Z03S02[NE]",
        "exits": [
            {
                "target": "D02Z03S13",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z03S02[NE]"
        ]
    },
    {
        "name": "D02Z03S02[N]",
        "exits": [
            {
                "target": "D02Z03S11[S]",
                "logic": []
            },
            {
                "target": "D02Z03S11[W]",
                "logic": []
            },
            {
                "target": "D02Z03S11[NW]",
                "logic": []
            },
            {
                "target": "D02Z03S10[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z03S02[N]"
        ]
    },
    {
        "name": "D02Z03S10[W]",
        "exits": [
            {
                "target": "D02Z03S11[S]",
                "logic": []
            },
            {
                "target": "D02Z03S11[W]",
                "logic": []
            },
            {
                "target": "D02Z03S11[NW]",
                "logic": []
            },
            {
                "target": "D02Z03S10[-W]",
                "logic": []
            },
            {
                "target": "D02Z03S10[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z03S10[W]",
            "D02Z03S11[E]",
            "D02Z03S22[W]",
            "D02Z03S11[NE]"
        ]
    },
    {
        "name": "D02Z03S15[E]",
        "exits": [
            {
                "target": "D02Z03S11[S]",
                "logic": []
            },
            {
                "target": "D02Z03S11[W]",
                "logic": []
            },
            {
                "target": "D02Z03S11[NW]",
                "logic": []
            },
            {
                "target": "D02Z03S10[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z03S15[E]"
        ]
    },
    {
        "name": "D02Z03S19[E]",
        "exits": [
            {
                "target": "D02Z03S11[S]",
                "logic": []
            },
            {
                "target": "D02Z03S11[W]",
                "logic": []
            },
            {
                "target": "D02Z03S11[NW]",
                "logic": []
            },
            {
                "target": "D02Z03S10[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z03S19[E]"
        ]
    },
    {
        "name": "D02Z03S07[N]",
        "exits": [
            {
                "target": "D02Z03S05[S]",
                "logic": []
            },
            {
                "target": "D02Z03S05[NE]",
                "logic": []
            },
            {
                "target": "RB08",
                "logic": [
                    {
                        "item_requirements": [
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z03S02[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z03S07[N]"
        ]
    },
    {
        "name": "D02Z03S11[S]",
        "exits": [
            {
                "target": "D02Z03S02[W]",
                "logic": []
            },
            {
                "target": "D02Z03S02[NW]",
                "logic": []
            },
            {
                "target": "D02Z03S02[NE]",
                "logic": []
            },
            {
                "target": "D02Z03S02[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "openedConventLadder"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S07[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z03S11[S]"
        ]
    },
    {
        "name": "D02Z03S13[W]",
        "exits": [
            {
                "target": "D02Z03S02[W]",
                "logic": []
            },
            {
                "target": "D02Z03S02[NW]",
                "logic": []
            },
            {
                "target": "D02Z03S02[NE]",
                "logic": []
            },
            {
                "target": "D02Z03S02[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "openedConventLadder"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S07[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z03S13[W]"
        ]
    },
    {
        "name": "D02Z03S21[E]",
        "exits": [
            {
                "target": "D02Z03S02[W]",
                "logic": []
            },
            {
                "target": "D02Z03S02[NW]",
                "logic": []
            },
            {
                "target": "D02Z03S02[NE]",
                "logic": []
            },
            {
                "target": "D02Z03S02[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "openedConventLadder"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z02S07[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z03S21[E]"
        ]
    },
    {
        "name": "D02Z03S07",
        "exits": [
            {
                "target": "D02Z03S07[W]",
                "logic": []
            },
            {
                "target": "D02Z03S07[NWW]",
                "logic": []
            },
            {
                "target": "D02Z03S07[NW]",
                "logic": []
            },
            {
                "target": "D02Z03S07[N]",
                "logic": []
            },
            {
                "target": "D02Z03S07[E]",
                "logic": []
            }
        ],
        "locations": [
            "CO15"
        ],
        "transitions": []
    },
    {
        "name": "D02Z03S05[S]",
        "exits": [
            {
                "target": "D02Z03S07",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z03S05[S]"
        ]
    },
    {
        "name": "D02Z03S06[S]",
        "exits": [
            {
                "target": "D02Z03S07",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z03S06[S]"
        ]
    },
    {
        "name": "D02Z03S08[W]",
        "exits": [
            {
                "target": "D02Z03S07",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z03S08[W]"
        ]
    },
    {
        "name": "D02Z03S17[E]",
        "exits": [
            {
                "target": "D02Z03S07",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z03S17[E]"
        ]
    },
    {
        "name": "D02Z03S24[E]",
        "exits": [
            {
                "target": "D02Z03S07",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z03S24[E]"
        ]
    },
    {
        "name": "D02Z03S06[W]",
        "exits": [
            {
                "target": "D02Z03S18[NW]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z03S18[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RB18",
                "logic": [
                    {
                        "item_requirements": [
                            "redWax1"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z03S06[S]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z03S06[W]",
            "D02Z03S18[SE]"
        ]
    },
    {
        "name": "D02Z03S09[W]",
        "exits": [
            {
                "target": "D02Z03S18[NW]",
                "logic": []
            },
            {
                "target": "D02Z03S18[NE]",
                "logic": []
            },
            {
                "target": "D02Z03S06[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z03S09[W]"
        ]
    },
    {
        "name": "D02Z03S23[E]",
        "exits": [
            {
                "target": "D02Z03S18[NW]",
                "logic": []
            },
            {
                "target": "D02Z03S18[NE]",
                "logic": []
            },
            {
                "target": "D02Z03S06[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z03S23[E]"
        ]
    },
    {
        "name": "D02Z03S17",
        "exits": [
            {
                "target": "D02Z03S17[E]",
                "logic": []
            }
        ],
        "locations": [
            "RB24"
        ],
        "transitions": []
    },
    {
        "name": "D02Z03S07[W]",
        "exits": [
            {
                "target": "D02Z03S17",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z03S07[W]"
        ]
    },
    {
        "name": "D02Z03S07[NWW]",
        "exits": [
            {
                "target": "D02Z03S24[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z03S07[NWW]"
        ]
    },
    {
        "name": "D02Z03S07[NW]",
        "exits": [
            {
                "target": "RB18",
                "logic": [
                    {
                        "item_requirements": [
                            "redWax1"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z03S06[W]",
                "logic": []
            },
            {
                "target": "D02Z03S06[S]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z03S07[NW]"
        ]
    },
    {
        "name": "D02Z03S12",
        "exits": [
            {
                "target": "D02Z03S12[E]",
                "logic": []
            }
        ],
        "locations": [
            "HE03"
        ],
        "transitions": []
    },
    {
        "name": "D02Z03S08[SW]",
        "exits": [
            {
                "target": "D02Z03S12",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z03S08[SW]"
        ]
    },
    {
        "name": "D02Z03S20",
        "exits": [
            {
                "target": "D02Z03S20[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "canBeatConventBoss"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D02Z03S20[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "canBeatConventBoss"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "BS03"
        ],
        "transitions": []
    },
    {
        "name": "D02Z03S09[E]",
        "exits": [
            {
                "target": "D02Z03S20",
                "logic": []
            },
            {
                "target": "D02Z03S20[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z03S09[E]"
        ]
    },
    {
        "name": "D02Z03S21[W]",
        "exits": [
            {
                "target": "D02Z03S20",
                "logic": []
            },
            {
                "target": "D02Z03S20[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z03S21[W]"
        ]
    },
    {
        "name": "D09Z01S06",
        "exits": [
            {
                "target": "D09Z01S06[-E]",
                "logic": [
                    {
                        "item_requirements": [
                            "peaksKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S06[E]",
                "logic": []
            }
        ],
        "locations": [
            "RESCUED_CHERUB_05"
        ],
        "transitions": []
    },
    {
        "name": "D02Z03S10[-W]",
        "exits": [
            {
                "target": "D09Z01S06",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z03S10[-W]"
        ]
    },
    {
        "name": "D09Z01S04[W]",
        "exits": [
            {
                "target": "D09Z01S06",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D09Z01S04[W]"
        ]
    },
    {
        "name": "D02Z03S15",
        "exits": [
            {
                "target": "D02Z03S15[E]",
                "logic": []
            }
        ],
        "locations": [
            "Lady[D02Z03S15]"
        ],
        "transitions": []
    },
    {
        "name": "D02Z03S11[W]",
        "exits": [
            {
                "target": "D02Z03S15",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z03S11[W]"
        ]
    },
    {
        "name": "D02Z03S19",
        "exits": [
            {
                "target": "D02Z03S19[E]",
                "logic": []
            }
        ],
        "locations": [
            "QI61"
        ],
        "transitions": []
    },
    {
        "name": "D02Z03S11[NW]",
        "exits": [
            {
                "target": "D02Z03S19",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z03S11[NW]"
        ]
    },
    {
        "name": "D09Z01S06[-E]",
        "exits": [
            {
                "target": "D02Z03S10[W]",
                "logic": []
            },
            {
                "target": "D02Z03S10[-W]",
                "logic": []
            },
            {
                "target": "D02Z03S10[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D09Z01S06[-E]"
        ]
    },
    {
        "name": "D02Z03S23",
        "exits": [
            {
                "target": "D02Z03S23[E]",
                "logic": []
            }
        ],
        "locations": [
            "RB107"
        ],
        "transitions": []
    },
    {
        "name": "D02Z03S18[NW]",
        "exits": [
            {
                "target": "D02Z03S23",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z03S18[NW]"
        ]
    },
    {
        "name": "D02Z03S09",
        "exits": [
            {
                "target": "D02Z03S09[W]",
                "logic": []
            },
            {
                "target": "D02Z03S09[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": []
    },
    {
        "name": "D02Z03S18[NE]",
        "exits": [
            {
                "target": "D02Z03S09",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z03S18[NE]"
        ]
    },
    {
        "name": "D02Z03S20[W]",
        "exits": [
            {
                "target": "D02Z03S09",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D02Z03S20[W]"
        ]
    },
    {
        "name": "D03Z01S01[W]",
        "exits": [
            {
                "target": "D03Z01S02[E]",
                "logic": []
            },
            {
                "target": "D03Z01S06[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canCrossGap3"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z01S01[W]"
        ]
    },
    {
        "name": "D03Z01S06[E]",
        "exits": [
            {
                "target": "D03Z01S06",
                "logic": []
            },
            {
                "target": "D03Z01S02[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canCrossGap7"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z01S06[E]",
            "D03Z01S02[W]"
        ]
    },
    {
        "name": "D20Z01S02[E]",
        "exits": [
            {
                "target": "D20Z01S03[W]",
                "logic": []
            },
            {
                "target": "D20Z01S03[N]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D20Z01S02[E]"
        ]
    },
    {
        "name": "D03Z01S01[-Cherubs]",
        "exits": [
            {
                "target": "D20Z01S01[W]",
                "logic": []
            },
            {
                "target": "D20Z01S01[E]",
                "logic": []
            },
            {
                "target": "D20Z01S01[S]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z01S01[-Cherubs]"
        ]
    },
    {
        "name": "D03Z02S15[E]",
        "exits": [
            {
                "target": "D20Z01S01[W]",
                "logic": []
            },
            {
                "target": "D20Z01S01[E]",
                "logic": []
            },
            {
                "target": "D20Z01S01[S]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z02S15[E]"
        ]
    },
    {
        "name": "D20Z01S02[W]",
        "exits": [
            {
                "target": "D20Z01S01[W]",
                "logic": []
            },
            {
                "target": "D20Z01S01[E]",
                "logic": []
            },
            {
                "target": "D20Z01S01[S]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D20Z01S02[W]"
        ]
    },
    {
        "name": "D03Z01S06",
        "exits": [
            {
                "target": "D03Z01S06[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "canBeatPerpetua"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z01S03[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "canBeatPerpetua"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "RB13",
            "QI14"
        ],
        "transitions": []
    },
    {
        "name": "D03Z01S03[E]",
        "exits": [
            {
                "target": "D03Z01S06",
                "logic": []
            },
            {
                "target": "D03Z01S03[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb",
                            "canCrossGap9"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z01S03[SW]",
                "logic": [
                    {
                        "item_requirements": [
                            "canCrossGap9"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z01S03[SE]",
                "logic": []
            },
            {
                "target": "D03Z01S03[-WestL]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen",
                            "canCrossGap9"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z01S03[-WestR]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen",
                            "canCrossGap9"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z01S03[-EastL]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen",
                            "canCrossGap5"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z01S03[-EastR]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "QI47",
                "logic": [
                    {
                        "item_requirements": [
                            "blood",
                            "canCrossGap9"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canCrossGap9"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RB22",
                "logic": [
                    {
                        "item_requirements": [
                            "canCrossGap9"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RESCUED_CHERUB_16",
                "logic": [
                    {
                        "item_requirements": [
                            "canCrossGap9"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "Amanecida[D03Z01S03]",
                "logic": [
                    {
                        "item_requirements": [
                            "canBeatJondoBoss",
                            "canCrossGap9"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z01S03[E]",
            "D03Z01S06[W]"
        ]
    },
    {
        "name": "D03Z01S04",
        "exits": [
            {
                "target": "D03Z01S04[NW]",
                "logic": []
            },
            {
                "target": "D03Z01S04[E]",
                "logic": []
            }
        ],
        "locations": [
            "QI63"
        ],
        "transitions": []
    },
    {
        "name": "D03Z01S03[W]",
        "exits": [
            {
                "target": "D03Z01S04",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z01S03[W]"
        ]
    },
    {
        "name": "D03Z01S05[E]",
        "exits": [
            {
                "target": "D03Z01S04",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z01S05[E]"
        ]
    },
    {
        "name": "D03Z02S10",
        "exits": [
            {
                "target": "D03Z02S10[W]",
                "logic": []
            },
            {
                "target": "D03Z02S10[N]",
                "logic": []
            },
            {
                "target": "D03Z02S10[S]",
                "logic": []
            },
            {
                "target": "D03Z02S10[E]",
                "logic": []
            },
            {
                "target": "D03Z02S10[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "RESCUED_CHERUB_17"
        ],
        "transitions": []
    },
    {
        "name": "D03Z01S03[SW]",
        "exits": [
            {
                "target": "D03Z02S10",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z01S03[SW]"
        ]
    },
    {
        "name": "D03Z01S03[-WestL]",
        "exits": [
            {
                "target": "D03Z02S10",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z01S03[-WestL]"
        ]
    },
    {
        "name": "D03Z02S02[W]",
        "exits": [
            {
                "target": "D03Z02S10",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z02S02[W]"
        ]
    },
    {
        "name": "D03Z02S09[N]",
        "exits": [
            {
                "target": "D03Z02S10",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z02S09[N]"
        ]
    },
    {
        "name": "D03Z02S13[E]",
        "exits": [
            {
                "target": "D03Z02S10",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z02S13[E]"
        ]
    },
    {
        "name": "D03Z02S01",
        "exits": [
            {
                "target": "PR10",
                "logic": [
                    {
                        "item_requirements": [
                            "canClimbOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canCrossGap8"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canEnemyBounce"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z02S02[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canEnemyBounce"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z01S03[SE]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "CO08"
        ],
        "transitions": []
    },
    {
        "name": "D03Z01S03[SE]",
        "exits": [
            {
                "target": "D03Z02S01",
                "logic": []
            },
            {
                "target": "D03Z01S03[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb",
                            "canCrossGap9"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z01S03[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z01S03[SW]",
                "logic": [
                    {
                        "item_requirements": [
                            "canCrossGap9"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z01S03[-WestL]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen",
                            "canCrossGap9"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z01S03[-WestR]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen",
                            "canCrossGap9"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z01S03[-EastL]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen",
                            "canCrossGap5"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z01S03[-EastR]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "QI47",
                "logic": [
                    {
                        "item_requirements": [
                            "blood",
                            "canCrossGap9"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canCrossGap9"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RB22",
                "logic": [
                    {
                        "item_requirements": [
                            "canCrossGap9"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RESCUED_CHERUB_16",
                "logic": [
                    {
                        "item_requirements": [
                            "canCrossGap9"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "Amanecida[D03Z01S03]",
                "logic": [
                    {
                        "item_requirements": [
                            "canBeatJondoBoss",
                            "canCrossGap9"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z01S03[SE]",
            "D03Z02S01[N]"
        ]
    },
    {
        "name": "D03Z01S03[-EastR]",
        "exits": [
            {
                "target": "D03Z02S01",
                "logic": []
            },
            {
                "target": "PR10",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z01S03[-EastR]"
        ]
    },
    {
        "name": "D03Z02S02[E]",
        "exits": [
            {
                "target": "D03Z02S01",
                "logic": []
            },
            {
                "target": "D03Z02S02[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z02S03[N]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z02S02[E]",
            "D03Z02S01[W]"
        ]
    },
    {
        "name": "D03Z01S03[-WestR]",
        "exits": [
            {
                "target": "D03Z02S02[W]",
                "logic": []
            },
            {
                "target": "D03Z02S02[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canEnemyBounce"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z02S03[N]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z01S03[-WestR]"
        ]
    },
    {
        "name": "D03Z01S03[-EastL]",
        "exits": [
            {
                "target": "D03Z02S02[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z02S02[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canEnemyBounce"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z02S03[N]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z01S03[-EastL]"
        ]
    },
    {
        "name": "D03Z02S03[N]",
        "exits": [
            {
                "target": "D03Z02S02[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "doubleJump",
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canEnemyBounce"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z02S02[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canEnemyBounce"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z02S03[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z02S06[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "brokeJondoBellW",
                            "brokeJondoBellE"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z02S05[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "canAirStall"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "boots"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z02S04[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z02S04[S]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "CO33",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z02S03[N]",
            "D03Z02S02[S]",
            "D03Z02S04[NW]",
            "D03Z02S03[SE2]"
        ]
    },
    {
        "name": "D03Z02S10[E]",
        "exits": [
            {
                "target": "D03Z02S02[W]",
                "logic": []
            },
            {
                "target": "D03Z02S02[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canEnemyBounce"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z02S03[N]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z02S10[E]"
        ]
    },
    {
        "name": "D03Z01S04[NW]",
        "exits": [
            {
                "target": "D03Z01S05[E]",
                "logic": []
            },
            {
                "target": "D17Z01S07[SE]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z01S04[NW]"
        ]
    },
    {
        "name": "D17Z01S07[SE]",
        "exits": [
            {
                "target": "D03Z01S05[E]",
                "logic": []
            },
            {
                "target": "D17Z01S07[SW]",
                "logic": []
            },
            {
                "target": "D17Z01S07[N]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D17Z01S07[SE]",
            "D03Z01S05[W]",
            "D17Z01S06[E]",
            "D17Z01S07[W]",
            "D17Z01S09[E]",
            "D17Z01S07[NW]"
        ]
    },
    {
        "name": "D03Z01S04[E]",
        "exits": [
            {
                "target": "D03Z01S03[W]",
                "logic": []
            },
            {
                "target": "D03Z01S03[SW]",
                "logic": []
            },
            {
                "target": "D03Z01S03[-WestL]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z01S03[-WestR]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z01S03[-EastL]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "QI47",
                "logic": [
                    {
                        "item_requirements": [
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RB22",
                "logic": []
            },
            {
                "target": "RESCUED_CHERUB_16",
                "logic": []
            },
            {
                "target": "Amanecida[D03Z01S03]",
                "logic": [
                    {
                        "item_requirements": [
                            "canBeatJondoBoss"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z01S03[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z01S03[SE]",
                "logic": []
            },
            {
                "target": "D03Z01S03[-EastR]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z01S04[E]"
        ]
    },
    {
        "name": "D03Z02S10[N]",
        "exits": [
            {
                "target": "D03Z01S03[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z01S03[SW]",
                "logic": []
            },
            {
                "target": "D03Z01S03[-WestL]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z01S03[-WestR]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z01S03[-EastL]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "QI47",
                "logic": [
                    {
                        "item_requirements": [
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RB22",
                "logic": []
            },
            {
                "target": "RESCUED_CHERUB_16",
                "logic": []
            },
            {
                "target": "Amanecida[D03Z01S03]",
                "logic": [
                    {
                        "item_requirements": [
                            "canBeatJondoBoss"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z01S03[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z01S03[SE]",
                "logic": []
            },
            {
                "target": "D03Z01S03[-EastR]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z02S10[N]"
        ]
    },
    {
        "name": "D17Z01S04[S]",
        "exits": [
            {
                "target": "D17Z01S07[SW]",
                "logic": []
            },
            {
                "target": "D17Z01S07[SE]",
                "logic": []
            },
            {
                "target": "D17Z01S07[N]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D17Z01S04[S]"
        ]
    },
    {
        "name": "D17Z01S08[E]",
        "exits": [
            {
                "target": "D17Z01S07[SW]",
                "logic": []
            },
            {
                "target": "D17Z01S07[SE]",
                "logic": []
            },
            {
                "target": "D17Z01S07[N]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D17Z01S08[E]"
        ]
    },
    {
        "name": "D03Z02S05[W]",
        "exits": [
            {
                "target": "D03Z02S03[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z02S03[N]",
                "logic": []
            },
            {
                "target": "D03Z02S06[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "brokeJondoBellW",
                            "brokeJondoBellE"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RESCUED_CHERUB_18",
                "logic": [
                    {
                        "item_requirements": [
                            "canCrossGap5"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canEnemyBounce",
                            "canCrossGap3"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z02S04[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "canCrossGap5"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canEnemyBounce",
                            "canCrossGap3"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z02S05[W]",
            "D03Z02S03[E]"
        ]
    },
    {
        "name": "D03Z02S06[W]",
        "exits": [
            {
                "target": "D03Z02S06",
                "logic": []
            },
            {
                "target": "D03Z02S07",
                "logic": []
            },
            {
                "target": "D03Z03S12[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z02S06[W]",
            "D03Z02S03[SE]",
            "D03Z02S07[E]",
            "D03Z02S03[SW]",
            "D03Z03S01[NL]",
            "D03Z02S03[SSL]",
            "D03Z02S03[SSC]",
            "D03Z02S03[SSR]",
            "D03Z03S01[NR]"
        ]
    },
    {
        "name": "D03Z02S07[N]",
        "exits": [
            {
                "target": "D03Z02S03[W]",
                "logic": []
            },
            {
                "target": "D03Z02S03[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z02S06[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "brokeJondoBellW",
                            "brokeJondoBellE",
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z02S07[N]"
        ]
    },
    {
        "name": "D03Z02S07",
        "exits": [
            {
                "target": "D03Z02S07[W]",
                "logic": []
            },
            {
                "target": "D03Z02S07[N]",
                "logic": []
            }
        ],
        "locations": [
            "CO07"
        ],
        "transitions": []
    },
    {
        "name": "D03Z02S03[W]",
        "exits": [
            {
                "target": "D03Z02S07",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z02S03[W]"
        ]
    },
    {
        "name": "D03Z02S08[E]",
        "exits": [
            {
                "target": "D03Z02S07",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z02S08[E]"
        ]
    },
    {
        "name": "D03Z02S04[NE]",
        "exits": [
            {
                "target": "RESCUED_CHERUB_18",
                "logic": []
            },
            {
                "target": "D03Z02S04[S]",
                "logic": []
            },
            {
                "target": "CO33",
                "logic": []
            },
            {
                "target": "HE06",
                "logic": [
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RESCUED_CHERUB_37",
                "logic": [
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "dash",
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "dash",
                            "canCrossGap2",
                            "canEnemyBounce"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "dash",
                            "canCrossGap3"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z02S05[W]",
                "logic": []
            },
            {
                "target": "D03Z02S03[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z02S11[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "dash",
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "dash",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "dash",
                            "canCrossGap2",
                            "canEnemyBounce"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z02S04[NE]",
            "D03Z02S05[S]",
            "D03Z02S11[W]",
            "D03Z02S05[E]"
        ]
    },
    {
        "name": "D03Z02S06[N]",
        "exits": [
            {
                "target": "D03Z02S04[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z02S04[S]",
                "logic": []
            },
            {
                "target": "CO33",
                "logic": []
            },
            {
                "target": "D03Z02S03[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z02S06[N]"
        ]
    },
    {
        "name": "D03Z02S06",
        "exits": [
            {
                "target": "D03Z02S06[N]",
                "logic": []
            }
        ],
        "locations": [
            "QI19"
        ],
        "transitions": []
    },
    {
        "name": "D03Z02S04[S]",
        "exits": [
            {
                "target": "D03Z02S06",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z02S04[S]"
        ]
    },
    {
        "name": "D03Z03S12[W]",
        "exits": [
            {
                "target": "D03Z02S06[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z03S02",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z03S12[W]",
            "D03Z03S01[S]",
            "D03Z03S18[E]",
            "D03Z03S01[W]",
            "D03Z03S02[W]",
            "D03Z03S12[E]"
        ]
    },
    {
        "name": "D03Z02S15[W]",
        "exits": [
            {
                "target": "D03Z02S11[E]",
                "logic": []
            },
            {
                "target": "HE06",
                "logic": [
                    {
                        "item_requirements": [
                            "dash",
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "dash",
                            "canCrossGap2"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "dash",
                            "preciseSkipsAllowed",
                            "canCrossGap1"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RESCUED_CHERUB_37",
                "logic": [
                    {
                        "item_requirements": [
                            "dash",
                            "canCrossGap1"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "dash",
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "dash",
                            "canEnemyBounce"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z02S04[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "dash",
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "dash",
                            "canCrossGap2"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "dash",
                            "preciseSkipsAllowed",
                            "canCrossGap1"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z02S15[W]"
        ]
    },
    {
        "name": "D03Z02S07[W]",
        "exits": [
            {
                "target": "D03Z02S08[E]",
                "logic": []
            },
            {
                "target": "QI41",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z02S09[S]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z02S07[W]"
        ]
    },
    {
        "name": "D03Z02S09[S]",
        "exits": [
            {
                "target": "QI41",
                "logic": []
            },
            {
                "target": "D03Z02S09[N]",
                "logic": []
            },
            {
                "target": "D03Z02S08[E]",
                "logic": []
            },
            {
                "target": "D03Z02S09[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z02S09[S]",
            "D03Z02S08[N]",
            "D03Z02S14[E]",
            "D03Z02S08[W]"
        ]
    },
    {
        "name": "D03Z02S10[S]",
        "exits": [
            {
                "target": "D03Z02S09[N]",
                "logic": []
            },
            {
                "target": "D03Z02S09[S]",
                "logic": []
            },
            {
                "target": "D03Z02S09[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z02S10[S]"
        ]
    },
    {
        "name": "D03Z02S10[-Cherubs]",
        "exits": [
            {
                "target": "D03Z02S09[N]",
                "logic": []
            },
            {
                "target": "D03Z02S09[S]",
                "logic": []
            },
            {
                "target": "D03Z02S09[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z02S10[-Cherubs]"
        ]
    },
    {
        "name": "D03Z02S12[E]",
        "exits": [
            {
                "target": "D03Z02S09[W]",
                "logic": []
            },
            {
                "target": "D03Z02S09[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z02S09[S]",
                "logic": [
                    {
                        "item_requirements": [
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z02S12[E]"
        ]
    },
    {
        "name": "D03Z02S12",
        "exits": [
            {
                "target": "D03Z02S12[E]",
                "logic": []
            }
        ],
        "locations": [
            "QI52"
        ],
        "transitions": []
    },
    {
        "name": "D03Z02S09[W]",
        "exits": [
            {
                "target": "D03Z02S12",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z02S09[W]"
        ]
    },
    {
        "name": "D03Z02S13[-Cherubs]",
        "exits": [
            {
                "target": "D03Z02S12",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z02S13[-Cherubs]"
        ]
    },
    {
        "name": "D03Z02S13",
        "exits": [
            {
                "target": "D03Z02S13[E]",
                "logic": []
            },
            {
                "target": "D03Z02S13[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "RB28"
        ],
        "transitions": []
    },
    {
        "name": "D03Z02S10[W]",
        "exits": [
            {
                "target": "D03Z02S13",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z02S10[W]"
        ]
    },
    {
        "name": "D03Z02S15",
        "exits": [
            {
                "target": "D03Z02S15[W]",
                "logic": []
            },
            {
                "target": "D03Z02S15[E]",
                "logic": []
            }
        ],
        "locations": [
            "QI103"
        ],
        "transitions": []
    },
    {
        "name": "D03Z02S11[E]",
        "exits": [
            {
                "target": "D03Z02S15",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z02S11[E]"
        ]
    },
    {
        "name": "D20Z01S01[W]",
        "exits": [
            {
                "target": "D03Z02S15",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D20Z01S01[W]"
        ]
    },
    {
        "name": "D03Z03S02[NE]",
        "exits": [
            {
                "target": "D03Z03S02",
                "logic": []
            },
            {
                "target": "D03Z03S12[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z03S02[NE]",
            "D03Z03S14[W]"
        ]
    },
    {
        "name": "D03Z03S02[E]",
        "exits": [
            {
                "target": "D03Z03S03[W]",
                "logic": []
            },
            {
                "target": "D03Z03S04[NW]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z03S02[E]"
        ]
    },
    {
        "name": "D03Z03S04[NW]",
        "exits": [
            {
                "target": "D03Z03S03[W]",
                "logic": []
            },
            {
                "target": "D03Z03S04[SW]",
                "logic": []
            },
            {
                "target": "D03Z03S05[NW]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canEnemyBounce"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z03S05[SW]",
                "logic": []
            },
            {
                "target": "D03Z03S04[SE]",
                "logic": [
                    {
                        "item_requirements": [
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z03S04[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z03S04[NW]",
            "D03Z03S03[NE]"
        ]
    },
    {
        "name": "D03Z03S04[SW]",
        "exits": [
            {
                "target": "D03Z03S04[NW]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z03S05[NW]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canEnemyBounce"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z03S05[SW]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z03S04[SE]",
                "logic": [
                    {
                        "item_requirements": [
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z03S04[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z03S04[SW]",
            "D03Z03S03[SE]"
        ]
    },
    {
        "name": "D03Z03S02",
        "exits": [
            {
                "target": "D03Z03S02[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z03S02[E]",
                "logic": []
            },
            {
                "target": "D03Z03S12[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "QI44"
        ],
        "transitions": []
    },
    {
        "name": "D03Z03S03[W]",
        "exits": [
            {
                "target": "D03Z03S02",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z03S03[W]"
        ]
    },
    {
        "name": "D03Z03S05[NW]",
        "exits": [
            {
                "target": "D03Z03S04[NW]",
                "logic": []
            },
            {
                "target": "D03Z03S04[SW]",
                "logic": []
            },
            {
                "target": "D03Z03S05[NE]",
                "logic": []
            },
            {
                "target": "D03Z03S05[SW]",
                "logic": []
            },
            {
                "target": "D03Z03S04[SE]",
                "logic": [
                    {
                        "item_requirements": [
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z03S04[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z03S05[NW]",
            "D03Z03S04[NE]"
        ]
    },
    {
        "name": "D03Z03S05[SW]",
        "exits": [
            {
                "target": "D03Z03S04[NW]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z03S04[SW]",
                "logic": []
            },
            {
                "target": "D03Z03S05[NW]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canEnemyBounce"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z03S04[SE]",
                "logic": [
                    {
                        "item_requirements": [
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z03S04[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z03S07[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z03S07[E]",
                "logic": []
            },
            {
                "target": "D03Z03S07[S]",
                "logic": []
            },
            {
                "target": "D03Z03S19[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z03S05[SW]",
            "D03Z03S04[E]",
            "D03Z03S07[SW]",
            "D03Z03S05[SE]"
        ]
    },
    {
        "name": "D03Z03S13[W]",
        "exits": [
            {
                "target": "D03Z03S04[SE]",
                "logic": []
            },
            {
                "target": "D03Z03S04[NW]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb",
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "canCrossGap10"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canCrossGap10"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z03S04[SW]",
                "logic": [
                    {
                        "item_requirements": [
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canCrossGap10"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z03S04[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z03S05[NW]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb",
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "canCrossGap10"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canEnemyBounce",
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canEnemyBounce",
                            "canCrossGap10"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z03S05[SW]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb",
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "canCrossGap10"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canCrossGap10"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z03S13[W]"
        ]
    },
    {
        "name": "D03Z03S06[W]",
        "exits": [
            {
                "target": "D03Z03S05[NW]",
                "logic": []
            },
            {
                "target": "D03Z03S05[NE]",
                "logic": []
            },
            {
                "target": "D03Z03S05[SW]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z03S06[W]"
        ]
    },
    {
        "name": "D03Z03S13",
        "exits": [
            {
                "target": "D03Z03S13[W]",
                "logic": []
            }
        ],
        "locations": [
            "Oil[D03Z03S13]"
        ],
        "transitions": []
    },
    {
        "name": "D03Z03S04[SE]",
        "exits": [
            {
                "target": "D03Z03S13",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z03S04[SE]"
        ]
    },
    {
        "name": "D03Z03S10",
        "exits": [
            {
                "target": "D03Z03S10[E]",
                "logic": []
            }
        ],
        "locations": [
            "QI13"
        ],
        "transitions": []
    },
    {
        "name": "D03Z03S04[-Cherubs]",
        "exits": [
            {
                "target": "D03Z03S10",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z03S04[-Cherubs]"
        ]
    },
    {
        "name": "D03Z03S09[SW]",
        "exits": [
            {
                "target": "D03Z03S10",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z03S09[SW]"
        ]
    },
    {
        "name": "D03Z03S06",
        "exits": [
            {
                "target": "D03Z03S06[W]",
                "logic": []
            }
        ],
        "locations": [
            "CO12",
            "RE07",
            "RESCUED_CHERUB_19"
        ],
        "transitions": []
    },
    {
        "name": "D03Z03S05[NE]",
        "exits": [
            {
                "target": "D03Z03S06",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z03S05[NE]"
        ]
    },
    {
        "name": "D03Z03S08[W]",
        "exits": [
            {
                "target": "D03Z03S07[NE]",
                "logic": []
            },
            {
                "target": "D03Z03S07[E]",
                "logic": []
            },
            {
                "target": "D03Z03S07[S]",
                "logic": []
            },
            {
                "target": "D03Z03S05[SW]",
                "logic": []
            },
            {
                "target": "D03Z03S19[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z03S08[W]"
        ]
    },
    {
        "name": "D03Z03S09[N]",
        "exits": [
            {
                "target": "D03Z03S07[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z03S07[E]",
                "logic": []
            },
            {
                "target": "D03Z03S07[S]",
                "logic": []
            },
            {
                "target": "D03Z03S05[SW]",
                "logic": []
            },
            {
                "target": "D03Z03S19[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z03S09[N]"
        ]
    },
    {
        "name": "D03Z03S11[W]",
        "exits": [
            {
                "target": "D03Z03S07[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z03S07[E]",
                "logic": []
            },
            {
                "target": "D03Z03S07[S]",
                "logic": []
            },
            {
                "target": "D03Z03S05[SW]",
                "logic": []
            },
            {
                "target": "D03Z03S19[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z03S11[W]"
        ]
    },
    {
        "name": "D03Z03S19[E]",
        "exits": [
            {
                "target": "D03Z03S07[NE]",
                "logic": []
            },
            {
                "target": "D03Z03S07[E]",
                "logic": []
            },
            {
                "target": "D03Z03S07[S]",
                "logic": []
            },
            {
                "target": "D03Z03S05[SW]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z03S19[E]",
            "D03Z03S07[NW]"
        ]
    },
    {
        "name": "D03Z03S08",
        "exits": [
            {
                "target": "D03Z03S08[W]",
                "logic": []
            },
            {
                "target": "D03Z03S08[-CherubsL]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z03S08[-CherubsR]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "QI10",
            "RESCUED_CHERUB_21"
        ],
        "transitions": []
    },
    {
        "name": "D03Z03S07[NE]",
        "exits": [
            {
                "target": "D03Z03S08",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z03S07[NE]"
        ]
    },
    {
        "name": "D03Z03S11",
        "exits": [
            {
                "target": "D03Z03S11[W]",
                "logic": []
            },
            {
                "target": "D03Z03S11[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": []
    },
    {
        "name": "D03Z03S07[E]",
        "exits": [
            {
                "target": "D03Z03S11",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z03S07[E]"
        ]
    },
    {
        "name": "D03Z03S08[-CherubsL]",
        "exits": [
            {
                "target": "D03Z03S11",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z03S08[-CherubsL]"
        ]
    },
    {
        "name": "D03Z03S08[-CherubsR]",
        "exits": [
            {
                "target": "D03Z03S11",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z03S08[-CherubsR]"
        ]
    },
    {
        "name": "D03Z03S15[W]",
        "exits": [
            {
                "target": "D03Z03S11",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z03S15[W]"
        ]
    },
    {
        "name": "D03Z03S09",
        "exits": [
            {
                "target": "D03Z03S09[SW]",
                "logic": []
            },
            {
                "target": "D03Z03S09[N]",
                "logic": []
            }
        ],
        "locations": [
            "RESCUED_CHERUB_20"
        ],
        "transitions": []
    },
    {
        "name": "D03Z03S07[S]",
        "exits": [
            {
                "target": "D03Z03S09",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z03S07[S]"
        ]
    },
    {
        "name": "D03Z03S10[E]",
        "exits": [
            {
                "target": "D03Z03S09",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z03S10[E]"
        ]
    },
    {
        "name": "D03Z03S15",
        "exits": [
            {
                "target": "D03Z03S15[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "canBeatGrievanceBoss"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D03Z03S15[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "canBeatGrievanceBoss"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "BS04"
        ],
        "transitions": []
    },
    {
        "name": "D03Z03S11[E]",
        "exits": [
            {
                "target": "D03Z03S15",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z03S11[E]"
        ]
    },
    {
        "name": "D03Z03S16[W]",
        "exits": [
            {
                "target": "D03Z03S15",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z03S16[W]"
        ]
    },
    {
        "name": "D03Z03S16",
        "exits": [
            {
                "target": "D03Z03S16[W]",
                "logic": []
            },
            {
                "target": "D03Z03S16[E]",
                "logic": []
            }
        ],
        "locations": [
            "QI39"
        ],
        "transitions": []
    },
    {
        "name": "D03Z03S15[E]",
        "exits": [
            {
                "target": "D03Z03S16",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z03S15[E]"
        ]
    },
    {
        "name": "D03Z03S17[W]",
        "exits": [
            {
                "target": "D03Z03S16",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D03Z03S17[W]"
        ]
    },
    {
        "name": "D04Z01S01[W]",
        "exits": [
            {
                "target": "D08Z02S01[W]",
                "logic": []
            },
            {
                "target": "D08Z02S01[E]",
                "logic": []
            },
            {
                "target": "D08Z02S02[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z01S01[W]"
        ]
    },
    {
        "name": "D08Z01S01[E]",
        "exits": [
            {
                "target": "D08Z02S01[W]",
                "logic": []
            },
            {
                "target": "D08Z02S01[E]",
                "logic": []
            },
            {
                "target": "D08Z02S02[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D08Z01S01[E]"
        ]
    },
    {
        "name": "D08Z02S02[W]",
        "exits": [
            {
                "target": "D08Z02S01[W]",
                "logic": []
            },
            {
                "target": "D08Z02S01[E]",
                "logic": []
            },
            {
                "target": "D08Z02S03[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "brokeBotTCStatue"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D08Z02S03[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D08Z02S02[W]",
            "D08Z02S01[SE]",
            "D08Z02S03[S]",
            "D08Z02S01[N]"
        ]
    },
    {
        "name": "D04Z01S02",
        "exits": [
            {
                "target": "D04Z01S02[W]",
                "logic": []
            },
            {
                "target": "D04Z01S02[NW]",
                "logic": []
            },
            {
                "target": "D04Z01S02[E]",
                "logic": []
            }
        ],
        "locations": [
            "RB14"
        ],
        "transitions": []
    },
    {
        "name": "D04Z01S01[E]",
        "exits": [
            {
                "target": "D04Z01S02",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z01S01[E]"
        ]
    },
    {
        "name": "D04Z01S01[NE]",
        "exits": [
            {
                "target": "D04Z01S02",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z01S01[NE]"
        ]
    },
    {
        "name": "D04Z01S03[W]",
        "exits": [
            {
                "target": "D04Z01S02",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z01S03[W]"
        ]
    },
    {
        "name": "D04Z01S01[N]",
        "exits": [
            {
                "target": "D04Z01S05[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "blood",
                            "canClimbOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canClimbOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D04Z01S05[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D04Z01S01",
                "logic": []
            },
            {
                "target": "D04Z01S01[NE]",
                "logic": []
            },
            {
                "target": "CO23",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z01S01[N]",
            "D04Z01S05[S]"
        ]
    },
    {
        "name": "D04Z01S06[S]",
        "exits": [
            {
                "target": "D04Z01S05[N]",
                "logic": []
            },
            {
                "target": "D04Z01S05[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D04Z01S01[N]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z01S06[S]"
        ]
    },
    {
        "name": "D04Z01S06[Cherubs]",
        "exits": [
            {
                "target": "D04Z01S05[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "blood",
                            "canClimbOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "canClimbOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D04Z01S05[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D04Z01S01[N]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z01S06[Cherubs]"
        ]
    },
    {
        "name": "D04Z01S01",
        "exits": [
            {
                "target": "D04Z01S01[W]",
                "logic": []
            },
            {
                "target": "D04Z01S01[E]",
                "logic": []
            },
            {
                "target": "D04Z01S01[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "canCrossGap3"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D04Z01S01[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "canCrossGap3"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "CO23",
                "logic": [
                    {
                        "item_requirements": [
                            "canCrossGap3"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "RESCUED_CHERUB_35"
        ],
        "transitions": []
    },
    {
        "name": "D04Z01S02[W]",
        "exits": [
            {
                "target": "D04Z01S01",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z01S02[W]"
        ]
    },
    {
        "name": "D04Z01S02[NW]",
        "exits": [
            {
                "target": "D04Z01S01",
                "logic": []
            },
            {
                "target": "D04Z01S01[NE]",
                "logic": []
            },
            {
                "target": "D04Z01S01[N]",
                "logic": []
            },
            {
                "target": "CO23",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z01S02[NW]"
        ]
    },
    {
        "name": "D04Z01S05[-Cherubs]",
        "exits": [
            {
                "target": "D04Z01S01",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z01S05[-Cherubs]"
        ]
    },
    {
        "name": "D08Z02S01[E]",
        "exits": [
            {
                "target": "D04Z01S01",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D08Z02S01[E]"
        ]
    },
    {
        "name": "D04Z01S03",
        "exits": [
            {
                "target": "D04Z01S03[W]",
                "logic": []
            },
            {
                "target": "D04Z01S03[E]",
                "logic": []
            }
        ],
        "locations": [
            "QI37",
            "CO39",
            "RESCUED_CHERUB_28"
        ],
        "transitions": []
    },
    {
        "name": "D04Z01S02[E]",
        "exits": [
            {
                "target": "D04Z01S03",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z01S02[E]"
        ]
    },
    {
        "name": "D04Z01S04[W]",
        "exits": [
            {
                "target": "D04Z01S03",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z01S04[W]"
        ]
    },
    {
        "name": "D05Z01S20[N]",
        "exits": [
            {
                "target": "D04Z01S03",
                "logic": []
            },
            {
                "target": "D05Z01S07[E]",
                "logic": []
            },
            {
                "target": "D05Z01S08[NE]",
                "logic": []
            },
            {
                "target": "D05Z01S06[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "canSurvivePoison3"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RB31",
                "logic": [
                    {
                        "item_requirements": [
                            "canSurvivePoison3"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z01S20[N]",
            "D04Z01S03[S]",
            "D05Z01S06[E]",
            "D05Z01S20[W]",
            "D05Z01S07[NW]",
            "D05Z01S20[E]"
        ]
    },
    {
        "name": "D04Z01S04",
        "exits": [
            {
                "target": "D04Z01S04[W]",
                "logic": []
            },
            {
                "target": "D04Z01S04[E]",
                "logic": []
            }
        ],
        "locations": [
            "RB21",
            "Amanecida[D04Z01S04]"
        ],
        "transitions": []
    },
    {
        "name": "D04Z01S03[E]",
        "exits": [
            {
                "target": "D04Z01S04",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z01S03[E]"
        ]
    },
    {
        "name": "D04Z02S01[W]",
        "exits": [
            {
                "target": "D04Z01S04",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S01[W]"
        ]
    },
    {
        "name": "D06Z01S18[-Cherubs]",
        "exits": [
            {
                "target": "D04Z01S04",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D06Z01S18[-Cherubs]"
        ]
    },
    {
        "name": "D04Z01S04[E]",
        "exits": [
            {
                "target": "D04Z02S01[W]",
                "logic": []
            },
            {
                "target": "D04Z02S01[E]",
                "logic": []
            },
            {
                "target": "RESCUED_CHERUB_30",
                "logic": [
                    {
                        "item_requirements": [
                            "pillar"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z01S04[E]"
        ]
    },
    {
        "name": "D04Z02S02[S]",
        "exits": [
            {
                "target": "D04Z02S01[N]",
                "logic": []
            },
            {
                "target": "RE402",
                "logic": []
            },
            {
                "target": "RESCUED_CHERUB_30",
                "logic": []
            },
            {
                "target": "D04Z02S01[W]",
                "logic": []
            },
            {
                "target": "D04Z02S01[E]",
                "logic": []
            },
            {
                "target": "D04Z02S03[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "dash",
                            "canCrossGap1"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S02[S]"
        ]
    },
    {
        "name": "D04Z02S03[W]",
        "exits": [
            {
                "target": "D04Z02S01[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "dash",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "dash",
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RE402",
                "logic": [
                    {
                        "item_requirements": [
                            "dash",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "dash",
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RESCUED_CHERUB_30",
                "logic": [
                    {
                        "item_requirements": [
                            "dash",
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "dash",
                            "canCrossGap1"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "pillar"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D04Z02S01[W]",
                "logic": []
            },
            {
                "target": "D04Z02S01[E]",
                "logic": []
            },
            {
                "target": "D04Z02S04[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "openedMoMLadder"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D04Z02S04[SW]",
                "logic": []
            },
            {
                "target": "D04Z02S04[W]",
                "logic": []
            },
            {
                "target": "D04Z02S05[W]",
                "logic": []
            },
            {
                "target": "D04Z02S19[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S03[W]",
            "D04Z02S01[NE]",
            "D04Z02S04[NW]",
            "D04Z02S03[E]",
            "D04Z02S19[W]",
            "D04Z02S04[NE]"
        ]
    },
    {
        "name": "D04Z03S01[W]",
        "exits": [
            {
                "target": "D04Z02S01[W]",
                "logic": []
            },
            {
                "target": "D04Z02S01[E]",
                "logic": []
            },
            {
                "target": "RESCUED_CHERUB_30",
                "logic": [
                    {
                        "item_requirements": [
                            "pillar"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z03S01[W]"
        ]
    },
    {
        "name": "D04Z01S06",
        "exits": [
            {
                "target": "D04Z01S06[S]",
                "logic": []
            },
            {
                "target": "D04Z01S06[Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S09[SW]",
                "logic": [
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "QI102"
        ],
        "transitions": []
    },
    {
        "name": "D04Z01S05[N]",
        "exits": [
            {
                "target": "D04Z01S06",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z01S05[N]"
        ]
    },
    {
        "name": "D09Z01S09[SW]",
        "exits": [
            {
                "target": "D04Z01S06",
                "logic": []
            },
            {
                "target": "D09Z01S09[Cell20]",
                "logic": [
                    {
                        "item_requirements": [
                            "silverKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S09[Cell21]",
                "logic": [
                    {
                        "item_requirements": [
                            "goldKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S08[Cell15]",
                "logic": [
                    {
                        "item_requirements": [
                            "silverKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S08[Cell16]",
                "logic": [
                    {
                        "item_requirements": [
                            "goldKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S08[Cell18]",
                "logic": [
                    {
                        "item_requirements": [
                            "silverKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S10[Cell12]",
                "logic": [
                    {
                        "item_requirements": [
                            "bronzeKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S10[Cell10]",
                "logic": [
                    {
                        "item_requirements": [
                            "silverKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S10[Cell11]",
                "logic": [
                    {
                        "item_requirements": [
                            "silverKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "CO27",
                "logic": []
            },
            {
                "target": "D09BZ01S01[Cell3]",
                "logic": []
            },
            {
                "target": "D09Z01S09[NW]",
                "logic": [
                    {
                        "item_requirements": [
                            "doubleJump",
                            "NormalLogic",
                            "dash",
                            "canAirStall"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "NormalLogic",
                            "dash",
                            "canDawnJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RB16",
                "logic": [
                    {
                        "item_requirements": [
                            "dash",
                            "doubleJump",
                            "canAirStall"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "dash",
                            "doubleJump",
                            "canDawnJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09BZ01S01[Cell19]",
                "logic": [
                    {
                        "item_requirements": [
                            "doubleJump",
                            "NormalLogic",
                            "dash",
                            "canAirStall"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "NormalLogic",
                            "dash",
                            "canDawnJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09BZ01S01[Cell24]",
                "logic": [
                    {
                        "item_requirements": [
                            "doubleJump",
                            "NormalLogic",
                            "dash",
                            "canAirStall"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "NormalLogic",
                            "dash",
                            "canDawnJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S02[N]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D09Z01S09[SW]",
            "D04Z01S06[E]",
            "D09Z01S07[SW]",
            "D09Z01S09[E]",
            "D09Z01S02[SW]",
            "D09Z01S07[E]",
            "D09Z01S08[SE]",
            "D09Z01S07[W]",
            "D09Z01S10[W]",
            "D09Z01S07[SE]",
            "D09Z01S02[Cell2]",
            "D09BZ01S01[Cell2]"
        ]
    },
    {
        "name": "D09Z01S12[E]",
        "exits": [
            {
                "target": "D09Z01S09[NW]",
                "logic": []
            },
            {
                "target": "RB16",
                "logic": [
                    {
                        "item_requirements": [
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09BZ01S01[Cell19]",
                "logic": []
            },
            {
                "target": "D09BZ01S01[Cell24]",
                "logic": [
                    {
                        "item_requirements": [
                            "D09BZ01S01[Cell24]"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S09[SW]",
                "logic": [
                    {
                        "item_requirements": [
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S09[Cell20]",
                "logic": [
                    {
                        "item_requirements": [
                            "silverKey",
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S09[Cell21]",
                "logic": [
                    {
                        "item_requirements": [
                            "goldKey",
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D09Z01S12[E]"
        ]
    },
    {
        "name": "D09BZ01S01[Cell19]",
        "exits": [
            {
                "target": "D09Z01S09[NW]",
                "logic": []
            },
            {
                "target": "RB16",
                "logic": [
                    {
                        "item_requirements": [
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09BZ01S01[Cell20]",
                "logic": []
            },
            {
                "target": "D09BZ01S01[Cell24]",
                "logic": [
                    {
                        "item_requirements": [
                            "D09BZ01S01[Cell24]"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S09[SW]",
                "logic": [
                    {
                        "item_requirements": [
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S09[Cell20]",
                "logic": [
                    {
                        "item_requirements": [
                            "silverKey",
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S09[Cell21]",
                "logic": [
                    {
                        "item_requirements": [
                            "goldKey",
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D09BZ01S01[Cell19]",
            "D09Z01S09[Cell19]"
        ]
    },
    {
        "name": "D09BZ01S01[Cell20]",
        "exits": [
            {
                "target": "D09Z01S09[SW]",
                "logic": []
            },
            {
                "target": "D09Z01S09[Cell20]",
                "logic": [
                    {
                        "item_requirements": [
                            "silverKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S09[Cell21]",
                "logic": [
                    {
                        "item_requirements": [
                            "goldKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S09[NW]",
                "logic": [
                    {
                        "item_requirements": [
                            "doubleJump",
                            "NormalLogic",
                            "dash",
                            "canAirStall"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "NormalLogic",
                            "dash",
                            "canDawnJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RB16",
                "logic": [
                    {
                        "item_requirements": [
                            "dash",
                            "doubleJump",
                            "canAirStall"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "dash",
                            "doubleJump",
                            "canDawnJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09BZ01S01[Cell19]",
                "logic": [
                    {
                        "item_requirements": [
                            "doubleJump",
                            "NormalLogic",
                            "dash",
                            "canAirStall"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "NormalLogic",
                            "dash",
                            "canDawnJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09BZ01S01[Cell24]",
                "logic": [
                    {
                        "item_requirements": [
                            "doubleJump",
                            "NormalLogic",
                            "dash",
                            "canAirStall"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "NormalLogic",
                            "dash",
                            "canDawnJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D09BZ01S01[Cell20]"
        ]
    },
    {
        "name": "D09BZ01S01[Cell21]",
        "exits": [
            {
                "target": "D09Z01S09[SW]",
                "logic": []
            },
            {
                "target": "D09Z01S09[Cell20]",
                "logic": [
                    {
                        "item_requirements": [
                            "silverKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S09[Cell21]",
                "logic": [
                    {
                        "item_requirements": [
                            "goldKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S09[NW]",
                "logic": [
                    {
                        "item_requirements": [
                            "doubleJump",
                            "NormalLogic",
                            "dash",
                            "canAirStall"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "NormalLogic",
                            "dash",
                            "canDawnJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RB16",
                "logic": [
                    {
                        "item_requirements": [
                            "dash",
                            "doubleJump",
                            "canAirStall"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "dash",
                            "doubleJump",
                            "canDawnJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09BZ01S01[Cell19]",
                "logic": [
                    {
                        "item_requirements": [
                            "doubleJump",
                            "NormalLogic",
                            "dash",
                            "canAirStall"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "NormalLogic",
                            "dash",
                            "canDawnJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09BZ01S01[Cell24]",
                "logic": [
                    {
                        "item_requirements": [
                            "doubleJump",
                            "NormalLogic",
                            "dash",
                            "canAirStall"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "NormalLogic",
                            "dash",
                            "canDawnJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D09BZ01S01[Cell21]"
        ]
    },
    {
        "name": "D09BZ01S01[Cell24]",
        "exits": [
            {
                "target": "D09Z01S09[NW]",
                "logic": [
                    {
                        "item_requirements": [
                            "D09Z01S12[E]"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "D09BZ01S01[Cell19]"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RB16",
                "logic": []
            },
            {
                "target": "D09BZ01S01[Cell19]",
                "logic": [
                    {
                        "item_requirements": [
                            "D09Z01S12[E]"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "D09BZ01S01[Cell19]"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S09[SW]",
                "logic": [
                    {
                        "item_requirements": [
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S09[Cell20]",
                "logic": [
                    {
                        "item_requirements": [
                            "silverKey",
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S09[Cell21]",
                "logic": [
                    {
                        "item_requirements": [
                            "goldKey",
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D09BZ01S01[Cell24]",
            "D09Z01S09[Cell24]"
        ]
    },
    {
        "name": "D04Z02S02",
        "exits": [
            {
                "target": "D04Z02S02[S]",
                "logic": []
            },
            {
                "target": "D04Z02S02[SE]",
                "logic": []
            },
            {
                "target": "D04Z02S02[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "doubleJump",
                            "HardLogic",
                            "EnemySkips",
                            "upwarpSkipsAllowed"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "HardLogic",
                            "EnemySkips",
                            "canEnemyUpslash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S02[S]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "CO17"
        ],
        "transitions": []
    },
    {
        "name": "D04Z02S01[N]",
        "exits": [
            {
                "target": "D04Z02S02",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S01[N]"
        ]
    },
    {
        "name": "D04Z02S15[W]",
        "exits": [
            {
                "target": "D04Z02S02",
                "logic": []
            },
            {
                "target": "D04Z02S02[NE]",
                "logic": []
            },
            {
                "target": "D06Z01S02[S]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S15[W]"
        ]
    },
    {
        "name": "D04Z02S17[W]",
        "exits": [
            {
                "target": "D04Z02S02",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S17[W]"
        ]
    },
    {
        "name": "D06Z01S02[S]",
        "exits": [
            {
                "target": "D04Z02S02",
                "logic": []
            },
            {
                "target": "D04Z02S02[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "doubleJump",
                            "HardLogic",
                            "EnemySkips",
                            "canEnemyUpslash",
                            "upwarpSkipsAllowed"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S18[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S01[SW]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D06Z01S02[S]",
            "D04Z02S02[N]",
            "D06Z01S18[E]",
            "D06Z01S02[W]",
            "D06Z01S08[W]",
            "D06Z01S02[E]"
        ]
    },
    {
        "name": "D04Z03S01",
        "exits": [
            {
                "target": "D04Z03S01[W]",
                "logic": []
            },
            {
                "target": "D04Z03S01[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": []
    },
    {
        "name": "D04Z02S01[E]",
        "exits": [
            {
                "target": "D04Z03S01",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S01[E]"
        ]
    },
    {
        "name": "D04Z02S04[W]",
        "exits": [
            {
                "target": "D04Z03S01",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S04[W]"
        ]
    },
    {
        "name": "D04Z02S02[SE]",
        "exits": [
            {
                "target": "D04Z02S17[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S02[SE]"
        ]
    },
    {
        "name": "D04Z02S15",
        "exits": [
            {
                "target": "D04Z02S15[W]",
                "logic": []
            },
            {
                "target": "D04Z02S15[E]",
                "logic": []
            }
        ],
        "locations": [
            "QI60"
        ],
        "transitions": []
    },
    {
        "name": "D04Z02S02[NE]",
        "exits": [
            {
                "target": "D04Z02S15",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S02[NE]"
        ]
    },
    {
        "name": "D04Z02S22[W]",
        "exits": [
            {
                "target": "D04Z02S15",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S22[W]"
        ]
    },
    {
        "name": "D04Z02S05[W]",
        "exits": [
            {
                "target": "D04Z02S04[SW]",
                "logic": []
            },
            {
                "target": "D04Z02S04[W]",
                "logic": []
            },
            {
                "target": "D04Z02S04[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb",
                            "doubleJump",
                            "openedMoMLadder"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D04Z02S03[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D04Z02S05[E]",
                "logic": []
            },
            {
                "target": "D05Z01S03[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S05[W]",
            "D04Z02S04[E]",
            "D05Z01S01[NW]",
            "D04Z02S04[SE]",
            "D05Z01S02[E]",
            "D05Z01S01[W]",
            "D05Z01S16[W]",
            "D05Z01S01[E]",
            "D05Z01S03[E]",
            "D05Z01S02[NW]"
        ]
    },
    {
        "name": "D04Z02S06[S]",
        "exits": [
            {
                "target": "D04Z02S04[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "openedMoMLadder"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D04Z02S03[W]",
                "logic": []
            },
            {
                "target": "D04Z02S04[SW]",
                "logic": []
            },
            {
                "target": "D04Z02S04[W]",
                "logic": []
            },
            {
                "target": "D04Z02S05[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S06[S]"
        ]
    },
    {
        "name": "D04Z02S06[-Cherubs]",
        "exits": [
            {
                "target": "D04Z02S04[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "openedMoMLadder"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D04Z02S03[W]",
                "logic": []
            },
            {
                "target": "D04Z02S04[SW]",
                "logic": []
            },
            {
                "target": "D04Z02S04[W]",
                "logic": []
            },
            {
                "target": "D04Z02S05[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S06[-Cherubs]"
        ]
    },
    {
        "name": "D04Z02S14[E]",
        "exits": [
            {
                "target": "D04Z02S04[SW]",
                "logic": []
            },
            {
                "target": "D04Z02S04[W]",
                "logic": []
            },
            {
                "target": "D04Z02S04[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb",
                            "doubleJump",
                            "openedMoMLadder"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D04Z02S03[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D04Z02S05[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S14[E]"
        ]
    },
    {
        "name": "D04Z03S01[E]",
        "exits": [
            {
                "target": "D04Z02S04[SW]",
                "logic": []
            },
            {
                "target": "D04Z02S04[W]",
                "logic": []
            },
            {
                "target": "D04Z02S04[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb",
                            "doubleJump",
                            "openedMoMLadder"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D04Z02S03[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D04Z02S05[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z03S01[E]"
        ]
    },
    {
        "name": "D04Z02S14",
        "exits": [
            {
                "target": "D04Z02S14[E]",
                "logic": []
            }
        ],
        "locations": [
            "Oil[D04Z02S14]"
        ],
        "transitions": []
    },
    {
        "name": "D04Z02S04[SW]",
        "exits": [
            {
                "target": "D04Z02S14",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S04[SW]"
        ]
    },
    {
        "name": "D04Z02S07[SW]",
        "exits": [
            {
                "target": "D04Z02S05[W]",
                "logic": []
            },
            {
                "target": "D04Z02S05[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S07[SW]"
        ]
    },
    {
        "name": "D04Z02S07[W]",
        "exits": [
            {
                "target": "D04Z02S19[E]",
                "logic": []
            },
            {
                "target": "D04Z02S03[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S07[W]"
        ]
    },
    {
        "name": "D04Z02S04[N]",
        "exits": [
            {
                "target": "D04Z02S06[S]",
                "logic": []
            },
            {
                "target": "D04Z02S06[NW]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D04Z02S06[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb",
                            "openedARLadder"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D04Z02S06[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "CO34",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D04Z02S09[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D04Z02S10[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S04[N]"
        ]
    },
    {
        "name": "D04Z02S09[W]",
        "exits": [
            {
                "target": "D04Z02S06[NW]",
                "logic": []
            },
            {
                "target": "D04Z02S06[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "openedARLadder"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "CO34",
                "logic": []
            },
            {
                "target": "D04Z02S06[S]",
                "logic": []
            },
            {
                "target": "D04Z02S06[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D04Z02S09[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D04Z02S10[W]",
                "logic": []
            },
            {
                "target": "D04Z02S08[S]",
                "logic": []
            },
            {
                "target": "D04Z02S20[Redento]",
                "logic": [
                    {
                        "item_requirements": [
                            "redentoRooms5"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S09[W]",
            "D04Z02S06[NE]",
            "D04Z02S08[W]",
            "D04Z02S09[E]",
            "D04Z02S20[W]",
            "D04Z02S08[E]"
        ]
    },
    {
        "name": "D04Z02S10[W]",
        "exits": [
            {
                "target": "D04Z02S06[S]",
                "logic": []
            },
            {
                "target": "D04Z02S06[NW]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D04Z02S06[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb",
                            "openedARLadder"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D04Z02S06[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "CO34",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D04Z02S09[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "QI01",
            "PR11"
        ],
        "transitions": [
            "D04Z02S10[W]",
            "D04Z02S06[E]"
        ]
    },
    {
        "name": "D04Z02S11[E]",
        "exits": [
            {
                "target": "D04Z02S06[NW]",
                "logic": []
            },
            {
                "target": "D04Z02S06[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "openedARLadder"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "CO34",
                "logic": []
            },
            {
                "target": "D04Z02S06[S]",
                "logic": []
            },
            {
                "target": "D04Z02S06[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D04Z02S09[W]",
                "logic": []
            },
            {
                "target": "D04Z02S10[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S11[E]"
        ]
    },
    {
        "name": "D06Z01S23[S]",
        "exits": [
            {
                "target": "D04Z02S06[NW]",
                "logic": []
            },
            {
                "target": "D04Z02S06[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "openedARLadder"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "CO34",
                "logic": []
            },
            {
                "target": "D04Z02S06[S]",
                "logic": []
            },
            {
                "target": "D04Z02S06[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D04Z02S09[W]",
                "logic": []
            },
            {
                "target": "D04Z02S10[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D06Z01S23[S]"
        ]
    },
    {
        "name": "D04Z02S07",
        "exits": [
            {
                "target": "D04Z02S07[SW]",
                "logic": []
            },
            {
                "target": "D04Z02S07[W]",
                "logic": []
            },
            {
                "target": "D04Z02S07[N]",
                "logic": []
            },
            {
                "target": "D04Z02S07[NE]",
                "logic": []
            },
            {
                "target": "D04Z02S07[SE]",
                "logic": []
            }
        ],
        "locations": [
            "CO35",
            "RB33"
        ],
        "transitions": []
    },
    {
        "name": "D04Z02S05[E]",
        "exits": [
            {
                "target": "D04Z02S07",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S05[E]"
        ]
    },
    {
        "name": "D04Z02S08[S]",
        "exits": [
            {
                "target": "D04Z02S07",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S08[S]"
        ]
    },
    {
        "name": "D04Z02S13[W]",
        "exits": [
            {
                "target": "D04Z02S07",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S13[W]"
        ]
    },
    {
        "name": "D04Z02S19[E]",
        "exits": [
            {
                "target": "D04Z02S07",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S19[E]"
        ]
    },
    {
        "name": "D04Z02S23[W]",
        "exits": [
            {
                "target": "D04Z02S07",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S23[W]"
        ]
    },
    {
        "name": "D04Z02S11",
        "exits": [
            {
                "target": "D04Z02S11[W]",
                "logic": []
            },
            {
                "target": "D04Z02S11[E]",
                "logic": []
            }
        ],
        "locations": [
            "CO20",
            "RESCUED_CHERUB_29"
        ],
        "transitions": []
    },
    {
        "name": "D04Z02S06[NW]",
        "exits": [
            {
                "target": "D04Z02S11",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S06[NW]"
        ]
    },
    {
        "name": "D04Z02S21[SE]",
        "exits": [
            {
                "target": "D04Z02S11",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S21[SE]"
        ]
    },
    {
        "name": "D04Z02S06[N]",
        "exits": [
            {
                "target": "D06Z01S23[Sword]",
                "logic": []
            },
            {
                "target": "D06Z01S23[S]",
                "logic": []
            },
            {
                "target": "D06Z01S20[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S06[N]"
        ]
    },
    {
        "name": "D06Z01S01[-Cherubs]",
        "exits": [
            {
                "target": "D06Z01S23[Sword]",
                "logic": []
            },
            {
                "target": "D06Z01S23[S]",
                "logic": []
            },
            {
                "target": "D06Z01S20[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D06Z01S01[-Cherubs]"
        ]
    },
    {
        "name": "D06Z01S20[W]",
        "exits": [
            {
                "target": "D06Z01S23[Sword]",
                "logic": []
            },
            {
                "target": "D06Z01S23[S]",
                "logic": []
            },
            {
                "target": "D06Z01S04[Health]",
                "logic": [
                    {
                        "item_requirements": [
                            "D06Z01S24[W]"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "canSurvivePoison2",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "canSurvivePoison2",
                            "blood",
                            "canClimbOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S03",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D06Z01S20[W]",
            "D06Z01S23[E]",
            "D06Z01S20[E]",
            "D06Z01S04[SW]",
            "D06Z01S04[W]",
            "D06Z01S03[E]"
        ]
    },
    {
        "name": "D06Z01S22[Sword]",
        "exits": [
            {
                "target": "D06Z01S23[Sword]",
                "logic": []
            },
            {
                "target": "D06Z01S23[S]",
                "logic": []
            },
            {
                "target": "D06Z01S20[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D06Z01S22[Sword]"
        ]
    },
    {
        "name": "D04Z02S16[W]",
        "exits": [
            {
                "target": "D04Z02S09[NE]",
                "logic": []
            },
            {
                "target": "D04Z02S09[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S16[W]"
        ]
    },
    {
        "name": "D04Z02S07[N]",
        "exits": [
            {
                "target": "D04Z02S08[S]",
                "logic": []
            },
            {
                "target": "D04Z02S09[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S07[N]"
        ]
    },
    {
        "name": "D04Z02S16[-Cherubs]",
        "exits": [
            {
                "target": "D04Z02S08[S]",
                "logic": []
            },
            {
                "target": "D04Z02S09[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S16[-Cherubs]"
        ]
    },
    {
        "name": "D04Z02S07[NE]",
        "exits": [
            {
                "target": "D04Z02S13[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S07[NE]"
        ]
    },
    {
        "name": "D04Z02S07[SE]",
        "exits": [
            {
                "target": "D04Z02S23[W]",
                "logic": []
            },
            {
                "target": "D04Z02S23[NE]",
                "logic": []
            },
            {
                "target": "D04Z02S24[NW]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S07[SE]"
        ]
    },
    {
        "name": "D04Z02S24[NW]",
        "exits": [
            {
                "target": "D04Z02S23[W]",
                "logic": []
            },
            {
                "target": "D04Z02S23[NE]",
                "logic": []
            },
            {
                "target": "D20Z02S03[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "canWalkOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canCrossGap5"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D20Z02S05[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S24[NW]",
            "D04Z02S23[SE]",
            "D20Z02S01[E]",
            "D04Z02S24[SW]",
            "D04Z02S25[W]",
            "D04Z02S24[SE]",
            "D20Z02S03[SE]",
            "D20Z02S01[W]",
            "D20Z02S04[E]",
            "D20Z02S03[W]"
        ]
    },
    {
        "name": "D04Z04S01[W]",
        "exits": [
            {
                "target": "D04Z02S23[W]",
                "logic": []
            },
            {
                "target": "D04Z02S23[NE]",
                "logic": []
            },
            {
                "target": "D04Z02S24[NW]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z04S01[W]"
        ]
    },
    {
        "name": "D04BZ02S01[Redento]",
        "exits": [
            {
                "target": "D04Z02S20[Redento]",
                "logic": [
                    {
                        "item_requirements": [
                            "redentoRooms5"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D04Z02S09[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04BZ02S01[Redento]"
        ]
    },
    {
        "name": "D04Z02S16",
        "exits": [
            {
                "target": "D04Z02S16[W]",
                "logic": []
            },
            {
                "target": "D04Z02S16[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "HE01"
        ],
        "transitions": []
    },
    {
        "name": "D04Z02S09[NE]",
        "exits": [
            {
                "target": "D04Z02S16",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S09[NE]"
        ]
    },
    {
        "name": "D04Z02S11[W]",
        "exits": [
            {
                "target": "D04Z02S21[SE]",
                "logic": []
            },
            {
                "target": "D04Z02S21[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D04Z02S22[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S11[W]"
        ]
    },
    {
        "name": "D04Z02S12[W]",
        "exits": [
            {
                "target": "D04Z02S21[NE]",
                "logic": []
            },
            {
                "target": "D04Z02S22[E]",
                "logic": []
            },
            {
                "target": "D04Z02S21[SE]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S12[W]"
        ]
    },
    {
        "name": "D04Z02S22[E]",
        "exits": [
            {
                "target": "D04Z02S22",
                "logic": []
            },
            {
                "target": "D04Z02S21[SE]",
                "logic": []
            },
            {
                "target": "D04Z02S21[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S22[E]",
            "D04Z02S21[W]"
        ]
    },
    {
        "name": "D04Z02S22",
        "exits": [
            {
                "target": "D04Z02S22[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "canBeatMothersBoss"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D04Z02S22[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "canBeatMothersBoss"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "BS05"
        ],
        "transitions": []
    },
    {
        "name": "D04Z02S15[E]",
        "exits": [
            {
                "target": "D04Z02S22",
                "logic": []
            },
            {
                "target": "D04Z02S22[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S15[E]"
        ]
    },
    {
        "name": "D04BZ02S01",
        "exits": [
            {
                "target": "D04BZ02S01[Redento]",
                "logic": []
            }
        ],
        "locations": [
            "RE03",
            "QI54"
        ],
        "transitions": []
    },
    {
        "name": "D04Z02S20[Redento]",
        "exits": [
            {
                "target": "D04BZ02S01",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S20[Redento]"
        ]
    },
    {
        "name": "D04Z02S12",
        "exits": [
            {
                "target": "D04Z02S12[W]",
                "logic": []
            }
        ],
        "locations": [
            "Sword[D04Z02S12]"
        ],
        "transitions": []
    },
    {
        "name": "D04Z02S21[NE]",
        "exits": [
            {
                "target": "D04Z02S12",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S21[NE]"
        ]
    },
    {
        "name": "D04Z04S01",
        "exits": [
            {
                "target": "D04Z04S01[W]",
                "logic": []
            },
            {
                "target": "D04Z04S01[E]",
                "logic": []
            }
        ],
        "locations": [
            "PR201"
        ],
        "transitions": []
    },
    {
        "name": "D04Z02S23[NE]",
        "exits": [
            {
                "target": "D04Z04S01",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z02S23[NE]"
        ]
    },
    {
        "name": "D04Z04S02[W]",
        "exits": [
            {
                "target": "D04Z04S01",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z04S02[W]"
        ]
    },
    {
        "name": "D04Z03S02[W]",
        "exits": [
            {
                "target": "D05Z01S22[FrontalN]",
                "logic": []
            },
            {
                "target": "D05Z01S22[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z03S02[W]"
        ]
    },
    {
        "name": "D05BZ01S01[FrontalN]",
        "exits": [
            {
                "target": "D05Z01S22[FrontalN]",
                "logic": []
            },
            {
                "target": "D05Z01S22[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05BZ01S01[FrontalN]"
        ]
    },
    {
        "name": "D04Z04S01[E]",
        "exits": [
            {
                "target": "D04Z04S02[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D04Z04S01[E]"
        ]
    },
    {
        "name": "D05Z01S15[E]",
        "exits": [
            {
                "target": "D05Z01S02[W]",
                "logic": []
            },
            {
                "target": "RB18",
                "logic": [
                    {
                        "item_requirements": [
                            "redWax1"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D04Z02S05[W]",
                "logic": []
            }
        ],
        "locations": [
            "RB19"
        ],
        "transitions": [
            "D05Z01S15[E]"
        ]
    },
    {
        "name": "D05Z01S15",
        "exits": [
            {
                "target": "D05Z01S15[W]",
                "logic": []
            },
            {
                "target": "D05Z01S15[E]",
                "logic": []
            }
        ],
        "locations": [
            "QI62"
        ],
        "transitions": []
    },
    {
        "name": "D05Z01S02[W]",
        "exits": [
            {
                "target": "D05Z01S15",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z01S02[W]"
        ]
    },
    {
        "name": "D05Z01S21[NE]",
        "exits": [
            {
                "target": "D05Z01S15",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z01S21[NE]"
        ]
    },
    {
        "name": "D05Z01S04[E]",
        "exits": [
            {
                "target": "D05Z01S03[W]",
                "logic": []
            },
            {
                "target": "D04Z02S05[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z01S04[E]"
        ]
    },
    {
        "name": "D05BZ01S01[FrontalS]",
        "exits": [
            {
                "target": "D05Z01S03[W]",
                "logic": []
            },
            {
                "target": "D04Z02S05[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05BZ01S01[FrontalS]"
        ]
    },
    {
        "name": "D05Z01S04",
        "exits": [
            {
                "target": "D05Z01S04[W]",
                "logic": []
            },
            {
                "target": "D05Z01S04[E]",
                "logic": []
            }
        ],
        "locations": [
            "CO18",
            "RESCUED_CHERUB_01"
        ],
        "transitions": []
    },
    {
        "name": "D05Z01S03[W]",
        "exits": [
            {
                "target": "D05Z01S04",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z01S03[W]"
        ]
    },
    {
        "name": "D05Z01S05[E]",
        "exits": [
            {
                "target": "D05Z01S04",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z01S05[E]"
        ]
    },
    {
        "name": "D05BZ01S01",
        "exits": [
            {
                "target": "D05BZ01S01[FrontalS]",
                "logic": []
            },
            {
                "target": "D05BZ01S01[FrontalN]",
                "logic": []
            }
        ],
        "locations": [
            "RB301"
        ],
        "transitions": []
    },
    {
        "name": "D05Z01S03[Frontal]",
        "exits": [
            {
                "target": "D05BZ01S01",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z01S03[Frontal]"
        ]
    },
    {
        "name": "D05Z01S22[FrontalN]",
        "exits": [
            {
                "target": "D05BZ01S01",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z01S22[FrontalN]"
        ]
    },
    {
        "name": "D05Z01S05",
        "exits": [
            {
                "target": "D05Z01S05[SW]",
                "logic": []
            },
            {
                "target": "D05Z01S05[E]",
                "logic": []
            },
            {
                "target": "CO22",
                "logic": [
                    {
                        "item_requirements": [
                            "canClimbOnRoot",
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump",
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D05Z01S17[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "QI50"
        ],
        "transitions": []
    },
    {
        "name": "D05Z01S04[W]",
        "exits": [
            {
                "target": "D05Z01S05",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z01S04[W]"
        ]
    },
    {
        "name": "D05Z01S07[E]",
        "exits": [
            {
                "target": "D05Z01S05",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z01S07[E]"
        ]
    },
    {
        "name": "D05Z01S17[W]",
        "exits": [
            {
                "target": "D05Z01S05",
                "logic": []
            },
            {
                "target": "CO22",
                "logic": [
                    {
                        "item_requirements": [
                            "canClimbOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z01S17[W]",
            "D05Z01S05[NE]"
        ]
    },
    {
        "name": "D05Z01S05[SW]",
        "exits": [
            {
                "target": "D05Z01S07[E]",
                "logic": []
            },
            {
                "target": "D05Z01S20[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "blood",
                            "canClimbOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "blood",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canClimbOnRoot",
                            "canCrossGap3"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canCrossGap7"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D05Z01S08[NE]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z01S05[SW]"
        ]
    },
    {
        "name": "D05Z01S08[NE]",
        "exits": [
            {
                "target": "D05Z01S07[E]",
                "logic": []
            },
            {
                "target": "D05Z01S20[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "blood",
                            "canClimbOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "blood",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canClimbOnRoot",
                            "canCrossGap3"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canCrossGap7"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D05Z01S08[W]",
                "logic": []
            },
            {
                "target": "D05Z01S08[Health]",
                "logic": []
            },
            {
                "target": "D05Z01S09[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z01S08[NE]",
            "D05Z01S07[SW]",
            "D05Z01S12[E]",
            "D05Z01S08[NW]",
            "D05Z01S09[W]",
            "D05Z01S08[E]"
        ]
    },
    {
        "name": "D05Z01S06[W]",
        "exits": [
            {
                "target": "RB31",
                "logic": []
            },
            {
                "target": "D05Z01S20[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "canSurvivePoison3"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z01S06[W]",
            "D05Z01S24[E]"
        ]
    },
    {
        "name": "D05Z01S10[E]",
        "exits": [
            {
                "target": "D05Z01S08[W]",
                "logic": []
            },
            {
                "target": "D05Z01S08[Health]",
                "logic": []
            },
            {
                "target": "D05Z01S08[NE]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z01S10[E]"
        ]
    },
    {
        "name": "D05Z01S14[W]",
        "exits": [
            {
                "target": "D05Z01S08[W]",
                "logic": []
            },
            {
                "target": "D05Z01S08[Health]",
                "logic": []
            },
            {
                "target": "D05Z01S08[NE]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z01S14[W]"
        ]
    },
    {
        "name": "D05Z01S10",
        "exits": [
            {
                "target": "D05Z01S10[W]",
                "logic": []
            },
            {
                "target": "D05Z01S10[NW]",
                "logic": []
            },
            {
                "target": "D05Z01S10[E]",
                "logic": []
            }
        ],
        "locations": [
            "PR07"
        ],
        "transitions": []
    },
    {
        "name": "D05Z01S08[W]",
        "exits": [
            {
                "target": "D05Z01S10",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z01S08[W]"
        ]
    },
    {
        "name": "D05Z01S11[NE]",
        "exits": [
            {
                "target": "D05Z01S10",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z01S11[NE]"
        ]
    },
    {
        "name": "D05Z01S11[E]",
        "exits": [
            {
                "target": "D05Z01S10",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z01S11[E]"
        ]
    },
    {
        "name": "D05Z01S18[W]",
        "exits": [
            {
                "target": "D05Z01S09[E]",
                "logic": []
            },
            {
                "target": "D05Z01S08[NE]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z01S18[W]"
        ]
    },
    {
        "name": "D05Z01S14",
        "exits": [
            {
                "target": "D05Z01S14[W]",
                "logic": []
            }
        ],
        "locations": [
            "Lady[D05Z01S14]"
        ],
        "transitions": []
    },
    {
        "name": "D05Z01S08[Health]",
        "exits": [
            {
                "target": "D05Z01S14",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z01S08[Health]"
        ]
    },
    {
        "name": "D05Z01S18",
        "exits": [
            {
                "target": "D05Z01S18[W]",
                "logic": []
            }
        ],
        "locations": [
            "PR15"
        ],
        "transitions": []
    },
    {
        "name": "D05Z01S09[E]",
        "exits": [
            {
                "target": "D05Z01S18",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z01S09[E]"
        ]
    },
    {
        "name": "D05Z01S11",
        "exits": [
            {
                "target": "D05Z01S11[SW]",
                "logic": [
                    {
                        "item_requirements": [
                            "HardLogic",
                            "tirana",
                            "obscureSkipsAllowed"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D05Z01S11[SE]",
                "logic": []
            },
            {
                "target": "D05Z01S11[E]",
                "logic": []
            }
        ],
        "locations": [
            "RB30",
            "RESCUED_CHERUB_02"
        ],
        "transitions": []
    },
    {
        "name": "D05Z01S10[W]",
        "exits": [
            {
                "target": "D05Z01S11",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z01S10[W]"
        ]
    },
    {
        "name": "D05Z01S10[NW]",
        "exits": [
            {
                "target": "D05Z01S11",
                "logic": []
            },
            {
                "target": "D05Z01S11[NE]",
                "logic": []
            },
            {
                "target": "RB203",
                "logic": [
                    {
                        "item_requirements": [
                            "D05Z01S11[NW]"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "CO28",
                "logic": []
            },
            {
                "target": "D05Z01S23[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z01S10[NW]"
        ]
    },
    {
        "name": "D05Z01S19[E]",
        "exits": [
            {
                "target": "D05Z01S11",
                "logic": []
            },
            {
                "target": "D05Z01S11[SW]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z01S19[E]"
        ]
    },
    {
        "name": "D05Z01S23[E]",
        "exits": [
            {
                "target": "D05Z01S11",
                "logic": []
            },
            {
                "target": "D05Z01S11[NE]",
                "logic": []
            },
            {
                "target": "RB203",
                "logic": [
                    {
                        "item_requirements": [
                            "D05Z01S11[NW]"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "CO28",
                "logic": []
            },
            {
                "target": "D05Z01S03[Frontal]",
                "logic": [
                    {
                        "item_requirements": [
                            "woodKey",
                            "D05Z01S23[E]"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "woodKey",
                            "D05Z01S10[NW]"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z01S23[E]",
            "D05Z01S11[NW]"
        ]
    },
    {
        "name": "D05Z02S01[W]",
        "exits": [
            {
                "target": "D05Z01S11",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z02S01[W]"
        ]
    },
    {
        "name": "D05Z01S19",
        "exits": [
            {
                "target": "D05Z01S19[W]",
                "logic": []
            },
            {
                "target": "D05Z01S19[E]",
                "logic": []
            }
        ],
        "locations": [
            "Oil[D05Z01S19]"
        ],
        "transitions": []
    },
    {
        "name": "D05Z01S11[SW]",
        "exits": [
            {
                "target": "D05Z01S19",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z01S11[SW]"
        ]
    },
    {
        "name": "D05Z02S15[E]",
        "exits": [
            {
                "target": "D05Z01S19",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z02S15[E]"
        ]
    },
    {
        "name": "D05Z01S11[SE]",
        "exits": [
            {
                "target": "D05Z02S01[W]",
                "logic": []
            },
            {
                "target": "D05Z02S01[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z01S11[SE]"
        ]
    },
    {
        "name": "D05Z02S02[NW]",
        "exits": [
            {
                "target": "D05Z02S01[W]",
                "logic": []
            },
            {
                "target": "D05Z02S01[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z02S02[NW]"
        ]
    },
    {
        "name": "D05Z01S21",
        "exits": [
            {
                "target": "D05Z01S21[SW]",
                "logic": []
            },
            {
                "target": "D05Z01S21[NW]",
                "logic": []
            },
            {
                "target": "D05Z01S21[NE]",
                "logic": []
            },
            {
                "target": "D05Z01S21[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "RESCUED_CHERUB_32"
        ],
        "transitions": []
    },
    {
        "name": "D05Z01S13[E]",
        "exits": [
            {
                "target": "D05Z01S21",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z01S13[E]"
        ]
    },
    {
        "name": "D05Z01S15[W]",
        "exits": [
            {
                "target": "D05Z01S21",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z01S15[W]"
        ]
    },
    {
        "name": "D05Z02S14[E]",
        "exits": [
            {
                "target": "D05Z01S21",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z02S14[E]"
        ]
    },
    {
        "name": "D05Z02S15",
        "exits": [
            {
                "target": "D05Z02S15[S]",
                "logic": []
            },
            {
                "target": "D05Z02S15[E]",
                "logic": []
            }
        ],
        "locations": [
            "QI104"
        ],
        "transitions": []
    },
    {
        "name": "D05Z01S19[W]",
        "exits": [
            {
                "target": "D05Z02S15",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z01S19[W]"
        ]
    },
    {
        "name": "D05Z02S12[N]",
        "exits": [
            {
                "target": "D05Z02S15",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z02S12[N]"
        ]
    },
    {
        "name": "D05Z02S14",
        "exits": [
            {
                "target": "D05Z02S14[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "canBeatCanvasesBoss"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D05Z02S06[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "canBeatCanvasesBoss"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "BS06"
        ],
        "transitions": []
    },
    {
        "name": "D05Z01S21[SW]",
        "exits": [
            {
                "target": "D05Z02S14",
                "logic": []
            },
            {
                "target": "D05Z02S14[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z01S21[SW]"
        ]
    },
    {
        "name": "D05Z02S06[NE]",
        "exits": [
            {
                "target": "D05Z02S14",
                "logic": []
            },
            {
                "target": "D05Z02S06[SE]",
                "logic": [
                    {
                        "item_requirements": [
                            "openedTSCGate"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D05Z02S05[W]",
                "logic": []
            },
            {
                "target": "D05Z02S07[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z02S06[NE]",
            "D05Z02S14[W]",
            "D05Z02S06[SW]",
            "D05Z02S05[E]",
            "D05Z02S07[E]",
            "D05Z02S06[NW]"
        ]
    },
    {
        "name": "D05Z01S13",
        "exits": [
            {
                "target": "D05Z01S13[E]",
                "logic": []
            }
        ],
        "locations": [
            "Sword[D05Z01S13]"
        ],
        "transitions": []
    },
    {
        "name": "D05Z01S21[NW]",
        "exits": [
            {
                "target": "D05Z01S13",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z01S21[NW]"
        ]
    },
    {
        "name": "D05Z02S11",
        "exits": [
            {
                "target": "D05Z02S11[W]",
                "logic": []
            }
        ],
        "locations": [
            "CO31"
        ],
        "transitions": []
    },
    {
        "name": "D05Z01S21[-Cherubs]",
        "exits": [
            {
                "target": "D05Z02S11",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z01S21[-Cherubs]"
        ]
    },
    {
        "name": "D05Z02S06[SE]",
        "exits": [
            {
                "target": "D05Z02S11",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z02S06[SE]"
        ]
    },
    {
        "name": "D04Z03S02",
        "exits": [
            {
                "target": "D04Z03S02[W]",
                "logic": []
            }
        ],
        "locations": [
            "HE201"
        ],
        "transitions": []
    },
    {
        "name": "D05Z01S22[E]",
        "exits": [
            {
                "target": "D04Z03S02",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z01S22[E]"
        ]
    },
    {
        "name": "D05Z02S02",
        "exits": [
            {
                "target": "D05Z02S02[SW]",
                "logic": []
            },
            {
                "target": "D05Z02S02[NW]",
                "logic": []
            },
            {
                "target": "D05Z02S02[SE]",
                "logic": []
            },
            {
                "target": "D05Z02S02[NE]",
                "logic": []
            }
        ],
        "locations": [
            "QI64"
        ],
        "transitions": []
    },
    {
        "name": "D05Z02S01[E]",
        "exits": [
            {
                "target": "D05Z02S02",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z02S01[E]"
        ]
    },
    {
        "name": "D05Z02S03[E]",
        "exits": [
            {
                "target": "D05Z02S02",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z02S03[E]"
        ]
    },
    {
        "name": "D05Z02S05[W]",
        "exits": [
            {
                "target": "D05Z02S02",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z02S05[W]"
        ]
    },
    {
        "name": "D05Z02S09[W]",
        "exits": [
            {
                "target": "D05Z02S02",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z02S09[W]"
        ]
    },
    {
        "name": "D05Z02S02[SW]",
        "exits": [
            {
                "target": "D05Z02S03[E]",
                "logic": []
            },
            {
                "target": "D05Z02S04[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z02S02[SW]"
        ]
    },
    {
        "name": "D05Z02S02[SE]",
        "exits": [
            {
                "target": "D05Z02S09[W]",
                "logic": []
            },
            {
                "target": "D05Z02S09[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "redWax3",
                            "blueWax3"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z02S02[SE]"
        ]
    },
    {
        "name": "D05Z02S08[W]",
        "exits": [
            {
                "target": "D05Z02S09[W]",
                "logic": []
            },
            {
                "target": "D05Z02S09[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "redWax3",
                            "blueWax3"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z02S08[W]"
        ]
    },
    {
        "name": "D05Z02S02[NE]",
        "exits": [
            {
                "target": "D05Z02S05[W]",
                "logic": []
            },
            {
                "target": "D05Z02S06[NE]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z02S02[NE]"
        ]
    },
    {
        "name": "D05BZ02S01[C]",
        "exits": [
            {
                "target": "D05Z02S04[W]",
                "logic": []
            },
            {
                "target": "D05Z02S04[C]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05BZ02S01[C]"
        ]
    },
    {
        "name": "D05BZ02S01",
        "exits": [
            {
                "target": "D05BZ02S01[C]",
                "logic": []
            }
        ],
        "locations": [
            "RB12",
            "QI49",
            "QI71"
        ],
        "transitions": []
    },
    {
        "name": "D05Z02S04[C]",
        "exits": [
            {
                "target": "D05BZ02S01",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z02S04[C]"
        ]
    },
    {
        "name": "D05Z02S11[W]",
        "exits": [
            {
                "target": "D05Z02S06[SE]",
                "logic": [
                    {
                        "item_requirements": [
                            "openedTSCGate"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D05Z02S06[NE]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z02S11[W]"
        ]
    },
    {
        "name": "D05Z02S10[E]",
        "exits": [
            {
                "target": "D05Z02S07[W]",
                "logic": []
            },
            {
                "target": "D05Z02S06[NE]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z02S10[E]"
        ]
    },
    {
        "name": "D05Z02S10",
        "exits": [
            {
                "target": "D05Z02S10[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D05Z02S10[E]",
                "logic": []
            }
        ],
        "locations": [
            "RE05",
            "PR05"
        ],
        "transitions": []
    },
    {
        "name": "D05Z02S07[W]",
        "exits": [
            {
                "target": "D05Z02S10",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z02S07[W]"
        ]
    },
    {
        "name": "D05Z02S13[E]",
        "exits": [
            {
                "target": "D05Z02S10",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z02S13[E]"
        ]
    },
    {
        "name": "D05Z02S08",
        "exits": [
            {
                "target": "D05Z02S08[W]",
                "logic": []
            }
        ],
        "locations": [
            "HE07"
        ],
        "transitions": []
    },
    {
        "name": "D05Z02S09[E]",
        "exits": [
            {
                "target": "D05Z02S08",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z02S09[E]"
        ]
    },
    {
        "name": "D05Z02S10[W]",
        "exits": [
            {
                "target": "D05Z02S13[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D05Z02S10[W]"
        ]
    },
    {
        "name": "D06Z01S01[SW]",
        "exits": [
            {
                "target": "D06Z01S01[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "masks1"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S01[NNW]",
                "logic": [
                    {
                        "item_requirements": [
                            "masks2"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S01[NNE]",
                "logic": [
                    {
                        "item_requirements": [
                            "masks2"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S01[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "masks3"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S01[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S03",
                "logic": []
            },
            {
                "target": "D06Z01S02[S]",
                "logic": []
            },
            {
                "target": "CO06",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RESCUED_CHERUB_36",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "taranto"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D06Z01S01[SW]",
            "D06Z01S14[E]",
            "D06Z01S01[SE]",
            "D06Z01S03[W]",
            "D06Z01S08[E]",
            "D06Z01S14[W]",
            "D06Z01S12[S]",
            "D06Z01S14[N]"
        ]
    },
    {
        "name": "D06Z01S03",
        "exits": [
            {
                "target": "D06Z01S01[SW]",
                "logic": [
                    {
                        "item_requirements": [
                            "canBeatLegionary"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S20[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "canBeatLegionary"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "QI02"
        ],
        "transitions": []
    },
    {
        "name": "D06Z01S01[W]",
        "exits": [
            {
                "target": "D06Z01S01[SW]",
                "logic": []
            },
            {
                "target": "D06Z01S01[NNW]",
                "logic": [
                    {
                        "item_requirements": [
                            "masks2"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S01[NNE]",
                "logic": [
                    {
                        "item_requirements": [
                            "masks2"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S01[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "masks3"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S01[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "QI03",
                "logic": [
                    {
                        "item_requirements": [
                            "canBeatLegionary"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S04[NW]",
                "logic": [
                    {
                        "item_requirements": [
                            "D06Z01S04[NW]"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canBeatLegionary"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "CO06",
                "logic": []
            },
            {
                "target": "RESCUED_CHERUB_36",
                "logic": []
            },
            {
                "target": "D06Z01S13[W]",
                "logic": []
            },
            {
                "target": "D06Z01S02[S]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D06Z01S01[W]",
            "D06Z01S07[E]",
            "D06Z01S01[E]",
            "D06Z01S06[WW]",
            "D06Z01S12[E]",
            "D06Z01S07[W]",
            "D06Z01S13[E]",
            "D06Z01S12[W]",
            "D06Z01S13[S]",
            "D06Z01S08[N]"
        ]
    },
    {
        "name": "D06Z01S16[-CherubsL]",
        "exits": [
            {
                "target": "D06Z01S01[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D06Z01S16[-CherubsL]"
        ]
    },
    {
        "name": "D06Z01S16[-CherubsR]",
        "exits": [
            {
                "target": "D06Z01S01[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D06Z01S16[-CherubsR]"
        ]
    },
    {
        "name": "D06Z01S04[NW]",
        "exits": [
            {
                "target": "QI03",
                "logic": [
                    {
                        "item_requirements": [
                            "canBeatLegionary"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S04[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "D06Z01S06[W]"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "D06Z01S20[E]",
                            "wallClimb",
                            "canSurvivePoison2",
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "D06Z01S20[E]",
                            "wallClimb",
                            "canSurvivePoison2",
                            "doubleJump",
                            "canDawnJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "D06Z01S20[E]",
                            "wallClimb",
                            "canSurvivePoison2",
                            "doubleJump",
                            "canClimbOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "D06Z01S03[E]",
                            "wallClimb",
                            "canSurvivePoison2",
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "D06Z01S03[E]",
                            "wallClimb",
                            "canSurvivePoison2",
                            "doubleJump",
                            "canDawnJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "D06Z01S03[E]",
                            "wallClimb",
                            "canSurvivePoison2",
                            "doubleJump",
                            "canClimbOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "D06Z01S24[W]",
                            "wallClimb",
                            "canSurvivePoison2",
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "D06Z01S24[W]",
                            "wallClimb",
                            "canSurvivePoison2",
                            "doubleJump",
                            "canDawnJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "D06Z01S24[W]",
                            "wallClimb",
                            "canSurvivePoison2",
                            "doubleJump",
                            "canClimbOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S01[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "D06Z01S01[E]"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canBeatLegionary"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D06Z01S04[NW]",
            "D06Z01S06[E]"
        ]
    },
    {
        "name": "D06Z01S04[NE]",
        "exits": [
            {
                "target": "D06Z01S04[NW]",
                "logic": [
                    {
                        "item_requirements": [
                            "D06Z01S06[E]"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "D06Z01S17[-Cherubs]"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "D06Z01S20[E]",
                            "wallClimb",
                            "canSurvivePoison2",
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "D06Z01S20[E]",
                            "wallClimb",
                            "canSurvivePoison2",
                            "doubleJump",
                            "canDawnJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "D06Z01S20[E]",
                            "wallClimb",
                            "canSurvivePoison2",
                            "doubleJump",
                            "canClimbOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "D06Z01S03[E]",
                            "wallClimb",
                            "canSurvivePoison2",
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "D06Z01S03[E]",
                            "wallClimb",
                            "canSurvivePoison2",
                            "doubleJump",
                            "canDawnJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "D06Z01S03[E]",
                            "wallClimb",
                            "canSurvivePoison2",
                            "doubleJump",
                            "canClimbOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "D06Z01S24[W]",
                            "wallClimb",
                            "canSurvivePoison2",
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "D06Z01S24[W]",
                            "wallClimb",
                            "canSurvivePoison2",
                            "doubleJump",
                            "canDawnJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "D06Z01S24[W]",
                            "wallClimb",
                            "canSurvivePoison2",
                            "doubleJump",
                            "canClimbOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "CO40"
        ],
        "transitions": [
            "D06Z01S04[NE]",
            "D06Z01S06[W]",
            "D06Z01S15[SW]",
            "D06Z01S06[EE]"
        ]
    },
    {
        "name": "D06Z01S01[NW]",
        "exits": [
            {
                "target": "D06Z01S16[-CherubsL]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen",
                            "canWalkOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "linen",
                            "canCrossGap7"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S16[-CherubsR]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S01[SW]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S01[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S01[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "canWalkOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canCrossGap8"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S01[NNW]",
                "logic": [
                    {
                        "item_requirements": [
                            "masks2",
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S01[NNE]",
                "logic": [
                    {
                        "item_requirements": [
                            "masks2",
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S01[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "masks3",
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S01[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S12[NE2]",
                "logic": [
                    {
                        "item_requirements": [
                            "canWalkOnRoot",
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canWalkOnRoot",
                            "canCrossGap5"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canCrossGap7",
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canCrossGap7",
                            "canCrossGap5"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D06Z01S01[NW]",
            "D06Z01S16[E]"
        ]
    },
    {
        "name": "D06Z01S09[-CherubsL]",
        "exits": [
            {
                "target": "D06Z01S16[-CherubsL]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S16[-CherubsR]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen",
                            "canAirStall"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "linen",
                            "canWalkOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "linen",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S01[NW]",
                "logic": [
                    {
                        "item_requirements": [
                            "canWalkOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canCrossGap5"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S12[NE2]",
                "logic": [
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "canWalkOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb",
                            "canAirStall"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D06Z01S09[-CherubsL]"
        ]
    },
    {
        "name": "D06Z01S09[-CherubsR]",
        "exits": [
            {
                "target": "D06Z01S16[-CherubsL]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "linen",
                            "canAirStall",
                            "canWalkOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "linen",
                            "canAirStall",
                            "wheel"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S16[-CherubsR]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S01[NW]",
                "logic": [
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canAirStall",
                            "canWalkOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canAirStall",
                            "wheel"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S12[NE2]",
                "logic": [
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canAirStall",
                            "canWalkOnRoot",
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canAirStall",
                            "canWalkOnRoot",
                            "canDawnJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canAirStall",
                            "wheel",
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canAirStall",
                            "wheel",
                            "canDawnJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D06Z01S09[-CherubsR]"
        ]
    },
    {
        "name": "D06Z01S12[NE2]",
        "exits": [
            {
                "target": "D06Z01S16[-CherubsL]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S16[-CherubsR]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen",
                            "canWalkOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "linen",
                            "canCrossGap1"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S01[NW]",
                "logic": [
                    {
                        "item_requirements": [
                            "canWalkOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canCrossGap5"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S12[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "D06Z01S05[E]"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "D06Z01S09[W]"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "CO06",
                "logic": []
            },
            {
                "target": "PR12",
                "logic": []
            },
            {
                "target": "RESCUED_CHERUB_36",
                "logic": []
            },
            {
                "target": "D06Z01S01[W]",
                "logic": []
            },
            {
                "target": "D06Z01S01[SW]",
                "logic": []
            },
            {
                "target": "D06Z01S05[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "D06Z01S05[E]"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "D06Z01S09[W]"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D06Z01S12[NE2]",
            "D06Z01S16[W]"
        ]
    },
    {
        "name": "D06Z01S01[NE]",
        "exits": [
            {
                "target": "D06Z01S01[SW]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S01[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S01[NW]",
                "logic": [
                    {
                        "item_requirements": [
                            "canWalkOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canCrossGap8"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S01[NNW]",
                "logic": [
                    {
                        "item_requirements": [
                            "masks2",
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S01[NNE]",
                "logic": [
                    {
                        "item_requirements": [
                            "masks2",
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S01[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "masks3",
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S01[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S17[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S26[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D06Z01S01[NE]",
            "D06Z01S17[W]"
        ]
    },
    {
        "name": "D06Z01S10[-CherubsL]",
        "exits": [
            {
                "target": "D06Z01S01[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S17[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S26[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "blood",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D06Z01S10[-CherubsL]"
        ]
    },
    {
        "name": "D06Z01S10[-CherubsR]",
        "exits": [
            {
                "target": "D06Z01S01[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S17[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S26[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D06Z01S10[-CherubsR]"
        ]
    },
    {
        "name": "D06Z01S26[W]",
        "exits": [
            {
                "target": "D06Z01S01[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S17[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D06Z01S26[W]",
            "D06Z01S17[E]"
        ]
    },
    {
        "name": "D06Z01S09",
        "exits": [
            {
                "target": "D06Z01S09[W]",
                "logic": []
            },
            {
                "target": "D06Z01S09[E]",
                "logic": []
            },
            {
                "target": "D06Z01S09[-CherubsL]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S09[-CherubsR]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": []
    },
    {
        "name": "D06Z01S01[NNW]",
        "exits": [
            {
                "target": "D06Z01S09",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D06Z01S01[NNW]"
        ]
    },
    {
        "name": "D06Z01S12[NE]",
        "exits": [
            {
                "target": "D06Z01S09",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D06Z01S12[NE]"
        ]
    },
    {
        "name": "D06Z01S01[NNE]",
        "exits": [
            {
                "target": "D06Z01S10[-CherubsL]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S10[-CherubsR]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S01[SW]",
                "logic": []
            },
            {
                "target": "D06Z01S01[W]",
                "logic": []
            },
            {
                "target": "D06Z01S01[NW]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen",
                            "canWalkOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "linen",
                            "canCrossGap3"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S01[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S01[NNW]",
                "logic": []
            },
            {
                "target": "D06Z01S01[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "masks3"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S01[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S21",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D06Z01S01[NNE]",
            "D06Z01S10[W]",
            "D06Z01S21[W]",
            "D06Z01S10[E]"
        ]
    },
    {
        "name": "D06Z01S01[N]",
        "exits": [
            {
                "target": "D06Z01S19[S]",
                "logic": []
            },
            {
                "target": "D06Z01S25[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D06Z01S01[N]"
        ]
    },
    {
        "name": "D06Z01S25[W]",
        "exits": [
            {
                "target": "D06Z01S19[S]",
                "logic": []
            },
            {
                "target": "D06Z01S25",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D06Z01S25[W]",
            "D06Z01S19[E]"
        ]
    },
    {
        "name": "D06Z01S09[E]",
        "exits": [
            {
                "target": "D06Z01S01[SW]",
                "logic": []
            },
            {
                "target": "D06Z01S01[W]",
                "logic": []
            },
            {
                "target": "D06Z01S01[NW]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S01[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen",
                            "canWalkOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "linen",
                            "canCrossGap3"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S01[NNW]",
                "logic": []
            },
            {
                "target": "D06Z01S01[NNE]",
                "logic": []
            },
            {
                "target": "D06Z01S01[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "masks3"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S01[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D06Z01S09[E]"
        ]
    },
    {
        "name": "D06Z01S19[S]",
        "exits": [
            {
                "target": "D06Z01S01[SW]",
                "logic": []
            },
            {
                "target": "D06Z01S01[W]",
                "logic": []
            },
            {
                "target": "D06Z01S01[NNW]",
                "logic": []
            },
            {
                "target": "D06Z01S01[NNE]",
                "logic": []
            },
            {
                "target": "D06Z01S01[N]",
                "logic": [
                    {
                        "item_requirements": [
                            "masks3"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D06Z01S19[S]"
        ]
    },
    {
        "name": "D06Z01S17[-Cherubs]",
        "exits": [
            {
                "target": "D06Z01S04[NW]",
                "logic": []
            },
            {
                "target": "D06Z01S04[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "D06Z01S06[W]"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "D06Z01S20[E]",
                            "wallClimb",
                            "canSurvivePoison2",
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "D06Z01S20[E]",
                            "wallClimb",
                            "canSurvivePoison2",
                            "doubleJump",
                            "canDawnJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "D06Z01S20[E]",
                            "wallClimb",
                            "canSurvivePoison2",
                            "doubleJump",
                            "canClimbOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "D06Z01S03[E]",
                            "wallClimb",
                            "canSurvivePoison2",
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "D06Z01S03[E]",
                            "wallClimb",
                            "canSurvivePoison2",
                            "doubleJump",
                            "canDawnJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "D06Z01S03[E]",
                            "wallClimb",
                            "canSurvivePoison2",
                            "doubleJump",
                            "canClimbOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "D06Z01S24[W]",
                            "wallClimb",
                            "canSurvivePoison2",
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "D06Z01S24[W]",
                            "wallClimb",
                            "canSurvivePoison2",
                            "doubleJump",
                            "canDawnJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "D06Z01S24[W]",
                            "wallClimb",
                            "canSurvivePoison2",
                            "doubleJump",
                            "canClimbOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D06Z01S17[-Cherubs]"
        ]
    },
    {
        "name": "D06Z01S24[W]",
        "exits": [
            {
                "target": "D06Z01S04[Health]",
                "logic": []
            },
            {
                "target": "D06Z01S20[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D06Z01S24[W]"
        ]
    },
    {
        "name": "D06Z01S24",
        "exits": [
            {
                "target": "D06Z01S24[W]",
                "logic": []
            }
        ],
        "locations": [
            "Lady[D06Z01S24]"
        ],
        "transitions": []
    },
    {
        "name": "D06Z01S04[Health]",
        "exits": [
            {
                "target": "D06Z01S24",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D06Z01S04[Health]"
        ]
    },
    {
        "name": "D06Z01S05[E]",
        "exits": [
            {
                "target": "D06Z01S12[NE]",
                "logic": []
            },
            {
                "target": "D06Z01S12[NE2]",
                "logic": [
                    {
                        "item_requirements": [
                            "D06Z01S16[W]"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "CO06",
                "logic": []
            },
            {
                "target": "PR12",
                "logic": [
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RESCUED_CHERUB_36",
                "logic": []
            },
            {
                "target": "D06Z01S01[W]",
                "logic": []
            },
            {
                "target": "D06Z01S01[SW]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D06Z01S05[E]",
            "D06Z01S12[NW]"
        ]
    },
    {
        "name": "D06Z01S09[W]",
        "exits": [
            {
                "target": "D06Z01S12[NE]",
                "logic": []
            },
            {
                "target": "D06Z01S12[NE2]",
                "logic": [
                    {
                        "item_requirements": [
                            "D06Z01S16[W]"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "CO06",
                "logic": []
            },
            {
                "target": "PR12",
                "logic": [
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RESCUED_CHERUB_36",
                "logic": []
            },
            {
                "target": "D06Z01S01[W]",
                "logic": []
            },
            {
                "target": "D06Z01S01[SW]",
                "logic": []
            },
            {
                "target": "D06Z01S05[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D06Z01S09[W]"
        ]
    },
    {
        "name": "D06Z01S11[W]",
        "exits": [
            {
                "target": "D06Z01S15[NE]",
                "logic": []
            },
            {
                "target": "D06Z01S21[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "D06Z01S21[E]"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "D06Z01S06[EE]",
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D06Z01S11[W]"
        ]
    },
    {
        "name": "D06Z01S21[E]",
        "exits": [
            {
                "target": "D06Z01S15[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "D06Z01S11[W]"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "D06Z01S06[EE]",
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S21",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D06Z01S21[E]",
            "D06Z01S15[NW]"
        ]
    },
    {
        "name": "D09Z01S01[E]",
        "exits": [
            {
                "target": "D06Z01S13[W]",
                "logic": []
            },
            {
                "target": "D06Z01S01[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D09Z01S01[E]"
        ]
    },
    {
        "name": "D06Z01S21",
        "exits": [
            {
                "target": "D06Z01S21[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "canBeatLegionary"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S01[NNE]",
                "logic": [
                    {
                        "item_requirements": [
                            "canBeatLegionary"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "QI04"
        ],
        "transitions": []
    },
    {
        "name": "D09Z01S01",
        "exits": [
            {
                "target": "D09Z01S01[W]",
                "logic": []
            },
            {
                "target": "D09Z01S01[E]",
                "logic": []
            }
        ],
        "locations": [
            "Amanecida[D09Z01S01]"
        ],
        "transitions": []
    },
    {
        "name": "D06Z01S13[W]",
        "exits": [
            {
                "target": "D09Z01S01",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D06Z01S13[W]"
        ]
    },
    {
        "name": "D09Z01S11[E]",
        "exits": [
            {
                "target": "D09Z01S01",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D09Z01S11[E]"
        ]
    },
    {
        "name": "D06Z01S11",
        "exits": [
            {
                "target": "D06Z01S11[W]",
                "logic": []
            }
        ],
        "locations": [
            "Sword[D06Z01S11]"
        ],
        "transitions": []
    },
    {
        "name": "D06Z01S15[NE]",
        "exits": [
            {
                "target": "D06Z01S11",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D06Z01S15[NE]"
        ]
    },
    {
        "name": "D06Z01S25",
        "exits": [
            {
                "target": "D06Z01S25[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "canBeatRooftopsBoss"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D06Z01S25[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "canBeatRooftopsBoss"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "BS16"
        ],
        "transitions": []
    },
    {
        "name": "D07Z01S01[W]",
        "exits": [
            {
                "target": "D06Z01S25",
                "logic": []
            },
            {
                "target": "D06Z01S25[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D07Z01S01[W]"
        ]
    },
    {
        "name": "D06Z01S22",
        "exits": [
            {
                "target": "D06Z01S22[Sword]",
                "logic": []
            }
        ],
        "locations": [
            "HE04"
        ],
        "transitions": []
    },
    {
        "name": "D06Z01S23[Sword]",
        "exits": [
            {
                "target": "D06Z01S22",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D06Z01S23[Sword]"
        ]
    },
    {
        "name": "D07Z01S01",
        "exits": [
            {
                "target": "D07Z01S01[W]",
                "logic": []
            },
            {
                "target": "D07Z01S01[E]",
                "logic": []
            }
        ],
        "locations": [
            "PR08"
        ],
        "transitions": []
    },
    {
        "name": "D06Z01S25[E]",
        "exits": [
            {
                "target": "D07Z01S01",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D06Z01S25[E]"
        ]
    },
    {
        "name": "D07Z01S02[W]",
        "exits": [
            {
                "target": "D07Z01S01",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D07Z01S02[W]"
        ]
    },
    {
        "name": "D07Z01S01[E]",
        "exits": [
            {
                "target": "D07Z01S02[W]",
                "logic": []
            },
            {
                "target": "D07Z01S02[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D07Z01S01[E]"
        ]
    },
    {
        "name": "D07Z01S03[W]",
        "exits": [
            {
                "target": "D07Z01S02[W]",
                "logic": []
            },
            {
                "target": "D07Z01S02[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D07Z01S03[W]"
        ]
    },
    {
        "name": "D07Z01S03",
        "exits": [
            {
                "target": "D07Z01S03[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": []
    },
    {
        "name": "D07Z01S02[E]",
        "exits": [
            {
                "target": "D07Z01S03",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D07Z01S02[E]"
        ]
    },
    {
        "name": "D08Z03S03",
        "exits": [
            {
                "target": "D08Z01S02[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "canBeatHallBoss"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D08Z03S02[NW]",
                "logic": [
                    {
                        "item_requirements": [
                            "canBeatHallBoss"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "LaudesBossTrigger[30000]"
        ],
        "transitions": []
    },
    {
        "name": "D08Z01S02[NE]",
        "exits": [
            {
                "target": "D08Z03S03",
                "logic": []
            },
            {
                "target": "D08Z01S02",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D08Z01S02[NE]",
            "D08Z03S03[W]"
        ]
    },
    {
        "name": "D08Z03S02[NW]",
        "exits": [
            {
                "target": "D08Z03S03",
                "logic": []
            },
            {
                "target": "D08Z03S02[SW]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D08Z03S02[NW]",
            "D08Z03S03[E]"
        ]
    },
    {
        "name": "D08Z01S02[SE]",
        "exits": [
            {
                "target": "D08Z02S03[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "brokeBotTCStatue"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D08Z02S03[E]",
                "logic": []
            },
            {
                "target": "D08Z02S02[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D08Z01S02[SE]"
        ]
    },
    {
        "name": "D08Z03S01[W]",
        "exits": [
            {
                "target": "D08Z02S03[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "brokeBotTCStatue"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D08Z02S03[E]",
                "logic": []
            },
            {
                "target": "D08Z02S02[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D08Z03S01[W]"
        ]
    },
    {
        "name": "D08Z01S02",
        "exits": [
            {
                "target": "D08Z01S02[SE]",
                "logic": []
            },
            {
                "target": "D08Z01S02[-Cherubs]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "HE101"
        ],
        "transitions": []
    },
    {
        "name": "D08Z02S03[W]",
        "exits": [
            {
                "target": "D08Z01S02",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D08Z02S03[W]"
        ]
    },
    {
        "name": "D08Z03S01",
        "exits": [
            {
                "target": "D08Z03S01[W]",
                "logic": []
            },
            {
                "target": "D08Z03S01[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "verses4"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "QI105"
        ],
        "transitions": []
    },
    {
        "name": "D08Z02S03[E]",
        "exits": [
            {
                "target": "D08Z03S01",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D08Z02S03[E]"
        ]
    },
    {
        "name": "D08Z03S02[SW]",
        "exits": [
            {
                "target": "D08Z03S01",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D08Z03S02[SW]"
        ]
    },
    {
        "name": "D08Z03S01[E]",
        "exits": [
            {
                "target": "D08Z03S02[SW]",
                "logic": []
            },
            {
                "target": "D08Z03S02[NW]",
                "logic": [
                    {
                        "item_requirements": [
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D08Z03S01[E]"
        ]
    },
    {
        "name": "D09Z01S01[W]",
        "exits": [
            {
                "target": "D09Z01S11[E]",
                "logic": []
            },
            {
                "target": "D09Z01S02[N]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D09Z01S01[W]"
        ]
    },
    {
        "name": "D09Z01S02[N]",
        "exits": [
            {
                "target": "D09Z01S11[E]",
                "logic": []
            },
            {
                "target": "D09Z01S02[Cell1]",
                "logic": [
                    {
                        "item_requirements": [
                            "bronzeKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S02[Cell6]",
                "logic": [
                    {
                        "item_requirements": [
                            "silverKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S02[Cell4]",
                "logic": [
                    {
                        "item_requirements": [
                            "goldKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S02[Cell3]",
                "logic": [
                    {
                        "item_requirements": [
                            "bronzeKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S02[Cell23]",
                "logic": [
                    {
                        "item_requirements": [
                            "bronzeKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RB11",
                "logic": []
            },
            {
                "target": "D09BZ01S01[Cell23]",
                "logic": [
                    {
                        "item_requirements": [
                            "bronzeKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "QI69",
                "logic": []
            }
        ],
        "locations": [
            "CO10",
            "QI51"
        ],
        "transitions": [
            "D09Z01S02[N]",
            "D09Z01S11[S]",
            "D09Z01S02[NW]",
            "D09Z01S07[NE]",
            "D09Z01S02[Cell22]",
            "D09BZ01S01[Cell22]",
            "D09Z01S02[Cell5]",
            "D09BZ01S01[Cell4]",
            "D09BZ01S01[Cell5]"
        ]
    },
    {
        "name": "D09Z01S04[E]",
        "exits": [
            {
                "target": "D09Z01S11[E]",
                "logic": []
            },
            {
                "target": "D09Z01S02[N]",
                "logic": []
            },
            {
                "target": "D09Z01S04[W]",
                "logic": []
            },
            {
                "target": "D09Z01S08[Cell7]",
                "logic": [
                    {
                        "item_requirements": [
                            "goldKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D09Z01S04[E]",
            "D09Z01S11[W]",
            "D09Z01S04[S]",
            "D09Z01S07[N]",
            "D09Z01S08[NE]",
            "D09Z01S07[NW]"
        ]
    },
    {
        "name": "D09Z01S02[Cell1]",
        "exits": [
            {
                "target": "D09BZ01S01[Cell1]",
                "logic": []
            }
        ],
        "locations": [
            "RESCUED_CHERUB_03"
        ],
        "transitions": [
            "D09Z01S02[Cell1]"
        ]
    },
    {
        "name": "D09Z01S02[Cell6]",
        "exits": [
            {
                "target": "D09BZ01S01[Cell6]",
                "logic": []
            }
        ],
        "locations": [
            "CO24"
        ],
        "transitions": [
            "D09Z01S02[Cell6]"
        ]
    },
    {
        "name": "D09Z01S02[Cell4]",
        "exits": [
            {
                "target": "D09Z01S02[N]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D09Z01S02[Cell4]"
        ]
    },
    {
        "name": "D09Z01S02[Cell3]",
        "exits": [
            {
                "target": "D09BZ01S01[Cell3]",
                "logic": []
            },
            {
                "target": "D09Z01S09[SW]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D09Z01S02[Cell3]"
        ]
    },
    {
        "name": "D09Z01S02[Cell23]",
        "exits": [
            {
                "target": "D09BZ01S01[Cell23]",
                "logic": [
                    {
                        "item_requirements": [
                            "bronzeKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "QI69",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D09Z01S02[Cell23]"
        ]
    },
    {
        "name": "D09Z01S08[Cell14]",
        "exits": [
            {
                "target": "D09BZ01S01[Cell15]",
                "logic": []
            },
            {
                "target": "RESCUED_CHERUB_34",
                "logic": []
            },
            {
                "target": "D09Z01S08[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "openedWotHPGate"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S08[S]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D09Z01S08[Cell14]",
            "D09BZ01S01[Cell14]"
        ]
    },
    {
        "name": "D09Z01S08[Cell15]",
        "exits": [
            {
                "target": "D09BZ01S01[Cell15]",
                "logic": []
            },
            {
                "target": "RESCUED_CHERUB_34",
                "logic": []
            },
            {
                "target": "D09Z01S08[Cell14]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D09Z01S08[Cell15]"
        ]
    },
    {
        "name": "D09Z01S08[Cell7]",
        "exits": [
            {
                "target": "D09BZ01S01[Cell7]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D09Z01S08[Cell7]"
        ]
    },
    {
        "name": "D09Z01S08[Cell16]",
        "exits": [
            {
                "target": "D09BZ01S01[Cell16]",
                "logic": []
            }
        ],
        "locations": [
            "CO26"
        ],
        "transitions": [
            "D09Z01S08[Cell16]"
        ]
    },
    {
        "name": "D09Z01S08[Cell18]",
        "exits": [
            {
                "target": "D09BZ01S01[Cell18]",
                "logic": []
            },
            {
                "target": "D09Z01S08[Cell17]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D09Z01S08[Cell18]"
        ]
    },
    {
        "name": "D09Z01S08[Cell17]",
        "exits": [
            {
                "target": "D09Z01S08[Cell15]",
                "logic": [
                    {
                        "item_requirements": [
                            "silverKey",
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S08[Cell7]",
                "logic": [
                    {
                        "item_requirements": [
                            "goldKey",
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S08[Cell16]",
                "logic": [
                    {
                        "item_requirements": [
                            "goldKey",
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S08[Cell18]",
                "logic": [
                    {
                        "item_requirements": [
                            "silverKey",
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S09[SW]",
                "logic": [
                    {
                        "item_requirements": [
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S04[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D09Z01S08[Cell17]",
            "D09BZ01S01[Cell17]"
        ]
    },
    {
        "name": "D09Z01S09[Cell20]",
        "exits": [
            {
                "target": "D09BZ01S01[Cell19]",
                "logic": []
            },
            {
                "target": "D09BZ01S01[Cell20]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D09Z01S09[Cell20]"
        ]
    },
    {
        "name": "D09Z01S09[Cell21]",
        "exits": [
            {
                "target": "D09BZ01S01[Cell21]",
                "logic": []
            }
        ],
        "locations": [
            "CO02"
        ],
        "transitions": [
            "D09Z01S09[Cell21]"
        ]
    },
    {
        "name": "D09Z01S10[Cell13]",
        "exits": [
            {
                "target": "D09BZ01S01[Cell12]",
                "logic": []
            }
        ],
        "locations": [
            "QI70"
        ],
        "transitions": [
            "D09Z01S10[Cell13]",
            "D09BZ01S01[Cell13]"
        ]
    },
    {
        "name": "D09Z01S10[Cell12]",
        "exits": [
            {
                "target": "D09BZ01S01[Cell12]",
                "logic": []
            },
            {
                "target": "D09Z01S10[Cell13]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D09Z01S10[Cell12]"
        ]
    },
    {
        "name": "D09Z01S10[Cell10]",
        "exits": [
            {
                "target": "D09BZ01S01[Cell10]",
                "logic": []
            }
        ],
        "locations": [
            "CO37"
        ],
        "transitions": [
            "D09Z01S10[Cell10]"
        ]
    },
    {
        "name": "D09Z01S10[Cell11]",
        "exits": [
            {
                "target": "D09BZ01S01[Cell11]",
                "logic": []
            }
        ],
        "locations": [
            "RESCUED_CHERUB_04"
        ],
        "transitions": [
            "D09Z01S10[Cell11]"
        ]
    },
    {
        "name": "D09Z01S03[W]",
        "exits": [
            {
                "target": "D09Z01S05[SE]",
                "logic": []
            },
            {
                "target": "D09Z01S05[NE]",
                "logic": []
            },
            {
                "target": "D09Z01S13[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D09Z01S03[W]"
        ]
    },
    {
        "name": "D09Z01S08[W]",
        "exits": [
            {
                "target": "D09Z01S05[SE]",
                "logic": []
            },
            {
                "target": "D09Z01S05[NE]",
                "logic": []
            },
            {
                "target": "D09Z01S13[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D09Z01S08[W]"
        ]
    },
    {
        "name": "D09Z01S13[E]",
        "exits": [
            {
                "target": "D09Z01S05[SE]",
                "logic": []
            },
            {
                "target": "D09Z01S05[NE]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D09Z01S13[E]",
            "D09Z01S05[W]"
        ]
    },
    {
        "name": "D09Z01S03",
        "exits": [],
        "locations": [
            "BS14"
        ],
        "transitions": []
    },
    {
        "name": "D09Z01S05[SE]",
        "exits": [
            {
                "target": "D09Z01S03",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D09Z01S05[SE]"
        ]
    },
    {
        "name": "D09Z01S08[S]",
        "exits": [
            {
                "target": "D09Z01S03",
                "logic": []
            },
            {
                "target": "D09Z01S03[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "canBeatPrisonBoss"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D09Z01S08[S]"
        ]
    },
    {
        "name": "D09Z01S05[NE]",
        "exits": [
            {
                "target": "D09Z01S08[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "openedWotHPGate"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S08[S]",
                "logic": []
            },
            {
                "target": "D09Z01S08[Cell14]",
                "logic": []
            },
            {
                "target": "QI72",
                "logic": [
                    {
                        "item_requirements": [
                            "openedWotHPGate"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D09Z01S05[NE]"
        ]
    },
    {
        "name": "D09BZ01S01[Cell7]",
        "exits": [
            {
                "target": "D09Z01S08[Cell7]",
                "logic": [
                    {
                        "item_requirements": [
                            "goldKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S04[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D09BZ01S01[Cell7]"
        ]
    },
    {
        "name": "D09BZ01S01[Cell15]",
        "exits": [
            {
                "target": "D09Z01S08[Cell15]",
                "logic": [
                    {
                        "item_requirements": [
                            "silverKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S08[Cell16]",
                "logic": [
                    {
                        "item_requirements": [
                            "goldKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S08[Cell18]",
                "logic": [
                    {
                        "item_requirements": [
                            "silverKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S09[SW]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D09BZ01S01[Cell15]"
        ]
    },
    {
        "name": "D09BZ01S01[Cell16]",
        "exits": [
            {
                "target": "D09Z01S08[Cell15]",
                "logic": [
                    {
                        "item_requirements": [
                            "silverKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S08[Cell16]",
                "logic": [
                    {
                        "item_requirements": [
                            "goldKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S08[Cell18]",
                "logic": [
                    {
                        "item_requirements": [
                            "silverKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S09[SW]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D09BZ01S01[Cell16]"
        ]
    },
    {
        "name": "D09BZ01S01[Cell18]",
        "exits": [
            {
                "target": "D09Z01S08[Cell15]",
                "logic": [
                    {
                        "item_requirements": [
                            "silverKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S08[Cell16]",
                "logic": [
                    {
                        "item_requirements": [
                            "goldKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S08[Cell18]",
                "logic": [
                    {
                        "item_requirements": [
                            "silverKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "QI72",
                "logic": [
                    {
                        "item_requirements": [
                            "openedWotHPGate"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S09[SW]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D09BZ01S01[Cell18]"
        ]
    },
    {
        "name": "D09Z01S06[E]",
        "exits": [
            {
                "target": "D09Z01S04[W]",
                "logic": []
            },
            {
                "target": "D09Z01S04[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D09Z01S06[E]"
        ]
    },
    {
        "name": "D09BZ01S01[Cell10]",
        "exits": [
            {
                "target": "D09Z01S10[Cell12]",
                "logic": [
                    {
                        "item_requirements": [
                            "bronzeKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S10[Cell10]",
                "logic": [
                    {
                        "item_requirements": [
                            "silverKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S10[Cell11]",
                "logic": [
                    {
                        "item_requirements": [
                            "silverKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "CO27",
                "logic": []
            },
            {
                "target": "D09Z01S09[SW]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D09BZ01S01[Cell10]"
        ]
    },
    {
        "name": "D09BZ01S01[Cell11]",
        "exits": [
            {
                "target": "D09Z01S10[Cell12]",
                "logic": [
                    {
                        "item_requirements": [
                            "bronzeKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S10[Cell10]",
                "logic": [
                    {
                        "item_requirements": [
                            "silverKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S10[Cell11]",
                "logic": [
                    {
                        "item_requirements": [
                            "silverKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "CO27",
                "logic": []
            },
            {
                "target": "D09Z01S09[SW]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D09BZ01S01[Cell11]"
        ]
    },
    {
        "name": "D09BZ01S01[Cell12]",
        "exits": [
            {
                "target": "D09Z01S10[Cell12]",
                "logic": [
                    {
                        "item_requirements": [
                            "bronzeKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S10[Cell10]",
                "logic": [
                    {
                        "item_requirements": [
                            "silverKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S10[Cell11]",
                "logic": [
                    {
                        "item_requirements": [
                            "silverKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "CO27",
                "logic": []
            },
            {
                "target": "D09Z01S09[SW]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D09BZ01S01[Cell12]"
        ]
    },
    {
        "name": "D09BZ01S01[Cell1]",
        "exits": [
            {
                "target": "D09Z01S02[N]",
                "logic": []
            },
            {
                "target": "D09Z01S02[Cell1]",
                "logic": [
                    {
                        "item_requirements": [
                            "bronzeKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S02[Cell6]",
                "logic": [
                    {
                        "item_requirements": [
                            "silverKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S02[Cell4]",
                "logic": [
                    {
                        "item_requirements": [
                            "goldKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S02[Cell3]",
                "logic": [
                    {
                        "item_requirements": [
                            "bronzeKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S02[Cell23]",
                "logic": [
                    {
                        "item_requirements": [
                            "bronzeKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RB11",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D09BZ01S01[Cell1]"
        ]
    },
    {
        "name": "D09BZ01S01[Cell3]",
        "exits": [
            {
                "target": "D09Z01S02[N]",
                "logic": []
            },
            {
                "target": "D09Z01S02[Cell1]",
                "logic": [
                    {
                        "item_requirements": [
                            "bronzeKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S02[Cell6]",
                "logic": [
                    {
                        "item_requirements": [
                            "silverKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S02[Cell4]",
                "logic": [
                    {
                        "item_requirements": [
                            "goldKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S02[Cell3]",
                "logic": [
                    {
                        "item_requirements": [
                            "bronzeKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S02[Cell23]",
                "logic": [
                    {
                        "item_requirements": [
                            "bronzeKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RB11",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D09BZ01S01[Cell3]"
        ]
    },
    {
        "name": "D09BZ01S01[Cell6]",
        "exits": [
            {
                "target": "D09Z01S02[N]",
                "logic": []
            },
            {
                "target": "D09Z01S02[Cell1]",
                "logic": [
                    {
                        "item_requirements": [
                            "bronzeKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S02[Cell6]",
                "logic": [
                    {
                        "item_requirements": [
                            "silverKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S02[Cell4]",
                "logic": [
                    {
                        "item_requirements": [
                            "goldKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S02[Cell3]",
                "logic": [
                    {
                        "item_requirements": [
                            "bronzeKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S02[Cell23]",
                "logic": [
                    {
                        "item_requirements": [
                            "bronzeKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RB11",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D09BZ01S01[Cell6]"
        ]
    },
    {
        "name": "D09BZ01S01[Cell23]",
        "exits": [
            {
                "target": "D09Z01S02[N]",
                "logic": []
            },
            {
                "target": "D09Z01S02[Cell1]",
                "logic": [
                    {
                        "item_requirements": [
                            "bronzeKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S02[Cell6]",
                "logic": [
                    {
                        "item_requirements": [
                            "silverKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S02[Cell4]",
                "logic": [
                    {
                        "item_requirements": [
                            "goldKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S02[Cell3]",
                "logic": [
                    {
                        "item_requirements": [
                            "bronzeKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D09Z01S02[Cell23]",
                "logic": [
                    {
                        "item_requirements": [
                            "bronzeKey"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RB11",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D09BZ01S01[Cell23]"
        ]
    },
    {
        "name": "D09Z01S12",
        "exits": [
            {
                "target": "D09Z01S12[E]",
                "logic": []
            }
        ],
        "locations": [
            "Oil[D09Z01S12]"
        ],
        "transitions": []
    },
    {
        "name": "D09Z01S09[NW]",
        "exits": [
            {
                "target": "D09Z01S12",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D09Z01S09[NW]"
        ]
    },
    {
        "name": "D17Z01S01[E]",
        "exits": [
            {
                "target": "D17Z01S02[W]",
                "logic": []
            },
            {
                "target": "D17Z01S05[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D17Z01S10[S]",
                "logic": [
                    {
                        "item_requirements": [
                            "blood",
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D17Z01S01[E]"
        ]
    },
    {
        "name": "D17Z01S05[W]",
        "exits": [
            {
                "target": "D17Z01S02[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D17Z01S05[S]",
                "logic": [
                    {
                        "item_requirements": [
                            "openedBotSSLadder"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D17Z01S11",
                "logic": []
            },
            {
                "target": "D17Z01S10[S]",
                "logic": [
                    {
                        "item_requirements": [
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D17Z01S05[W]",
            "D17Z01S02[E]",
            "D17Z01S11[W]",
            "D17Z01S05[E]"
        ]
    },
    {
        "name": "D17Z01S10[S]",
        "exits": [
            {
                "target": "D17Z01S02[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D17Z01S05[W]",
                "logic": []
            },
            {
                "target": "D17Z01S13[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D17Z01S10[S]",
            "D17Z01S02[N]"
        ]
    },
    {
        "name": "D17Z01S01",
        "exits": [
            {
                "target": "D17Z01S01[E]",
                "logic": []
            }
        ],
        "locations": [
            "RESCUED_CHERUB_06"
        ],
        "transitions": []
    },
    {
        "name": "D17Z01S02[W]",
        "exits": [
            {
                "target": "D17Z01S01",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D17Z01S02[W]"
        ]
    },
    {
        "name": "D17Z01S14[-Cherubs1]",
        "exits": [
            {
                "target": "D17Z01S01",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D17Z01S14[-Cherubs1]"
        ]
    },
    {
        "name": "D17Z01S14[-Cherubs2]",
        "exits": [
            {
                "target": "D17Z01S01",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D17Z01S14[-Cherubs2]"
        ]
    },
    {
        "name": "D17Z01S14[-Cherubs3]",
        "exits": [
            {
                "target": "D17Z01S01",
                "logic": []
            }
        ],
        "locations": [
            "RB204"
        ],
        "transitions": [
            "D17Z01S14[-Cherubs3]"
        ]
    },
    {
        "name": "D17Z01S04[N]",
        "exits": [
            {
                "target": "D17Z01S05[W]",
                "logic": []
            },
            {
                "target": "D17Z01S05[S]",
                "logic": [
                    {
                        "item_requirements": [
                            "openedBotSSLadder"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D17Z01S04[N]"
        ]
    },
    {
        "name": "D17Z01S13[E]",
        "exits": [
            {
                "target": "D17Z01S10[S]",
                "logic": []
            },
            {
                "target": "D17Z01S14[-Cherubs2]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen",
                            "canCrossGap8"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "linen",
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D17Z01S14[-Cherubs3]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D17Z01S14[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "scapular",
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D17Z01S14[-Cherubs1]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen",
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "linen",
                            "canCrossGap11"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "PR203",
                "logic": [
                    {
                        "item_requirements": [
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D17Z01S13[E]",
            "D17Z01S10[W]",
            "D17Z01S14[E]",
            "D17Z01S13[W]"
        ]
    },
    {
        "name": "D17Z01S11",
        "exits": [
            {
                "target": "D17Z01S11[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "canBeatBrotherhoodBoss"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D17Z01S05[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "canBeatBrotherhoodBoss"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "BS13"
        ],
        "transitions": []
    },
    {
        "name": "D17BZ01S01",
        "exits": [
            {
                "target": "D17BZ01S01[relic]",
                "logic": []
            }
        ],
        "locations": [
            "RE01"
        ],
        "transitions": []
    },
    {
        "name": "D17Z01S03[relic]",
        "exits": [
            {
                "target": "D17BZ01S01",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D17Z01S03[relic]"
        ]
    },
    {
        "name": "D17Z01S04[W]",
        "exits": [
            {
                "target": "D17Z01S12[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D17Z01S04[W]"
        ]
    },
    {
        "name": "D17Z01S04[FrontL]",
        "exits": [
            {
                "target": "D17BZ02S01[FrontL]",
                "logic": []
            },
            {
                "target": "CO25",
                "logic": [
                    {
                        "item_requirements": [
                            "dash",
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D17Z01S04[FrontR]",
                "logic": [
                    {
                        "item_requirements": [
                            "dash",
                            "wallClimb"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D17Z01S04[FrontL]"
        ]
    },
    {
        "name": "D17Z01S04[FrontR]",
        "exits": [
            {
                "target": "CO25",
                "logic": []
            },
            {
                "target": "D17Z01S04",
                "logic": []
            },
            {
                "target": "D17Z01S04[N]",
                "logic": []
            },
            {
                "target": "RB25",
                "logic": [
                    {
                        "item_requirements": [
                            "blueWax1"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RB26",
                "logic": [
                    {
                        "item_requirements": [
                            "blueWax1",
                            "D01Z04S13[SE]"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "blueWax1",
                            "D05Z02S12[W]"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D17Z01S04[FrontR]",
            "D17BZ02S01[FrontR]"
        ]
    },
    {
        "name": "D17Z01S04",
        "exits": [
            {
                "target": "D17Z01S04[W]",
                "logic": []
            },
            {
                "target": "D17Z01S04[S]",
                "logic": []
            },
            {
                "target": "D17Z01S04[FrontL]",
                "logic": []
            }
        ],
        "locations": [
            "RE401"
        ],
        "transitions": []
    },
    {
        "name": "D17Z01S05[S]",
        "exits": [
            {
                "target": "D17Z01S04",
                "logic": []
            },
            {
                "target": "D17Z01S04[N]",
                "logic": []
            },
            {
                "target": "D17Z01S04[FrontR]",
                "logic": []
            },
            {
                "target": "RB25",
                "logic": [
                    {
                        "item_requirements": [
                            "blueWax1"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "RB26",
                "logic": [
                    {
                        "item_requirements": [
                            "blueWax1",
                            "D01Z04S13[SE]"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "blueWax1",
                            "D05Z02S12[W]"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D17Z01S05[S]"
        ]
    },
    {
        "name": "D17Z01S07[N]",
        "exits": [
            {
                "target": "D17Z01S04",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D17Z01S07[N]"
        ]
    },
    {
        "name": "D17Z01S12[E]",
        "exits": [
            {
                "target": "D17Z01S04",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D17Z01S12[E]"
        ]
    },
    {
        "name": "D17BZ02S01[FrontL]",
        "exits": [
            {
                "target": "D17Z01S04",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D17BZ02S01[FrontL]"
        ]
    },
    {
        "name": "D17Z01S08",
        "exits": [
            {
                "target": "D17Z01S08[E]",
                "logic": []
            }
        ],
        "locations": [
            "Sword[D17Z01S08]"
        ],
        "transitions": []
    },
    {
        "name": "D17Z01S07[SW]",
        "exits": [
            {
                "target": "D17Z01S08",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D17Z01S07[SW]"
        ]
    },
    {
        "name": "D17Z01S15[E]",
        "exits": [
            {
                "target": "D17Z01S14[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "scapular"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D17Z01S14[-Cherubs1]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D17Z01S14[-Cherubs2]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen",
                            "canCrossGap10"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "linen",
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "PR203",
                "logic": []
            },
            {
                "target": "D17Z01S14[-Cherubs3]",
                "logic": [
                    {
                        "item_requirements": [
                            "linen",
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D17Z01S13[E]",
                "logic": [
                    {
                        "item_requirements": [
                            "blood"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [],
        "transitions": [
            "D17Z01S15[E]"
        ]
    },
    {
        "name": "D17Z01S15",
        "exits": [
            {
                "target": "D17Z01S15[E]",
                "logic": []
            }
        ],
        "locations": [
            "QI204",
            "QI301"
        ],
        "transitions": []
    },
    {
        "name": "D17Z01S14[W]",
        "exits": [
            {
                "target": "D17Z01S15",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D17Z01S14[W]"
        ]
    },
    {
        "name": "D20Z01S02",
        "exits": [
            {
                "target": "D20Z01S02[W]",
                "logic": []
            },
            {
                "target": "D20Z01S02[E]",
                "logic": []
            }
        ],
        "locations": [
            "RB108"
        ],
        "transitions": []
    },
    {
        "name": "D20Z01S01[E]",
        "exits": [
            {
                "target": "D20Z01S02",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D20Z01S01[E]"
        ]
    },
    {
        "name": "D20Z01S03[W]",
        "exits": [
            {
                "target": "D20Z01S02",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D20Z01S03[W]"
        ]
    },
    {
        "name": "D20Z02S11[SW]",
        "exits": [
            {
                "target": "D20Z02S12[E]",
                "logic": []
            },
            {
                "target": "D20Z01S11[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D20Z02S11[SW]"
        ]
    },
    {
        "name": "D20Z02S11",
        "exits": [
            {
                "target": "D20Z02S11[SW]",
                "logic": []
            },
            {
                "target": "D20Z01S11[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "HardLogic",
                            "mourningSkipAllowed",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "HardLogic",
                            "mourningSkipAllowed",
                            "tirana",
                            "obscureSkipsAllowed"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D20Z02S10[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "HardLogic",
                            "mourningSkipAllowed",
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "HardLogic",
                            "mourningSkipAllowed",
                            "tirana",
                            "obscureSkipsAllowed"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            }
        ],
        "locations": [
            "PR202"
        ],
        "transitions": []
    },
    {
        "name": "D20Z02S10[W]",
        "exits": [
            {
                "target": "D20Z02S11",
                "logic": []
            },
            {
                "target": "D20Z01S11[W]",
                "logic": [
                    {
                        "item_requirements": [
                            "HardLogic",
                            "mourningSkipAllowed"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D20Z02S10[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D20Z02S10[W]",
            "D20Z02S11[E]"
        ]
    },
    {
        "name": "D20Z02S12[E]",
        "exits": [
            {
                "target": "D20Z02S11",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D20Z02S12[E]"
        ]
    },
    {
        "name": "D20Z03S01[W]",
        "exits": [
            {
                "target": "D20Z01S14[E]",
                "logic": []
            },
            {
                "target": "D20Z01S11[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D20Z03S01[W]"
        ]
    },
    {
        "name": "D20Z03S01",
        "exits": [
            {
                "target": "D20Z03S01[W]",
                "logic": []
            }
        ],
        "locations": [
            "QI203"
        ],
        "transitions": []
    },
    {
        "name": "D20Z01S14[E]",
        "exits": [
            {
                "target": "D20Z03S01",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D20Z01S14[E]"
        ]
    },
    {
        "name": "D20Z02S02[W]",
        "exits": [
            {
                "target": "D20Z02S03[NE]",
                "logic": []
            },
            {
                "target": "D04Z02S24[NW]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D20Z02S02[W]"
        ]
    },
    {
        "name": "D20Z02S05[E]",
        "exits": [
            {
                "target": "D04Z02S24[NW]",
                "logic": [
                    {
                        "item_requirements": [
                            "dash"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D20Z02S06[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "nail"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canCrossGap3"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canClimbOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canDiveLaser"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D20Z02S06[SW]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D20Z02S05[E]",
            "D20Z02S04[W]",
            "D20Z02S06[SE]",
            "D20Z02S05[SW]"
        ]
    },
    {
        "name": "D20Z02S02",
        "exits": [
            {
                "target": "D20Z02S02[W]",
                "logic": []
            }
        ],
        "locations": [
            "RB201"
        ],
        "transitions": []
    },
    {
        "name": "D20Z02S03[NE]",
        "exits": [
            {
                "target": "D20Z02S02",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D20Z02S03[NE]"
        ]
    },
    {
        "name": "D20Z02S06[NE]",
        "exits": [
            {
                "target": "D20Z02S05[E]",
                "logic": []
            },
            {
                "target": "D20Z02S06[SW]",
                "logic": []
            },
            {
                "target": "D20Z02S07[W]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D20Z02S06[NE]",
            "D20Z02S05[NW]",
            "D20Z02S07[E]",
            "D20Z02S06[NW]"
        ]
    },
    {
        "name": "D20Z02S09[E]",
        "exits": [
            {
                "target": "D20Z02S06[SW]",
                "logic": []
            },
            {
                "target": "D20Z02S06[NE]",
                "logic": [
                    {
                        "item_requirements": [
                            "doubleJump"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canClimbOnRoot"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "canDiveLaser"
                        ],
                        "location_requirements": [],
                        "state_modifiers": []
                    }
                ]
            },
            {
                "target": "D20Z02S05[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D20Z02S09[E]"
        ]
    },
    {
        "name": "D20Z02S09",
        "exits": [
            {
                "target": "D20Z02S09[W]",
                "logic": []
            },
            {
                "target": "D20Z02S09[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": []
    },
    {
        "name": "D20Z02S06[SW]",
        "exits": [
            {
                "target": "D20Z02S09",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D20Z02S06[SW]"
        ]
    },
    {
        "name": "D20Z02S10[E]",
        "exits": [
            {
                "target": "D20Z02S09",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D20Z02S10[E]"
        ]
    },
    {
        "name": "D20Z02S08[E]",
        "exits": [
            {
                "target": "D20Z02S07[W]",
                "logic": []
            },
            {
                "target": "D20Z02S06[NE]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D20Z02S08[E]"
        ]
    },
    {
        "name": "D20Z02S08",
        "exits": [
            {
                "target": "D20Z02S08[E]",
                "logic": []
            }
        ],
        "locations": [
            "BossTrigger[5000]",
            "QI202"
        ],
        "transitions": []
    },
    {
        "name": "D20Z02S07[W]",
        "exits": [
            {
                "target": "D20Z02S08",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D20Z02S07[W]"
        ]
    },
    {
        "name": "D20Z02S09[W]",
        "exits": [
            {
                "target": "D20Z02S10[W]",
                "logic": []
            },
            {
                "target": "D20Z02S10[E]",
                "logic": []
            }
        ],
        "locations": [],
        "transitions": [
            "D20Z02S09[W]"
        ]
    },
    {
        "name": "RESCUED_CHERUB_08",
        "exits": [],
        "locations": [
            "RESCUED_CHERUB_08"
        ],
        "transitions": []
    },
    {
        "name": "CO21",
        "exits": [],
        "locations": [
            "CO21"
        ],
        "transitions": []
    },
    {
        "name": "PR16",
        "exits": [],
        "locations": [
            "PR16"
        ],
        "transitions": []
    },
    {
        "name": "RESCUED_CHERUB_13",
        "exits": [],
        "locations": [
            "RESCUED_CHERUB_13"
        ],
        "transitions": []
    },
    {
        "name": "RESCUED_CHERUB_12",
        "exits": [],
        "locations": [
            "RESCUED_CHERUB_12"
        ],
        "transitions": []
    },
    {
        "name": "CO32",
        "exits": [],
        "locations": [
            "CO32"
        ],
        "transitions": []
    },
    {
        "name": "CO44",
        "exits": [],
        "locations": [
            "CO44"
        ],
        "transitions": []
    },
    {
        "name": "RESCUED_CHERUB_22",
        "exits": [],
        "locations": [
            "RESCUED_CHERUB_22"
        ],
        "transitions": []
    },
    {
        "name": "CO11",
        "exits": [],
        "locations": [
            "CO11"
        ],
        "transitions": []
    },
    {
        "name": "QI59",
        "exits": [],
        "locations": [
            "QI59"
        ],
        "transitions": []
    },
    {
        "name": "RB10",
        "exits": [],
        "locations": [
            "RB10"
        ],
        "transitions": []
    },
    {
        "name": "RESCUED_CHERUB_23",
        "exits": [],
        "locations": [
            "RESCUED_CHERUB_23"
        ],
        "transitions": []
    },
    {
        "name": "QI68",
        "exits": [],
        "locations": [
            "QI68"
        ],
        "transitions": []
    },
    {
        "name": "CO19",
        "exits": [],
        "locations": [
            "CO19"
        ],
        "transitions": []
    },
    {
        "name": "RESCUED_CHERUB_27",
        "exits": [],
        "locations": [
            "RESCUED_CHERUB_27"
        ],
        "transitions": []
    },
    {
        "name": "RESCUED_CHERUB_24",
        "exits": [],
        "locations": [
            "RESCUED_CHERUB_24"
        ],
        "transitions": []
    },
    {
        "name": "QI46",
        "exits": [],
        "locations": [
            "QI46"
        ],
        "transitions": []
    },
    {
        "name": "CO29",
        "exits": [],
        "locations": [
            "CO29"
        ],
        "transitions": []
    },
    {
        "name": "QI08",
        "exits": [],
        "locations": [
            "QI08"
        ],
        "transitions": []
    },
    {
        "name": "CO01",
        "exits": [],
        "locations": [
            "CO01"
        ],
        "transitions": []
    },
    {
        "name": "RESCUED_CHERUB_25",
        "exits": [],
        "locations": [
            "RESCUED_CHERUB_25"
        ],
        "transitions": []
    },
    {
        "name": "RB15",
        "exits": [],
        "locations": [
            "RB15"
        ],
        "transitions": []
    },
    {
        "name": "CO42",
        "exits": [],
        "locations": [
            "CO42"
        ],
        "transitions": []
    },
    {
        "name": "RESCUED_CHERUB_31",
        "exits": [],
        "locations": [
            "RESCUED_CHERUB_31"
        ],
        "transitions": []
    },
    {
        "name": "CO05",
        "exits": [],
        "locations": [
            "CO05"
        ],
        "transitions": []
    },
    {
        "name": "RB08",
        "exits": [],
        "locations": [
            "RB08"
        ],
        "transitions": []
    },
    {
        "name": "QI47",
        "exits": [],
        "locations": [
            "QI47"
        ],
        "transitions": []
    },
    {
        "name": "RB22",
        "exits": [],
        "locations": [
            "RB22"
        ],
        "transitions": []
    },
    {
        "name": "RESCUED_CHERUB_16",
        "exits": [],
        "locations": [
            "RESCUED_CHERUB_16"
        ],
        "transitions": []
    },
    {
        "name": "Amanecida[D03Z01S03]",
        "exits": [],
        "locations": [
            "Amanecida[D03Z01S03]"
        ],
        "transitions": []
    },
    {
        "name": "PR10",
        "exits": [],
        "locations": [
            "PR10"
        ],
        "transitions": []
    },
    {
        "name": "CO33",
        "exits": [],
        "locations": [
            "CO33"
        ],
        "transitions": []
    },
    {
        "name": "RESCUED_CHERUB_18",
        "exits": [],
        "locations": [
            "RESCUED_CHERUB_18"
        ],
        "transitions": []
    },
    {
        "name": "QI41",
        "exits": [],
        "locations": [
            "QI41"
        ],
        "transitions": []
    },
    {
        "name": "HE06",
        "exits": [],
        "locations": [
            "HE06"
        ],
        "transitions": []
    },
    {
        "name": "RESCUED_CHERUB_37",
        "exits": [],
        "locations": [
            "RESCUED_CHERUB_37"
        ],
        "transitions": []
    },
    {
        "name": "RB06",
        "exits": [],
        "locations": [
            "RB06"
        ],
        "transitions": []
    },
    {
        "name": "CO23",
        "exits": [],
        "locations": [
            "CO23"
        ],
        "transitions": []
    },
    {
        "name": "RE402",
        "exits": [],
        "locations": [
            "RE402"
        ],
        "transitions": []
    },
    {
        "name": "RESCUED_CHERUB_30",
        "exits": [],
        "locations": [
            "RESCUED_CHERUB_30"
        ],
        "transitions": []
    },
    {
        "name": "CO34",
        "exits": [],
        "locations": [
            "CO34"
        ],
        "transitions": []
    },
    {
        "name": "CO22",
        "exits": [],
        "locations": [
            "CO22"
        ],
        "transitions": []
    },
    {
        "name": "RB31",
        "exits": [],
        "locations": [
            "RB31"
        ],
        "transitions": []
    },
    {
        "name": "RB203",
        "exits": [],
        "locations": [
            "RB203"
        ],
        "transitions": []
    },
    {
        "name": "CO28",
        "exits": [],
        "locations": [
            "CO28"
        ],
        "transitions": []
    },
    {
        "name": "QI03",
        "exits": [],
        "locations": [
            "QI03"
        ],
        "transitions": []
    },
    {
        "name": "CO06",
        "exits": [],
        "locations": [
            "CO06"
        ],
        "transitions": []
    },
    {
        "name": "PR12",
        "exits": [],
        "locations": [
            "PR12"
        ],
        "transitions": []
    },
    {
        "name": "RESCUED_CHERUB_36",
        "exits": [],
        "locations": [
            "RESCUED_CHERUB_36"
        ],
        "transitions": []
    },
    {
        "name": "RB11",
        "exits": [],
        "locations": [
            "RB11"
        ],
        "transitions": []
    },
    {
        "name": "QI72",
        "exits": [],
        "locations": [
            "QI72"
        ],
        "transitions": []
    },
    {
        "name": "RB16",
        "exits": [],
        "locations": [
            "RB16"
        ],
        "transitions": []
    },
    {
        "name": "CO27",
        "exits": [],
        "locations": [
            "CO27"
        ],
        "transitions": []
    },
    {
        "name": "QI69",
        "exits": [],
        "locations": [
            "QI69"
        ],
        "transitions": []
    },
    {
        "name": "RESCUED_CHERUB_34",
        "exits": [],
        "locations": [
            "RESCUED_CHERUB_34"
        ],
        "transitions": []
    },
    {
        "name": "PR203",
        "exits": [],
        "locations": [
            "PR203"
        ],
        "transitions": []
    },
    {
        "name": "CO25",
        "exits": [],
        "locations": [
            "CO25"
        ],
        "transitions": []
    },
    {
        "name": "RB202",
        "exits": [],
        "locations": [
            "RB202"
        ],
        "transitions": []
    },
    {
        "name": "RB18",
        "exits": [],
        "locations": [
            "RB18"
        ],
        "transitions": []
    },
    {
        "name": "RB25",
        "exits": [],
        "locations": [
            "RB25"
        ],
        "transitions": []
    },
    {
        "name": "RB26",
        "exits": [],
        "locations": [
            "RB26"
        ],
        "transitions": []
    }
]
locations = [
    {
        "name": "PR14",
        "logic": []
    },
    {
        "name": "RB07",
        "logic": [
            {
                "item_requirements": [
                    "blood"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "doubleJump"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "CO04",
        "logic": []
    },
    {
        "name": "QI55",
        "logic": [
            {
                "item_requirements": [
                    "blood",
                    "dash",
                    "canWaterJump"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "RESCUED_CHERUB_07",
        "logic": []
    },
    {
        "name": "QI31",
        "logic": []
    },
    {
        "name": "RE02",
        "logic": [
            {
                "item_requirements": [
                    "hand"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "RE04",
        "logic": [
            {
                "item_requirements": [
                    "cloth"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "RE10",
        "logic": [
            {
                "item_requirements": [
                    "hatchedEgg"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "RB01",
        "logic": []
    },
    {
        "name": "QI66",
        "logic": [
            {
                "item_requirements": [
                    "herbs1"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "Tirso[500]",
        "logic": [
            {
                "item_requirements": [
                    "herbs2"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "Tirso[1000]",
        "logic": [
            {
                "item_requirements": [
                    "herbs3"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "Tirso[2000]",
        "logic": [
            {
                "item_requirements": [
                    "herbs4"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "Tirso[5000]",
        "logic": [
            {
                "item_requirements": [
                    "herbs5"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "Tirso[10000]",
        "logic": [
            {
                "item_requirements": [
                    "herbs6"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "QI56",
        "logic": [
            {
                "item_requirements": [
                    "herbs6",
                    "canBeatMercyBoss",
                    "canBeatConventBoss",
                    "canBeatGrievanceBoss",
                    "canBeatMothersBoss",
                    "canBeatCanvasesBoss",
                    "canBeatPrisonBoss"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "RESCUED_CHERUB_08",
        "logic": []
    },
    {
        "name": "Lvdovico[500]",
        "logic": [
            {
                "item_requirements": [
                    "tentudiaRemains1"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "Lvdovico[1000]",
        "logic": [
            {
                "item_requirements": [
                    "tentudiaRemains2"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "PR03",
        "logic": [
            {
                "item_requirements": [
                    "tentudiaRemains3"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "QI01",
        "logic": []
    },
    {
        "name": "CO43",
        "logic": []
    },
    {
        "name": "CO16",
        "logic": []
    },
    {
        "name": "Sword[D01Z02S06]",
        "logic": []
    },
    {
        "name": "QI65",
        "logic": []
    },
    {
        "name": "RB104",
        "logic": []
    },
    {
        "name": "RB105",
        "logic": []
    },
    {
        "name": "PR11",
        "logic": [
            {
                "item_requirements": [
                    "marksOfRefuge3",
                    "cord",
                    "D06Z01S02[W]"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "Undertaker[250]",
        "logic": [
            {
                "item_requirements": [
                    "bones4"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "Undertaker[500]",
        "logic": [
            {
                "item_requirements": [
                    "bones8"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "Undertaker[750]",
        "logic": [
            {
                "item_requirements": [
                    "bones12"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "Undertaker[1000]",
        "logic": [
            {
                "item_requirements": [
                    "bones16"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "Undertaker[1250]",
        "logic": [
            {
                "item_requirements": [
                    "bones20"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "Undertaker[1500]",
        "logic": [
            {
                "item_requirements": [
                    "bones24"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "Undertaker[1750]",
        "logic": [
            {
                "item_requirements": [
                    "bones28"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "Undertaker[2000]",
        "logic": [
            {
                "item_requirements": [
                    "bones32"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "Undertaker[2500]",
        "logic": [
            {
                "item_requirements": [
                    "bones36"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "Undertaker[3000]",
        "logic": [
            {
                "item_requirements": [
                    "bones40"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "Undertaker[5000]",
        "logic": [
            {
                "item_requirements": [
                    "bones44"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "QI201",
        "logic": [
            {
                "item_requirements": [
                    "canBeatOssuaryBoss"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "RB04",
        "logic": []
    },
    {
        "name": "CO14",
        "logic": [
            {
                "item_requirements": [
                    "dash"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "CO36",
        "logic": []
    },
    {
        "name": "RESCUED_CHERUB_10",
        "logic": []
    },
    {
        "name": "QI06",
        "logic": [
            {
                "item_requirements": [
                    "blood"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "boots"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "canCrossGap3"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "RB20",
        "logic": [
            {
                "item_requirements": [
                    "redentoRooms3"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "HE02",
        "logic": []
    },
    {
        "name": "RESCUED_CHERUB_38",
        "logic": [
            {
                "item_requirements": [
                    "canCrossGap2"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "lorquiana"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "cante"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "aubade"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "cantina"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "ruby"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "chargeBeam"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "rangedAttack"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "preciseSkipsAllowed"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "CO30",
        "logic": []
    },
    {
        "name": "CO03",
        "logic": []
    },
    {
        "name": "RESCUED_CHERUB_09",
        "logic": []
    },
    {
        "name": "PR01",
        "logic": []
    },
    {
        "name": "RB17",
        "logic": []
    },
    {
        "name": "QI48",
        "logic": []
    },
    {
        "name": "CO21",
        "logic": []
    },
    {
        "name": "CO38",
        "logic": [
            {
                "item_requirements": [
                    "dash"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "RESCUED_CHERUB_33",
        "logic": [
            {
                "item_requirements": [
                    "doubleJump"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "pillar"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "cante"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "tirana"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "BS01",
        "logic": [
            {
                "item_requirements": [
                    "canBeatMercyBoss"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "QI38",
        "logic": []
    },
    {
        "name": "QI58",
        "logic": []
    },
    {
        "name": "RB05",
        "logic": []
    },
    {
        "name": "RB09",
        "logic": []
    },
    {
        "name": "CO09",
        "logic": []
    },
    {
        "name": "QI67",
        "logic": [
            {
                "item_requirements": [
                    "dash",
                    "canWaterJump"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "PR16",
        "logic": []
    },
    {
        "name": "RESCUED_CHERUB_13",
        "logic": []
    },
    {
        "name": "Oil[D01Z05S07]",
        "logic": []
    },
    {
        "name": "QI12",
        "logic": []
    },
    {
        "name": "RESCUED_CHERUB_14",
        "logic": []
    },
    {
        "name": "QI45",
        "logic": []
    },
    {
        "name": "RESCUED_CHERUB_12",
        "logic": []
    },
    {
        "name": "RESCUED_CHERUB_11",
        "logic": []
    },
    {
        "name": "CO41",
        "logic": []
    },
    {
        "name": "CO32",
        "logic": []
    },
    {
        "name": "RESCUED_CHERUB_15",
        "logic": []
    },
    {
        "name": "Lady[D01Z05S22]",
        "logic": []
    },
    {
        "name": "QI75",
        "logic": []
    },
    {
        "name": "Sword[D01Z05S24]",
        "logic": []
    },
    {
        "name": "CO44",
        "logic": []
    },
    {
        "name": "RESCUED_CHERUB_22",
        "logic": []
    },
    {
        "name": "Lady[D01Z05S26]",
        "logic": []
    },
    {
        "name": "RB03",
        "logic": []
    },
    {
        "name": "QI101",
        "logic": []
    },
    {
        "name": "CO11",
        "logic": []
    },
    {
        "name": "QI59",
        "logic": []
    },
    {
        "name": "RB10",
        "logic": []
    },
    {
        "name": "RESCUED_CHERUB_23",
        "logic": []
    },
    {
        "name": "QI20",
        "logic": []
    },
    {
        "name": "QI68",
        "logic": []
    },
    {
        "name": "QI07",
        "logic": []
    },
    {
        "name": "CO19",
        "logic": []
    },
    {
        "name": "RESCUED_CHERUB_27",
        "logic": []
    },
    {
        "name": "PR04",
        "logic": [
            {
                "item_requirements": [
                    "driedFlowers"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "HE05",
        "logic": [
            {
                "item_requirements": [
                    "canWalkOnRoot"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "canCrossGap11"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "doubleJump",
                    "canEnemyBounce"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "RESCUED_CHERUB_24",
        "logic": []
    },
    {
        "name": "QI46",
        "logic": []
    },
    {
        "name": "CO29",
        "logic": []
    },
    {
        "name": "QI08",
        "logic": []
    },
    {
        "name": "RB32",
        "logic": []
    },
    {
        "name": "CO01",
        "logic": []
    },
    {
        "name": "RESCUED_CHERUB_25",
        "logic": []
    },
    {
        "name": "RB15",
        "logic": []
    },
    {
        "name": "RB38",
        "logic": []
    },
    {
        "name": "CO42",
        "logic": []
    },
    {
        "name": "RESCUED_CHERUB_31",
        "logic": []
    },
    {
        "name": "Oil[D02Z02S10]",
        "logic": []
    },
    {
        "name": "QI53",
        "logic": []
    },
    {
        "name": "RESCUED_CHERUB_26",
        "logic": []
    },
    {
        "name": "Lady[D02Z02S12]",
        "logic": []
    },
    {
        "name": "HE11",
        "logic": []
    },
    {
        "name": "RB106",
        "logic": []
    },
    {
        "name": "Amanecida[D02Z02S14]",
        "logic": [
            {
                "item_requirements": [
                    "canBeatGraveyardBoss"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "QI11",
        "logic": []
    },
    {
        "name": "RB37",
        "logic": []
    },
    {
        "name": "RB02",
        "logic": []
    },
    {
        "name": "CO05",
        "logic": []
    },
    {
        "name": "RB08",
        "logic": []
    },
    {
        "name": "CO15",
        "logic": []
    },
    {
        "name": "HE03",
        "logic": [
            {
                "item_requirements": [
                    "canSurvivePoison1",
                    "dash"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "Sword[D02Z03S13]",
        "logic": []
    },
    {
        "name": "Lady[D02Z03S15]",
        "logic": []
    },
    {
        "name": "RB24",
        "logic": []
    },
    {
        "name": "QI61",
        "logic": []
    },
    {
        "name": "BS03",
        "logic": [
            {
                "item_requirements": [
                    "canBeatConventBoss"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "QI40",
        "logic": []
    },
    {
        "name": "QI57",
        "logic": [
            {
                "item_requirements": [
                    "emptyThimble"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "RB107",
        "logic": []
    },
    {
        "name": "CO13",
        "logic": []
    },
    {
        "name": "QI47",
        "logic": []
    },
    {
        "name": "RB22",
        "logic": []
    },
    {
        "name": "RESCUED_CHERUB_16",
        "logic": []
    },
    {
        "name": "Amanecida[D03Z01S03]",
        "logic": []
    },
    {
        "name": "QI63",
        "logic": [
            {
                "item_requirements": [
                    "blood"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "doubleJump"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "upwarpSkipsAllowed"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "RB13",
        "logic": [
            {
                "item_requirements": [
                    "canBeatPerpetua"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "QI14",
        "logic": [
            {
                "item_requirements": [
                    "canBeatPerpetua",
                    "egg"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "CO08",
        "logic": []
    },
    {
        "name": "PR10",
        "logic": []
    },
    {
        "name": "CO33",
        "logic": []
    },
    {
        "name": "RESCUED_CHERUB_18",
        "logic": []
    },
    {
        "name": "QI19",
        "logic": []
    },
    {
        "name": "CO07",
        "logic": []
    },
    {
        "name": "QI41",
        "logic": []
    },
    {
        "name": "RESCUED_CHERUB_17",
        "logic": []
    },
    {
        "name": "HE06",
        "logic": []
    },
    {
        "name": "RESCUED_CHERUB_37",
        "logic": []
    },
    {
        "name": "QI52",
        "logic": []
    },
    {
        "name": "RB28",
        "logic": [
            {
                "item_requirements": [
                    "canWalkOnRoot"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "canCrossGap3"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "QI103",
        "logic": []
    },
    {
        "name": "QI44",
        "logic": [
            {
                "item_requirements": [
                    "canSurvivePoison1"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "CO12",
        "logic": [
            {
                "item_requirements": [
                    "canSurvivePoison1"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "RE07",
        "logic": [
            {
                "item_requirements": [
                    "wallClimb"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "RESCUED_CHERUB_19",
        "logic": [
            {
                "item_requirements": [
                    "wallClimb"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "canCrossGap11",
                    "taranto",
                    "obscureSkipsAllowed"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "QI10",
        "logic": [
            {
                "item_requirements": [
                    "blood"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "canCrossGap11"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "RESCUED_CHERUB_21",
        "logic": [
            {
                "item_requirements": [
                    "blood",
                    "doubleJump"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "blood",
                    "pillar"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "blood",
                    "cante"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "blood",
                    "verdiales"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "blood",
                    "tirana"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "blood",
                    "aubade",
                    "canAirStall"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "canCrossGap11",
                    "doubleJump"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "canCrossGap11",
                    "pillar"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "canCrossGap11",
                    "cante"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "canCrossGap11",
                    "verdiales"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "canCrossGap11",
                    "tirana"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "canCrossGap11",
                    "aubade",
                    "canAirStall"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "RESCUED_CHERUB_20",
        "logic": [
            {
                "item_requirements": [
                    "canClimbOnRoot"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "doubleJump"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "pillar"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "lorquiana"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "zarabanda"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "cante"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "aubade"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "tirana"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "QI13",
        "logic": [
            {
                "item_requirements": [
                    "ceremonyItems3"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "RB06",
        "logic": []
    },
    {
        "name": "Oil[D03Z03S13]",
        "logic": []
    },
    {
        "name": "BS04",
        "logic": [
            {
                "item_requirements": [
                    "canBeatGrievanceBoss"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "QI39",
        "logic": []
    },
    {
        "name": "CO23",
        "logic": []
    },
    {
        "name": "RESCUED_CHERUB_35",
        "logic": []
    },
    {
        "name": "RB14",
        "logic": [
            {
                "item_requirements": [
                    "canClimbOnRoot"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "canCrossGap3"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "QI37",
        "logic": []
    },
    {
        "name": "CO39",
        "logic": [
            {
                "item_requirements": [
                    "canClimbOnRoot"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "canCrossGap3"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "RESCUED_CHERUB_28",
        "logic": []
    },
    {
        "name": "RB21",
        "logic": [
            {
                "item_requirements": [
                    "redentoRooms4"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "Amanecida[D04Z01S04]",
        "logic": [
            {
                "item_requirements": [
                    "canBeatPatioBoss"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "QI102",
        "logic": []
    },
    {
        "name": "RE402",
        "logic": []
    },
    {
        "name": "RESCUED_CHERUB_30",
        "logic": []
    },
    {
        "name": "CO17",
        "logic": []
    },
    {
        "name": "CO34",
        "logic": []
    },
    {
        "name": "CO35",
        "logic": [
            {
                "item_requirements": [
                    "dash",
                    "blood"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "dash",
                    "canCrossGap3"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "RB33",
        "logic": []
    },
    {
        "name": "CO20",
        "logic": []
    },
    {
        "name": "RESCUED_CHERUB_29",
        "logic": []
    },
    {
        "name": "Sword[D04Z02S12]",
        "logic": []
    },
    {
        "name": "Oil[D04Z02S14]",
        "logic": []
    },
    {
        "name": "QI60",
        "logic": []
    },
    {
        "name": "HE01",
        "logic": [
            {
                "item_requirements": [
                    "wallClimb",
                    "blood"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "wallClimb",
                    "doubleJump"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "BS05",
        "logic": [
            {
                "item_requirements": [
                    "canBeatMothersBoss"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "RE03",
        "logic": []
    },
    {
        "name": "QI54",
        "logic": [
            {
                "item_requirements": [
                    "redentoRooms5"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "HE201",
        "logic": [
            {
                "item_requirements": [
                    "traitorEyes2"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "PR201",
        "logic": [
            {
                "item_requirements": [
                    "miriamRooms5",
                    "dash",
                    "wallClimb"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "CO18",
        "logic": []
    },
    {
        "name": "RESCUED_CHERUB_01",
        "logic": []
    },
    {
        "name": "QI50",
        "logic": [
            {
                "item_requirements": [
                    "canBreakHoles"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "CO22",
        "logic": []
    },
    {
        "name": "RB31",
        "logic": []
    },
    {
        "name": "PR07",
        "logic": [
            {
                "item_requirements": [
                    "blood"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "doubleJump"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "canEnemyBounce",
                    "canCrossGap2"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "RB203",
        "logic": []
    },
    {
        "name": "CO28",
        "logic": []
    },
    {
        "name": "RB30",
        "logic": []
    },
    {
        "name": "RESCUED_CHERUB_02",
        "logic": []
    },
    {
        "name": "Sword[D05Z01S13]",
        "logic": []
    },
    {
        "name": "Lady[D05Z01S14]",
        "logic": []
    },
    {
        "name": "QI62",
        "logic": []
    },
    {
        "name": "PR15",
        "logic": []
    },
    {
        "name": "Oil[D05Z01S19]",
        "logic": []
    },
    {
        "name": "RESCUED_CHERUB_32",
        "logic": [
            {
                "item_requirements": [
                    "blood",
                    "canWalkOnRoot"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "blood",
                    "doubleJump"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "blood",
                    "canCrossGap5",
                    "pillar"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "obscureSkipsAllowed",
                    "zarabanda"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "obscureSkipsAllowed",
                    "aubade"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "obscureSkipsAllowed",
                    "cantina"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "RB301",
        "logic": []
    },
    {
        "name": "QI64",
        "logic": []
    },
    {
        "name": "HE07",
        "logic": []
    },
    {
        "name": "RE05",
        "logic": [
            {
                "item_requirements": [
                    "cherubs20"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "PR05",
        "logic": [
            {
                "item_requirements": [
                    "cherubs38"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "CO31",
        "logic": []
    },
    {
        "name": "BS06",
        "logic": [
            {
                "item_requirements": [
                    "canBeatCanvasesBoss"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "QI104",
        "logic": [
            {
                "item_requirements": [
                    "dash"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "RB12",
        "logic": []
    },
    {
        "name": "QI49",
        "logic": []
    },
    {
        "name": "QI71",
        "logic": []
    },
    {
        "name": "QI02",
        "logic": [
            {
                "item_requirements": [
                    "canBeatLegionary"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "QI03",
        "logic": []
    },
    {
        "name": "QI04",
        "logic": [
            {
                "item_requirements": [
                    "canBeatLegionary"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "Sword[D06Z01S11]",
        "logic": []
    },
    {
        "name": "CO06",
        "logic": []
    },
    {
        "name": "PR12",
        "logic": []
    },
    {
        "name": "RESCUED_CHERUB_36",
        "logic": []
    },
    {
        "name": "CO40",
        "logic": [
            {
                "item_requirements": [
                    "wallClimb",
                    "canCrossGap10"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "wallClimb",
                    "canClimbOnRoot",
                    "blood"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "wallClimb",
                    "canClimbOnRoot",
                    "doubleJump",
                    "canAirStall"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "HE04",
        "logic": []
    },
    {
        "name": "Lady[D06Z01S24]",
        "logic": []
    },
    {
        "name": "BS16",
        "logic": [
            {
                "item_requirements": [
                    "canBeatRooftopsBoss"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "PR08",
        "logic": []
    },
    {
        "name": "BS12",
        "logic": [
            {
                "item_requirements": [
                    "holyWounds3",
                    "canBeatBridgeBoss"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "PR09",
        "logic": [
            {
                "item_requirements": [
                    "holyWounds3",
                    "canBeatBridgeBoss"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "HE101",
        "logic": []
    },
    {
        "name": "QI105",
        "logic": []
    },
    {
        "name": "LaudesBossTrigger[30000]",
        "logic": [
            {
                "item_requirements": [
                    "canBeatHallBoss"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "Amanecida[D09Z01S01]",
        "logic": [
            {
                "item_requirements": [
                    "canBeatWallBoss"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "QI51",
        "logic": []
    },
    {
        "name": "RB11",
        "logic": []
    },
    {
        "name": "BS14",
        "logic": [
            {
                "item_requirements": [
                    "canBeatPrisonBoss"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "RESCUED_CHERUB_05",
        "logic": []
    },
    {
        "name": "QI72",
        "logic": []
    },
    {
        "name": "RB16",
        "logic": []
    },
    {
        "name": "QI70",
        "logic": []
    },
    {
        "name": "CO27",
        "logic": []
    },
    {
        "name": "Oil[D09Z01S12]",
        "logic": []
    },
    {
        "name": "CO10",
        "logic": []
    },
    {
        "name": "QI69",
        "logic": []
    },
    {
        "name": "RESCUED_CHERUB_03",
        "logic": []
    },
    {
        "name": "CO24",
        "logic": []
    },
    {
        "name": "RESCUED_CHERUB_34",
        "logic": []
    },
    {
        "name": "CO26",
        "logic": []
    },
    {
        "name": "CO02",
        "logic": [
            {
                "item_requirements": [
                    "blood",
                    "canClimbOnRoot",
                    "canSurvivePoison2",
                    "dash"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "CO37",
        "logic": []
    },
    {
        "name": "RESCUED_CHERUB_04",
        "logic": [
            {
                "item_requirements": [
                    "canSurvivePoison1",
                    "dash"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "debla"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "taranto"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "cante"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "verdiales"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "aubade"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "cantina"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "RB204",
        "logic": []
    },
    {
        "name": "RESCUED_CHERUB_06",
        "logic": []
    },
    {
        "name": "RE401",
        "logic": [
            {
                "item_requirements": [
                    "redentoRooms2"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "Sword[D17Z01S08]",
        "logic": []
    },
    {
        "name": "BS13",
        "logic": [
            {
                "item_requirements": [
                    "canBeatBrotherhoodBoss"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "PR203",
        "logic": []
    },
    {
        "name": "QI204",
        "logic": [
            {
                "item_requirements": [
                    "canBeatBridgeBoss",
                    "holyWounds3"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "QI301",
        "logic": [
            {
                "item_requirements": [
                    "canBeatRooftopsBoss",
                    "trueHeart"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "RE01",
        "logic": []
    },
    {
        "name": "CO25",
        "logic": []
    },
    {
        "name": "RB108",
        "logic": []
    },
    {
        "name": "RB202",
        "logic": []
    },
    {
        "name": "RB201",
        "logic": []
    },
    {
        "name": "BossTrigger[5000]",
        "logic": [
            {
                "item_requirements": [
                    "canBeatMourningBoss"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "QI202",
        "logic": [
            {
                "item_requirements": [
                    "canBeatMourningBoss"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "PR202",
        "logic": []
    },
    {
        "name": "QI203",
        "logic": []
    },
    {
        "name": "QI106",
        "logic": []
    },
    {
        "name": "RB18",
        "logic": []
    },
    {
        "name": "RB19",
        "logic": [
            {
                "item_requirements": [
                    "redWax1",
                    "D02Z03S18[SE]"
                ],
                "location_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "redWax1",
                    "D02Z03S07[NW]"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "RB25",
        "logic": []
    },
    {
        "name": "RB26",
        "logic": []
    },
    {
        "name": "QI107",
        "logic": [
            {
                "item_requirements": [
                    "amanecidaRooms1"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "QI108",
        "logic": [
            {
                "item_requirements": [
                    "amanecidaRooms2"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "QI109",
        "logic": [
            {
                "item_requirements": [
                    "amanecidaRooms3"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "QI110",
        "logic": [
            {
                "item_requirements": [
                    "amanecidaRooms4"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "PR101",
        "logic": [
            {
                "item_requirements": [
                    "amanecidaRooms4"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "QI32",
        "logic": [
            {
                "item_requirements": [
                    "guiltBead",
                    "guiltRooms1"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "QI33",
        "logic": [
            {
                "item_requirements": [
                    "guiltBead",
                    "guiltRooms2"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "QI34",
        "logic": [
            {
                "item_requirements": [
                    "guiltBead",
                    "guiltRooms3"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "QI35",
        "logic": [
            {
                "item_requirements": [
                    "guiltBead",
                    "guiltRooms4"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "QI79",
        "logic": [
            {
                "item_requirements": [
                    "guiltBead",
                    "guiltRooms5"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "QI80",
        "logic": [
            {
                "item_requirements": [
                    "guiltBead",
                    "guiltRooms6"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "QI81",
        "logic": [
            {
                "item_requirements": [
                    "guiltBead",
                    "guiltRooms7"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "Arena_NailManager[1000]",
        "logic": [
            {
                "item_requirements": [
                    "guiltBead",
                    "guiltRooms1"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "HE10",
        "logic": [
            {
                "item_requirements": [
                    "guiltBead",
                    "guiltRooms2"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "Arena_NailManager[3000]",
        "logic": [
            {
                "item_requirements": [
                    "guiltBead",
                    "guiltRooms3"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "RB34",
        "logic": [
            {
                "item_requirements": [
                    "guiltBead",
                    "guiltRooms4"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "Arena_NailManager[5000]",
        "logic": [
            {
                "item_requirements": [
                    "guiltBead",
                    "guiltRooms5"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "RB35",
        "logic": [
            {
                "item_requirements": [
                    "guiltBead",
                    "guiltRooms6"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "RB36",
        "logic": [
            {
                "item_requirements": [
                    "guiltBead",
                    "guiltRooms7"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "COMBO_1",
        "logic": [
            {
                "item_requirements": [
                    "swordRooms1",
                    "tears0"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "COMBO_2",
        "logic": [
            {
                "item_requirements": [
                    "swordRooms2",
                    "tears0"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "COMBO_3",
        "logic": [
            {
                "item_requirements": [
                    "swordRooms4",
                    "tears0"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "CHARGED_1",
        "logic": [
            {
                "item_requirements": [
                    "swordRooms1",
                    "tears0"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "CHARGED_2",
        "logic": [
            {
                "item_requirements": [
                    "swordRooms3",
                    "tears0"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "CHARGED_3",
        "logic": [
            {
                "item_requirements": [
                    "swordRooms6",
                    "tears0"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "RANGED_1",
        "logic": [
            {
                "item_requirements": [
                    "swordRooms2",
                    "tears0"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "RANGED_2",
        "logic": [
            {
                "item_requirements": [
                    "swordRooms5",
                    "tears0"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "RANGED_3",
        "logic": [
            {
                "item_requirements": [
                    "swordRooms7",
                    "tears0"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "VERTICAL_1",
        "logic": [
            {
                "item_requirements": [
                    "swordRooms1",
                    "tears0"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "VERTICAL_2",
        "logic": [
            {
                "item_requirements": [
                    "swordRooms3",
                    "tears0"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "VERTICAL_3",
        "logic": [
            {
                "item_requirements": [
                    "swordRooms6",
                    "tears0"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "LUNGE_1",
        "logic": [
            {
                "item_requirements": [
                    "swordRooms1",
                    "tears0"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "LUNGE_2",
        "logic": [
            {
                "item_requirements": [
                    "swordRooms2",
                    "tears0"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    },
    {
        "name": "LUNGE_3",
        "logic": [
            {
                "item_requirements": [
                    "swordRooms4",
                    "tears0"
                ],
                "location_requirements": [],
                "state_modifiers": []
            }
        ]
    }
]
transitions = [
    {
        "name": "D01Z01S01[W]",
        "logic": []
    },
    {
        "name": "D01Z01S01[E]",
        "logic": []
    },
    {
        "name": "D01Z01S01[S]",
        "logic": []
    },
    {
        "name": "D01Z01S02[W]",
        "logic": []
    },
    {
        "name": "D01Z01S02[E]",
        "logic": []
    },
    {
        "name": "D01Z01S03[W]",
        "logic": []
    },
    {
        "name": "D01Z01S03[E]",
        "logic": []
    },
    {
        "name": "D01Z01S07[W]",
        "logic": []
    },
    {
        "name": "D01Z01S07[E]",
        "logic": []
    },
    {
        "name": "D01Z02S01[W]",
        "logic": []
    },
    {
        "name": "D01Z02S01[E]",
        "logic": []
    },
    {
        "name": "D01Z02S02[SW]",
        "logic": []
    },
    {
        "name": "D01Z02S02[SE]",
        "logic": []
    },
    {
        "name": "D01Z02S02[W]",
        "logic": []
    },
    {
        "name": "D01Z02S02[E]",
        "logic": []
    },
    {
        "name": "D01Z02S02[NE]",
        "logic": []
    },
    {
        "name": "D01Z02S03[W]",
        "logic": []
    },
    {
        "name": "D01Z02S03[NW]",
        "logic": []
    },
    {
        "name": "D01Z02S03[E]",
        "logic": []
    },
    {
        "name": "D01Z02S03[church]",
        "logic": []
    },
    {
        "name": "D01Z02S04[W]",
        "logic": []
    },
    {
        "name": "D01Z02S04[E]",
        "logic": []
    },
    {
        "name": "D01Z02S04[Ossary]",
        "logic": []
    },
    {
        "name": "D01Z02S05[W]",
        "logic": []
    },
    {
        "name": "D01Z02S05[E]",
        "logic": []
    },
    {
        "name": "D01Z02S06[W]",
        "logic": []
    },
    {
        "name": "D01Z02S06[E]",
        "logic": []
    },
    {
        "name": "D01Z02S07[E]",
        "logic": []
    },
    {
        "name": "D01BZ04S01[church]",
        "logic": []
    },
    {
        "name": "D01BZ06S01[Ossary]",
        "logic": []
    },
    {
        "name": "D01BZ06S01[E]",
        "logic": []
    },
    {
        "name": "D01BZ08S01[W]",
        "logic": []
    },
    {
        "name": "D01Z03S01[W]",
        "logic": []
    },
    {
        "name": "D01Z03S01[E]",
        "logic": []
    },
    {
        "name": "D01Z03S01[SE]",
        "logic": []
    },
    {
        "name": "D01Z03S02[W]",
        "logic": []
    },
    {
        "name": "D01Z03S02[SW]",
        "logic": []
    },
    {
        "name": "D01Z03S02[E]",
        "logic": []
    },
    {
        "name": "D01Z03S02[S]",
        "logic": []
    },
    {
        "name": "D01Z03S03[W]",
        "logic": []
    },
    {
        "name": "D01Z03S03[E]",
        "logic": []
    },
    {
        "name": "D01Z03S03[-Cherubs]",
        "logic": []
    },
    {
        "name": "D01Z03S04[SW]",
        "logic": []
    },
    {
        "name": "D01Z03S04[W]",
        "logic": []
    },
    {
        "name": "D01Z03S04[NW]",
        "logic": []
    },
    {
        "name": "D01Z03S04[SE]",
        "logic": []
    },
    {
        "name": "D01Z03S04[E]",
        "logic": []
    },
    {
        "name": "D01Z03S05[W]",
        "logic": []
    },
    {
        "name": "D01Z03S05[E]",
        "logic": []
    },
    {
        "name": "D01Z03S05[Cherubs]",
        "logic": []
    },
    {
        "name": "D01Z03S06[W]",
        "logic": []
    },
    {
        "name": "D01Z03S06[E]",
        "logic": []
    },
    {
        "name": "D01Z03S07[E]",
        "logic": []
    },
    {
        "name": "D01Z03S07[-Cherubs]",
        "logic": []
    },
    {
        "name": "D01Z04S01[NW]",
        "logic": []
    },
    {
        "name": "D01Z04S01[NE]",
        "logic": []
    },
    {
        "name": "D01Z04S01[W]",
        "logic": []
    },
    {
        "name": "D01Z04S01[E]",
        "logic": []
    },
    {
        "name": "D01Z04S01[SE]",
        "logic": []
    },
    {
        "name": "D01Z04S01[S]",
        "logic": []
    },
    {
        "name": "D01Z04S02[W]",
        "logic": []
    },
    {
        "name": "D01Z04S03[E]",
        "logic": []
    },
    {
        "name": "D01Z04S05[NW]",
        "logic": []
    },
    {
        "name": "D01Z04S05[SW]",
        "logic": []
    },
    {
        "name": "D01Z04S06[E]",
        "logic": []
    },
    {
        "name": "D01Z04S06[NW]",
        "logic": []
    },
    {
        "name": "D01Z04S06[SW]",
        "logic": []
    },
    {
        "name": "D01Z04S07[W]",
        "logic": []
    },
    {
        "name": "D01Z04S08[E]",
        "logic": []
    },
    {
        "name": "D01Z04S09[W]",
        "logic": []
    },
    {
        "name": "D01Z04S09[E]",
        "logic": []
    },
    {
        "name": "D01Z04S09[C]",
        "logic": []
    },
    {
        "name": "D01Z04S10[NW]",
        "logic": []
    },
    {
        "name": "D01Z04S10[SW]",
        "logic": []
    },
    {
        "name": "D01Z04S10[SE]",
        "logic": []
    },
    {
        "name": "D01Z04S11[NE]",
        "logic": []
    },
    {
        "name": "D01Z04S12[NW]",
        "logic": []
    },
    {
        "name": "D01Z04S12[W]",
        "logic": []
    },
    {
        "name": "D01Z04S12[SE]",
        "logic": []
    },
    {
        "name": "D01Z04S13[NW]",
        "logic": []
    },
    {
        "name": "D01Z04S13[NE]",
        "logic": []
    },
    {
        "name": "D01Z04S13[SW]",
        "logic": []
    },
    {
        "name": "D01Z04S13[SE]",
        "logic": []
    },
    {
        "name": "D01Z04S14[E]",
        "logic": []
    },
    {
        "name": "D01Z04S15[N]",
        "logic": []
    },
    {
        "name": "D01Z04S15[NE]",
        "logic": []
    },
    {
        "name": "D01Z04S15[W]",
        "logic": []
    },
    {
        "name": "D01Z04S15[E]",
        "logic": []
    },
    {
        "name": "D01Z04S15[SW]",
        "logic": []
    },
    {
        "name": "D01Z04S15[SE]",
        "logic": []
    },
    {
        "name": "D01Z04S16[W]",
        "logic": []
    },
    {
        "name": "D01Z04S16[E]",
        "logic": []
    },
    {
        "name": "D01Z04S17[W]",
        "logic": []
    },
    {
        "name": "D01Z04S18[W]",
        "logic": []
    },
    {
        "name": "D01Z04S18[E]",
        "logic": []
    },
    {
        "name": "D01Z04S19[W]",
        "logic": []
    },
    {
        "name": "D01Z04S19[E]",
        "logic": []
    },
    {
        "name": "D01BZ02S01[C]",
        "logic": []
    },
    {
        "name": "D01Z05S01[N]",
        "logic": []
    },
    {
        "name": "D01Z05S01[W]",
        "logic": []
    },
    {
        "name": "D01Z05S01[S]",
        "logic": []
    },
    {
        "name": "D01Z05S02[N]",
        "logic": []
    },
    {
        "name": "D01Z05S02[W]",
        "logic": []
    },
    {
        "name": "D01Z05S02[E]",
        "logic": []
    },
    {
        "name": "D01Z05S02[S]",
        "logic": []
    },
    {
        "name": "D01Z05S03[NW]",
        "logic": []
    },
    {
        "name": "D01Z05S03[NE]",
        "logic": []
    },
    {
        "name": "D01Z05S03[W]",
        "logic": []
    },
    {
        "name": "D01Z05S03[E]",
        "logic": []
    },
    {
        "name": "D01Z05S03[S]",
        "logic": []
    },
    {
        "name": "D01Z05S04[W]",
        "logic": []
    },
    {
        "name": "D01Z05S04[E]",
        "logic": []
    },
    {
        "name": "D01Z05S05[N]",
        "logic": []
    },
    {
        "name": "D01Z05S05[NW]",
        "logic": []
    },
    {
        "name": "D01Z05S05[NE]",
        "logic": []
    },
    {
        "name": "D01Z05S05[SW]",
        "logic": []
    },
    {
        "name": "D01Z05S05[E]",
        "logic": []
    },
    {
        "name": "D01Z05S06[W]",
        "logic": []
    },
    {
        "name": "D01Z05S07[E]",
        "logic": []
    },
    {
        "name": "D01Z05S08[W]",
        "logic": []
    },
    {
        "name": "D01Z05S09[NW]",
        "logic": []
    },
    {
        "name": "D01Z05S09[SE]",
        "logic": []
    },
    {
        "name": "D01Z05S10[W]",
        "logic": []
    },
    {
        "name": "D01Z05S10[NE]",
        "logic": []
    },
    {
        "name": "D01Z05S10[SE]",
        "logic": []
    },
    {
        "name": "D01Z05S10[S]",
        "logic": []
    },
    {
        "name": "D01Z05S11[W]",
        "logic": []
    },
    {
        "name": "D01Z05S12[W]",
        "logic": []
    },
    {
        "name": "D01Z05S12[E]",
        "logic": []
    },
    {
        "name": "D01Z05S13[SW]",
        "logic": []
    },
    {
        "name": "D01Z05S13[N]",
        "logic": []
    },
    {
        "name": "D01Z05S13[E]",
        "logic": []
    },
    {
        "name": "D01Z05S14[W]",
        "logic": []
    },
    {
        "name": "D01Z05S14[N]",
        "logic": []
    },
    {
        "name": "D01Z05S14[SE]",
        "logic": []
    },
    {
        "name": "D01Z05S15[W]",
        "logic": []
    },
    {
        "name": "D01Z05S15[SW]",
        "logic": []
    },
    {
        "name": "D01Z05S15[SE]",
        "logic": []
    },
    {
        "name": "D01Z05S16[N]",
        "logic": []
    },
    {
        "name": "D01Z05S16[SW]",
        "logic": []
    },
    {
        "name": "D01Z05S16[SE]",
        "logic": []
    },
    {
        "name": "D01Z05S17[W]",
        "logic": []
    },
    {
        "name": "D01Z05S17[E]",
        "logic": []
    },
    {
        "name": "D01Z05S18[E]",
        "logic": []
    },
    {
        "name": "D01Z05S19[W]",
        "logic": []
    },
    {
        "name": "D01Z05S19[E]",
        "logic": []
    },
    {
        "name": "D01Z05S20[W]",
        "logic": []
    },
    {
        "name": "D01Z05S20[N]",
        "logic": []
    },
    {
        "name": "D01Z05S21[W]",
        "logic": []
    },
    {
        "name": "D01Z05S21[E]",
        "logic": []
    },
    {
        "name": "D01Z05S21[Reward]",
        "logic": []
    },
    {
        "name": "D01Z05S22[E]",
        "logic": []
    },
    {
        "name": "D01Z05S23[W]",
        "logic": []
    },
    {
        "name": "D01Z05S23[E]",
        "logic": []
    },
    {
        "name": "D01Z05S24[W]",
        "logic": []
    },
    {
        "name": "D01Z05S24[E]",
        "logic": []
    },
    {
        "name": "D01Z05S25[NE]",
        "logic": []
    },
    {
        "name": "D01Z05S25[W]",
        "logic": []
    },
    {
        "name": "D01Z05S25[E]",
        "logic": []
    },
    {
        "name": "D01Z05S25[SW]",
        "logic": []
    },
    {
        "name": "D01Z05S25[SE]",
        "logic": []
    },
    {
        "name": "D01Z05S25[EchoesW]",
        "logic": []
    },
    {
        "name": "D01Z05S25[EchoesE]",
        "logic": []
    },
    {
        "name": "D01Z05S26[W]",
        "logic": []
    },
    {
        "name": "D01Z05S27[E]",
        "logic": []
    },
    {
        "name": "D01BZ05S01[Reward]",
        "logic": []
    },
    {
        "name": "D01BZ09S01[W]",
        "logic": []
    },
    {
        "name": "D01Z06S01[N]",
        "logic": []
    },
    {
        "name": "D01Z06S01[Santos]",
        "logic": []
    },
    {
        "name": "D01BZ07S01[Santos]",
        "logic": []
    },
    {
        "name": "D02Z01S01[SW]",
        "logic": []
    },
    {
        "name": "D02Z01S01[W]",
        "logic": []
    },
    {
        "name": "D02Z01S01[SE]",
        "logic": []
    },
    {
        "name": "D02Z01S02[W]",
        "logic": []
    },
    {
        "name": "D02Z01S02[NW]",
        "logic": []
    },
    {
        "name": "D02Z01S02[E]",
        "logic": []
    },
    {
        "name": "D02Z01S02[NE]",
        "logic": []
    },
    {
        "name": "D02Z01S02[]",
        "logic": []
    },
    {
        "name": "D02Z01S03[SW]",
        "logic": []
    },
    {
        "name": "D02Z01S03[W]",
        "logic": []
    },
    {
        "name": "D02Z01S03[SE]",
        "logic": []
    },
    {
        "name": "D02Z01S04[E]",
        "logic": []
    },
    {
        "name": "D02Z01S04[-N]",
        "logic": []
    },
    {
        "name": "D02Z01S05[E]",
        "logic": []
    },
    {
        "name": "D02Z01S06[W]",
        "logic": []
    },
    {
        "name": "D02Z01S06[E]",
        "logic": []
    },
    {
        "name": "D02Z01S08[E]",
        "logic": []
    },
    {
        "name": "D02Z01S09[W]",
        "logic": []
    },
    {
        "name": "D02Z01S09[-CherubsL]",
        "logic": []
    },
    {
        "name": "D02Z01S09[-CherubsR]",
        "logic": []
    },
    {
        "name": "D02Z02S01[W]",
        "logic": []
    },
    {
        "name": "D02Z02S01[NW]",
        "logic": []
    },
    {
        "name": "D02Z02S01[E]",
        "logic": []
    },
    {
        "name": "D02Z02S02[SE]",
        "logic": []
    },
    {
        "name": "D02Z02S02[NW]",
        "logic": []
    },
    {
        "name": "D02Z02S02[NE]",
        "logic": []
    },
    {
        "name": "D02Z02S02[-CherubsR]",
        "logic": []
    },
    {
        "name": "D02Z02S03[SW]",
        "logic": []
    },
    {
        "name": "D02Z02S03[NW]",
        "logic": []
    },
    {
        "name": "D02Z02S03[NE]",
        "logic": []
    },
    {
        "name": "D02Z02S03[-Cherubs]",
        "logic": []
    },
    {
        "name": "D02Z02S04[W]",
        "logic": []
    },
    {
        "name": "D02Z02S04[SE]",
        "logic": []
    },
    {
        "name": "D02Z02S04[E]",
        "logic": []
    },
    {
        "name": "D02Z02S04[NE]",
        "logic": []
    },
    {
        "name": "D02Z02S04[-CherubsL]",
        "logic": []
    },
    {
        "name": "D02Z02S05[SW]",
        "logic": []
    },
    {
        "name": "D02Z02S05[W]",
        "logic": []
    },
    {
        "name": "D02Z02S05[SE]",
        "logic": []
    },
    {
        "name": "D02Z02S05[E]",
        "logic": []
    },
    {
        "name": "D02Z02S05[NW]",
        "logic": []
    },
    {
        "name": "D02Z02S05[-CherubsL]",
        "logic": []
    },
    {
        "name": "D02Z02S05[-CherubsR]",
        "logic": []
    },
    {
        "name": "D02Z02S06[E]",
        "logic": []
    },
    {
        "name": "D02Z02S07[W]",
        "logic": []
    },
    {
        "name": "D02Z02S07[E]",
        "logic": []
    },
    {
        "name": "D02Z02S08[W]",
        "logic": []
    },
    {
        "name": "D02Z02S08[E]",
        "logic": []
    },
    {
        "name": "D02Z02S08[C]",
        "logic": []
    },
    {
        "name": "D02Z02S09[E]",
        "logic": []
    },
    {
        "name": "D02Z02S10[W]",
        "logic": []
    },
    {
        "name": "D02Z02S11[W]",
        "logic": []
    },
    {
        "name": "D02Z02S11[SE]",
        "logic": []
    },
    {
        "name": "D02Z02S11[E]",
        "logic": []
    },
    {
        "name": "D02Z02S11[NW]",
        "logic": []
    },
    {
        "name": "D02Z02S11[NE]",
        "logic": []
    },
    {
        "name": "D02Z02S11[-Cherubs]",
        "logic": []
    },
    {
        "name": "D02Z02S12[W]",
        "logic": []
    },
    {
        "name": "D02Z02S13[W]",
        "logic": []
    },
    {
        "name": "D02Z02S14[W]",
        "logic": []
    },
    {
        "name": "D02Z02S14[-Cherubs]",
        "logic": []
    },
    {
        "name": "D02BZ02S01[C]",
        "logic": []
    },
    {
        "name": "D02Z03S01[W]",
        "logic": []
    },
    {
        "name": "D02Z03S01[E]",
        "logic": []
    },
    {
        "name": "D02Z03S02[S]",
        "logic": []
    },
    {
        "name": "D02Z03S02[W]",
        "logic": []
    },
    {
        "name": "D02Z03S02[NW]",
        "logic": []
    },
    {
        "name": "D02Z03S02[NE]",
        "logic": []
    },
    {
        "name": "D02Z03S02[N]",
        "logic": []
    },
    {
        "name": "D02Z03S03[W]",
        "logic": []
    },
    {
        "name": "D02Z03S03[NW]",
        "logic": []
    },
    {
        "name": "D02Z03S03[E]",
        "logic": []
    },
    {
        "name": "D02Z03S05[S]",
        "logic": []
    },
    {
        "name": "D02Z03S05[E]",
        "logic": []
    },
    {
        "name": "D02Z03S05[NE]",
        "logic": []
    },
    {
        "name": "D02Z03S06[W]",
        "logic": []
    },
    {
        "name": "D02Z03S06[S]",
        "logic": []
    },
    {
        "name": "D02Z03S07[W]",
        "logic": []
    },
    {
        "name": "D02Z03S07[NWW]",
        "logic": []
    },
    {
        "name": "D02Z03S07[NW]",
        "logic": []
    },
    {
        "name": "D02Z03S07[N]",
        "logic": []
    },
    {
        "name": "D02Z03S07[E]",
        "logic": []
    },
    {
        "name": "D02Z03S08[SW]",
        "logic": []
    },
    {
        "name": "D02Z03S08[W]",
        "logic": []
    },
    {
        "name": "D02Z03S08[SE]",
        "logic": []
    },
    {
        "name": "D02Z03S08[E]",
        "logic": []
    },
    {
        "name": "D02Z03S08[NE]",
        "logic": []
    },
    {
        "name": "D02Z03S09[W]",
        "logic": []
    },
    {
        "name": "D02Z03S09[E]",
        "logic": []
    },
    {
        "name": "D02Z03S10[W]",
        "logic": []
    },
    {
        "name": "D02Z03S10[-W]",
        "logic": []
    },
    {
        "name": "D02Z03S10[-Cherubs]",
        "logic": []
    },
    {
        "name": "D02Z03S11[S]",
        "logic": []
    },
    {
        "name": "D02Z03S11[W]",
        "logic": []
    },
    {
        "name": "D02Z03S11[NW]",
        "logic": []
    },
    {
        "name": "D02Z03S11[E]",
        "logic": []
    },
    {
        "name": "D02Z03S11[NE]",
        "logic": []
    },
    {
        "name": "D02Z03S12[E]",
        "logic": []
    },
    {
        "name": "D02Z03S13[W]",
        "logic": []
    },
    {
        "name": "D02Z03S14[W]",
        "logic": []
    },
    {
        "name": "D02Z03S14[E]",
        "logic": []
    },
    {
        "name": "D02Z03S15[E]",
        "logic": []
    },
    {
        "name": "D02Z03S16[W]",
        "logic": []
    },
    {
        "name": "D02Z03S16[N]",
        "logic": []
    },
    {
        "name": "D02Z03S17[E]",
        "logic": []
    },
    {
        "name": "D02Z03S18[NW]",
        "logic": []
    },
    {
        "name": "D02Z03S18[SE]",
        "logic": []
    },
    {
        "name": "D02Z03S18[NE]",
        "logic": []
    },
    {
        "name": "D02Z03S19[E]",
        "logic": []
    },
    {
        "name": "D02Z03S20[W]",
        "logic": []
    },
    {
        "name": "D02Z03S20[E]",
        "logic": []
    },
    {
        "name": "D02Z03S21[W]",
        "logic": []
    },
    {
        "name": "D02Z03S21[E]",
        "logic": []
    },
    {
        "name": "D02Z03S22[W]",
        "logic": []
    },
    {
        "name": "D02Z03S23[E]",
        "logic": []
    },
    {
        "name": "D02Z03S24[E]",
        "logic": []
    },
    {
        "name": "D03Z01S01[W]",
        "logic": []
    },
    {
        "name": "D03Z01S01[NE]",
        "logic": []
    },
    {
        "name": "D03Z01S01[S]",
        "logic": []
    },
    {
        "name": "D03Z01S01[-Cherubs]",
        "logic": []
    },
    {
        "name": "D03Z01S02[W]",
        "logic": []
    },
    {
        "name": "D03Z01S02[E]",
        "logic": []
    },
    {
        "name": "D03Z01S03[W]",
        "logic": []
    },
    {
        "name": "D03Z01S03[E]",
        "logic": []
    },
    {
        "name": "D03Z01S03[SW]",
        "logic": []
    },
    {
        "name": "D03Z01S03[SE]",
        "logic": []
    },
    {
        "name": "D03Z01S03[-WestL]",
        "logic": []
    },
    {
        "name": "D03Z01S03[-WestR]",
        "logic": []
    },
    {
        "name": "D03Z01S03[-EastL]",
        "logic": []
    },
    {
        "name": "D03Z01S03[-EastR]",
        "logic": []
    },
    {
        "name": "D03Z01S04[NW]",
        "logic": []
    },
    {
        "name": "D03Z01S04[E]",
        "logic": []
    },
    {
        "name": "D03Z01S05[W]",
        "logic": []
    },
    {
        "name": "D03Z01S05[E]",
        "logic": []
    },
    {
        "name": "D03Z01S06[W]",
        "logic": []
    },
    {
        "name": "D03Z01S06[E]",
        "logic": []
    },
    {
        "name": "D03Z02S01[W]",
        "logic": []
    },
    {
        "name": "D03Z02S01[N]",
        "logic": []
    },
    {
        "name": "D03Z02S02[W]",
        "logic": []
    },
    {
        "name": "D03Z02S02[E]",
        "logic": []
    },
    {
        "name": "D03Z02S02[S]",
        "logic": []
    },
    {
        "name": "D03Z02S03[W]",
        "logic": []
    },
    {
        "name": "D03Z02S03[E]",
        "logic": []
    },
    {
        "name": "D03Z02S03[N]",
        "logic": []
    },
    {
        "name": "D03Z02S03[SE2]",
        "logic": []
    },
    {
        "name": "D03Z02S03[SW]",
        "logic": []
    },
    {
        "name": "D03Z02S03[SE]",
        "logic": []
    },
    {
        "name": "D03Z02S03[SSL]",
        "logic": []
    },
    {
        "name": "D03Z02S03[SSC]",
        "logic": []
    },
    {
        "name": "D03Z02S03[SSR]",
        "logic": []
    },
    {
        "name": "D03Z02S04[NW]",
        "logic": []
    },
    {
        "name": "D03Z02S04[NE]",
        "logic": []
    },
    {
        "name": "D03Z02S04[S]",
        "logic": []
    },
    {
        "name": "D03Z02S05[W]",
        "logic": []
    },
    {
        "name": "D03Z02S05[E]",
        "logic": []
    },
    {
        "name": "D03Z02S05[S]",
        "logic": []
    },
    {
        "name": "D03Z02S06[W]",
        "logic": []
    },
    {
        "name": "D03Z02S06[N]",
        "logic": []
    },
    {
        "name": "D03Z02S07[W]",
        "logic": []
    },
    {
        "name": "D03Z02S07[E]",
        "logic": []
    },
    {
        "name": "D03Z02S07[N]",
        "logic": []
    },
    {
        "name": "D03Z02S08[W]",
        "logic": []
    },
    {
        "name": "D03Z02S08[E]",
        "logic": []
    },
    {
        "name": "D03Z02S08[N]",
        "logic": []
    },
    {
        "name": "D03Z02S09[W]",
        "logic": []
    },
    {
        "name": "D03Z02S09[N]",
        "logic": []
    },
    {
        "name": "D03Z02S09[S]",
        "logic": []
    },
    {
        "name": "D03Z02S10[W]",
        "logic": []
    },
    {
        "name": "D03Z02S10[N]",
        "logic": []
    },
    {
        "name": "D03Z02S10[S]",
        "logic": []
    },
    {
        "name": "D03Z02S10[E]",
        "logic": []
    },
    {
        "name": "D03Z02S10[-Cherubs]",
        "logic": []
    },
    {
        "name": "D03Z02S11[W]",
        "logic": []
    },
    {
        "name": "D03Z02S11[E]",
        "logic": []
    },
    {
        "name": "D03Z02S12[E]",
        "logic": []
    },
    {
        "name": "D03Z02S13[E]",
        "logic": []
    },
    {
        "name": "D03Z02S13[-Cherubs]",
        "logic": []
    },
    {
        "name": "D03Z02S14[E]",
        "logic": []
    },
    {
        "name": "D03Z02S15[W]",
        "logic": []
    },
    {
        "name": "D03Z02S15[E]",
        "logic": []
    },
    {
        "name": "D03Z03S01[W]",
        "logic": []
    },
    {
        "name": "D03Z03S01[S]",
        "logic": []
    },
    {
        "name": "D03Z03S01[NL]",
        "logic": []
    },
    {
        "name": "D03Z03S01[NR]",
        "logic": []
    },
    {
        "name": "D03Z03S02[W]",
        "logic": []
    },
    {
        "name": "D03Z03S02[NE]",
        "logic": []
    },
    {
        "name": "D03Z03S02[E]",
        "logic": []
    },
    {
        "name": "D03Z03S03[W]",
        "logic": []
    },
    {
        "name": "D03Z03S03[NE]",
        "logic": []
    },
    {
        "name": "D03Z03S03[SE]",
        "logic": []
    },
    {
        "name": "D03Z03S04[NW]",
        "logic": []
    },
    {
        "name": "D03Z03S04[NE]",
        "logic": []
    },
    {
        "name": "D03Z03S04[E]",
        "logic": []
    },
    {
        "name": "D03Z03S04[SW]",
        "logic": []
    },
    {
        "name": "D03Z03S04[SE]",
        "logic": []
    },
    {
        "name": "D03Z03S04[-Cherubs]",
        "logic": []
    },
    {
        "name": "D03Z03S05[NW]",
        "logic": []
    },
    {
        "name": "D03Z03S05[NE]",
        "logic": []
    },
    {
        "name": "D03Z03S05[SW]",
        "logic": []
    },
    {
        "name": "D03Z03S05[SE]",
        "logic": []
    },
    {
        "name": "D03Z03S06[W]",
        "logic": []
    },
    {
        "name": "D03Z03S07[NW]",
        "logic": []
    },
    {
        "name": "D03Z03S07[NE]",
        "logic": []
    },
    {
        "name": "D03Z03S07[SW]",
        "logic": []
    },
    {
        "name": "D03Z03S07[E]",
        "logic": []
    },
    {
        "name": "D03Z03S07[S]",
        "logic": []
    },
    {
        "name": "D03Z03S08[W]",
        "logic": []
    },
    {
        "name": "D03Z03S08[-CherubsL]",
        "logic": []
    },
    {
        "name": "D03Z03S08[-CherubsR]",
        "logic": []
    },
    {
        "name": "D03Z03S09[SW]",
        "logic": []
    },
    {
        "name": "D03Z03S09[N]",
        "logic": []
    },
    {
        "name": "D03Z03S10[E]",
        "logic": []
    },
    {
        "name": "D03Z03S11[W]",
        "logic": []
    },
    {
        "name": "D03Z03S11[E]",
        "logic": []
    },
    {
        "name": "D03Z03S12[W]",
        "logic": []
    },
    {
        "name": "D03Z03S12[E]",
        "logic": []
    },
    {
        "name": "D03Z03S13[W]",
        "logic": []
    },
    {
        "name": "D03Z03S14[W]",
        "logic": []
    },
    {
        "name": "D03Z03S15[W]",
        "logic": []
    },
    {
        "name": "D03Z03S15[E]",
        "logic": []
    },
    {
        "name": "D03Z03S16[W]",
        "logic": []
    },
    {
        "name": "D03Z03S16[E]",
        "logic": []
    },
    {
        "name": "D03Z03S17[W]",
        "logic": []
    },
    {
        "name": "D03Z03S17[E]",
        "logic": []
    },
    {
        "name": "D03Z03S18[E]",
        "logic": []
    },
    {
        "name": "D03Z03S19[E]",
        "logic": []
    },
    {
        "name": "D04Z01S01[W]",
        "logic": []
    },
    {
        "name": "D04Z01S01[E]",
        "logic": []
    },
    {
        "name": "D04Z01S01[NE]",
        "logic": []
    },
    {
        "name": "D04Z01S01[N]",
        "logic": []
    },
    {
        "name": "D04Z01S02[W]",
        "logic": []
    },
    {
        "name": "D04Z01S02[NW]",
        "logic": []
    },
    {
        "name": "D04Z01S02[E]",
        "logic": []
    },
    {
        "name": "D04Z01S03[W]",
        "logic": []
    },
    {
        "name": "D04Z01S03[E]",
        "logic": []
    },
    {
        "name": "D04Z01S03[S]",
        "logic": []
    },
    {
        "name": "D04Z01S04[W]",
        "logic": []
    },
    {
        "name": "D04Z01S04[E]",
        "logic": []
    },
    {
        "name": "D04Z01S05[S]",
        "logic": []
    },
    {
        "name": "D04Z01S05[N]",
        "logic": []
    },
    {
        "name": "D04Z01S05[-Cherubs]",
        "logic": []
    },
    {
        "name": "D04Z01S06[S]",
        "logic": []
    },
    {
        "name": "D04Z01S06[E]",
        "logic": []
    },
    {
        "name": "D04Z01S06[Cherubs]",
        "logic": []
    },
    {
        "name": "D04Z02S01[W]",
        "logic": []
    },
    {
        "name": "D04Z02S01[N]",
        "logic": []
    },
    {
        "name": "D04Z02S01[E]",
        "logic": []
    },
    {
        "name": "D04Z02S01[NE]",
        "logic": []
    },
    {
        "name": "D04Z02S02[S]",
        "logic": []
    },
    {
        "name": "D04Z02S02[SE]",
        "logic": []
    },
    {
        "name": "D04Z02S02[NE]",
        "logic": []
    },
    {
        "name": "D04Z02S02[N]",
        "logic": []
    },
    {
        "name": "D04Z02S03[W]",
        "logic": []
    },
    {
        "name": "D04Z02S03[E]",
        "logic": []
    },
    {
        "name": "D04Z02S04[SW]",
        "logic": []
    },
    {
        "name": "D04Z02S04[SE]",
        "logic": []
    },
    {
        "name": "D04Z02S04[W]",
        "logic": []
    },
    {
        "name": "D04Z02S04[E]",
        "logic": []
    },
    {
        "name": "D04Z02S04[NW]",
        "logic": []
    },
    {
        "name": "D04Z02S04[NE]",
        "logic": []
    },
    {
        "name": "D04Z02S04[N]",
        "logic": []
    },
    {
        "name": "D04Z02S05[W]",
        "logic": []
    },
    {
        "name": "D04Z02S05[E]",
        "logic": []
    },
    {
        "name": "D04Z02S06[S]",
        "logic": []
    },
    {
        "name": "D04Z02S06[NW]",
        "logic": []
    },
    {
        "name": "D04Z02S06[N]",
        "logic": []
    },
    {
        "name": "D04Z02S06[NE]",
        "logic": []
    },
    {
        "name": "D04Z02S06[E]",
        "logic": []
    },
    {
        "name": "D04Z02S06[-Cherubs]",
        "logic": []
    },
    {
        "name": "D04Z02S07[SW]",
        "logic": []
    },
    {
        "name": "D04Z02S07[W]",
        "logic": []
    },
    {
        "name": "D04Z02S07[N]",
        "logic": []
    },
    {
        "name": "D04Z02S07[NE]",
        "logic": []
    },
    {
        "name": "D04Z02S07[SE]",
        "logic": []
    },
    {
        "name": "D04Z02S08[W]",
        "logic": []
    },
    {
        "name": "D04Z02S08[E]",
        "logic": []
    },
    {
        "name": "D04Z02S08[S]",
        "logic": []
    },
    {
        "name": "D04Z02S09[W]",
        "logic": []
    },
    {
        "name": "D04Z02S09[E]",
        "logic": []
    },
    {
        "name": "D04Z02S09[NE]",
        "logic": []
    },
    {
        "name": "D04Z02S10[W]",
        "logic": []
    },
    {
        "name": "D04Z02S11[W]",
        "logic": []
    },
    {
        "name": "D04Z02S11[E]",
        "logic": []
    },
    {
        "name": "D04Z02S12[W]",
        "logic": []
    },
    {
        "name": "D04Z02S13[W]",
        "logic": []
    },
    {
        "name": "D04Z02S14[E]",
        "logic": []
    },
    {
        "name": "D04Z02S15[W]",
        "logic": []
    },
    {
        "name": "D04Z02S15[E]",
        "logic": []
    },
    {
        "name": "D04Z02S16[W]",
        "logic": []
    },
    {
        "name": "D04Z02S16[-Cherubs]",
        "logic": []
    },
    {
        "name": "D04Z02S17[W]",
        "logic": []
    },
    {
        "name": "D04Z02S19[W]",
        "logic": []
    },
    {
        "name": "D04Z02S19[E]",
        "logic": []
    },
    {
        "name": "D04Z02S20[W]",
        "logic": []
    },
    {
        "name": "D04Z02S20[Redento]",
        "logic": []
    },
    {
        "name": "D04Z02S21[W]",
        "logic": []
    },
    {
        "name": "D04Z02S21[SE]",
        "logic": []
    },
    {
        "name": "D04Z02S21[NE]",
        "logic": []
    },
    {
        "name": "D04Z02S22[W]",
        "logic": []
    },
    {
        "name": "D04Z02S22[E]",
        "logic": []
    },
    {
        "name": "D04Z02S23[W]",
        "logic": []
    },
    {
        "name": "D04Z02S23[SE]",
        "logic": []
    },
    {
        "name": "D04Z02S23[NE]",
        "logic": []
    },
    {
        "name": "D04Z02S24[NW]",
        "logic": []
    },
    {
        "name": "D04Z02S24[SW]",
        "logic": []
    },
    {
        "name": "D04Z02S24[SE]",
        "logic": []
    },
    {
        "name": "D04Z02S25[W]",
        "logic": []
    },
    {
        "name": "D04BZ02S01[Redento]",
        "logic": []
    },
    {
        "name": "D04Z03S01[W]",
        "logic": []
    },
    {
        "name": "D04Z03S01[E]",
        "logic": []
    },
    {
        "name": "D04Z03S02[W]",
        "logic": []
    },
    {
        "name": "D04Z04S01[W]",
        "logic": []
    },
    {
        "name": "D04Z04S01[E]",
        "logic": []
    },
    {
        "name": "D04Z04S02[W]",
        "logic": []
    },
    {
        "name": "D05Z01S01[W]",
        "logic": []
    },
    {
        "name": "D05Z01S01[NW]",
        "logic": []
    },
    {
        "name": "D05Z01S01[E]",
        "logic": []
    },
    {
        "name": "D05Z01S02[W]",
        "logic": []
    },
    {
        "name": "D05Z01S02[NW]",
        "logic": []
    },
    {
        "name": "D05Z01S02[E]",
        "logic": []
    },
    {
        "name": "D05Z01S03[W]",
        "logic": []
    },
    {
        "name": "D05Z01S03[E]",
        "logic": []
    },
    {
        "name": "D05Z01S03[Frontal]",
        "logic": []
    },
    {
        "name": "D05Z01S04[W]",
        "logic": []
    },
    {
        "name": "D05Z01S04[E]",
        "logic": []
    },
    {
        "name": "D05Z01S05[SW]",
        "logic": []
    },
    {
        "name": "D05Z01S05[E]",
        "logic": []
    },
    {
        "name": "D05Z01S05[NE]",
        "logic": []
    },
    {
        "name": "D05Z01S06[W]",
        "logic": []
    },
    {
        "name": "D05Z01S06[E]",
        "logic": []
    },
    {
        "name": "D05Z01S07[SW]",
        "logic": []
    },
    {
        "name": "D05Z01S07[NW]",
        "logic": []
    },
    {
        "name": "D05Z01S07[E]",
        "logic": []
    },
    {
        "name": "D05Z01S08[W]",
        "logic": []
    },
    {
        "name": "D05Z01S08[NW]",
        "logic": []
    },
    {
        "name": "D05Z01S08[E]",
        "logic": []
    },
    {
        "name": "D05Z01S08[Health]",
        "logic": []
    },
    {
        "name": "D05Z01S08[NE]",
        "logic": []
    },
    {
        "name": "D05Z01S09[W]",
        "logic": []
    },
    {
        "name": "D05Z01S09[E]",
        "logic": []
    },
    {
        "name": "D05Z01S10[W]",
        "logic": []
    },
    {
        "name": "D05Z01S10[NW]",
        "logic": []
    },
    {
        "name": "D05Z01S10[E]",
        "logic": []
    },
    {
        "name": "D05Z01S11[SW]",
        "logic": []
    },
    {
        "name": "D05Z01S11[NW]",
        "logic": []
    },
    {
        "name": "D05Z01S11[NE]",
        "logic": []
    },
    {
        "name": "D05Z01S11[SE]",
        "logic": []
    },
    {
        "name": "D05Z01S11[E]",
        "logic": []
    },
    {
        "name": "D05Z01S12[E]",
        "logic": []
    },
    {
        "name": "D05Z01S13[E]",
        "logic": []
    },
    {
        "name": "D05Z01S14[W]",
        "logic": []
    },
    {
        "name": "D05Z01S15[W]",
        "logic": []
    },
    {
        "name": "D05Z01S15[E]",
        "logic": []
    },
    {
        "name": "D05Z01S16[W]",
        "logic": []
    },
    {
        "name": "D05Z01S17[W]",
        "logic": []
    },
    {
        "name": "D05Z01S18[W]",
        "logic": []
    },
    {
        "name": "D05Z01S19[W]",
        "logic": []
    },
    {
        "name": "D05Z01S19[E]",
        "logic": []
    },
    {
        "name": "D05Z01S20[W]",
        "logic": []
    },
    {
        "name": "D05Z01S20[E]",
        "logic": []
    },
    {
        "name": "D05Z01S20[N]",
        "logic": []
    },
    {
        "name": "D05Z01S21[SW]",
        "logic": []
    },
    {
        "name": "D05Z01S21[NW]",
        "logic": []
    },
    {
        "name": "D05Z01S21[NE]",
        "logic": []
    },
    {
        "name": "D05Z01S21[-Cherubs]",
        "logic": []
    },
    {
        "name": "D05Z01S22[FrontalN]",
        "logic": []
    },
    {
        "name": "D05Z01S22[E]",
        "logic": []
    },
    {
        "name": "D05Z01S23[E]",
        "logic": []
    },
    {
        "name": "D05Z01S24[E]",
        "logic": []
    },
    {
        "name": "D05BZ01S01[FrontalS]",
        "logic": []
    },
    {
        "name": "D05BZ01S01[FrontalN]",
        "logic": []
    },
    {
        "name": "D05Z02S01[W]",
        "logic": []
    },
    {
        "name": "D05Z02S01[E]",
        "logic": []
    },
    {
        "name": "D05Z02S02[SW]",
        "logic": []
    },
    {
        "name": "D05Z02S02[NW]",
        "logic": []
    },
    {
        "name": "D05Z02S02[SE]",
        "logic": []
    },
    {
        "name": "D05Z02S02[NE]",
        "logic": []
    },
    {
        "name": "D05Z02S03[W]",
        "logic": []
    },
    {
        "name": "D05Z02S03[E]",
        "logic": []
    },
    {
        "name": "D05Z02S04[W]",
        "logic": []
    },
    {
        "name": "D05Z02S04[E]",
        "logic": []
    },
    {
        "name": "D05Z02S04[C]",
        "logic": []
    },
    {
        "name": "D05Z02S05[W]",
        "logic": []
    },
    {
        "name": "D05Z02S05[E]",
        "logic": []
    },
    {
        "name": "D05Z02S06[SW]",
        "logic": []
    },
    {
        "name": "D05Z02S06[NW]",
        "logic": []
    },
    {
        "name": "D05Z02S06[SE]",
        "logic": []
    },
    {
        "name": "D05Z02S06[NE]",
        "logic": []
    },
    {
        "name": "D05Z02S07[W]",
        "logic": []
    },
    {
        "name": "D05Z02S07[E]",
        "logic": []
    },
    {
        "name": "D05Z02S08[W]",
        "logic": []
    },
    {
        "name": "D05Z02S09[W]",
        "logic": []
    },
    {
        "name": "D05Z02S09[E]",
        "logic": []
    },
    {
        "name": "D05Z02S10[W]",
        "logic": []
    },
    {
        "name": "D05Z02S10[E]",
        "logic": []
    },
    {
        "name": "D05Z02S11[W]",
        "logic": []
    },
    {
        "name": "D05Z02S12[W]",
        "logic": []
    },
    {
        "name": "D05Z02S12[E]",
        "logic": []
    },
    {
        "name": "D05Z02S12[N]",
        "logic": []
    },
    {
        "name": "D05Z02S13[E]",
        "logic": []
    },
    {
        "name": "D05Z02S14[W]",
        "logic": []
    },
    {
        "name": "D05Z02S14[E]",
        "logic": []
    },
    {
        "name": "D05Z02S15[S]",
        "logic": []
    },
    {
        "name": "D05Z02S15[E]",
        "logic": []
    },
    {
        "name": "D05BZ02S01[C]",
        "logic": []
    },
    {
        "name": "D06Z01S01[SW]",
        "logic": []
    },
    {
        "name": "D06Z01S01[SE]",
        "logic": []
    },
    {
        "name": "D06Z01S01[W]",
        "logic": []
    },
    {
        "name": "D06Z01S01[E]",
        "logic": []
    },
    {
        "name": "D06Z01S01[NW]",
        "logic": []
    },
    {
        "name": "D06Z01S01[NE]",
        "logic": []
    },
    {
        "name": "D06Z01S01[NNW]",
        "logic": []
    },
    {
        "name": "D06Z01S01[NNE]",
        "logic": []
    },
    {
        "name": "D06Z01S01[N]",
        "logic": []
    },
    {
        "name": "D06Z01S01[-Cherubs]",
        "logic": []
    },
    {
        "name": "D06Z01S02[W]",
        "logic": []
    },
    {
        "name": "D06Z01S02[E]",
        "logic": []
    },
    {
        "name": "D06Z01S02[S]",
        "logic": []
    },
    {
        "name": "D06Z01S03[W]",
        "logic": []
    },
    {
        "name": "D06Z01S03[E]",
        "logic": []
    },
    {
        "name": "D06Z01S04[SW]",
        "logic": []
    },
    {
        "name": "D06Z01S04[W]",
        "logic": []
    },
    {
        "name": "D06Z01S04[Health]",
        "logic": []
    },
    {
        "name": "D06Z01S04[NW]",
        "logic": []
    },
    {
        "name": "D06Z01S04[NE]",
        "logic": []
    },
    {
        "name": "D06Z01S05[E]",
        "logic": []
    },
    {
        "name": "D06Z01S06[WW]",
        "logic": []
    },
    {
        "name": "D06Z01S06[E]",
        "logic": []
    },
    {
        "name": "D06Z01S06[W]",
        "logic": []
    },
    {
        "name": "D06Z01S06[EE]",
        "logic": []
    },
    {
        "name": "D06Z01S07[W]",
        "logic": []
    },
    {
        "name": "D06Z01S07[E]",
        "logic": []
    },
    {
        "name": "D06Z01S08[W]",
        "logic": []
    },
    {
        "name": "D06Z01S08[E]",
        "logic": []
    },
    {
        "name": "D06Z01S08[N]",
        "logic": []
    },
    {
        "name": "D06Z01S09[W]",
        "logic": []
    },
    {
        "name": "D06Z01S09[E]",
        "logic": []
    },
    {
        "name": "D06Z01S09[-CherubsL]",
        "logic": []
    },
    {
        "name": "D06Z01S09[-CherubsR]",
        "logic": []
    },
    {
        "name": "D06Z01S10[W]",
        "logic": []
    },
    {
        "name": "D06Z01S10[E]",
        "logic": []
    },
    {
        "name": "D06Z01S10[-CherubsL]",
        "logic": []
    },
    {
        "name": "D06Z01S10[-CherubsR]",
        "logic": []
    },
    {
        "name": "D06Z01S11[W]",
        "logic": []
    },
    {
        "name": "D06Z01S12[S]",
        "logic": []
    },
    {
        "name": "D06Z01S12[W]",
        "logic": []
    },
    {
        "name": "D06Z01S12[E]",
        "logic": []
    },
    {
        "name": "D06Z01S12[NW]",
        "logic": []
    },
    {
        "name": "D06Z01S12[NE]",
        "logic": []
    },
    {
        "name": "D06Z01S12[NE2]",
        "logic": []
    },
    {
        "name": "D06Z01S13[W]",
        "logic": []
    },
    {
        "name": "D06Z01S13[E]",
        "logic": []
    },
    {
        "name": "D06Z01S13[S]",
        "logic": []
    },
    {
        "name": "D06Z01S14[W]",
        "logic": []
    },
    {
        "name": "D06Z01S14[E]",
        "logic": []
    },
    {
        "name": "D06Z01S14[N]",
        "logic": []
    },
    {
        "name": "D06Z01S15[SW]",
        "logic": []
    },
    {
        "name": "D06Z01S15[NW]",
        "logic": []
    },
    {
        "name": "D06Z01S15[NE]",
        "logic": []
    },
    {
        "name": "D06Z01S16[W]",
        "logic": []
    },
    {
        "name": "D06Z01S16[E]",
        "logic": []
    },
    {
        "name": "D06Z01S16[-CherubsL]",
        "logic": []
    },
    {
        "name": "D06Z01S16[-CherubsR]",
        "logic": []
    },
    {
        "name": "D06Z01S17[W]",
        "logic": []
    },
    {
        "name": "D06Z01S17[E]",
        "logic": []
    },
    {
        "name": "D06Z01S17[-Cherubs]",
        "logic": []
    },
    {
        "name": "D06Z01S18[E]",
        "logic": []
    },
    {
        "name": "D06Z01S18[-Cherubs]",
        "logic": []
    },
    {
        "name": "D06Z01S19[S]",
        "logic": []
    },
    {
        "name": "D06Z01S19[E]",
        "logic": []
    },
    {
        "name": "D06Z01S20[W]",
        "logic": []
    },
    {
        "name": "D06Z01S20[E]",
        "logic": []
    },
    {
        "name": "D06Z01S21[W]",
        "logic": []
    },
    {
        "name": "D06Z01S21[E]",
        "logic": []
    },
    {
        "name": "D06Z01S22[Sword]",
        "logic": []
    },
    {
        "name": "D06Z01S23[Sword]",
        "logic": []
    },
    {
        "name": "D06Z01S23[E]",
        "logic": []
    },
    {
        "name": "D06Z01S23[S]",
        "logic": []
    },
    {
        "name": "D06Z01S24[W]",
        "logic": []
    },
    {
        "name": "D06Z01S25[W]",
        "logic": []
    },
    {
        "name": "D06Z01S25[E]",
        "logic": []
    },
    {
        "name": "D06Z01S26[W]",
        "logic": []
    },
    {
        "name": "D07Z01S01[W]",
        "logic": []
    },
    {
        "name": "D07Z01S01[E]",
        "logic": []
    },
    {
        "name": "D07Z01S02[W]",
        "logic": []
    },
    {
        "name": "D07Z01S02[E]",
        "logic": []
    },
    {
        "name": "D07Z01S03[W]",
        "logic": []
    },
    {
        "name": "D08Z01S01[W]",
        "logic": []
    },
    {
        "name": "D08Z01S01[E]",
        "logic": []
    },
    {
        "name": "D08Z01S02[NE]",
        "logic": []
    },
    {
        "name": "D08Z01S02[SE]",
        "logic": []
    },
    {
        "name": "D08Z01S02[-Cherubs]",
        "logic": []
    },
    {
        "name": "D08Z02S01[W]",
        "logic": []
    },
    {
        "name": "D08Z02S01[SE]",
        "logic": []
    },
    {
        "name": "D08Z02S01[E]",
        "logic": []
    },
    {
        "name": "D08Z02S01[N]",
        "logic": []
    },
    {
        "name": "D08Z02S02[W]",
        "logic": []
    },
    {
        "name": "D08Z02S03[W]",
        "logic": []
    },
    {
        "name": "D08Z02S03[E]",
        "logic": []
    },
    {
        "name": "D08Z02S03[S]",
        "logic": []
    },
    {
        "name": "D08Z03S01[W]",
        "logic": []
    },
    {
        "name": "D08Z03S01[E]",
        "logic": []
    },
    {
        "name": "D08Z03S02[SW]",
        "logic": []
    },
    {
        "name": "D08Z03S02[NW]",
        "logic": []
    },
    {
        "name": "D08Z03S03[W]",
        "logic": []
    },
    {
        "name": "D08Z03S03[E]",
        "logic": []
    },
    {
        "name": "D09Z01S01[W]",
        "logic": []
    },
    {
        "name": "D09Z01S01[E]",
        "logic": []
    },
    {
        "name": "D09Z01S02[SW]",
        "logic": []
    },
    {
        "name": "D09Z01S02[NW]",
        "logic": []
    },
    {
        "name": "D09Z01S02[N]",
        "logic": []
    },
    {
        "name": "D09Z01S02[Cell1]",
        "logic": []
    },
    {
        "name": "D09Z01S02[Cell6]",
        "logic": []
    },
    {
        "name": "D09Z01S02[Cell5]",
        "logic": []
    },
    {
        "name": "D09Z01S02[Cell4]",
        "logic": []
    },
    {
        "name": "D09Z01S02[Cell2]",
        "logic": []
    },
    {
        "name": "D09Z01S02[Cell3]",
        "logic": []
    },
    {
        "name": "D09Z01S02[Cell22]",
        "logic": []
    },
    {
        "name": "D09Z01S02[Cell23]",
        "logic": []
    },
    {
        "name": "D09Z01S03[W]",
        "logic": []
    },
    {
        "name": "D09Z01S04[W]",
        "logic": []
    },
    {
        "name": "D09Z01S04[E]",
        "logic": []
    },
    {
        "name": "D09Z01S04[S]",
        "logic": []
    },
    {
        "name": "D09Z01S05[W]",
        "logic": []
    },
    {
        "name": "D09Z01S05[SE]",
        "logic": []
    },
    {
        "name": "D09Z01S05[NE]",
        "logic": []
    },
    {
        "name": "D09Z01S06[-E]",
        "logic": []
    },
    {
        "name": "D09Z01S06[E]",
        "logic": []
    },
    {
        "name": "D09Z01S07[SW]",
        "logic": []
    },
    {
        "name": "D09Z01S07[SE]",
        "logic": []
    },
    {
        "name": "D09Z01S07[W]",
        "logic": []
    },
    {
        "name": "D09Z01S07[E]",
        "logic": []
    },
    {
        "name": "D09Z01S07[NW]",
        "logic": []
    },
    {
        "name": "D09Z01S07[N]",
        "logic": []
    },
    {
        "name": "D09Z01S07[NE]",
        "logic": []
    },
    {
        "name": "D09Z01S08[W]",
        "logic": []
    },
    {
        "name": "D09Z01S08[S]",
        "logic": []
    },
    {
        "name": "D09Z01S08[SE]",
        "logic": []
    },
    {
        "name": "D09Z01S08[NE]",
        "logic": []
    },
    {
        "name": "D09Z01S08[Cell14]",
        "logic": []
    },
    {
        "name": "D09Z01S08[Cell15]",
        "logic": []
    },
    {
        "name": "D09Z01S08[Cell7]",
        "logic": []
    },
    {
        "name": "D09Z01S08[Cell16]",
        "logic": []
    },
    {
        "name": "D09Z01S08[Cell18]",
        "logic": []
    },
    {
        "name": "D09Z01S08[Cell17]",
        "logic": []
    },
    {
        "name": "D09Z01S09[SW]",
        "logic": []
    },
    {
        "name": "D09Z01S09[NW]",
        "logic": []
    },
    {
        "name": "D09Z01S09[E]",
        "logic": []
    },
    {
        "name": "D09Z01S09[Cell24]",
        "logic": []
    },
    {
        "name": "D09Z01S09[Cell19]",
        "logic": []
    },
    {
        "name": "D09Z01S09[Cell20]",
        "logic": []
    },
    {
        "name": "D09Z01S09[Cell21]",
        "logic": []
    },
    {
        "name": "D09Z01S10[W]",
        "logic": []
    },
    {
        "name": "D09Z01S10[Cell13]",
        "logic": []
    },
    {
        "name": "D09Z01S10[Cell12]",
        "logic": []
    },
    {
        "name": "D09Z01S10[Cell10]",
        "logic": []
    },
    {
        "name": "D09Z01S10[Cell11]",
        "logic": []
    },
    {
        "name": "D09Z01S11[W]",
        "logic": []
    },
    {
        "name": "D09Z01S11[E]",
        "logic": []
    },
    {
        "name": "D09Z01S11[S]",
        "logic": []
    },
    {
        "name": "D09Z01S12[E]",
        "logic": []
    },
    {
        "name": "D09Z01S13[E]",
        "logic": []
    },
    {
        "name": "D09BZ01S01[Cell1]",
        "logic": []
    },
    {
        "name": "D09BZ01S01[Cell2]",
        "logic": []
    },
    {
        "name": "D09BZ01S01[Cell3]",
        "logic": []
    },
    {
        "name": "D09BZ01S01[Cell4]",
        "logic": []
    },
    {
        "name": "D09BZ01S01[Cell5]",
        "logic": []
    },
    {
        "name": "D09BZ01S01[Cell6]",
        "logic": []
    },
    {
        "name": "D09BZ01S01[Cell7]",
        "logic": []
    },
    {
        "name": "D09BZ01S01[Cell10]",
        "logic": []
    },
    {
        "name": "D09BZ01S01[Cell11]",
        "logic": []
    },
    {
        "name": "D09BZ01S01[Cell12]",
        "logic": []
    },
    {
        "name": "D09BZ01S01[Cell13]",
        "logic": []
    },
    {
        "name": "D09BZ01S01[Cell14]",
        "logic": []
    },
    {
        "name": "D09BZ01S01[Cell15]",
        "logic": []
    },
    {
        "name": "D09BZ01S01[Cell16]",
        "logic": []
    },
    {
        "name": "D09BZ01S01[Cell17]",
        "logic": []
    },
    {
        "name": "D09BZ01S01[Cell18]",
        "logic": []
    },
    {
        "name": "D09BZ01S01[Cell19]",
        "logic": []
    },
    {
        "name": "D09BZ01S01[Cell20]",
        "logic": []
    },
    {
        "name": "D09BZ01S01[Cell21]",
        "logic": []
    },
    {
        "name": "D09BZ01S01[Cell22]",
        "logic": []
    },
    {
        "name": "D09BZ01S01[Cell23]",
        "logic": []
    },
    {
        "name": "D09BZ01S01[Cell24]",
        "logic": []
    },
    {
        "name": "D17Z01S01[E]",
        "logic": []
    },
    {
        "name": "D17Z01S02[W]",
        "logic": []
    },
    {
        "name": "D17Z01S02[E]",
        "logic": []
    },
    {
        "name": "D17Z01S02[N]",
        "logic": []
    },
    {
        "name": "D17Z01S03[W]",
        "logic": []
    },
    {
        "name": "D17Z01S03[E]",
        "logic": []
    },
    {
        "name": "D17Z01S03[relic]",
        "logic": []
    },
    {
        "name": "D17Z01S04[W]",
        "logic": []
    },
    {
        "name": "D17Z01S04[S]",
        "logic": []
    },
    {
        "name": "D17Z01S04[FrontL]",
        "logic": []
    },
    {
        "name": "D17Z01S04[N]",
        "logic": []
    },
    {
        "name": "D17Z01S04[FrontR]",
        "logic": []
    },
    {
        "name": "D17Z01S05[W]",
        "logic": []
    },
    {
        "name": "D17Z01S05[E]",
        "logic": []
    },
    {
        "name": "D17Z01S05[S]",
        "logic": []
    },
    {
        "name": "D17Z01S06[E]",
        "logic": []
    },
    {
        "name": "D17Z01S07[SW]",
        "logic": []
    },
    {
        "name": "D17Z01S07[SE]",
        "logic": []
    },
    {
        "name": "D17Z01S07[W]",
        "logic": []
    },
    {
        "name": "D17Z01S07[NW]",
        "logic": []
    },
    {
        "name": "D17Z01S07[N]",
        "logic": []
    },
    {
        "name": "D17Z01S08[E]",
        "logic": []
    },
    {
        "name": "D17Z01S09[E]",
        "logic": []
    },
    {
        "name": "D17Z01S10[W]",
        "logic": []
    },
    {
        "name": "D17Z01S10[S]",
        "logic": []
    },
    {
        "name": "D17Z01S11[W]",
        "logic": []
    },
    {
        "name": "D17Z01S11[E]",
        "logic": []
    },
    {
        "name": "D17Z01S12[E]",
        "logic": []
    },
    {
        "name": "D17Z01S13[W]",
        "logic": []
    },
    {
        "name": "D17Z01S13[E]",
        "logic": []
    },
    {
        "name": "D17Z01S14[W]",
        "logic": []
    },
    {
        "name": "D17Z01S14[E]",
        "logic": []
    },
    {
        "name": "D17Z01S14[-Cherubs1]",
        "logic": []
    },
    {
        "name": "D17Z01S14[-Cherubs2]",
        "logic": []
    },
    {
        "name": "D17Z01S14[-Cherubs3]",
        "logic": []
    },
    {
        "name": "D17Z01S15[E]",
        "logic": []
    },
    {
        "name": "D17BZ01S01[relic]",
        "logic": []
    },
    {
        "name": "D17BZ02S01[FrontL]",
        "logic": []
    },
    {
        "name": "D17BZ02S01[FrontR]",
        "logic": []
    },
    {
        "name": "D20Z01S01[W]",
        "logic": []
    },
    {
        "name": "D20Z01S01[E]",
        "logic": []
    },
    {
        "name": "D20Z01S01[S]",
        "logic": []
    },
    {
        "name": "D20Z01S02[W]",
        "logic": []
    },
    {
        "name": "D20Z01S02[E]",
        "logic": []
    },
    {
        "name": "D20Z01S03[W]",
        "logic": []
    },
    {
        "name": "D20Z01S03[N]",
        "logic": []
    },
    {
        "name": "D20Z01S04[W]",
        "logic": []
    },
    {
        "name": "D20Z01S04[E]",
        "logic": []
    },
    {
        "name": "D20Z01S04[N]",
        "logic": []
    },
    {
        "name": "D20Z01S05[W]",
        "logic": []
    },
    {
        "name": "D20Z01S05[E]",
        "logic": []
    },
    {
        "name": "D20Z01S06[NE]",
        "logic": []
    },
    {
        "name": "D20Z01S06[SE]",
        "logic": []
    },
    {
        "name": "D20Z01S07[NW]",
        "logic": []
    },
    {
        "name": "D20Z01S07[NE]",
        "logic": []
    },
    {
        "name": "D20Z01S07[SE]",
        "logic": []
    },
    {
        "name": "D20Z01S08[W]",
        "logic": []
    },
    {
        "name": "D20Z01S09[W]",
        "logic": []
    },
    {
        "name": "D20Z01S09[E]",
        "logic": []
    },
    {
        "name": "D20Z01S10[W]",
        "logic": []
    },
    {
        "name": "D20Z01S10[E]",
        "logic": []
    },
    {
        "name": "D20Z01S11[W]",
        "logic": []
    },
    {
        "name": "D20Z01S11[NW]",
        "logic": []
    },
    {
        "name": "D20Z01S11[NE]",
        "logic": []
    },
    {
        "name": "D20Z01S11[SE]",
        "logic": []
    },
    {
        "name": "D20Z01S12[E]",
        "logic": []
    },
    {
        "name": "D20Z01S13[W]",
        "logic": []
    },
    {
        "name": "D20Z01S13[E]",
        "logic": []
    },
    {
        "name": "D20Z01S13[N]",
        "logic": []
    },
    {
        "name": "D20Z01S14[S]",
        "logic": []
    },
    {
        "name": "D20Z01S14[E]",
        "logic": []
    },
    {
        "name": "D20Z02S01[W]",
        "logic": []
    },
    {
        "name": "D20Z02S01[E]",
        "logic": []
    },
    {
        "name": "D20Z02S02[W]",
        "logic": []
    },
    {
        "name": "D20Z02S03[W]",
        "logic": []
    },
    {
        "name": "D20Z02S03[NE]",
        "logic": []
    },
    {
        "name": "D20Z02S03[SE]",
        "logic": []
    },
    {
        "name": "D20Z02S04[W]",
        "logic": []
    },
    {
        "name": "D20Z02S04[E]",
        "logic": []
    },
    {
        "name": "D20Z02S05[SW]",
        "logic": []
    },
    {
        "name": "D20Z02S05[NW]",
        "logic": []
    },
    {
        "name": "D20Z02S05[E]",
        "logic": []
    },
    {
        "name": "D20Z02S06[SW]",
        "logic": []
    },
    {
        "name": "D20Z02S06[SE]",
        "logic": []
    },
    {
        "name": "D20Z02S06[NW]",
        "logic": []
    },
    {
        "name": "D20Z02S06[NE]",
        "logic": []
    },
    {
        "name": "D20Z02S07[W]",
        "logic": []
    },
    {
        "name": "D20Z02S07[E]",
        "logic": []
    },
    {
        "name": "D20Z02S08[E]",
        "logic": []
    },
    {
        "name": "D20Z02S09[W]",
        "logic": []
    },
    {
        "name": "D20Z02S09[E]",
        "logic": []
    },
    {
        "name": "D20Z02S10[W]",
        "logic": []
    },
    {
        "name": "D20Z02S10[E]",
        "logic": []
    },
    {
        "name": "D20Z02S11[SW]",
        "logic": []
    },
    {
        "name": "D20Z02S11[NW]",
        "logic": []
    },
    {
        "name": "D20Z02S11[E]",
        "logic": []
    },
    {
        "name": "D20Z02S12[W]",
        "logic": []
    },
    {
        "name": "D20Z02S12[E]",
        "logic": []
    },
    {
        "name": "D20Z03S01[W]",
        "logic": []
    }
]
