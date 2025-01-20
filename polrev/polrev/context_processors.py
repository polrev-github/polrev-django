def header_image(request):
    if request.path != "/" and request.user_agent.is_pc:  # Home page
        return {"header_image": "img/site-header-short.jpg"}
    else:  # Other pages
        return {"header_image": "img/site-header.jpg"}
