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
            messages.error(request, '请输入有效的数字。')
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
                messages.error(request, '请输入有效的数字。')
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
            messages.error(request, '请输入有效的数字。')
            return render(request, 'calculator/force_analysis.html')  # 입력 페이지로 돌아가기

    return render(request, 'calculator/shouli2.html', {
        'μ': μ,
        'Z1': Z1,
        'm': m,
        'kf': kf,
        'R': R,
        'shouli2': shouli2
    })

def shouli3(request):
    R = None  # Q 값 초기화
    Z3 = None  # Z 값 초기화
    shouli3 = None  # 결과 초기화

    if request.method == 'POST':
        try:
            R = float(request.POST.get('R'))  # 축 방향 외력 (N)
            Z3 = int(request.POST.get('Z3'))     # 볼트 개수

            if Z3 <= 0:
                messages.error(request, 'Z应大于0')
                return render(request, 'calculator/force_analysis.html')  # 입력 페이지로 돌아가기
            else:
                shouli3 = R / Z3  # F = Q / Z 계산

                return render(request, 'calculator/shouli3.html', {
                    'R': R,
                    'Z3': Z3,
                    'shouli3': shouli3
                })

        except (ValueError, TypeError):
            messages.error(request, '请输入有效的数字。')
            return render(request, 'calculator/force_analysis.html')  # 입력 페이지로 돌아가기

    return render(request, 'calculator/shouli3.html', {
        'R': R,
        'Z3': Z3,
        'shouli3': shouli3
    })

def shouli4(request):
    μ = None
    T = None
    kf = None
    shouli4 = None
    r_values = []
    r_index = 1

    if request.method == 'POST':
        try:
            kf = float(request.POST.get('kf'))
            T = float(request.POST.get('T'))
            μ = float(request.POST.get('μ'))

            while f'r{r_index}' in request.POST:
                r_value = float(request.POST[f'r{r_index}'])
                r_values.append(r_value)
                r_index += 1
                if not r_values:
                    messages.error(request, "请输入r值！")
                    return render(request, 'calculator/force_analysis.html')
                r_sum = sum(r_values)# Use rMax if r values are empty
                if r_sum == 0:
                    messages.error(request,"r值之和为零，无法计算。")
                    return render(request, 'calculator/force_analysis.html')
                shouli4 = (kf * T) / (μ * r_sum)
            return render(request, 'calculator/shouli4.html', {
                'shouli4': shouli4,
                'kf': kf,
                'T': T,
                'μ': μ,
                'r_values': r_values
            })

        except ValueError:
            messages.error(request, '请输入有效的数字。')
            return render(request, 'calculator/force_analysis.html')

    return render(request, 'calculator/shouli4.html', {
        'shouli4': shouli4,
        'kf': kf,
        'T': T,
        'μ': μ,
        'r_values': r_values      
    })

def shouli5(request):
    M = None
    shouli5 = None
    r_values5 = []
    r_index5 = 1

    if request.method == 'POST':
        try:
            M = float(request.POST.get('M'))
            while f'r{r_index5}' in request.POST:
                r_value5 = float(request.POST[f'r{r_index5}'])
                r_values5.append(r_value5)
                r_index5 += 1
                if not r_values5:
                    messages.error(request, "请输入r值！")
                    return render(request, 'calculator/force_analysis.html')
                r_max = max(r_values5)
                r_sum5 = sum([r**2 for r in r_values5])# Use rMax if r values are empty
                if r_sum5 == 0:
                    messages.error(request,"r值之和为零，无法计算。")
                    return render(request, 'calculator/force_analysis.html')
                shouli5 = (M * r_max) / (r_sum5)
            return render(request, 'calculator/shouli5.html', {
                'shouli5': shouli5,
                'M': M,
                'r_values5': r_values5,
                'r_max': r_max
            })

        except ValueError:
            messages.error(request, '请输入有效的数字。')
            return render(request, 'calculator/force_analysis.html')

    return render(request, 'calculator/shouli5.html', {
                'shouli5': shouli5,
                'M': M,
                'r_values5': r_values5,
                'r_max': r_max     
    })

def shouli6(request):
    σ_s = None  
    d1 = None  
    d2 = None 
    H = None 
    shouli6 = None  # 결과 초기화

    if request.method == 'POST':
        try:
            σ_s = float(request.POST.get('σ_s'))  # 축 방향 외력 (N)
            d1 = float(request.POST.get('d1'))  # 축 방향 외력 (N)
            d2 = float(request.POST.get('d2'))  # 축 방향 외력 (N)
            H = float(request.POST.get('H'))  # 축 방향 외력 (N)
            material = request.POST.get('material')

            if material == 'carbonSteel':
                material_text = "碳素钢"
                shouli6 = 0.65 * σ_s * 3.14159 * ((d2 + d1 - H/6) ** 2) / 16
            elif material == 'alloySteel':
                material_text = "合金钢"
                shouli6 = 0.75 * σ_s * 3.14159 * ((d2 + d1 - H/6) ** 2) / 16
        except (ValueError, TypeError):
            messages.error(request, '请输入有效的数字。')
            return render(request, 'calculator/force_analysis.html')

    return render(request, 'calculator/shouli6.html', {
        'σ_s': σ_s,
        'd1': d1,
        'd2': d2,
        'H': H,
        'shouli6': shouli6,
        'material': material_text
    })

def shouli7(request):
    K = None  # Q 값 초기화
    F = None  # Z 값 초기화
    d = None  # 결과 초기화
    shouli7 = None

    if request.method == 'POST':
        try:
            K = float(request.POST.get('K'))  # 축 방향 외력 (N)
            F = float(request.POST.get('F'))     # 볼트 개수
            d = float(request.POST.get('d'))     # 볼트 개수

            if K == 0  or d <= 0:
                messages.error(request, '输入值应大于0')
                return render(request, 'calculator/force_analysis.html')  # 입력 페이지로 돌아가기
            else:
                shouli7 = ((K * F) * d)

                return render(request, 'calculator/shouli7.html', {
                    'K': K,
                    'F': F,
                    'd': d,
                    'shouli7': shouli7
                })

        except (ValueError, TypeError):
            messages.error(request, '请输入有效的数字。')
            return render(request, 'calculator/force_analysis.html')  # 입력 페이지로 돌아가기

    return render(request, 'calculator/shouli7.html', {
        'K': K,
        'F': F,
        'd': d,
        'shouli7': shouli7
    })

    F = None 
    σ_s = None  
    qiangdu1 = None 

    if request.method == 'POST':
        try:
            F = float(request.POST.get('F'))  # 축 방향 외력 (N)
            σ_s = float(request.POST.get('σ_s'))  # 축 방향 외력 (N)


            if σ_s == 0:
                messages.error(request, 'Z不能为0')
                return render(request, 'calculator/strength_calculation.html')  # 입력 페이지로 돌아가기
            else:
                qiangdu1 = ( (5.8 * F) / (3.14159 * σ_s) ) ** (1/2) # F = Q / Z 계산

                return render(request, 'calculator/qiangdu1.html', {
                    'F': F,
                    'σ_s': σ_s,
                    'qiangdu1': qiangdu1
                })

        except (ValueError, TypeError):
            messages.error(request, '请输入有效的数字。')
            return render(request, 'calculator/strength_calculation.html')  # 입력 페이지로 돌아가기

    return render(request, 'calculator/qiangdu1.html', {
        'F': F,
        'σ_s': σ_s,
        'qiangdu1': qiangdu1
    })

def qiangdu1(request):
    F = None 
    σ_s = None  
    d1 = None
    qiangdu1 = None 
    result1 = None

    if request.method == 'POST':
        try:
            F = float(request.POST.get('F'))  # 축 방향 외력 (N)
            σ_s = float(request.POST.get('σ_s'))  # 축 방향 외력 (N)
            d1 = float(request.POST.get('d1'))

            if d1 == 0:
                messages.error(request, 'd1不能为0')
                return render(request, 'calculator/strength_calculation.html')  # 입력 페이지로 돌아가기
            else:
                qiangdu1 = ( (6.8 * F) / (3.14159 * (d1 ** 2)) ) 

                if qiangdu1 <= σ_s:
                    result1 = '校核通过'
                    
                    return render(request, 'calculator/qiangdu1.html', {
                        'F': F,
                        'σ_s': σ_s,
                        'd1' : d1,
                        'qiangdu1': qiangdu1,
                        'result1': result1
                    })
               
                else:
                    result1 = '校核未通过'

                    return render(request, 'calculator/qiangdu1.html', {
                        'F': F,
                        'σ_s': σ_s,
                        'd1' : d1,
                        'qiangdu1': qiangdu1,
                        'result1': result1
                    })

        except (ValueError, TypeError):
            messages.error(request, '请输入有效的数字。')
            return render(request, 'calculator/strength_calculation.html')  # 입력 페이지로 돌아가기

    return render(request, 'calculator/qiangdu1.html', {
        'F': F,
        'σ_s': σ_s,
        'd1' : d1,
        'qiangdu1': qiangdu1,
        'result1': result1
    })

def qiangdu2(request):
    F = None 
    σ_s = None  
    d1 = None
    S_s = None
    qiangdu2_1 = None 
    qiangdu2_2 = None 
    result2 = None

    if request.method == 'POST':
        try:
            F = float(request.POST.get('F'))  # 축 방향 외력 (N)
            σ_s = float(request.POST.get('σ_s'))  # 축 방향 외력 (N)
            d1 = float(request.POST.get('d1'))
            S_s = float(request.POST.get('S_s'))

            if d1 == 0:
                messages.error(request, 'd1不能为0')
                return render(request, 'calculator/strength_calculation.html')  # 입력 페이지로 돌아가기
            else:
                qiangdu2_1 = ( (5.2 * F) / (3.14159 * (d1 ** 2)) ) 
                qiangdu2_2 = (σ_s / S_s)

                if qiangdu2_1 <= qiangdu2_2:
                    result2 = '校核通过'
                    
                    return render(request, 'calculator/qiangdu2.html', {
                        'F': F,
                        'σ_s': σ_s,
                        'S_s': S_s,
                        'd1' : d1,
                        'qiangdu2_1': qiangdu2_1,
                        'qiangdu2_2': qiangdu2_2,
                        'result2': result2
                    })
               
                else:
                    result2 = '校核未通过'

                    return render(request, 'calculator/qiangdu2.html', {
                        'F': F,
                        'σ_s': σ_s,
                        'S_s': S_s,
                        'd1' : d1,
                        'qiangdu2_1': qiangdu2_1,
                        'qiangdu2_2': qiangdu2_2,
                        'result2': result2
                    })

        except (ValueError, TypeError):
            messages.error(request, '请输入有效的数字。')
            return render(request, 'calculator/strength_calculation.html')  # 입력 페이지로 돌아가기

    return render(request, 'calculator/qiangdu1.html', {
        'F': F,
        'σ_s': σ_s,
        'S_s': S_s,
        'd1' : d1,
        'qiangdu2_1': qiangdu2_1,
        'qiangdu2_2': qiangdu2_2,
        'result2': result2
    })

def qiangdu3(request):
    ε = None 
    Kt = None  
    Ku = None
    σ1t = None
    Kσ = None 
    Sa = None 
    qiangdu3 = None

    if request.method == 'POST':
        try:
            ε = float(request.POST.get('ε'))  # 축 방향 외력 (N)
            Kt = float(request.POST.get('Kt'))  # 축 방향 외력 (N)
            Ku = float(request.POST.get('Ku'))
            σ1t = float(request.POST.get('σ1t'))
            Kσ = float(request.POST.get('Kσ'))
            Sa = float(request.POST.get('Sa'))

            if Kσ == 0 or Sa == 0:
                messages.error(request, 'Kσ和Sa不能为0')
                return render(request, 'calculator/qiangdu3.html')  # 입력 페이지로 돌아가기
            else:
                qiangdu3 = ( (ε * Kt * Ku * σ1t) / (Kσ * Sa) ) 

                return render(request, 'calculator/qiangdu3.html', {
                    'ε': ε,
                    'Kt': Kt,
                    'Ku': Ku,
                    'σ1t' : σ1t,
                    'Kσ' : Kσ,
                    'Sa' : Sa,
                    'qiangdu3': qiangdu3,
                })

        except (ValueError, TypeError):
            messages.error(request, '请输入有效的数字。')
            return render(request, 'calculator/strength_calculation.html')  # 입력 페이지로 돌아가기
    
    return render(request, 'calculator/qiangdu3.html', {
        'ε': ε,
        'Kt': Kt,
        'Ku': Ku,
        'σ1t' : σ1t,
        'Kσ' : Kσ,
        'Sa' : Sa,
        'qiangdu3': qiangdu3
    })

def qiangdu4(request):
    σap = None 
    F = None  
    d1 = None
    CL = None
    CF = None 
    qiangdu4 = None 
    result4 = None

    if request.method == 'POST':
        try:
            σap = float(request.POST.get('σap'))
            F = float(request.POST.get('F'))  # 축 방향 외력 (N)
            d1 = float(request.POST.get('d1'))  # 축 방향 외력 (N)
            CL = float(request.POST.get('CL'))
            CF = float(request.POST.get('CF'))
            gd = CL + CF

            if d1 == 0 or gd == 0:
                messages.error(request, 'd1和(C_L+C_F)不能为0')
                return render(request, 'calculator/strength_calculation.html')  # 입력 페이지로 돌아가기
            else:
                qiangdu4 = (2 * F / (3.14159 * (d1 ** 2))) * (CL / gd)

                if qiangdu4 <= σap:
                    result4 = '校核通过'
                    
                    return render(request, 'calculator/qiangdu4.html', {
                        'F': F,
                        'σap': σap,
                        'CL': CL,
                        'CF': CF,
                        'd1' : d1,
                        'qiangdu4': qiangdu4,
                        'result4': result4
                    })
               
                else:
                    result4 = '校核未通过'

                    return render(request, 'calculator/qiangdu4.html', {
                        'F': F,
                        'σap': σap,
                        'CL': CL,
                        'CF': CF,
                        'd1' : d1,
                        'qiangdu4': qiangdu4,
                        'result4': result4
                    })

        except (ValueError, TypeError):
            messages.error(request, '请输入有效的数字。')
            return render(request, 'calculator/strength_calculation.html')  # 입력 페이지로 돌아가기

    return render(request, 'calculator/qiangdu4.html', {
        'F': F,
        'σap': σap,
        'CL': CL,
        'CF': CF,
        'd1' : d1,
        'qiangdu4': qiangdu4,
        'result4': result4
    })

def qiangdu5(request):
    σ_s = None  
    Fs = None  
    m = None 
    d0 = None 
    qiangdu5_1 = None
    qiangdu5_2 = None
    result5 = None

    if request.method == 'POST':
        try:
            σ_s = float(request.POST.get('σ_s'))  # 축 방향 외력 (N)
            Fs = float(request.POST.get('Fs'))  # 축 방향 외력 (N)
            m = int(request.POST.get('m'))  # 축 방향 외력 (N)
            d0 = float(request.POST.get('d0'))  # 축 방향 외력 (N)
            zaihe = request.POST.get('zaihe')
            
            if d0 == 0 or m == 0:
                messages.error(request, 'd1和(C_L+C_F)不能为0')
                return render(request, 'calculator/strength_calculation.html') 
            else:
                if zaihe == 'jingzaihe':
                    zaihe_text = "静载荷"
                    qiangdu5_1 = (4 * Fs / (m * 3.14159 * (d0 ** 2)))
                    qiangdu5_2 = σ_s / 2.5

                    if qiangdu5_1 <= qiangdu5_2: 
                        result5 = '校核通过'

                        return render(request, 'calculator/qiangdu5.html', {
                        'σ_s': σ_s,
                        'Fs': Fs,
                        'm': m,
                        'd0': d0,
                        'qiangdu5_1': qiangdu5_1,
                        'qiangdu5_2': qiangdu5_2,
                        'zaihe': zaihe_text,
                        'result5': result5
                    })

                    else:
                        result5 = '校核未通过'

                        return render(request, 'calculator/qiangdu5.html', {
                            'σ_s': σ_s,
                            'Fs': Fs,
                            'm': m,
                            'd0': d0,
                            'qiangdu5_1': qiangdu5_1,
                            'qiangdu5_2': qiangdu5_2,
                            'zaihe': zaihe_text,
                            'result5': result5
                        })

                elif zaihe == 'bianzaihe':
                    zaihe_text = "变载荷"
                    qiangdu5_1 = (4 * Fs / (m * 3.14159 * (d0 ** 2)))
                    qiangdu5_2 = σ_s / 4.25

                    if qiangdu5_1 <= qiangdu5_2: 
                        result5 = '校核通过'

                        return render(request, 'calculator/qiangdu5.html', {
                        'σ_s': σ_s,
                        'Fs': Fs,
                        'm': m,
                        'd0': d0,
                        'qiangdu5_1': qiangdu5_1,
                        'qiangdu5_2': qiangdu5_2,
                        'zaihe': zaihe_text,
                        'result5': result5
                    })

                    else:
                        result5 = '校核未通过'

                        return render(request, 'calculator/qiangdu5.html', {
                            'σ_s': σ_s,
                            'Fs': Fs,
                            'm': m,
                            'd0': d0,
                            'qiangdu5_1': qiangdu5_1,
                            'qiangdu5_2': qiangdu5_2,
                            'zaihe': zaihe_text,
                            'result5': result5
                        })

        except (ValueError, TypeError):
            messages.error(request, '请输入有效的数字。')
            return render(request, 'calculator/strength_calculation.html')

    return render(request, 'calculator/qiangdu5.html', {
        'σ_s': σ_s,
        'Fs': Fs,
        'm': m,
        'd0': d0,
        'qiangdu5_1': qiangdu5_1,
        'qiangdu5_2': qiangdu5_2,
        'zaihe': zaihe_text,
        'result5': result5
    })

def qiangdu6(request):
    σ_s = None  
    Fs = None  
    d0 = None 
    δ = None
    qiangdu6_1 = None
    qiangdu6_2 = None
    result6 = None

    if request.method == 'POST':
        try:
            σ_s = float(request.POST.get('σ_s'))  # 축 방향 외력 (N)
            Fs = float(request.POST.get('Fs'))  # 축 방향 외력 (N)
            d0 = float(request.POST.get('d0'))  
            δ = float(request.POST.get('δ'))  # 축 방향 외력 (N)
            jinshu = request.POST.get('jinshu')
            
            if d0 == 0 or δ == 0:
                messages.error(request, 'd1和δ不能为0')
                return render(request, 'calculator/strength_calculation.html') 
            else:
                if jinshu == 'gang':
                    jinshu_text = "钢"
                    qiangdu6_1 = (Fs / (d0 * δ))
                    qiangdu6_2 = σ_s / 1.25

                    if qiangdu6_1 <= qiangdu6_2: 
                        result6 = '校核通过'

                        return render(request, 'calculator/qiangdu6.html', {
                        'σ_s': σ_s,
                        'Fs': Fs,
                        'd0': d0,
                        'δ': δ,
                        'qiangdu6_1': qiangdu6_1,
                        'qiangdu6_2': qiangdu6_2,
                        'jinshu': jinshu_text,
                        'result6': result6
                    })

                    else:
                        result6 = '校核未通过'

                        return render(request, 'calculator/qiangdu6.html', {
                            'σ_s': σ_s,
                            'Fs': Fs,
                            'd0': d0,
                            'δ': δ,
                            'qiangdu6_1': qiangdu6_1,
                            'qiangdu6_2': qiangdu6_2,
                            'jinshu': jinshu_text,
                            'result6': result6
                        })

                elif jinshu == 'zhutie':
                    jinshu_text = "铸铁"
                    qiangdu6_1 = ( Fs / (d0 * δ))
                    qiangdu6_2 = σ_s / 2.25

                    if qiangdu6_1 <= qiangdu6_2: 
                        result6 = '校核通过'

                        return render(request, 'calculator/qiangdu6.html', {
                        'σ_s': σ_s,
                        'Fs': Fs,
                        'd0': d0,
                        'δ': δ,
                        'qiangdu6_1': qiangdu6_1,
                        'qiangdu6_2': qiangdu6_2,
                        'jinshu': jinshu_text,
                        'result6': result6
                    })

                    else:
                        result6 = '校核未通过'

                        return render(request, 'calculator/qiangdu6.html', {
                        'σ_s': σ_s,
                        'Fs': Fs,
                        'd0': d0,
                        'δ': δ,
                        'qiangdu6_1': qiangdu6_1,
                        'qiangdu6_2': qiangdu6_2,
                        'jinshu': jinshu_text,
                        'result6': result6
                        })

        except (ValueError, TypeError):
            messages.error(request, '请输入有效的数字。')
            return render(request, 'calculator/strength_calculation.html')

    return render(request, 'calculator/qiangdu6.html', {
        'σ_s': σ_s,
        'Fs': Fs,
        'd0': d0,
        'δ': δ,
        'qiangdu6_1': qiangdu6_1,
        'qiangdu6_2': qiangdu6_2,
        'jinshu': jinshu_text,
        'result6': result6
    })

def strength_calculation(request):
    return render(request, 'calculator/strength_calculation.html')

def shape_material_analysis(request):
    return render(request, 'calculator/shape_material_analysis.html')

def standard_support(request):
    return render(request, 'calculator/standard_support.html')

def thread_parameter_definition(request):
    return render(request, 'calculator/thread_parameter_definition.html')
