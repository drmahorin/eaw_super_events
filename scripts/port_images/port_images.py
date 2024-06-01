import shutil

dir_from = '../../sources/old_pictures_cropped/'

images = {
    'eaw_super_event_nightmare_moon_civil_war': 'EAWSE_NIGHTMARE_MOON_CV',
    'eaw_super_event_daybreaker_ascends': 'EAWSE_DAYBREAKER',
    'eaw_super_event_two_sisters_war': 'EAWSE_TWO_SISTERS_WAR',
    'eaw_super_event_lunar_equus': 'EAWSE_LUNAR_EQUUS',
    'eaw_super_event_solar_equus': 'EAWSE_SOLAR_EQUUS',
    'eaw_super_event_golden_delicious': 'EAWSE_BALTIMARE_GOLDEN',
    'eaw_super_event_cricket_chafer': 'EAWSE_BALTIMARE_CHAFER',
    'eaw_super_event_bal_anarchists': 'EAWSE_BALTIMARE_ANARCHISTS',
    'eaw_super_event_lavander_berry': 'EAWSE_BALTIMARE_LAVANDER',
    'eaw_super_event_ahuizotl': 'EAWSE_AHUIZOTL_EMPIRE',
    'eaw_super_event_lsp_mayor': 'EAWSE_LSP_MAYOR',
    'eaw_super_event_lsp_pine_chest': 'EAWSE_LSP_PINE_CHEST',
    'eaw_super_event_lsp_rockfeller': 'EAWSE_LSP_ROCKFELLER',
    'eaw_super_event_lsp_starry_plough': 'EAWSE_LSP_STARRY',
    'eaw_super_event_lsp_sugar_sprinkle': 'EAWSE_LSP_SPRINKLE',
    'eaw_super_event_stalliongrad_unites_equestria': 'EAWSE_STG_UNITES_EQUESTRIA',
    'eaw_super_event_dark_wing_unites_equestria': 'EAWSE_DARK_WING_UNITES_EQS',
    'eaw_super_event_vanhoover': 'EAWSE_VANHOOVER',
    'eaw_super_event_scs_confederate': 'EAWSE_SCS_CONFEDERATE',
    'eaw_super_event_our_equestria': 'EAWSE_STL_OUR',
    'eaw_super_event_sombra_returns': 'EAWSE_SOMBRA_RETURNS',
    'eaw_super_event_sombra_victory': 'EAWSE_SOMBRA_VICTORY',
    'eaw_super_event_great_war': 'EAWSE_GREAT_WAR',
    'eaw_super_event_great_war_stg': 'EAWSE_GREAT_WAR_STG',
    'eaw_super_event_great_war_equestrian_victory': 'EAWSE_GREAT_WAR_EV',
    'eaw_super_event_great_war_changelings_victory': 'EAWSE_GREAT_WAR_CV',
    'eaw_super_event_great_war_solar_victory': 'EAWSE_GREAT_WAR_SV',
    'eaw_super_event_great_war_lunar_victory': 'EAWSE_GREAT_WAR_LV',
    'eaw_super_event_stalliongrad_defeats_changelings': 'EAWSE_STG_DEFEATS_CHN',
    'eaw_super_event_great_war_changelings_defeated': 'EAWSE_GREAT_WAR_CHN_D',
    'eaw_super_event_elf_uprising': 'EAWSE_ELF_U',
    'eaw_super_event_elf_victory': 'EAWSE_ELF_V',
    'eaw_super_event_elf_defeated': 'EAWSE_ELF_D',
    'eaw_super_event_stalliongrad_marches_on_equestria': 'EAWSE_STG_ATTACK_EQS',
    'eaw_super_event_stalliongrad_defeated': 'EAWSE_STG_DEFEATED',
    'eaw_super_event_world_socialist_republic': 'EAWSE_WORLD_SOC_REP',
    'eaw_super_event_stalliongrad_intervention': 'EAWSE_STG_INTERVENTION',
    'eaw_super_event_grf_highhill': 'EAWSE_GRF_WESTERN_EMPIRE_HIGHHILL',
    'eaw_super_event_grf_ironclaw': 'EAWSE_GRF_WESTERN_EMPIRE_IRONCLAW',
    'eaw_super_event_grf_goldfeather': 'EAWSE_GRF_GOLDFEATHER',
    'eaw_super_event_grf_virgil': 'EAWSE_GRF_WESTERN_EMPIRE_VIRGIL',
    'eaw_super_event_twilight_sparkle_princess_of_harmony': 'EAWSE_TS_PH',
    'eaw_super_event_thorax_uprising_successful': 'EAWSE_THX_UPRISING_S',
    'eaw_super_event_chrysalis_coronation_empress': 'EAWSE_CHRYSALIS_CORONATION',
    'eaw_super_event_grover_v_death': 'EAWSE_GROVER_V',
    'eaw_super_event_grover_vi_coronation': 'EAWSE_GROVER_VI_CORONATION',
    'eaw_super_event_grover_ii_resurrection': 'EAWSE_GROVER_II_RESURRECTION',
    'eaw_super_event_lord_protector': 'EAWSE_LORD_PROTECTOR_START',
    'eaw_super_event_griff_empire_final': 'EAWSE_GRIFF_EMPIRE_FINAL',
    'eaw_super_event_herzland_ang_leer': 'EAWSE_HERZLAND_ANG_LEER',
    'eaw_super_event_herzland_ang_othmar': 'EAWSE_HERZLAND_ANG_KINGDOM',
    'eaw_super_event_herzland_ang_commune': 'EAWSE_HERZLAND_ANG_ANARCHY',
    'eaw_super_event_herzland_ang_bluhm': 'EAWSE_HERZLAND_ANG_BLUHM',
    'eaw_super_event_herzland_ang_ordenstaat': 'EAWSE_HERZLAND_ANG_ORDENSTAAT',
    'eaw_super_event_herzland_ang_weschler': 'EAWSE_HERZLAND_ANG_WESCHLER',
    'eaw_super_event_herzland_pyt_friendship': 'EAWSE_HERZLAND_PYT_HARMONY_EQS',
    'eaw_super_event_herzland_pyt_holy_republic': 'EAWSE_HERZLAND_PYT_HARMONY_REPUBLIC',
    'eaw_super_event_herzland_pyt_com': 'EAWSE_HERZLAND_PYT_COM',
    'eaw_super_event_herzland_pyt_dietrich': 'EAWSE_HERZLAND_PYT_DIETRICH',
    'eaw_super_event_herzland_holy_empire': 'EAWSE_HERZLAND_PYT_TRUTHAHN',
    'eaw_super_event_herzland_pyt_erebus_empire': 'EAWSE_HERZLAND_PYT_EREBUS',
    'eaw_super_event_herzland_pyt_erebus_republic': 'EAWSE_HERZLAND_PYT_REPUBLIC',
    'eaw_super_event_herzland_yal_archon': 'EAWSE_HERZLAND_YAL_ARCHONT',
    'eaw_super_event_herzland_yal_grover_ii': 'EAWSE_HERZLAND_YAL_GROVER_II',
    'eaw_super_event_herzland_yal_boreas': 'EAWSE_HERZLAND_YAL_BOREAS',
    'eaw_super_event_herzland_yal_new_spark': 'EAWSE_HERZLAND_YAL_NEW_SPARK',
    'eaw_super_event_herzland_yal_technocracy': 'EAWSE_HERZLAND_YAL_TECHNOCRACY',
    'eaw_super_event_herzland_yal_com': 'EAWSE_HERZLAND_YAL_COM',
    'eaw_super_event_herzland_kat_duskfeather': 'EAWSE_HERZLAND_KAT_COM',
    'eaw_super_event_herzland_kat_katerintreue': 'EAWSE_HERZLAND_KAT_KATERINTREUE',
    'eaw_super_event_herzland_kat_hector': 'EAWSE_HERZLAND_KAT_REPUBLIC',
    'eaw_super_event_herzland_kat_grimclaw': 'EAWSE_HERZLAND_KAT_NEUTRAL',
    'eaw_super_event_herzland_rou_com': 'EAWSE_HERZLAND_ROU_COM',
    'eaw_super_event_herzland_rou_harmony': 'EAWSE_HERZLAND_ROU_HARMONY',
    'eaw_super_event_herzland_rou_neutral': 'EAWSE_HERZLAND_ROU_NEUTRAL',
    'eaw_super_event_herzland_rou_erion': 'EAWSE_HERZLAND_ROU_EYR',
    'eaw_super_event_herzland_fea_com': 'EAWSE_HERZLAND_FEA_STAPPENBELD',
    'eaw_super_event_herzland_fea_coghel': 'EAWSE_HERZLAND_FEA_KOGCHEL',
    'eaw_super_event_herzland_fea_rozenkamp': 'EAWSE_HERZLAND_FEA_ROZENKAMP',
    'eaw_super_event_herzland_fea_heeren': 'EAWSE_HERZLAND_FEA_HEEREN',
    'eaw_super_event_herzland_fea_moldernik': 'EAWSE_HERZLAND_FEA_MOLDERNIK',
    'eaw_super_event_herzland_fea_supremacy': 'EAWSE_HERZLAND_FEA_VORST',
    'eaw_super_event_herzland_new_empire': 'EAWSE_HERZLAND_FEA_DUKE',
    'eaw_super_event_herzland_fea_unwilling_dictator': 'EAWSE_HERZLAND_FEA_UNWILLING_DICTATOR',
    'eaw_super_event_herzland_fea_coalition': 'EAWSE_HERZLAND_FEA_COALITION',
    'eaw_super_event_herzland_stw_harmony': 'EAWSE_HERZLAND_STW_HARMONY',
    'eaw_super_event_herzland_stw_communism': 'EAWSE_HERZLAND_STW_COM',
    'eaw_super_event_herzland_stw_neutral': 'EAWSE_HERZLAND_STW_NEUTRAL',
    'eaw_super_event_herzland_stw_supremacy': 'EAWSE_HERZLAND_STW_SUPREMACY',
    'eaw_super_event_herzland_brz_harmony': 'EAWSE_HERZLAND_BRZ_HARMONY',
    'eaw_super_event_herzland_brz_standart': 'EAWSE_HERZLAND_BRZ_NEUTRAL',
    'eaw_super_event_herzland_brz_communism': 'EAWSE_HERZLAND_BRZ_COM',
    'eaw_super_event_herzland_brz_juche': 'EAWSE_HERZLAND_BRZ_JUCHE',
    'eaw_super_event_herzland_brz_supremacy': 'EAWSE_HERZLAND_BRZ_LOUDBARK',
    'eaw_super_event_herzland_brz_prelate': 'EAWSE_HERZLAND_BRZ_CHURCH',
    'eaw_super_event_lord_protector_unites_herzland': 'EAWSE_LP_UH',
    'eaw_super_event_bronzehill_revenge_juche': 'EAWSE_HERZLAND_BRZ_REVENGE_COM',
    'eaw_super_event_bronzehill_revenge_supremacy': 'EAWSE_HERZLAND_BRZ_REVENGE_EMPIRE_OF_DOGS',
    'eaw_super_event_river_federation_rct_harmony': 'EAWSE_RIV_RCT_RS',
    'eaw_super_event_river_federation_rct_arclight': 'EAWSE_RIV_RCT_AL',
    'eaw_super_event_river_federation_rct_dsr': 'EAWSE_RIV_RCT_NW',
    'eaw_super_event_river_federation_rct_ussr': 'EAWSE_RIV_RCT_CH',
    'eaw_super_event_river_federation_lct_harmony': 'EAWSE_RIV_LCT_DS',
    'eaw_super_event_river_federation_lct_supremacy': 'EAWSE_RIV_LCT_WL',
    'eaw_super_event_river_federation_lct_neutral': 'EAWSE_RIV_LCT_WB',
    'eaw_super_event_river_federation_bak_harmony': 'EAWSE_RIV_BAK_WL',
    'eaw_super_event_river_federation_bak_neutral': 'EAWSE_RIV_BAK_TD',
    'eaw_super_event_river_federation_bak_ussr': 'EAWSE_RIV_BAK_BF',
    'eaw_super_event_river_federation_bak_supremacy': 'EAWSE_RIV_BAK_FS',
    'eaw_super_event_river_federation_dmt_harmony': 'EAWSE_RIV_DMT_MOLLY',
    'eaw_super_event_river_federation_dmt_supremacy': 'EAWSE_RIV_DMT_ROVER',
    'eaw_super_event_river_federation_dmt_communist': 'EAWSE_RIV_DMT_COM',
    'eaw_super_event_river_federation_wit_ws': 'EAWSE_RIV_WIT_WS',
    'eaw_super_event_river_federation_wit_communist': 'EAWSE_RIV_WIT_V',
    'eaw_super_event_river_federation_wit_harmony': 'EAWSE_RIV_WIT_HARMONY',
    'eaw_super_event_river_federation_wit_neutral': 'EAWSE_RIV_WIT_NEUTRAL',
    'eaw_super_event_river_federation_nim_harmony': 'EAWSE_RIV_NIM_MK',
    'eaw_super_event_river_federation_dep_neutral': 'EAWSE_RIV_DEP_KG',
    'eaw_super_event_river_federation_fre_harmony': 'EAWSE_RIV_FRE_CR',
    'eaw_super_event_river_empire': 'EAWSE_RIV_EMP',
    'eaw_super_event_holy_pony_empire': 'EAWSE_HOLY_PONY_EMPIRE',
    'eaw_super_event_ost_griffonian_empire': 'EAWSE_OST_GRIFFONIA',
    'eaw_super_event_longsword_golden_morning': 'EAWSE_LNS_GM',
    'eaw_super_event_longsword_powner': 'EAWSE_LNS_POWNER',
    'eaw_super_event_griffonian_empire_river_coalition_war': 'EAWSE_GRI_RIV_WAR_GRI',
    'eaw_super_event_river_coalition_victory': 'EAWSE_GRI_RIV_WAR_RIV_V',
    'eaw_super_event_griffonian_empire_victory': 'EAWSE_GRI_RIV_WAR_GRI_V',
    'eaw_super_event_triumph_republican_dream1': 'EAWSE_REPUBLIC_WIN',
    'eaw_super_event_triumph_republican_dream2': 'EAWSE_REPUBLIC_WIN_COM',
    'eaw_super_event_triumph_republican_dream3': 'EAWSE_REPUBLIC_WIN_AUTH',
    'eaw_super_event_triumph_republican_dream4': 'EAWSE_REPUBLIC_WIN_S',
    'eaw_super_event_death_republican_dream': 'EAWSE_REPUBLIC_LOSE',
    'eaw_super_event_pan_griffonian_dream': 'EAWSE_PAN_GRIFFONIA_DREAM',
    'eaw_super_event_cloudbury_kingdom': 'EAWSE_CLOUDBURY_KINGDOM',
    'eaw_super_event_maresoc': 'EAWSE_MARESOC',
    'eaw_super_event_equestria_in_exile_strikes_back': 'EAWSE_ESB',
    'eaw_super_event_equestria_in_exile_victory': 'EAWSE_EQC_LIBERATES_EQS',
    'eaw_super_event_new_mareland_equalists': 'EAWSE_NEW_MARELAND_EQUALIST',
    'eaw_super_event_new_mareland_kingfisher': 'EAWSE_NEW_MARELAND_KINGFISHER',
    'eaw_super_event_new_mareland_lunar_dominion': 'EAWSE_NEW_MARELAND_LUNAR_DOMINION',
    'eaw_super_event_new_mareland_last_stand': 'EAWSE_NEW_MARELAND_LAST_STAND',
    'eaw_super_event_karthinian_empire': 'EAWSE_KARTHIN',
    'eaw_super_event_karthinian_workers_empire': 'EAWSE_KARTHIN_COM',
    'eaw_super_event_karthinian_republic': 'EAWSE_KARTHIN_REPUBLIC',
    'eaw_super_event_karthinian_kingdom': 'EAWSE_KARTHIN_KINGDOM',
    'eaw_super_event_evi_brodfeld': 'EAWSE_EVI_BRODFELD',
    'eaw_super_event_evi_gla': 'EAWSE_EVI_GLA',
    'eaw_super_event_evi_gryphian_host': 'EAWSE_EVI_GRYPHIAN_HOST',
    'eaw_super_event_evi_lushi': 'EAWSE_EVI_LUSHI',
    'eaw_super_event_evi_gryphus': 'EAWSE_EVI_GRYPHUS',
    'eaw_super_event_barrad_asinti': 'EAWSE_BAR_ASINTI',
    'eaw_super_event_barrad_leopold': 'EAWSE_BAR_LEOPOLD',
    'eaw_super_event_barrad_silver_star': 'EAWSE_BAR_SILVER',
    'eaw_super_event_barrad_viira_herald': 'EAWSE_BAR_VIIRA_H',
    'eaw_super_event_barrad_viira_goddess': 'EAWSE_BAR_VIIRA_G',
    'eaw_super_event_barrad_ambrosius': 'EAWSE_BAR_AMBROSIUS',
    'eaw_super_event_barrad_fall_of_pentarchy': 'EAWSE_BAR_FALL',
    'eaw_super_event_barrad_viira_victory': 'EAWSE_BAR_VIIRA_END',
    'eaw_super_event_aquileian_revolution': 'EAWSE_AQUILEIA_REVOLT',
    'eaw_super_event_aquileian_empire': 'EAWSE_AQUILEIA_EMPIRE',
    'eaw_super_event_aquileian_victory': 'EAWSE_AQUILEIAN_REPUBLIC_VICTORY',
    'eaw_super_event_dread_league_apocalypse': 'EAWSE_DED',
    'eaw_super_event_dread_league_black_crusade': 'EAWSE_DED_BC',
    'eaw_super_event_arcturian_order_holy_crusade': 'EAWSE_LIGHT_CRUSADE',
    'eaw_super_event_arcturian_order_victory': 'EAWSE_DED_DEFEATED',
    'eaw_super_event_imperium_of_maar': 'EAWSE_IMPERIUM_OF_MAAR',
    'eaw_super_event_free_territory': 'EAWSE_GRIFFONIAN_ANARCHY',
    'eaw_super_event_trimmel_on_griffonian_throne': 'EAWSE_TRIMMEL_ON_GRIFFONIAN_THRONE',
    'eaw_super_event_pan_griffonian_commonwealth': 'EAWSE_PAN_GRIFFONIA',
    'eaw_super_event_falcor_revenge': 'EAWSE_FALCOR_REVENGE',
    'eaw_super_event_great_zaphia': 'EAWSE_GREAT_ZAPHIA',
    'eaw_super_event_megali': 'EAWSE_MEGALI',
    'eaw_super_event_war_of_two_continents_eqs_gri': 'EAWSE_WAR_TWO_CONT_EQS_VS_GRI',
    'eaw_super_event_war_of_two_continents_chn_gri': 'EAWSE_WAR_TWO_CONT_CHN_VS_GRI',
    'eaw_super_event_war_of_two_continents_stg_gri': 'EAWSE_WAR_TWO_CONT_STG_VS_GRI',
    'eaw_super_event_war_of_two_continents_sol_gri': 'EAWSE_WAR_TWO_CONT_SOL_VS_GRI',
    'eaw_super_event_war_of_two_continents_nlr_gri': 'EAWSE_WAR_TWO_CONT_NLR_VS_GRI',
    'eaw_super_event_war_of_two_continents_maresoc_equus': 'EAWSE_WAR_TWO_CONT_MARESOC_VS_EQUUS',
    'eaw_super_event_war_of_two_continents_viira_equus': 'EAWSE_WAR_TWO_CONT_VIIRA_VS_EQUUS',
    'eaw_super_event_war_of_two_continents_juche_equus': 'EAWSE_WAR_TWO_CONT_JUCHE_VS_EQUUS',
    'eaw_super_event_war_of_two_continents_hlq_eqs': 'EAWSE_WAR_TWO_CONT_HLQ_VS_EQS',
    'eaw_super_event_war_of_two_continents_riv_chn': 'EAWSE_WAR_TWO_CONT_RIV_VS_CHN',
    'eaw_super_event_north_zebrica_war': 'EAWSE_NORTH_ZEBRICA_WAR',
    'eaw_super_event_hip_victory_harmony': 'EAWSE_HIP_HARMONY',
    'eaw_super_event_hip_victory_posada': 'EAWSE_HIP_COM',
    'eaw_super_event_hip_victory_af': 'EAWSE_HIP_AF',
    'eaw_super_event_hip_victory_falanga': 'EAWSE_HIP_FALANGA',
    'eaw_super_event_hip_victory_siren': 'EAWSE_HIP_SIREN',
    'eaw_super_event_hip_siren_final': 'EAWSE_HIP_SIREN_FINALE',
    'eaw_super_event_hip_posada_final': 'EAWSE_HIP_POSADA_FINALE',
    'eaw_super_event_col_first_civil_war': 'EAWSE_COL_FIRST_CIVIL_WAR',
    'eaw_super_event_col_second_civil_war': 'EAWSE_COL_SECOND_CIVIL_WAR',
    'eaw_super_event_col_third_civil_war': 'EAWSE_COL_THIRD_CIVIL_WAR',
    'eaw_super_event_white_severyana': 'EAWSE_TOBUCK_WHITE',
    'eaw_super_event_tsardom_of_severyana': 'EAWSE_TOBUCK_SEVERYANA',
    'eaw_super_event_neo_hazrumenia': 'EAWSE_TOBUCK_NEO_HAZRUMENIA',
    'eaw_super_event_tno_twilight': 'EAWSE_TNO_TWILIGHT',
    'eaw_super_event_tno_sablin': 'EAWSE_TNO_SABLIN',
}

for file in images:
    shutil.copy2(dir_from + file + '.tga', './out/' + images[file].lower() + '.tga')