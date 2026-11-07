def pick_peaks(arr):

    pos = []
    for i in range(1, len(arr) - 1):
        if arr[i - 1] < arr[i] > arr[i + 1]:
            pos.append(i)
        elif arr[i - 1] < arr[i] == arr[i + 1]:
            j = i
            while j < len(arr) - 2:
                j += 1
                if arr[j] == arr[j+1]:
                    continue
                elif arr[j] > arr[j+1]:
                    pos.append(i)
                    break
                else:
                    break

    peaks = [arr[i] for i in pos]

    return {"pos": pos, "peaks": peaks}


if __name__ == "__main__":
    print(pick_peaks([1,2,3,6,4,1,2,3,2,1]))
    print(pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3]))