import csv

# Define the data
data = [
['R&D Spend', 'Administration',	'Marketing Spend',	'State', 'Profit'],
['165349.2', '136897.8', '471784.1', 'New York', '192261.83'],
['162597.7', '151377.59','443898.53', 'California', '191792.06'],
['153441.51', '101145.55', '407934.54',	'Florida', '191050.39'],
['144372.41', '118671.85', '383199.62',	'New York',	'182901.99'],
['42107.34', '91391.77', '366168.42', 'Florida', '166187.94'],
['131876.9', '99814.71', '362861.36', 'New York', '156991.12'],
['134615.46', '147198.87', '127716.82',	'California', '156122.51'],
['130298.13', '145530.06', '323876.68',	'Florida', '155752.6'],
['120542.52', '148718.95', '311613.29', 'New York', '152211.77'],
['123334.88', '108679.17',	'304981.62', 'California', '149759.96'],
['101913.08', '110594.11', '229160.95',	'Florida', '146121.95'],
['100671.96', '91790.61', '249744.55', 'California', '144259.4'],
['93863.75', '127320.38', '249839.44', 'Florida', '141585.52'],
['91992.39', '135495.07', '252664.93', 'California', '134307.35'],
['119943.24', '156547.42', '256512.92',	'Florida', '132602.65'],
['114523.61', '122616.84', '261776.23',	'New York',	'129917.04'],
['78013.11', '121597.55', '264346.06', 'California', '126992.93'],
['94657.16', '145077.58', '282574.31',	'New York',	'125370.37'],
['91749.16', '114175.79', '294919.57',	'Florida', '124266.9'],
['86419.7',	 '153514.11', '0', 'New York', '122776.86'],
['76253.86', '113867.3', '298664.47', 'California',	'118474.03'],
['78389.47', '153773.43', '299737.29', 'New York', '111313.02'],
['73994.56', '122782.75', '303319.26', 'Florida', '110352.25'],
['67532.53', '105751.03', '304768.73', 'Florida', '108733.99'],
['77044.01', '99281.34', '140574.81', 'New York', '108552.04'],
['64664.71', '139553.16', '137962.62', 'California', '107404.34'],
['75328.87', '144135.98', '134050.07', 'Florida', '105733.54'],
['72107.6',	'127864.55', '353183.81', 'New York', '105008.31'],
['66051.52', '182645.56', '118148.2', 'Florida', '103282.38'],
['65605.48', '153032.06', '107138.38', 'New York', '101004.64'],
['61994.48', '115641.28', '91131.24', 'Florida', '99937.59'],
['61136.38', '152701.92', '88218.23', 'New York', '97483.56'],
['63408.86', '129219.61', '46085.25', 'California',	'97427.84'],
['55493.95', '103057.49', '214634.81', 'Florida', '96778.92'],
['46426.07', '157693.92', '210797.67', 'California', '96712.8'],
['46014.02', '85047.44', '205517.64', 'New York', '96479.51'],
['28663.76', '127056.21', '201126.82', 'Florida', '90708.19'],
['44069.95', '51283.14', '197029.42', 'California',	'89949.14'],
['20229.59', '65947.93', '185265.1', 'New York', '81229.06'],
['38558.51', '82982.09', '174999.3', 'California', '81005.76'],
['28754.33', '118546.05', '172795.67', 'California', '78239.91'],
['27892.92', '84710.77', '164470.71', 'Florida', '77798.83'],
['23640.93', '96189.63', '148001.11', 'California', '71498.49'],
['15505.73', '127382.3', '35534.17', 'New York', '69758.98'],
['22177.74', '154806.14', '28334.72', 'California',	'65200.33'],
['1000.23',	'124153.04', '1903.93',	 'New York', '64926.08'],
['1315.46',	'115816.21', '297114.46', 'Florida', '49490.75'],
['0', '135426.92',	'0', 'California',	'42559.73'],
['542.05', '51743.15',	'0', 'New York', '35673.41'],
['0', '116983.8', '45173.06', 'California',	'14681.4'],

]

# Specify the file path
file_path = '/Users/jogbaner/Multiple_Linear_Regression/50_startups.csv'

# Write the data to the CSV file
with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"Startups data CSV file has created successfully at {file_path}")