from django.shortcuts import render
from django.http import HttpResponse,HttpResponseBadRequest

def one(request):
    return HttpResponse(" hey i am first app of your project ")

# Create your views here.
def userform(request):
    ans = 0
    try:
        if request.method == "GET":
            n1 = int(request.GET.get('n1', 0))
            n2 = int(request.GET.get('n2', 0))
            ans = n1 + n2
    except (TypeError, ValueError):
        ans = "Invalid input. Please enter valid integers."
    return render(request, "one/userform.html", {'ans': ans})

def user(request):
    ans = 0
    data = {
        'n1': '',
        'n2': '',
        'ans': ans
    }
    try:
        if request.method == "POST":
            n1 = int(request.POST.get('n1', 0))
            n2 = int(request.POST.get('n2', 0))
            ans = n1 + n2
            data = {
                'n1': n1,
                'n2': n2,
                'ans': ans
            }
    except (TypeError, ValueError):
        data['ans'] = "Invalid input. Please enter valid integers."
    return render(request, "one/userpost.html", data)

def calculator(request):
    result = ''
    if request.method == 'POST':
        try:
            n1 = int(request.POST.get('n1'))
            n2 = int(request.POST.get('n2'))
            opr = request.POST.get('opr')
            if opr == '+':
                result = n1 + n2
            elif opr == '-':
                result = n1 - n2
            elif opr == '*':
                result = n1 * n2
            elif opr == '/':
                result = n1 / n2
            else:
                result = "Invalid operator"
        except :
            pass
    
    return render(request, "one/calculator.html", {'result': result})


def evenodd(request):
    ans = ''
    if request.method == "POST":
        try:
            n1 = int(request.POST.get('n1'))
            if n1 % 2 == 0:
                ans = "Even Number"
            else:
                ans = "Odd Number"
        except ValueError:
            ans = "Please enter a valid number"
    return render(request, "one/evenodd.html", {'ans': ans})

def calculate_marks(request):
    total = 0
    percentage = 0
    grade = ''
    if request.method == "POST":
        try:
            marks = []
            for i in range(1, 6):
                mark = int(request.POST.get(f'subject{i}', 0))
                marks.append(mark)
            
            total = sum(marks)
            percentage = (total / 500) * 100
            
            if percentage >= 90:
                grade = 'A'
            elif percentage >= 80:
                grade = 'B'
            elif percentage >= 70:
                grade = 'C'
            elif percentage >= 60:
                grade = 'D'
            else:
                grade = 'F'
        except ValueError:
            total = "Invalid input"
            percentage = "Invalid input"
            grade = "Invalid input"
            
    return render(request, "one/calculate_marks.html", {'total': total, 'percentage': percentage, 'grade': grade})
