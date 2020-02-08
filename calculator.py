import math

print('There are:', (21 * 60) + 15, 'seconds in 21 minutes and 15 seconds')

print('There are', 5 * 0.6, 'miles in 5 kilometers')

seconds = (21 * 60) + 15

pace = (21.25 / 5) * 1.609 * 60

minutes = int(pace / 60)

seconds = int(pace % 60)

print('Average pace is:', minutes, 'minutes and', seconds, 'seconds per mile')
