from django import forms
from django.core.exceptions import ValidationError
from .models import Coupon
from django.utils import timezone
from django.shortcuts import get_object_or_404

class CouponApplyForm(forms.Form):
    code = forms.CharField(label='Coupon',)

    def clean_code(self):
        now = timezone.now()
        code = self.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__iexact=code)
        except Coupon.DoesNotExist:
            raise ValidationError("Coupon does not exist.")

        if(coupon.valid_from>now or coupon.valid_to <now):
            raise ValidationError("Coupon expired.")
        elif(not coupon.active):
            raise ValidationError("Coupon is no longer valid.")

        return code
