from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UploadForm
from model.predict import predict_tumor
import os
from .models import PredictionHistory
from .utils import generate_pdf  # PDF generator
from django.conf import settings
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from .models import PredictionHistory

# Home View
def home(request):
    return render(request, 'home.html')

# ✅ Predict View (Login Required)
@login_required
def predict(request):
    context = {}
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            path = os.path.join(settings.MEDIA_ROOT, image.name)
            with open(path, 'wb+') as f:
                for chunk in image.chunks():
                    f.write(chunk)

            result, confidence = predict_tumor(path)

            # ✅ Save to DB
            history = PredictionHistory.objects.create(
                user=request.user,
                image=image,
                predicted_class=result,
                confidence=round(confidence, 2)
            )

            # ✅ Generate PDF
            pdf_path = generate_pdf(
                username=request.user.username,
                predicted_class=result,
                confidence=confidence,
                image_path=path
            )
            pdf_url = f"/media/report_{request.user.username}.pdf"

            # ✅ Return result page with download link
            context = {
                'image_path': f"/media/{image.name}",
                'result': result,
                'confidence': round(confidence, 2),
                'pdf_url': f"/media/report_{request.user.username}.pdf"
            }
            return render(request, 'result.html', context)
    else:
        form = UploadForm()
    return render(request, 'predict.html', {'form': form})


@login_required
def dashboard(request):
    stats = (
        PredictionHistory.objects
        .filter(user=request.user)
        .values('predicted_class')
        .annotate(total=Count('predicted_class'))
    )

    chartLabels = [item['predicted_class'].capitalize() for item in stats]
    chartData = [item['total'] for item in stats]

    return render(request, 'dashboard.html', {
        'chartLabels': chartLabels,
        'chartData': chartData,
    })

# ✅ My Prediction History (Login Required)
@login_required
def my_predictions(request):
    predictions = PredictionHistory.objects.filter(user=request.user).order_by('-date')
    return render(request, 'my_predictions.html', {'predictions': predictions})

# About Page
def about(request):
    return render(request, 'about.html')

# Contact Page
def contact(request):
    return render(request, 'contact.html')
