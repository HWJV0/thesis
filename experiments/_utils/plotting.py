def get_colors():
    return ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

def convert_figures_to_images_html(figures):
    images_html = ""
    for figure in figures:
        image = str(base64.b64encode(figure.to_image(format="png", scale=2)))[2:-1]
        images_html += (f'<img src="data:image/png;base64,{image}"><br>')
    return images_html
 
def convert_figures_to_html(template_file, images_html):
    with open(template_file,'r') as f:
        template_html = f.read()
    report_html = template_html.replace("{{ FIGURES }}", images_html)
    return report_html
 
def convert_html_to_pdf(source_html, output_filename):
    with open(f"{output_filename}", "w+b") as f:
        pisa_status = pisa.CreatePDF(source_html, dest=f)
    return pisa_status.err
