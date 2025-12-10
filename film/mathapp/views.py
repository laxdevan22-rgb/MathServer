from django.shortcuts import render
def measure(request):
    km = int(request.POST.get('range', 0))
    lt = int(request.POST.get('energize', 0))
    measure = km /lt if request.method == 'POST' else 0
    print("range=",km)
    print("energize=",lt)
    print("measure=",measure)
    return render(request, 'mathapp/solomon.html', {'km': km, 'lt': lt, 'measure': measure})

