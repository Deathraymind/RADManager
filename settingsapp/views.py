from django.shortcuts import render, redirect
from .forms import AppSettingsForm
from .models import AppSettings

def edit_settings(request):
    settings = AppSettings.objects.first()
    if request.method == 'POST':
        form = AppSettingsForm(request.POST, instance=settings)
        if form.is_valid():
            # Iterate through the cleaned data and print
            for field, value in form.cleaned_data.items():
                print(f"{field}: {value}")

            form.save()
            return redirect('settingsapp:edit_settings')
    else:
        form = AppSettingsForm(instance=settings)

    return render(request, 'settingsapp/edit_settings.html', {'form': form})




