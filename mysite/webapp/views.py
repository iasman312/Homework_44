from django.shortcuts import render

secret_nums = [5, 1, 2, 9]


def index_view(request):
    return render(request, 'index.html')


def results(request):
    numbers = list(map(int, request.POST.split(' ')))
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
    context = {'cows': cows, 'bulls': bulls}
    return render(request, 'index.html', context)


