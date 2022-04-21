def bubbleSort(array):
    # loop to access each array element
    for i in range(10):

        # loop to compare array elements
        for i in range(0, (10) - i - 1):

            # compare two adjacent elements
            # change > to < to sort in descending order
            if [i] > [i + 1]:
                # swapping elements if elements
                # are not in the intended order
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp


            data = [-2, 45, 0, 11, -9]

            bubbleSort(data)

            print('Sorted Array in Ascending Order:')
            print(data)