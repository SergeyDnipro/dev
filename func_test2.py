def car_speed(**kwargs):
    for func_argument in kwargs:
        if kwargs[func_argument] < 0:
            raise ValueError('ERROR')
    result_distance = kwargs['speed'] * kwargs['time']
    return f"weight: {kwargs['weight']}, " \
           f"time: {kwargs['time']}, " \
           f"speed:{kwargs['speed']}, " \
           f"result_distance:{result_distance}"


if __name__ == 'main':
    print(car_speed(time=10, speed=-1, weight=1000))