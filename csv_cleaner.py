import pandas

columns_to_keep = ['points', 'reboundsTotal', 'assists', 'turnovers', 'personId', 'gameId', 'playerteamName']

chunk_size = 4000

input_file = 'PlayerStatistics.csv'
output_file = 'PlayerStatsFinalFinal.csv'

first_chunk = True

for chunk in pandas.read_csv(input_file, usecols=columns_to_keep, chunksize = chunk_size):
	chunk.to_csv(output_file, mode='a', header=first_chunk, index = False)
	first_chunk = False



