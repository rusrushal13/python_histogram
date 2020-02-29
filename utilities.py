from constants import INTEGER_ONE


def count_in_between(inputs, first_value, second_value):
    """
    Count the numbers between the two values.

    ARGS:
        inputs(list)
        first_value(int)
        second_value(int)
    """
    count = 0
    for element in inputs:
        if element >= first_value and element < second_value:
            count += INTEGER_ONE
    return count


def fetch_inputs():
    """
    Fetch inputs for the program.

    ARGS:
    """
    with open('inputs.txt', 'r') as file:
        data = file.readlines()
        comma_seperated_inputs = list(map(int, data[0].split(',')))
        bucket_size = int(data[1])

    return comma_seperated_inputs, bucket_size


def fetch_min_max_bucket_sizes(inputs, bucket_size):
    """
    Fetch the bucket sizes from the inputs given.

    ARGS:
        inputs(list)
        bucket_size(int)
    """
    min_bucket_size = min(INTEGER_ONE, min(inputs))
    if min_bucket_size < 0:
        min_bucket_size += 1 - bucket_size
    max_bucket_size = max(inputs) // bucket_size + INTEGER_ONE
    return min_bucket_size, max_bucket_size


def show_histogram(histogram):
    """
    Print the histogram on the screen.

    ARGS:
        histogram(list): List of list contain buckets and count.
    """
    for key, value in histogram:
        print('{} : {}'.format(key, value))
