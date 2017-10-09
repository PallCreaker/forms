from django import forms
from .models import Drilling

class DrillModelForm(forms.ModelForm):

    DRILLING_CHOICE = (
        ('long_drill', 'ロングドリル'),
        ('gide_drill', 'ガイドドリル')
    )
    DRILLING_EXCHANGE = (
        ('new_drill', '新品'),
        ('Regrinding', '再研磨')
    )
    DRILLING_STARTEND = (
        ('start', '開始'),
        ('end', '終了')
    )
    drilling = forms.ChoiceField(label='ドリル選択', choices=DRILLING_CHOICE, widget=forms.RadioSelect())
    drilling_exchange = forms.ChoiceField(label='新品 or 再研磨', choices=DRILLING_EXCHANGE, widget=forms.RadioSelect())
    StartEnd = forms.ChoiceField(label='開始 or 終了', choices=DRILLING_STARTEND, widget=forms.RadioSelect())

    class Meta:
        model = Drilling
        fields = "__all__"
 
    # def __init__(self, *args, **kwargs):
        # super().__init__(*args, **kwargs)
        # for field in self.fields.values():
            # print(field)
            # if not field.name in ['drilling', 'drilling_exchange', 'StartEnd']:
            # field.widget.attrs["class"] = "form-control"