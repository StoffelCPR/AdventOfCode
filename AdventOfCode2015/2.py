with open("resources/2.txt", 'r') as present_list:
    presents = present_list.readlines()

square_feet = 0
feet_of_ribbon = 0

for present in presents:
    present_measurements = [int(x) for x in present.split("x")]
    length_width = present_measurements[0] * present_measurements[1]
    width_height = present_measurements[1] * present_measurements[2]
    height_length = present_measurements[2] * present_measurements[0]

    square_feet_smallest_side = min(length_width, width_height, height_length)
    square_feet += 2 * length_width + 2 * width_height + 2 * height_length + square_feet_smallest_side

    feet_of_ribbon += present_measurements[0] * present_measurements[1] * present_measurements[2]
    present_measurements.sort()
    feet_of_ribbon += 2 * present_measurements[0] + 2 * present_measurements[1]

print("Wrapping paper: " + str(square_feet))
print("Feet of ribbon: " + str(feet_of_ribbon))


