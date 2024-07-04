import sys
import os
import blendfile


def bytesToMb(sizeInBytes):
	return sizeInBytes / (1024 * 1024)


def analyzeBlendFile(filePath, thresholdMb):
	blend = blendfile.open_blend(filePath)

	stats = {}
	statsDetailed = {}
	totalSize = 0

	for block in blend.blocks:
		sizeMb = bytesToMb(block.size)
		totalSize += sizeMb

		code = block.code.decode('utf-8').strip()
		if code in stats:
			stats[code] += sizeMb
		else:
			stats[code] = sizeMb

		typeName = block.dna_type_name
		if code not in statsDetailed:
			statsDetailed[code] = {}
		if typeName in statsDetailed[code]:
			statsDetailed[code][typeName] += sizeMb
		else:
			statsDetailed[code][typeName] = sizeMb

	sortedItems = sorted(
		stats.items(),
		key=lambda it: it[1],
		reverse=True
	)
	for key, value in sortedItems:
		if value >= thresholdMb:
			print(f'{key}: {value:.2f} MB')

	print('----------------------')
	print(f'Total: {totalSize:.2f} MB')
	print()

	# remove anything below the threshold
	remove = []
	for code in statsDetailed.keys():
		for typeName, value in statsDetailed[code].items():
			if value < thresholdMb:
				remove.append([code, typeName])
	for code, typeName in remove:
		del statsDetailed[code][typeName]

	# remove empty entries
	remove = []
	for code in statsDetailed.keys():
		if len(statsDetailed[code]) == 0:
			remove.append(code)
	for code in remove:
		del statsDetailed[code]

	for code in statsDetailed.keys():
		print(code)
		sortedItems = sorted(
			statsDetailed[code].items(),
			key=lambda it: it[1],
			reverse=True
		)
		for typeName, value in sortedItems:
			print(f'  {typeName}: {value:.2f} MB')


if __name__ == '__main__':
	blendFilePath = sys.argv[1]
	thresholdMb = float(sys.argv[2])

	if os.path.isfile(blendFilePath):
		analyzeBlendFile(blendFilePath, thresholdMb)
	else:
		print(f'File not found: {blendFilePath}')
