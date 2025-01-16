import os

spreadsheet_id_dic = {"L4.csv": "1cz6I5zQtIvttM_xOOOcE4L9DtKYUq2iJRWfPh0qhN1g",
                      "L5.csv": "1eTu1NVtg6dkeHKnlatNznBGPvDihkVVkD23m2GLGXuY",
                      "L6.csv": "1jkYI_V_dBRG_ygG9MssX6KfJOWMcsBNyiLKDz029GTQ",
                      "L7.csv": "1Ncjklfb8dLG0FqW6VpW9Ibmfd1j_4ZVzY1ycHibJc4c",
                      "L9.csv": "17AR1ESEcXajxxpbPzqGJedJv_RJV8gOV5Wv9w-YBHhU",
                      "L10.csv": "1F9HWppdZwxZ19S8gVIJVdLDJS87tFq9tnGi7R9-XApQ",
                      "L11.csv": "15HrUsjt8PLIXiiaa69J8Ad32_YlMUWIOe2oQoH37eyw",
                      "L12.csv": "1u8UkuIZYmGPP-moQUuACzu7fCbYLpJ_gLkYqWEqwFaU",
                      "L13.csv": "1aTQe9czrAv0a7CyenfGTp7rlYLk_wx4dh05b_fsxZbE",
                      "L14.csv": "1E6rGGa3gslJFQ8G-zUwP30D6dvh3J3vMZ58n3iLH3y8",
                      "L1.csv": "1gheriDXo6CGvZ17c-D9W3_kVxnam453rzdLH2E7yxg4",
                      "L2.csv": "1LHA3Z0urv4mQos0Ug3aN24BOjXM9cvFiuyuebbf3gA8"}

to_download = [2, 3, 10, 11]

# 週三班
L4_video_id_dic = {5: "1tNFBwjCRBgzfkow313pBhlT_OYBRgO1N", 6: "1InkySFIMhDJVsATlIy7KxSIg_yfUdHIy",  # '11/30', '12/7'
                   7: "1BE1uvksFcK_JddW8iIohl2LnhFuc6LNx", 8: "1JIXUpT79Ezim0poY95Pk8dYSDyyE5-TL",  # '12/14', '12/21'
                   9: "1Q_LdhPNqdI4rkKRZDA5m0zQH9L3d1Bzq", 10: "1biKLQ_X5t8Cw7GyxYZgfeeh_jLzyiK88",  # '12/28', '1/4'
                   11: "1kZMmuMMTGBEeKdSiAL_eYtWGdDZ3W7cd", 12: "1ercjZVr-9qzBgyR-rK4gdjGao2XjSQtg",  # '1/11', '1/18'
                   14: "1-W_sVGiEF0Lmt6LdWES6XgeAV8mcdYRv", 15: "1gBBBhV_1YnMFvW1v7bnBCD1TPXPZwdvF",  # '2/1', '2/8'
                   16: "1X35MisV9kfDGnXq550LAC7SihIJkObtv", 17: "1T-gPOodAVZb9jZOmLZ5fjS3ujmg1Y4FJ"}  # '2/15', '2/22'

L5_video_id_dic = {5: "1BjcYW0I9_IzhJ1niFaF5MrW0tuHG4pYn", 6: "1-E0tMgQ9ZyDr54vwVLaYePbnFIUJbEKb",  # '3/1', '3/8'
                   7: "1WaHRsQZyN-wsVdDEDmjxG_I3c_lNlpmd", 8: "15Yt_fb-kAhgndFvpxUwiAH-IWNEptrBV",  # '3/15', '3/22'
                   9: "1xW_5_rud4GU0wqJZgm6pX9jNPnGmXD8S", 10: "1WV1JcAL1tHhQT8f7AEGpao1BPlZEisPa",  # '4/12', '4/19'
                   11: "1xAWKIj53F34r4-Wfir_CZBHpfkWte8q5", 12: "19hkHHoOtl0PHHC3nNvcNy6oR1uJ8e459",  # '4/26', '5/3'
                   13: "1JV-HZ6JpDeBDQJywGm1ENbnXOcFR-cu8", 14: "1bXAE2iE0FSGUGWtkIfXwe83fifqLIr10",  # '5/10', '5/17'
                   15: "1m1sNrHeDr75PTe3UjflNmtxGk9dKdQmr", 16: "1Y8lDzQ7AAkgYJYR2DDg-Aa3MQzzoYAEv"}  # '5/24', '5/31'

L6_video_id_dic = {5: "1iSkL7NIy4zXo-lOUiNtWtC-xXHP9oWSQ", 6: "17d-CH8V5yTBLC6MugrLyvilQyVKuRcMM",  # '6/7', '6/14'
                   7: "11LBxNAsBcMWCyDOFdiU18qHWHGI7luaz", 8: "114_FN91pXCtti4nQ1pAMY17lQZYmWAmF",  # '6/21', '6/28'
                   9: "1tt2tUCkvLmgmZlyFe-aJ4uOHUQ7vakvQ", 10: "14PGnk55tU6LNpm_Gw3zLZXuty_4gllfN",  # '7/5', '7/12'
                   11: "1fV1YcR_3CPxH1AFeFMkLq8hjQLzACvso", 12: "1H6QDHFcGxdE55SZgsVcTANqZkqo_8N_p",  # '7/19', '7/26'
                   13: "18LsJ7qFB8oZEq0OYioXweFLLoZ0qoXr8", 14: "1V1PTxjgA68NEjun_uQNyAvTz4hoE522R",  # '8/2', '8/9'
                   15: "1IzrlsxXf5LNa9hIgbB6_Hz2vRY-1mZrx", 16: "1S9kZkPzBUcZvO0rneFVVjAkzpXFbwCC7"}  # '8/16', '8/23'

L7_video_id_dic = {5: "1vT-S8QS9zLcdIpeQ3CryOHspR5YBh-BE", 6: "1P2GwguH5CSb9oX6AujgFWjmbB3xFyNle",  # '8/30', '9/6'
                   7: "1e9YeGnV3ur9JAcDnrJJIriof4oj7Z7V0", 8: "1uOFz7jqRG7cFvK6CIGss5P0SDuO4-GUO",  # '9/13', '9/20'
                   9: "1g7T3tOz4M14e6cmny7h_wsSrYNlPxsDM", 10: "1cjuWnuPruWYyMXKcAv3n5FU-1SLIOZux",  # '9/27', '10/4'
                   11: "1q7TeAEyvBNpndYQuoiTrKVfZCbBAyP_U", 12: "1cm7Ila4kM0r_GG5fTTH-zZZmrui2ZpAN",  # '10/11', '10/18'
                   13: "170Fn3jA9wqB1g_ousp4M_T8pTocucUbG", 14: "1mRXJQfW5YwYB9SFTnkRy1289zZbg2zev",  # '10/25', '11/1'
                   15: "1_IqLhMv6wzp9sdM24ds6rWpWZoogAe1D", 16: "114g92oUyAxpd70bqCTHhxJPhEHl-4rWb"}  # '11/8', '11/15'

# 週一班
L9_video_id_dic = {5: "1-S7fhqW1QE9LFzJN7ldJunrI-B-qPtJd", 6: "12gItLsRQnrzBFpfHIfmsju9oQIFF9V20",  # '7/18', '7/25'
                   7: "1tv0epVHVfn-bQOoIqEKPNklE2akBd3da", 8: "1ncXyw0UfKDPKfhfky6MMszP1c47tL4qb",  # '8/1', '8/8'
                   9: "1QkpCywEUciZcYUSqEQIyXfukhYnk3Az9", 10: "1TdnsUFWV39hGOpbkLavVKK381qy3vjXx",  # '8/15', '8/22'
                   11: "1zgAIxUIJFm6PCx17wLAYAYLzkNVQ505b", 12: "1pjavR4pU9LptLybyY3y8wqYNpHV2rv7l",  # '8/29', '9/5'
                   13: "1V3Vov8uGQzJ26QhlePYzaAyY2cvl-D-e", 14: "1JzBTGKlawElk1_59nPxT20wAjc18Dg-V",  # '9/12', '9/19'
                   15: "1b8htir65KEdiXjgEkg5XW3_1lGlXsadL", 16: "1C83jQYmkYrpRikyDg4YjrDsK7aTULxmn"}  # '9/26', '10/3'

L10_video_id_dic = {5: "1njPeT_3aWbECeGIKdpFP79IEk8_43aOp", 6: "1nWzedkYF9LaR8Tu5gBOu1p8nxlJjJ2CC",  # '10/17', '10/24'
                    7: "1SyC2hXxJKFmraJuSIGQXpw5mwS10R9EA", 8: "1SJgxYYur93hxaFfNREhbClImGRYSIxKm",  # '10/31', '11/7'
                    9: "1N_2wiBQ5QtZp2B-DUdMaRgx7rlB3UHuB", 10: "13_Eg-snn4VtGMxfGfKSynD7SlV5u28H1",  # '11/14', '11/21'
                    11: "1M5Vf_D3ha_eArnT8q9P9MuJWflBg6KIH", 13: "1JIXUpT79Ezim0poY95Pk8dYSDyyE5-TL",  # '11/28', '12/12'
                    14: "1BkRBdLBnI_pL0XXpp1hKm60r4Cdym5rF", 15: "1lpskCHYvQlPxXk3SPgiOf0fpmdhTwR-6",  # '12/19', '12/26'
                    16: "1_UNgaPITzWctYdmtbniB0SCQ9IrQ2Ea8", 17: "1M6z6wl3qcH8tnLItDkakCm2c5S8FXaTo"}  # '1/9', '1/16'

L11_video_id_dic = {5: "1mSFKQxlmL4rZPSIG3mTTNNfsqfljNgoS", 6: "1C6pKOnY-fpcjBponMuXr74jw46U3hNSg",  # '1/30', '2/6'
                    7: "1W2Z7fyCx5wu2yL7qhGPjDfKMNGfBHfPV", 8: "1JV9QKitG381MWk2eVMwMVes_3X2Fee0-",  # '2/13', '2/20'
                    9: "1IEqPu7E9w4WZVwO4ZSbZcarAiTFnOrEm", 10: "1BchLC9wFRTO4rGlMlHErrALQgnTMxePQ",  # '3/6', '3/13'
                    11: "1u7_Qq0pPBkOL2lGotUsRJ3QaBquP0hw0", 12: "1jYW3dLh2OOgqUgH9yn8Rz9A0cGe1mZul",  # '3/20', '4/10'
                    13: "1X7DHisKoDKueJmYsCMulkwf-fv7ISgpN", 14: "1titfhhIPEnyLD4E-kEPiprhZ1RCI-noA",  # '4/17', '4/24'
                    15: "15_kJD_cvTbDhCOjZYL8crtGWBtU1-5Ld", 16: "1-QnnLdWMJ8fOxeHkPqA_Do4ICBJYfOK2"}  # '5/1', '5/8'

L12_video_id_dic = {5: "1rtiRbkIIMULlrsFmeHyjv999gvNR_cGD", 6: "1kvOKQIjPNSUbneyQb-Y5bZPJOi6XkGcd",  # '5/15', '5/22'
                    7: "11cTScrFKOtWPx7pwkFuy3G0-M8ByrGp9", 8: "1eTqr2VoMLQyX33V7w3YFumHFcyvuebxL"}  # '5/29', '6/5'

# 週二班
L13_video_id_dic = {5: "1G_Q4sADsZrFmgTIR8wUkuFZRwDxXqIfK", 6: "1Pbiid6V-lQapYGAWgloU1qpcLwMtKPbP",  # '11/22', '11/29'
                    8: "1GrqUmxTPimEKIquh6FMIH9e2IG0uAuoV", 9: "1OuYVtRFTUpzpwCXZ6T_jN4Sjp2966vwO",  # '12/13', '12/20'
                    10: "1VCu-5YI5NmaqCYpbHVKcYL6sBQ6_kyyf", 11: "16lGCtcLS_vDOQARVE70YA4taQneoqZx0",  # '12/27', '1/3'
                    13: "1368m0cTveUA6Wj2FFcdVmKefAPWFYc32", 14: "1P3O_DZm39PioeoLOj6rk4pKZiadqLsvL",  # '1/17', '1/31'
                    15: "12VhOcc3Uk8Wm8nwh-yFU-077kdwgaoGQ", 16: "1IQrpVsk77NSVpkkfw3oteK-dzE9nb7Y8",  # '2/7', '2/14'
                    20: "170W_vAZUJRkwhT2d528C1TG7ATXBM1wr", 21: "1LYemJlVqWpSe61FxQZZBpuY3_mfPacaw"}  # '2/21', '3/7'

L14_video_id_dic = {5: "1CpDLebghx9cM991dQPLvjNwWkyXG06M4", 6: "1_ZrEOsC--rB_PG3DiMft5ZUjd7mj-7Tf",  # '3/14', '3/21'
                    7: "1_3kJYWSi1W0W6tLla7YuhtYjPsc6qcKk", 8: "1J8N490h9B8NnH5afRCSC8v9etcHYdz4q",  # '4/11', '4/18'
                    9: "1sbc9_fZY4EeGCiHTVv2Ykb8Nrvg7PC-A", 10: "1KOomOitYyehw9lhoC3LfyndHqV_HgxaW",  # '4/25', '5/2'
                    11: "1tm3hTg_PQY54mVJEY5ijGU7xhcNlTJSY", 12: "1ptMzNWktZZrkCrKpyxo5tS4CjFfBdYuN",  # '5/9', '5/16'
                    13: "1XtvtOjfdSCz3tWsEuSmNZaod2sOyw25w", 14: "1QuYhPIDK-cWsDZtesJ3wpIsTJTvuC_Fe",  # '5/23', '5/30'
                    15: "1mvK57TqO7YDi5LWddoz5AzJhJgxuH-6P", 16: "1mAOO8c2WqS86Nds7e6CCzWgJq8YS5ZJL"}  # '6/6', '6/13'

L1_video_id_dic = {5: "1eaZzanBkiRrSN4-1AJuKC_SlcY1rKRrJ", 6: "1Hgt4Cd2faD_MG0h3YSYlD8oSWLIAN8EN",  # '6/20', '6/27'
                   7: "1o6uuq6IBD8YwpZVZc-78d8GMkt2hwCmI", 8: "15ur3hRfLIwyEJNC4V6zEHowr8wYRqHVW",  # '7/4', '7/11'
                   9: "19l_k8kvOpWsEdBAjCt1myyknyVUcn0Su", 10: "1rbpiqscG8oT4OnHTBvRPJg9NyenM7tCu",  # '7/18', '7/25'
                   11: "1veMPejEVepEJD5O4y4MOs7EsGPFzxFE0", 12: "1ogWiLlS4jhQ2pmeNAGATaDBgyR7Emo0B",  # '8/1', '8/8'
                   13: "1JkY-loD13VuCv1GP0JAPfL9uBP4qRllq", 14: "1l5rJb_E0YabYSPocoL9hb69nrB1xsOkz",  # '8/15', '8/22'
                   15: "17dkVy1a_9y0sAOzzt_ZR14c-5b8KZfHO", 16: "1Rj1b0qZArw1YCGhx0cyB4kXmqhCZrdEL"}  # '8/29', '9/5'

L2_video_id_dic = {5: "1OYgwxna6vESe9aHdrnYmwZKaDaTrw7Ui", 6: "1m_jiPW2YzYjJdkYRHbs3Bobn-5ovDucw",  # '9/12', '9/19'
                   7: "1Uj3nlUmT4Zn2IldE5PlsjGLGw75EUVCT", 8: "1UzSrPKi-AE2K8NsXAMNy4ckICCLv2UwT",  # '9/26', '10/3'
                   9: "1NMQOVqmPfsWoD7J45_kwwV1t-lelmvo7", 10: "1uOtYwqeOdaNDrhAfRr2p23XeRRyiaPYx",  # '10/17', '10/24'
                   11: "1upkSLTYYJKh-ChDYfvw3v--8faDoF_g5", 12: "1DqMA2nC52Z_C-TtFLnt8RWsWo0tHdPDF",  # '10/31', '11/7'
                   13: "15BjS3NgpBQD1JcHjMIS8Ad93dmkm3VFg", 14: "1TmxQTPQDVhniadl8eGCF_A-wifPmT6SX",  # '11/14', '11/21'
                   15: "1qHzGCMkPAGpWH1kA5Y6rxYjhRkEJOxK0", 16: "18wT6h4mXBN5ZNhAoOowVt5YnJ9k67K4e"}  # '11/28', '12/5'

single_sheet_namelist = ["L4課後雲端", "L5課後雲端", "L6課後雲端", "L7課後雲端", "L9課後雲端", "L10課後雲端", "L11課後雲端",
                         "L12課後雲端", "L13課後雲端", "L14課後雲端", "L1課後雲端", "L2課後雲端"]

# Only used in local
project_path = "/Users/robinhsieh/Programming/Python/CloudFileSharely"
# Only used in CI/CD
# project_path = os.environ.get("GITHUB_WORKSPACE", "")
