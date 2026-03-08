from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors
from django.conf import settings
import os
import datetime

# Tumor-based symptoms
SYMPTOMS_BY_CLASS = {
    'pituitary': ["Headaches", "Vision problems", "Hormonal changes"],
    'glioma': ["Seizures", "Memory issues", "Cognitive difficulty"],
    'meningioma': ["Hearing loss", "Facial numbness", "Vision loss"],
    'notumor': ["No symptoms — Healthy scan"]
}

def generate_pdf(username, predicted_class, confidence, image_path):
    pdf_path = os.path.join(settings.MEDIA_ROOT, f"report_{username}.pdf")
    c = canvas.Canvas(pdf_path, pagesize=A4)
    width, height = A4

    y = height - 60  # Start height

    # Title
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(colors.HexColor('#1E40AF'))
    c.drawString(50, y, "🧠 AI Brain Tumor Detection Report")
    y -= 40

    # Basic Info
    c.setFillColor(colors.black)
    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Patient Name: {username}")
    y -= 20
    c.drawString(50, y, f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
    y -= 20
    c.drawString(50, y, f"Predicted Class: {predicted_class.upper()}")
    y -= 20
    c.drawString(50, y, f"Confidence: {confidence:.2f}%")
    y -= 30

    # Divider
    c.setStrokeColor(colors.grey)
    c.line(50, y, width - 50, y)
    y -= 30

    # Diagnosis
    diagnosis_map = {
        'pituitary': "Possible Pituitary Tumor detected. Recommend endocrinology consultation.",
        'glioma': "Possible Glioma tumor. Neurology consultation is advised.",
        'meningioma': "Possible Meningioma tumor. Please consult a specialist.",
        'notumor': "No tumor detected. Brain scan appears normal."
    }

    diagnosis_text = diagnosis_map.get(predicted_class.lower(), "Result unavailable.")

    c.setFont("Helvetica-Bold", 13)
    c.setFillColor(colors.HexColor('#DC2626'))
    c.drawString(50, y, "🔍 Diagnosis")
    y -= 20
    c.setFont("Helvetica", 11)
    c.setFillColor(colors.black)
    c.drawString(60, y, diagnosis_text)
    y -= 40

    # Symptoms
    c.setFont("Helvetica-Bold", 13)
    c.drawString(50, y, "🧬 Possible Symptoms")
    y -= 20
    c.setFont("Helvetica", 11)
    symptoms = SYMPTOMS_BY_CLASS.get(predicted_class.lower(), ["N/A"])
    for symptom in symptoms:
        c.drawString(60, y, f"• {symptom}")
        y -= 15
    y -= 20

    # Divider
    c.setStrokeColor(colors.grey)
    c.line(50, y, width - 50, y)
    y -= 30

    # Image
    if os.path.exists(image_path):
        c.setFont("Helvetica-Bold", 13)
        c.drawString(50, y, "🧾 Uploaded MRI Scan")
        y -= 20

        # Calculate image size
        img_width = 240
        img_height = 240
        img_x = 50
        img_y = y - img_height

        if img_y < 50:
            img_y = 50  # Avoid going below the page

        c.drawImage(image_path, img_x, img_y, width=img_width, height=img_height, preserveAspectRatio=True)
        y = img_y - 30
    else:
        c.setFont("Helvetica-Oblique", 10)
        c.drawString(50, y, "No image found.")
        y -= 20

    # Footer
    c.setFont("Helvetica-Oblique", 9)
    c.setFillColor(colors.grey)
    c.drawString(50, 40, "This report is AI-generated. Please consult a medical professional for diagnosis confirmation.")
    c.drawString(50, 25, "© 2025 Brain Tumor Detection by Biku | All rights reserved.")

    c.showPage()
    c.save()

    return pdf_path
