from django import forms

class ForceCalculationForm(forms.Form):
    Q = forms.FloatField(label='轴向外力 (Q)', min_value=0, required=True)
    Z = forms.IntegerField(label='螺栓个数 (Z)', min_value=1, required=True)