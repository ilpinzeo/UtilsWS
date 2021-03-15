from django.shortcuts import render
from django.http import HttpResponse, FileResponse, HttpResponseBadRequest
from PIL import Image
from io import BytesIO
import json
import os

def image2pdf(request):
    response = HttpResponse()

    try:
        if len(request.FILES) == 0:
            raise Exception("FILES non inizializzato")

        files = request.FILES.getlist("files")

        if len(files) == 0:
            raise Exception("Parametro files mancante")

        images_list = []
        for image_file in files:
            image = Image.open(image_file)
            image.convert("RGB")
            images_list.append(image)

        with BytesIO() as out_in_memory_file:
            images_list[0].save(out_in_memory_file, format="PDF", save_all=True, append_images=images_list[1:])

            response = HttpResponse()
            response["Content-Disposition"] = "attachment; filename=out.pdf"
            
            out_in_memory_file.seek(0)
            response.write(out_in_memory_file.read())
            
    except Exception as e:
        response = HttpResponseBadRequest(e)

    return response