from django.shortcuts import render, HttpResponse
from .summarize import create_news_summary

# Create your views here.
def summarize(request):
    # Access the 'query' parameter from the GET request
    query = request.GET.get('query')  # Get the keyword from the query parameter
    
    if query:  # Check if the query is provided
        summary = create_news_summary(query)  # Call the summary creation function
        
        summary_lines = summary.split('*') if summary else []
        
        print(summary_lines)
        return render(request, "search.html", {'summary': summary_lines, 'query': query})  # Render the result template with the summary
    else:
        return render(request, "search.html")  # Render the input form template