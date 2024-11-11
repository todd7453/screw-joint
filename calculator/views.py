from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ForceCalculationForm
from django.contrib import messages
from .models import Calculation


def home(request):
    return render(request, 'calculator/home.html')

def force_analysis(request):
    return render(request, 'calculator/force_analysis.html')  # 입력 페이지로 이동

def shouli1(request):
    Q = None  # Q 값 초기화
    Z = None  # Z 값 초기화
    shouli1 = None  # 결과 초기화

    if request.method == 'POST':
        try:
            Q = float(request.POST.get('Q'))  # 축 방향 외력 (N)
            Z = int(request.POST.get('Z'))     # 볼트 개수

            if Z <= 0:
                messages.error(request, 'Z应大于0')
                return render(request, 'calculator/force_analysis.html')  # 입력 페이지로 돌아가기
            else:
                shouli1 = Q / Z  # F = Q / Z 계산

                return render(request, 'calculator/shouli1.html', {
                    'Q': Q,
                    'Z': Z,
                    'shouli1': shouli1
                })

        except (ValueError, TypeError):
            messages.error(request, '유효한 숫자를 입력해 주세요.')
            return render(request, 'calculator/force_analysis.html')  # 입력 페이지로 돌아가기

    return render(request, 'calculator/shouli1.html', {
        'Q': Q,
        'Z': Z,
        'shouli1': shouli1
    })

def shouli2(request):
    μ = None 
    m = None 
    Z1 = None 
    kf = None 
    R = None 
    shouli2 = None 

    if request.method == 'POST':
        try:
            μ = float(request.POST.get('μ'))  
            Z1 = int(request.POST.get('Z1'))     
            m = int(request.POST.get('m'))
            kf = float(request.POST.get('kf')) 
            R = float(request.POST.get('R')) 

            if Z1 <= 0 or m <= 0 or Z1 <= 0:
                messages.error(request, '请输入正确的值')
                return render(request, 'calculator/force_analysis.html')  # 입력 페이지로 돌아가기
            else:
                shouli2 = (kf * R) / (μ * m * Z1) 
                
                return render(request, 'calculator/shouli2.html', {
                    'μ': μ,
                    'Z1': Z1,
                    'm': m,
                    'kf': kf,
                    'R': R,
                    'shouli2': shouli2
                })

        except (ValueError, TypeError):
            messages.error(request, '유효한 숫자를 입력해 주세요.')
            return render(request, 'calculator/force_analysis.html')  # 입력 페이지로 돌아가기

    return render(request, 'calculator/shouli2.html', {
        'μ': μ,
        'Z1': Z1,
        'm': m,
        'kf': kf,
        'R': R,
        'shouli2': shouli2
    })



def strength_calculation(request):
    return render(request, 'calculator/strength_calculation.html')

def shape_material_analysis(request):
    return render(request, 'calculator/shape_material_analysis.html')

def standard_support(request):
    return render(request, 'calculator/standard_support.html')

def thread_parameter_definition(request):
    return render(request, 'calculator/thread_parameter_definition.html')
