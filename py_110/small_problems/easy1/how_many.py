def count_occurrences(vehicles):
    tally = {
            vehicle: vehicles.count(vehicle)
            for vehicle in vehicles
            }
    
    for key, value in tally.items():
        print(f'{key} => {value}')

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)