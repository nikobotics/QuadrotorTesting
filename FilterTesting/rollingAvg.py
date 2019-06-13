def resolve_carrier_signal_ROLL_AVG(data, length = 10):
    s = len(data)
    newData = [0] * s
    sum = 0
    lastN = [0] * length

    for a in range(s):
        next = data[a]
        nextI = a % length
        sum += next
        sum -= lastN[nextI]
        lastN[nextI] = next

        if a < length:
            if a == 0:
                newData[a] = sum
            else:
                newData[a] = sum / a
        else:
            newData[a] = sum / length
    
    return newData

