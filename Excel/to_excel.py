import pandas as pd

df = pd.DataFrame({'Name': ['Manchester City', 'Real Madrid', 'Liverpool',
                            'FC Bayern München', 'FC Barcelona', 'Juventus'],
                   'League': ['English Premier League (1)', 'Spain Primera Division (1)',
                              'English Premier League (1)', 'German 1. Bundesliga (1)',
                              'Spain Primera Division (1)', 'Italian Serie A (1)'],
                   'TransferBudget': [176000000, 188500000, 90000000,
                                      100000000, 180500000, 105000000]})
df.to_excel('teams.xlsx')