from django.shortcuts import render

secret_nums = [5, 1, 2, 9]


def index_view(request):
    return render(request, 'index.html')


def results(request):
    error = None
    try:
        numbers = list(map(int, request.POST.split(' ')))
    except:
        error = "Enter integers"
        return
    for i in numbers:
        if 0 >= i > 9:
            error = "Enter a number between 0 and 10"
    if len(numbers) != 4:
        error = "Enter 4 digits"
    elif set(numbers) != 4:
        error = "Enter 4 different digits"
    cows = 0
    bulls = 0
    count = 0
    for i in secret_nums:
        for j in numbers:
            if i == j:
                cows += 1
    for i in range(0, 4):
        if secret_nums[i] == numbers[i]:
            bulls += 1
            count += 1
    cows -= bulls
    context = {'cows': cows, 'bulls': bulls, 'error': error}
    return render(request, 'index.html', context)


