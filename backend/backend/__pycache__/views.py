from django.http import JsonResponse
from .pinecone_service import query_similar_vectors, upsert_vector  # Import logic from a service file
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the home page!")

def query_similar_vectors_view(request):
    query_vector = request.GET.get('query_vector')  # Or pass a JSON body, depending on your needs
    try:
        result = query_similar_vectors(query_vector)
        return JsonResponse(result, safe=False)
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)

def upsert_vector_view(request):
    vector_data = request.POST.get('vector_data')  # Or pass a JSON body
    try:
        result = upsert_vector(vector_data)
        return JsonResponse(result)
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
